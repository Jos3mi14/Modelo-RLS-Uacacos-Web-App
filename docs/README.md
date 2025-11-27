# Predicción de Temperatura mediante Regresión Lineal Simple (RLS)

## 📋 Descripción del Proyecto

Este proyecto implementa un modelo de **Regresión Lineal Simple (RLS)** para predecir la temperatura ambiental basándose en la humedad, utilizando datos históricos de sensores IoT almacenados en Firebase.

### 🎯 Objetivo
Desarrollar un modelo de predicción mediante RLS y evaluarlo mediante métricas estadísticas, cumpliendo con los requisitos académicos del curso de Administración de Bases de Datos.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **NumPy**: Operaciones matemáticas y arrays
- **Pandas**: Manipulación y análisis de datos
- **Matplotlib**: Visualización de gráficas
- **Scikit-learn**: Modelo de Machine Learning (Regresión Lineal)

---

## 📂 Estructura del Proyecto

```
RLS_Datos-Historicos/
│
├── Documentacion/                  # 📚 Carpeta con toda la documentación
│   ├── README.md                   # Documentación completa del proyecto
│   ├── INSTRUCCIONES.md            # Guía rápida de uso
│   ├── EXPLICACION_MATEMATICA.md   # Fórmulas y teoría matemática
│   └── RESUMEN.md                  # Vista general del proyecto
│
├── venv/                           # Entorno virtual Python
├── Datos-Historicos.json           # Datos de Firebase (4032 registros)
├── prediccion_rls_simple.py        # Script principal del modelo RLS
├── requirements.txt                # Dependencias necesarias
└── grafica_regresion_lineal.png    # Gráfica generada automáticamente
```

---

## 🚀 Instalación y Configuración

### Paso 1: Activar el Entorno Virtual

**En Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**En Linux/Mac:**
```bash
source venv/bin/activate
```

### Paso 2: Verificar Instalación de Dependencias

Las dependencias ya están instaladas, pero si necesitas reinstalarlas:

```powershell
pip install -r requirements.txt
```

---

## ▶️ Ejecución del Programa

Con el entorno virtual activado, ejecuta:

```powershell
python prediccion_rls_simple.py
```

El programa usa una implementación manual de RLS (sin sklearn) para mayor simplicidad y rapidez.

---

## 📊 Funcionamiento del Modelo

### 1. **Carga de Datos**
   - Lee el archivo `Datos-Historicos.json` de Firebase
   - Extrae 4032 registros con datos de temperatura, humedad, luz y sonido

### 2. **Análisis Exploratorio**
   - Muestra estadísticas descriptivas
   - Identifica rangos y valores atípicos
   - Verifica integridad de los datos

### 3. **Preparación de Datos**
   - **Variable independiente (X)**: Humedad (%)
   - **Variable dependiente (y)**: Temperatura (°C)
   - División: 80% entrenamiento, 20% prueba

### 4. **Entrenamiento del Modelo**
   - Utiliza Regresión Lineal Simple
   - Calcula la ecuación: `Temperatura = m × Humedad + b`
   - Encuentra los coeficientes óptimos

### 5. **Evaluación del Modelo**
   Se calculan las siguientes métricas:
   
   - **R² (Coeficiente de Determinación)**: Mide qué tan bien el modelo explica la variabilidad (0-1)
   - **MSE (Error Cuadrático Medio)**: Promedio de errores al cuadrado
   - **RMSE (Raíz del MSE)**: Error promedio en grados Celsius
   - **MAE (Error Absoluto Medio)**: Promedio de errores absolutos

### 6. **Visualización**
   Genera 3 gráficas:
   
   1. **Línea de Regresión**: Muestra el ajuste del modelo con los datos de entrenamiento
   2. **Predicciones vs Reales**: Compara las predicciones con los valores reales
   3. **Distribución de Errores**: Histograma de residuos para verificar la precisión

### 7. **Predicciones de Ejemplo**
   Muestra predicciones para diferentes valores de humedad (30%, 40%, 50%, 60%, 70%)

---

## 📈 Interpretación de Resultados

### R² (Coeficiente de Determinación)
- **R² > 0.7**: Excelente ajuste
- **0.5 < R² < 0.7**: Ajuste moderado
- **R² < 0.5**: Ajuste débil

### RMSE (Raíz del Error Cuadrático Medio)
- Indica el error promedio en °C
- Mientras más bajo, mejor es el modelo

---

## 📌 Ecuación de Regresión Lineal

La ecuación general es:

```
y = mx + b
```

Donde:
- **y**: Temperatura predicha (°C)
- **x**: Humedad (%)
- **m**: Pendiente (coeficiente)
- **b**: Intercepto (temperatura cuando humedad = 0)

---

## 🎨 Ejemplo de Salida

```
📂 Cargando datos desde el archivo JSON...
✅ Datos cargados correctamente: 4031 registros

============================================================
📊 ANÁLISIS EXPLORATORIO DE DATOS
============================================================

📈 Estadísticas Descriptivas:
         humedad         luz      sonido  temperatura
count  4031.000000  4031.000000  4031.0  4031.000000
mean     44.523970     0.622473     0.5    23.476149
std      13.245789     0.485032     0.5     4.567821
min      30.000000     0.000000     0.0    16.000000
...

============================================================
🤖 ENTRENAMIENTO DEL MODELO
============================================================

✅ Modelo entrenado exitosamente

📐 Ecuación de la recta:
   Temperatura = -0.1234 × Humedad + 28.9876

============================================================
📊 EVALUACIÓN DEL MODELO
============================================================

📈 Métricas de Rendimiento:
   - R² (Coeficiente de Determinación): 0.7543
   - RMSE (Raíz del Error Cuadrático Medio): 2.34°C
   - MAE (Error Absoluto Medio): 1.89°C

✅ Gráfica guardada como: grafica_regresion_lineal.png
```

---

## 📝 Comentarios en el Código

El archivo `prediccion_rls.py` está **completamente comentado** con:
- Descripción de cada función
- Explicación de parámetros y retornos
- Interpretación de métricas
- Paso a paso del proceso

---

## 🎓 Propósito Académico

Este proyecto cumple con los siguientes requisitos:

✅ **Modelo de predicción mediante RLS**  
✅ **Evaluación con métricas estadísticas** (R², MSE, RMSE, MAE)  
✅ **Representación gráfica clara**  
✅ **Código comentado y documentado**  
✅ **Uso de entorno virtual**  
✅ **Lógica simple y comprensible**  

---

## 🐛 Solución de Problemas

### Error: "No se encontró el archivo"
- Verifica que `Datos-Historicos.json` esté en la misma carpeta que `prediccion_rls.py`

### Error: "ModuleNotFoundError"
- Asegúrate de tener el entorno virtual activado
- Reinstala las dependencias: `pip install -r requirements.txt`

### La gráfica no se muestra
- Verifica que tengas un entorno gráfico (no funciona en SSH sin X11)
- La gráfica se guarda automáticamente como PNG incluso si no se muestra

---

## 👨‍💻 Autor

**Proyecto Académico**  
Administración de Bases de Datos - 5to Semestre  
Universidad - Noviembre 2025

---

## 📄 Licencia

Este proyecto es de uso académico y educativo.
