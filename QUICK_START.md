# 🚀 GUÍA RÁPIDA DE INICIO

## Paso 1: Crear y Activar Entorno Virtual

```powershell
# Abre PowerShell y navega a la carpeta del proyecto
cd "c:\Users\samue\Documents\Contador"

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
.\venv\Scripts\Activate.ps1

# Si tienes error de permisos, ejecuta primero:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Paso 2: Instalar Dependencias

```powershell
pip install -r requirements.txt
```

## Paso 3: Ejecutar la Aplicación

```powershell
python app.py
```

**Resultado esperado:**
```
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

## Paso 4: Abrir en Navegador

1. Abre tu navegador (Chrome, Edge, Firefox, etc.)
2. Ve a: `http://127.0.0.1:5000`
3. ¡Listo! La interfaz está lista para usar

## 📤 Cómo Usar la Herramienta

1. **Carga un archivo** (.txt o .docx)
2. **Arrastralo** al área designada o **haz clic** para seleccionar
3. **Obtén instantáneamente:**
   - ✓ Stats totales obtenidos
   - ✓ Líneas de contenido
   - ✓ Caracteres contados
   - ✓ Líneas faltantes para próximo stat
   - ✓ Barra de progreso visual

## 🔥 Características Principales

✅ Limpia automáticamente BBCode: `[b]`, `[color]`, `[i]`, etc.  
✅ Limpia automáticamente HTML: `<div>`, `<span>`, etc.  
✅ Cuenta solo texto plano (sin etiquetas)  
✅ Cálculo cíclico de stats: +1 (80L), +2 (120L), +3 (150L), +4 (230L)...  
✅ Interfaz moderna con Tailwind CSS  
✅ Soporte para .txt y .docx  
✅ Máximo 16MB por archivo  

## 📋 Archivos de Prueba

Se incluye `ejemplo_rol.txt` con:
- Etiquetas BBCode
- Etiquetas HTML
- Texto de rol ejemplar
- Diálogos y descripción

## ⚙️ Parar la Aplicación

Presiona `CTRL+C` en PowerShell para detener el servidor.

## 🆘 Problemas Comunes

**"No module named flask"**
```powershell
pip install flask
```

**Puerto 5000 ocupado**
- Edita `app.py` línea final: `port=5001`

**Error en archivos .docx**
```powershell
pip install python-docx
```

## 📊 Tabla de Progresión de Stats

| Líneas | Stats | Incremento | Próximo Stat En |
|--------|-------|-----------|-----------------|
| 79     | 0     | -         | +80 en 80 líneas|
| 80     | 1     | +80       | +40 en 120 líneas|
| 120    | 2     | +40       | +30 en 150 líneas|
| 150    | 3     | +30       | +80 en 230 líneas|
| 230    | 4     | +80       | +40 en 270 líneas|
| 270    | 5     | +40       | +30 en 300 líneas|
| 300    | 6     | +30       | +80 en 380 líneas|
| 380    | 7     | +80       | Ciclo continúa... |

¡Listo! 🎉 Disfruta auditando tus textos de RPG.
