# 📐 Explicación Matemática del Modelo RLS

## ¿Qué es la Regresión Lineal Simple?

La **Regresión Lineal Simple (RLS)** es un método estadístico que modela la relación entre dos variables:
- Una **variable independiente** (X) → En nuestro caso: **Humedad**
- Una **variable dependiente** (Y) → En nuestro caso: **Temperatura**

---

## 📊 Ecuación de la Recta

La RLS busca encontrar la mejor línea recta que representa la relación entre X e Y:

```
y = mx + b
```

Donde:
- **y** = Variable dependiente (Temperatura predicha)
- **x** = Variable independiente (Humedad)
- **m** = Pendiente de la recta (coeficiente)
- **b** = Intercepto (valor de Y cuando X = 0)

---

## 🔢 Fórmulas para Calcular m y b

### 1. Cálculo de la Pendiente (m)

```
m = Σ[(xi - x̄)(yi - ȳ)] / Σ[(xi - x̄)²]
```

**Paso a paso:**
1. Calcular el promedio de X (humedad): `x̄`
2. Calcular el promedio de Y (temperatura): `ȳ`
3. Para cada dato:
   - Restar el promedio: `(xi - x̄)` y `(yi - ȳ)`
   - Multiplicar ambas diferencias: `(xi - x̄)(yi - ȳ)`
   - Elevar al cuadrado la diferencia de X: `(xi - x̄)²`
4. Sumar todos los productos del numerador
5. Sumar todos los cuadrados del denominador
6. Dividir numerador / denominador

**Interpretación de m:**
- Si `m > 0`: Relación positiva (X aumenta → Y aumenta)
- Si `m < 0`: Relación negativa (X aumenta → Y disminuye)
- Si `m = 0`: No hay relación lineal

**En nuestro caso:**
```
m = -0.2368
```
→ Relación negativa: A mayor humedad, menor temperatura

### 2. Cálculo del Intercepto (b)

```
b = ȳ - m × x̄
```

**Paso a paso:**
1. Tomar el promedio de Y: `ȳ`
2. Multiplicar la pendiente por el promedio de X: `m × x̄`
3. Restar: `ȳ - (m × x̄)`

**Interpretación de b:**
- Es el valor de Y cuando X = 0
- En nuestro caso: temperatura esperada con 0% de humedad

**En nuestro caso:**
```
b = 32.5309
```
→ Con 0% de humedad, se esperaría ~32.5°C

---

## 📈 Métricas de Evaluación

### 1. R² (Coeficiente de Determinación)

Mide qué tan bien el modelo explica la variabilidad de los datos.

```
R² = 1 - (SS_res / SS_tot)
```

Donde:
- **SS_res** = Suma de cuadrados de residuos = `Σ(yi - ŷi)²`
- **SS_tot** = Suma total de cuadrados = `Σ(yi - ȳ)²`

**Interpretación:**
- **R² = 1.0** → Modelo perfecto (100% de ajuste)
- **R² = 0.8-1.0** → Excelente ajuste
- **R² = 0.5-0.8** → Ajuste moderado
- **R² < 0.5** → Ajuste débil
- **R² = 0.0** → El modelo no explica nada

**Nuestro resultado:**
```
R² = 0.6352 (63.52%)
```
→ El modelo explica el 63.52% de la variación en temperatura

### 2. MSE (Error Cuadrático Medio)

Promedio de los errores al cuadrado.

```
MSE = (1/n) × Σ(yi - ŷi)²
```

**Interpretación:**
- Penaliza más los errores grandes
- Mientras más bajo, mejor
- Siempre es positivo

**Nuestro resultado:**
```
MSE = 11.3507
```

### 3. RMSE (Raíz del Error Cuadrático Medio)

Es la raíz cuadrada del MSE, en las mismas unidades que Y.

```
RMSE = √MSE
```

**Interpretación:**
- Indica el error promedio del modelo
- En las mismas unidades que la variable dependiente (°C)
- Más intuitivo que el MSE

**Nuestro resultado:**
```
RMSE = 3.37°C
```
→ El modelo se equivoca en promedio ±3.37 grados

### 4. MAE (Error Absoluto Medio)

Promedio de los valores absolutos de los errores.

```
MAE = (1/n) × Σ|yi - ŷi|
```

**Interpretación:**
- No penaliza tanto los errores grandes como MSE
- Más robusto ante valores atípicos
- En las mismas unidades que Y (°C)

**Nuestro resultado:**
```
MAE = 2.68°C
```
→ Error absoluto promedio de 2.68 grados

---

## 🎯 Ejemplo Práctico

### Predicción con Humedad = 50%

Usando la ecuación:
```
y = mx + b
y = (-0.2368 × 50) + 32.5309
y = -11.84 + 32.5309
y = 20.69°C
```

**Interpretación:**
Con una humedad del 50%, el modelo predice una temperatura de aproximadamente 20.69°C.

---

## 📊 Residuos (Errores)

Los **residuos** son las diferencias entre los valores reales y predichos:

```
residuo = yi - ŷi
```

**Características de buenos residuos:**
- Distribución aproximadamente normal (campana de Gauss)
- Media cercana a 0
- Sin patrones evidentes (aleatorios)

**En nuestro modelo:**
- Media de residuos: ~0°C ✅
- Distribución: Aproximadamente normal ✅
- Indica que el modelo no tiene sesgos sistemáticos

---

## 🧮 Resumen de Fórmulas

| Concepto | Fórmula | Nuestro Valor |
|----------|---------|---------------|
| Pendiente | `m = Σ[(xi - x̄)(yi - ȳ)] / Σ[(xi - x̄)²]` | -0.2368 |
| Intercepto | `b = ȳ - m × x̄` | 32.5309 |
| Predicción | `ŷ = mx + b` | Variable |
| R² | `1 - (SS_res / SS_tot)` | 0.6352 |
| MSE | `(1/n) × Σ(yi - ŷi)²` | 11.3507 |
| RMSE | `√MSE` | 3.37°C |
| MAE | `(1/n) × Σ\|yi - ŷi\|` | 2.68°C |

---

## 💡 Conclusiones del Análisis

1. **Relación Inversa**: Existe una relación inversa moderada entre humedad y temperatura
2. **Predictibilidad**: El modelo puede predecir ~63% de la variación en temperatura
3. **Error Aceptable**: Con un error promedio de ±3.37°C, el modelo es útil para estimaciones generales
4. **Aplicación**: Este modelo puede usarse para estimar temperatura conociendo solo la humedad

---

## 🔍 Limitaciones

- El modelo es **lineal**, pero la relación real podría ser más compleja
- Solo usa **una variable** (humedad) para predecir temperatura
- No considera otros factores como luz, sonido, hora del día, etc.
- El R² de 0.63 indica que hay otros factores no capturados por el modelo

---

## 📚 Referencias Matemáticas

- **Regresión Lineal Simple**: Método de Mínimos Cuadrados Ordinarios (MCO)
- **Objetivo**: Minimizar la suma de los cuadrados de los residuos
- **Suposiciones**: Linealidad, independencia, homocedasticidad, normalidad

---

**¡Matemáticas aplicadas a datos reales! 🎓**
