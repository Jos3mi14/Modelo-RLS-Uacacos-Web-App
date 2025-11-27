# 🌡️ Predicción de Temperatura con Regresión Lineal Simple

## 👥 Equipo Uacacos
**Universidad Autónoma de Querétaro**  
Administración de Bases de Datos - 5to Semestre

---

## 📋 Descripción

Modelo de **Regresión Lineal Simple (RLS)** que predice la temperatura ambiental basándose en la humedad, utilizando 4,032 registros históricos de sensores IoT almacenados en Firebase.

### 🎯 Objetivo
Desarrollar e implementar un modelo de predicción mediante RLS, evaluándolo con métricas estadísticas para análisis de datos ambientales.

---

## 🛠️ Tecnologías

- **Python 3.14+**
- **NumPy** - Cálculos matemáticos
- **Pandas** - Análisis de datos
- **Matplotlib** - Visualizaciones

---

## 📊 Resultados

### Ecuación del Modelo
```
Temperatura = -0.2368 × Humedad + 32.5309
```

### Métricas de Rendimiento
- **R² = 0.6352** - El modelo explica 63.52% de la variabilidad
- **RMSE = 3.37°C** - Error promedio
- **MAE = 2.68°C** - Error absoluto medio

**Interpretación**: Relación inversa entre humedad y temperatura (↑ humedad → ↓ temperatura)

---

## 📂 Estructura del Proyecto

```
Modelo-RLS-Uacacos-Web-App/
│
├── README.md                    # 📖 Este archivo - Documentación principal
├── prediccion_rls_simple.py     # 🐍 Script principal del modelo
├── Datos-Historicos.json        # 📊 4,032 registros de Firebase
├── grafica_regresion_lineal.png # 📈 Visualización generada
├── requirements.txt             # 📦 Dependencias (numpy, pandas, matplotlib)
├── venv/                        # 🔧 Entorno virtual Python
│
└── docs/                        # 📚 Documentación complementaria
    ├── INSTRUCCIONES.md         #    → Guía rápida (3 pasos)
    ├── EXPLICACION_MATEMATICA.md#    → Fórmulas y teoría RLS
    └── RESUMEN.md               #    → Checklist del proyecto
```

---

## 🚀 Inicio Rápido

### 1. Activar Entorno Virtual
```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Instalar Dependencias (si es necesario)
```powershell
pip install -r requirements.txt
```

### 3. Ejecutar el Modelo
```powershell
python prediccion_rls_simple.py
```

La gráfica se genera automáticamente como `grafica_regresion_lineal.png`

---

## 🔬 Características del Modelo

### Implementación
- **Algoritmo**: Regresión Lineal Simple (implementación manual)
- **Sin librerías ML**: No usa scikit-learn, código desde cero
- **Variables**: Humedad (X) → Temperatura (Y)
- **División de datos**: 80% entrenamiento, 20% prueba

### Proceso
1. **Carga** 4,032 registros de Firebase
2. **Analiza** estadísticas de temperatura y humedad
3. **Entrena** modelo con fórmulas matemáticas manuales
4. **Evalúa** con 4 métricas (R², MSE, RMSE, MAE)
5. **Genera** 3 gráficas profesionales
6. **Predice** temperatura para nuevos valores de humedad

### Visualizaciones Generadas
1. **Línea de Regresión** - Ajuste del modelo
2. **Predicciones vs Reales** - Precisión del modelo
3. **Distribución de Errores** - Análisis de residuos

---

## 📖 Documentación Adicional

Para información complementaria, consulta la carpeta [`docs/`](docs/):

| Documento | Contenido |
|-----------|----------|
| **[INSTRUCCIONES.md](docs/INSTRUCCIONES.md)** | Guía rápida de ejecución (3 pasos) |
| **[EXPLICACION_MATEMATICA.md](docs/EXPLICACION_MATEMATICA.md)** | Fórmulas matemáticas y teoría detallada |
| **[RESUMEN.md](docs/RESUMEN.md)** | Checklist completo del proyecto |

---

## ✨ Características Destacadas

✅ **Implementación manual** - RLS desde cero sin sklearn  
✅ **Código educativo** - `prediccion_rls_simple.py` completamente comentado  
✅ **Ejecución rápida** - Procesamiento en ~5 segundos  
✅ **3 gráficas automáticas** - Visualizaciones de alta calidad (300 DPI)  
✅ **8 funciones modulares** - Código organizado y mantenible  

---

## 🎓 Requisitos Cumplidos

✅ Modelo de predicción mediante RLS  
✅ Evaluación con métricas estadísticas (R², MSE, RMSE, MAE)  
✅ Representación gráfica clara  
✅ Código comentado y documentado  
✅ Uso de entorno virtual  
✅ Lógica simple y comprensible  

---

## 🔧 Requisitos del Sistema

- Python 3.14 o superior
- Windows/Linux/Mac
- ~50MB de espacio libre

---

## 🐛 Solución de Problemas

| Problema | Solución |
|----------|----------|
| Error al activar venv | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| ModuleNotFoundError | `pip install -r requirements.txt` |
| Archivo JSON no encontrado | Verificar que esté en la misma carpeta que el script |

---

## 👨‍💻 Autores

**Equipo Uacacos**  
Universidad Autónoma de Querétaro  
Administración de Bases de Datos - 5to Semestre  
Noviembre 2025

---

## 📄 Licencia

Proyecto de uso académico y educativo.
