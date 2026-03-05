# Auditor de Texto RPG 🎭

Una herramienta Flask para auditar y calcular estadísticas de contenido de rol, limpiando etiquetas BBCode y HTML automáticamente.

## 🚀 Características

- **Limpieza automática** de etiquetas BBCode y HTML
- **Cálculo de caracteres** contando solo texto plano
- **Cálculo de líneas** dividiendo caracteres entre 100
- **Sistema de Stats cíclico** con progresión configurable
- **Interfaz moderna** con Tailwind CSS y diseño oscuro
- **Soporte de archivos** .txt y .docx
- **Indicadores visuales** con barras de progreso

## 📊 Progresión de Stats

- **+1**: A 80 líneas
- **+2**: A 120 líneas (80 + 40)
- **+3**: A 150 líneas (120 + 30)
- **+4**: A 230 líneas (150 + 80)
- **+5**: A 270 líneas (230 + 40)
- **+6**: A 300 líneas (270 + 30)
- **+7**: A 380 líneas (300 + 80)
- **+8**: A 420 líneas (380 + 40)
- **+9**: A 450 líneas (420 + 30)
- Y así sucesivamente con ciclos de [80, 40, 30]...

## 🛠️ Instalación y Ejecución

### 1. Crear Entorno Virtual

**En Windows (PowerShell):**
```powershell
# Navegar a la carpeta del proyecto
cd "c:\Users\samue\Documents\Contador"

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
.\venv\Scripts\Activate.ps1
```

Si tienes problemas de permisos en PowerShell, ejecuta:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Instalar Dependencias

```powershell
pip install -r requirements.txt
```

### 3. Ejecutar la Aplicación

```powershell
python app.py
```

La aplicación se ejecutará en: **http://127.0.0.1:5000**

### 4. Usar la Herramienta

1. Abre tu navegador en la dirección anterior
2. Carga un archivo .txt o .docx (máximo 16MB)
3. Arrastra el archivo al área de carga o haz clic para seleccionar
4. Obtén instantáneamente:
   - **Stats**: Puntos de estadística calculados
   - **Líneas**: Cantidad total de líneas
   - **Caracteres**: Número de caracteres planos
   - **Líneas Faltantes**: Para alcanzar el próximo stat
   - **Barra de progreso**: Visual del avance

## 📁 Estructura del Proyecto

```
Contador/
├── app.py                 # Servidor Flask y lógica
├── requirements.txt       # Dependencias Python
├── .gitignore            # Archivos a ignorar en git
├── README.md             # Este archivo
├── templates/
│   └── index.html        # Interfaz web (Tailwind CSS)
└── uploads/              # Carpeta temporal para archivos
```

## 🔧 Tecnologías Utilizadas

- **Flask** 3.0.0 - Servidor web
- **python-docx** 0.8.11 - Lectura de archivos Word
- **Tailwind CSS** - Estilos (CDN)
- **Regex** - Limpieza de etiquetas

## 📝 Detalles Técnicos

### Limpieza de Texto

El script limpia:
- Etiquetas BBCode: `[b]`, `[color=red]`, `[/tag]`, etc.
- Etiquetas HTML: `<div>`, `<span>`, `</p>`, etc.
- Espacios múltiples y saltos de línea innecesarios

### Cálculo de Líneas

Fórmula: `Caracteres / 100 = Líneas`

Simula el rendimiento de texto en Calibri 11pt en página A4 con márgenes estándar.

### Cálculo de Stats

Implementa una progresión cíclica donde cada ciclo suma nuevos incrementos:
- Ciclo 1: +80, +120, +150 líneas
- Ciclo 2: +80, +120, +150 líneas más
- Y así sucesivamente...

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"
```powershell
pip install -r requirements.txt
```

### Puerto 5000 en uso
Modifica en `app.py` la línea:
```python
app.run(debug=True, host='127.0.0.1', port=5001)  # Cambia 5000 a otro puerto
```

### Error al abrir archivo .docx
Asegúrate de que python-docx esté instalado:
```powershell
pip install python-docx
```

## 📄 Archivos Soportados

- `.txt` - Archivos de texto plano
- `.docx` - Documentos Word (.doc antiguo no soportado)

## 🔒 Seguridad

- Validación de tipos de archivo
- Límite de tamaño: 16MB
- Eliminación automática de archivos temporales
- Nombres de archivo seguros (sanitizados)

## 📧 Notas

- Los archivos se procesan temporalmente y se eliminan automáticamente
- No se guardan copias de los archivos subidos
- La aplicación es local (127.0.0.1) por defecto

¡Disfruta contando tus stats de rol! 🎲
