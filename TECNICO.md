# 📖 GUÍA TÉCNICA DETALLADA DEL PROYECTO

## 🏗️ Arquitectura General

```
Cliente (Navegador)
        ↓
    index.html (Interfaz)
        ↓
    /api/audit (Endpoint Flask)
        ↓
    app.py (Lógica)
        ↓
    Retorna JSON con resultados
```

---

## 📄 ARCHIVO: app.py

### Funciones Principales

#### 1. `clean_text(texto)`
**Propósito:** Limpiar etiquetas BBCode y HTML del texto
```python
# Entrada:
"[b]Hola[/b] <span>mundo</span>"

# Proceso:
- Regex: r'\[/?[^\]]*\]'  → Quita BBCode
- Regex: r'<[^>]*>'        → Quita HTML
- Regex: r'\s+'            → Normaliza espacios

# Salida:
"Hola mundo"
```

#### 2. `count_characters(texto)`
**Propósito:** Contar caracteres del texto unificado
```python
# Entrada:
"Hola mundo\n\nMás texto"

# Proceso:
- Unifica: ' '.join(texto.split())
- Elimina saltos de línea

# Salida:
14  (caracteres)
```

#### 3. `calculate_lines(char_count)`
**Propósito:** Calcular líneas usando Calibri 11pt en A4
```python
# Fórmula:
Caracteres / 100 = Líneas

# Ejemplo:
1000 caracteres / 100 = 10 líneas
```

#### 4. `calculate_stats(lines)`
**Propósito:** Calcular stats con progresión cíclica

**Progresión:**
```
Ciclo 1:  +1 (80L), +2 (200L), +3 (350L)
Ciclo 2:  +4 (430L), +5 (550L), +6 (700L)
Ciclo 3:  +7 (780L), +8 (900L), +9 (1080L)
...
```

**Lógica:**
```python
increments = [80, 120, 150]  # Incrementos base

# Generar thresholds acumulativos:
80, 80+120=200, 80+120+150=350, 
350+80=430, 430+120=550, 550+150=700, ...

# Contar cuántos thresholds se alcanzan
```

#### 5. `extract_text_from_file(file_path)`
**Propósito:** Extraer texto de .txt o .docx
```python
# Para .txt:
- Leer archivo con encoding UTF-8

# Para .docx:
- Usar python-docx
- Extraer todos los párrafos
- Unir con saltos de línea
```

#### 6. `audit_text(texto_limpio)`
**Propósito:** Realizar auditoría completa

**Retorna:**
```json
{
  "characters": 1500,
  "lines": 15.0,
  "stats": 2,
  "lines_for_next_stat": 50.0
}
```

#### 7. Endpoint: `@app.route('/api/audit', methods=['POST'])`
**Propósito:** Recibir archivo, procesarlo y retornar resultados

**Flujo:**
1. Validar archivo (.txt o .docx)
2. Validar tamaño (máx 16MB)
3. Guardar temporalmente
4. Extraer texto
5. Limpiar etiquetas
6. Realizar auditoría
7. Eliminar archivo temporal
8. Retornar JSON

---

## 🎨 ARCHIVO: templates/index.html

### Estructura HTML

#### Secciones Principales:

1. **Loading Spinner**
   - Mostrado mientras se procesa el archivo
   - Centrado en la pantalla

2. **Header**
   - Título: "Auditor de Texto RPG"
   - Subtítulo descriptivo

3. **Upload Section**
   - Área drag-and-drop
   - Input tipo file (oculto)
   - Etiqueta clickeable
   - Muestra nombre del archivo

4. **Results Grid**
   - 4 tarjetas: Stats, Líneas, Caracteres, Líneas Faltantes
   - Diseño responsivo (1 columna en mobile, 2 en desktop)

5. **Progress Bar**
   - Barra visual del progreso hacia próximo stat
   - Ancho dinámico según progreso

6. **Info Cards**
   - 3 tarjetas informativas
   - Cálculo de líneas
   - Limpieza automática
   - Progresión de stats

### Estilos Tailwind CSS

```css
/* Colores principales */
bg-slate-900       /* Fondo oscuro */
text-orange-400    /* Texto naranja */
border-orange-500  /* Bordes naranja */

/* Gradientes */
gradient-orange    /* Linear gradient naranja */
glow-orange        /* Box shadow naranja */
hover-glow         /* Efecto hover con glow */

/* Animaciones */
fade-in            /* Entrada de elementos */
spin               /* Spinner de loading */
```

### JavaScript (Funciones principales)

#### `handleFile()`
- Valida extensión (.txt, .docx)
- Valida tamaño (máx 16MB)
- Llama uploadFile()

#### `uploadFile(file)`
- Crea FormData
- POST a /api/audit
- Muestra loading
- Maneja respuesta

#### `displayResults(data)`
- Rellena valores en HTML
- Calcula progreso (0-100%)
- Anima barra de progreso
- Muestra resultados

#### `showError(message)`
- Muestra mensaje de error
- Oculta resultados previos

---

## 🔄 FLUJO COMPLETO DE EJECUCIÓN

```
1. Usuario abre http://127.0.0.1:5000
   ↓
2. Flask sirve index.html
   ↓
3. Usuario arrastra o selecciona archivo
   ↓
4. JavaScript valida:
   - Extensión ✓
   - Tamaño ✓
   ↓
5. POST a /api/audit con FormData
   ↓
6. Flask procesa:
   a. Valida archivo
   b. Guarda temporalmente
   c. Extrae texto
   d. Limpia etiquetas
   e. Calcula caracteres
   f. Calcula líneas
   g. Calcula stats
   h. Calcula líneas faltantes
   i. Elimina archivo temporal
   ↓
7. Retorna JSON con resultados
   ↓
8. JavaScript recibe respuesta
   ↓
9. Anima y muestra resultados
   ↓
10. Barra de progreso se llena
```

---

## 🧮 EJEMPLOS DE CÁLCULO

### Ejemplo 1: Texto simple
```
Entrada: "Hola [b]mundo[/b]"

1. clean_text() → "Hola mundo" (9 caracteres)
2. count_characters() → 9 caracteres
3. calculate_lines() → 9 / 100 = 0.09 líneas
4. calculate_stats() → 0 stats (< 80 líneas)
5. lines_for_next_stat() → 80 - 0.09 = 79.91 líneas
```

### Ejemplo 2: Texto largo
```
Entrada: 8000 caracteres limpios

1. count_characters() → 8000 caracteres
2. calculate_lines() → 8000 / 100 = 80 líneas
3. calculate_stats() → 1 stat
   - Threshold 1: 80 líneas ✓
   - Threshold 2: 200 líneas ✗
4. lines_for_next_stat() → 200 - 80 = 120 líneas
```

### Ejemplo 3: Texto de rol extenso
```
Entrada: 35000 caracteres

1. count_characters() → 35000
2. calculate_lines() → 350 líneas
3. calculate_stats():
   - 80 líneas ✓ (stat 1)
   - 200 líneas ✓ (stat 2)
   - 350 líneas ✓ (stat 3)
   = 3 stats totales
4. lines_for_next_stat() → 430 - 350 = 80 líneas
```

---

## 🔒 MEDIDAS DE SEGURIDAD

1. **Validación de archivos:**
   ```python
   if not allowed_file(filename):
       return jsonify({'error': ...}), 400
   ```

2. **Sanitización de nombres:**
   ```python
   filename = secure_filename(file.filename)
   ```

3. **Límite de tamaño:**
   ```python
   app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
   ```

4. **Limpieza de archivos:**
   ```python
   if os.path.exists(file_path):
       os.remove(file_path)
   ```

5. **Manejo de errores:**
   ```python
   try:
       # procesar
   except Exception as e:
       return jsonify({'error': str(e)}), 500
   ```

---

## 📦 DEPENDENCIAS Y VERSIONES

| Paquete | Versión | Uso |
|---------|---------|-----|
| Flask | 3.0.0 | Servidor web |
| python-docx | 0.8.11 | Leer archivos .docx |
| Werkzeug | 3.0.1 | WSGI utilities |
| Jinja2 | 3.1.6+ | Template engine |
| click | 8.1.3+ | CLI utilities |
| itsdangerous | 2.1.2+ | Data signing |
| blinker | 1.6.2+ | Signal support |
| lxml | 2.3.2+ | XML processing |
| MarkupSafe | 2.1.1+ | Safe string handling |

---

## 🐛 POSIBLES MEJORAS FUTURAS

1. **Base de datos:**
   - Guardar historial de auditorías
   - Estadísticas por usuario

2. **Funcionalidades:**
   - Exportar resultados a PDF/Excel
   - Soporte para múltiples idiomas
   - Ajuste de parámetros de stats

3. **UI/UX:**
   - Gráficos de progresión histórica
   - Temas personalizables
   - Modo claro/oscuro

4. **Performance:**
   - Caché de resultados
   - Procesamiento asincrónico
   - Compresión de archivos

5. **Seguridad:**
   - Autenticación de usuarios
   - Rate limiting
   - Encriptación de datos

---

## 📞 SOPORTE Y DEBUGGING

### Habilitar modo verbose
```python
# En app.py
app.run(debug=True)  # Ya está habilitado
```

### Ver logs de Flask
```
[2026-03-05 10:30:45.123] POST /api/audit 200
[2026-03-05 10:30:46.456] GET / 200
```

### Comprobar rutas
```python
# En PowerShell/CMD
python -c "from app import app; app.debug = True; print(app.url_map)"
```

---

## ✅ CHECKLIST DE VERIFICACIÓN

- ✓ Flask se inicia sin errores
- ✓ Interfaz carga correctamente
- ✓ Upload drag-and-drop funciona
- ✓ .txt se procesa correctamente
- ✓ .docx se procesa correctamente
- ✓ Limpieza BBCode funciona
- ✓ Limpieza HTML funciona
- ✓ Cálculo de stats correcto
- ✓ Barra de progreso anima suavemente
- ✓ Archivos se limpian después de procesar
- ✓ Manejo de errores funciona
- ✓ Loading spinner muestra/oculta correctamente

---

Este documento sirve como referencia técnica completa del proyecto.
Para preguntas específicas, consulta los comentarios en el código.
