# 🌡️ Proyecto RLS - Predicción de Temperatura

## 📋 Descripción Rápida
Modelo de **Regresión Lineal Simple (RLS)** para predecir temperatura basándose en humedad, usando 4032 registros históricos de sensores IoT de Firebase.

---

## 🚀 Inicio Rápido

### Para ejecutar el programa:
```powershell
# 1. Activar entorno virtual
.\venv\Scripts\Activate.ps1

# 2. Ejecutar modelo
python prediccion_rls_simple.py
```

---

## 📂 Estructura del Proyecto

```
RLS_Datos-Historicos/
│
├── 📚 Documentacion/               ← Toda la documentación aquí
│   ├── README.md                   → Documentación técnica completa
│   ├── INSTRUCCIONES.md            → Guía rápida (3 pasos)
│   ├── EXPLICACION_MATEMATICA.md   → Fórmulas y teoría
│   └── RESUMEN.md                  → Vista general del proyecto
│
├── 🐍 prediccion_rls_simple.py     ← Script principal
├── 📊 Datos-Historicos.json        ← Datos de Firebase (4032 registros)
├── 📈 grafica_regresion_lineal.png ← Gráfica generada
├── 📦 requirements.txt             ← Dependencias (numpy, pandas, matplotlib)
└── 🔧 venv/                        ← Entorno virtual Python
```

---

## 📊 Resultados del Modelo

### Ecuación Final
```
Temperatura = -0.2368 × Humedad + 32.5309
```

### Métricas de Rendimiento
- **R² = 0.6352** → Explica 63.52% de la variabilidad
- **RMSE = 3.37°C** → Error promedio de ±3.37 grados
- **MAE = 2.68°C** → Error absoluto medio

---

## 📚 Documentación

| Archivo | Descripción | Para qué leerlo |
|---------|-------------|-----------------|
| **[README.md](Documentacion/README.md)** | Documentación técnica completa | Entender todo el proyecto |
| **[INSTRUCCIONES.md](Documentacion/INSTRUCCIONES.md)** | Guía rápida de uso | Ejecutar el programa rápidamente |
| **[EXPLICACION_MATEMATICA.md](Documentacion/EXPLICACION_MATEMATICA.md)** | Fórmulas y teoría | Comprender las matemáticas |
| **[RESUMEN.md](Documentacion/RESUMEN.md)** | Vista general | Ver estado y checklist |

---

## ✅ Requisitos Cumplidos

- [x] Modelo RLS implementado manualmente
- [x] Evaluación con métricas (R², MSE, RMSE, MAE)
- [x] Representación gráfica (3 visualizaciones)
- [x] Uso de datos JSON de Firebase
- [x] Código completamente comentado
- [x] Entorno virtual configurado
- [x] Lógica simple y comprensible
- [x] Documentación organizada

---

## 🎯 Características Principales

✅ Implementación **manual** de RLS (sin sklearn)  
✅ Solo 3 dependencias: numpy, pandas, matplotlib  
✅ Ejecución **rápida** (~5 segundos)  
✅ **8 funciones** modulares bien documentadas  
✅ **3 gráficas** profesionales automáticas  
✅ Código **educativo** con comentarios detallados  

---

## 🔧 Tecnologías Utilizadas

- **Python 3.14+**
- **NumPy** - Operaciones matemáticas
- **Pandas** - Análisis de datos
- **Matplotlib** - Visualizaciones

---

## 📞 Notas Importantes

- La gráfica se guarda automáticamente como `grafica_regresion_lineal.png`
- Los datos se dividen en 80% entrenamiento y 20% prueba
- Relación encontrada: **inversa** (a mayor humedad → menor temperatura)
- El programa procesa **4032 registros** en segundos

---

## 🎓 Uso Académico

**Proyecto:** Regresión Lineal Simple  
**Materia:** Administración de Bases de Datos  
**Semestre:** 5to  
**Fecha:** Noviembre 2025  

---

## 📈 Vista Previa de Resultados

Al ejecutar el programa verás:
1. Carga de 4032 registros ✅
2. Análisis exploratorio de datos 📊
3. División de datos (80/20) 🔀
4. Entrenamiento del modelo 🤖
5. Ecuación de la recta 📐
6. Métricas de evaluación 📈
7. Gráficas generadas 🎨
8. Predicciones de ejemplo 🔮

---

**Estado: ✅ PROYECTO COMPLETO Y FUNCIONAL**

Para más detalles, consulta la [documentación completa](Documentacion/README.md).
