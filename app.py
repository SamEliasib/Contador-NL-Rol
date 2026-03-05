from flask import Flask, render_template, request, jsonify
import os
import re
from werkzeug.utils import secure_filename
from docx import Document

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_FOLDER', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB máximo

# Crear carpeta de uploads si no existe
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'txt', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def clean_text(texto):
    """
    Limpia etiquetas BBCode y HTML del texto.
    Mantiene solo el texto plano.
    """
    # Limpiar etiquetas BBCode: [tag], [tag=value], etc.
    texto = re.sub(r'\[/?[^\]]*\]', '', texto)
    
    # Limpiar etiquetas HTML: <tag>, </tag>, etc.
    texto = re.sub(r'<[^>]*>', '', texto)
    
    # Limpiar espacios múltiples
    texto = re.sub(r'\s+', ' ', texto)
    
    return texto.strip()

def extract_text_from_file(file_path):
    """
    Extrae texto de archivos .txt o .docx
    """
    file_ext = file_path.rsplit('.', 1)[1].lower()
    
    if file_ext == 'txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif file_ext == 'docx':
        doc = Document(file_path)
        return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    
    return ""

def count_characters(texto):
    """
    Cuenta caracteres del texto unificado (sin saltos de línea)
    """
    # Remover saltos de línea y espacios múltiples
    texto_unificado = ' '.join(texto.split())
    return len(texto_unificado)

def calculate_lines(char_count):
    """
    Calcula líneas dividiendo caracteres entre 100
    (simulando Calibri 11pt en A4)
    """
    return char_count / 100

def calculate_stats(lines):
    """
    Calcula stats con progresión cíclica [80, 40, 30]:
    
    Progresión de umbrales:
    - Stat 1: 80 líneas (+80)
    - Stat 2: 120 líneas (+40)
    - Stat 3: 150 líneas (+30)
    - Stat 4: 230 líneas (+80) ← Ciclo reinicia
    - Stat 5: 270 líneas (+40)
    - Stat 6: 300 líneas (+30)
    - Stat 7: 380 líneas (+80)
    - Stat 8: 420 líneas (+40)
    - Stat 9: 450 líneas (+30)
    """
    if lines < 80:
        return 0
    
    # Thresholds acumulativos de cada stat con ciclo [80, 40, 30]
    thresholds = []
    current = 0
    increments = [80, 40, 30]  # Ciclo de incrementos
    
    # Generar suficientes thresholds para cubrir hasta líneas muy altas
    for i in range(100):  # Generar hasta 100 stats
        current += increments[i % 3]
        thresholds.append(current)
    
    # Contar cuántos thresholds se alcanzan
    stats = 0
    for threshold in thresholds:
        if lines >= threshold:
            stats += 1
        else:
            break
    
    return stats

def audit_text(texto_limpio):
    """
    Realiza auditoría completa del texto
    """
    char_count = count_characters(texto_limpio)
    lines = calculate_lines(char_count)
    stats = calculate_stats(lines)
    
    # Calcular líneas faltantes para próximo stat
    increments = [80, 40, 30]
    
    # Generar thresholds acumulativos
    thresholds = []
    current = 0
    for i in range(100):
        current += increments[i % 3]
        thresholds.append(current)
    
    # Encontrar próximo threshold
    lines_for_next_stat = 0
    for threshold in thresholds:
        if lines < threshold:
            lines_for_next_stat = threshold - lines
            break
    
    return {
        'characters': int(char_count),
        'lines': round(lines, 2),
        'stats': int(stats),
        'lines_for_next_stat': max(0, round(lines_for_next_stat, 2))
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/audit', methods=['POST'])
def api_audit():
    try:
        # Validar que existe archivo
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Solo se permiten archivos .txt y .docx'}), 400
        
        # Guardar archivo temporalmente
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        try:
            # Extraer texto
            texto_raw = extract_text_from_file(file_path)
            
            # Limpiar etiquetas
            texto_limpio = clean_text(texto_raw)
            
            if not texto_limpio:
                return jsonify({'error': 'El archivo está vacío o solo contiene etiquetas'}), 400
            
            # Realizar auditoría
            resultado = audit_text(texto_limpio)
            
            return jsonify(resultado), 200
        
        finally:
            # Eliminar archivo temporal
            if os.path.exists(file_path):
                os.remove(file_path)
    
    except Exception as e:
        return jsonify({'error': f'Error procesando archivo: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
