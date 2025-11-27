"""
Modelo de Predicción mediante Regresión Lineal Simple (RLS)
============================================================
Este script realiza una predicción de temperatura basada en humedad
usando los datos históricos de sensores ambientales de Firebase.

VERSIÓN SIMPLIFICADA - Sin sklearn, solo NumPy y Pandas
Implementación manual de RLS para mayor simplicidad y rapidez.

Autor: Análisis de Datos Ambientales
Fecha: Noviembre 2025
"""

# ============================================
# IMPORTACIÓN DE LIBRERÍAS NECESARIAS
# ============================================
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de estilo para gráficas más profesionales
plt.style.use('seaborn-v0_8-darkgrid')


# ============================================
# FUNCIÓN 1: CARGAR DATOS DESDE JSON
# ============================================
def cargar_datos_json(ruta_archivo):
    """
    Lee el archivo JSON de Firebase y extrae los datos históricos.
    
    Parámetros:
    -----------
    ruta_archivo : str
        Ruta completa al archivo JSON
    
    Retorna:
    --------
    pandas.DataFrame
        DataFrame con los datos procesados
    """
    print("📂 Cargando datos desde el archivo JSON...")
    
    # Abrir y leer el archivo JSON
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    
    # Extraer el array de historico_ambiente (ignorando el primer elemento que es null)
    historico = datos['historico_ambiente'][1:]  # Saltamos el índice 0 que es null
    
    # Convertir a DataFrame de pandas para mejor manipulación
    df = pd.DataFrame(historico)
    
    print(f"✅ Datos cargados correctamente: {len(df)} registros")
    return df


# ============================================
# FUNCIÓN 2: ANÁLISIS EXPLORATORIO BÁSICO
# ============================================
def analisis_exploratorio(df):
    """
    Muestra estadísticas descriptivas de los datos.
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame con los datos
    """
    print("\n" + "="*60)
    print("📊 ANÁLISIS EXPLORATORIO DE DATOS")
    print("="*60)
    
    # Estadísticas descriptivas
    print("\n📈 Estadísticas Descriptivas:")
    print(df.describe())
    
    # Valores nulos
    print(f"\n🔍 Valores nulos por columna:")
    print(df.isnull().sum())
    
    # Información general
    print(f"\n📋 Información del Dataset:")
    print(f"   - Total de registros: {len(df)}")
    print(f"   - Variables: {list(df.columns)}")


# ============================================
# FUNCIÓN 3: PREPARAR DATOS PARA RLS
# ============================================
def preparar_datos_rls(df):
    """
    Prepara los datos para el modelo de Regresión Lineal Simple.
    Usaremos HUMEDAD como variable independiente (X)
    y TEMPERATURA como variable dependiente (Y).
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame con los datos originales
    
    Retorna:
    --------
    X_train, X_test, y_train, y_test : arrays
        Datos divididos en entrenamiento y prueba
    """
    print("\n" + "="*60)
    print("🔧 PREPARACIÓN DE DATOS PARA REGRESIÓN LINEAL")
    print("="*60)
    
    # Seleccionar las variables
    # X = Variable independiente (humedad)
    # y = Variable dependiente (temperatura)
    X = df['humedad'].values  # Array 1D
    y = df['temperatura'].values  # Array 1D
    
    print(f"\n📌 Variable independiente (X): Humedad")
    print(f"📌 Variable dependiente (y): Temperatura")
    
    # Dividir datos manualmente en entrenamiento (80%) y prueba (20%)
    # Mezclar los datos primero para una división aleatoria
    np.random.seed(42)  # Para reproducibilidad
    indices = np.arange(len(X))
    np.random.shuffle(indices)
    
    # Calcular el índice de corte (80% para entrenamiento)
    corte = int(0.8 * len(X))
    
    # Dividir usando los índices mezclados
    indices_train = indices[:corte]
    indices_test = indices[corte:]
    
    X_train = X[indices_train]
    X_test = X[indices_test]
    y_train = y[indices_train]
    y_test = y[indices_test]
    
    print(f"\n✅ Datos divididos:")
    print(f"   - Entrenamiento: {len(X_train)} registros (80%)")
    print(f"   - Prueba: {len(X_test)} registros (20%)")
    
    return X_train, X_test, y_train, y_test


# ============================================
# FUNCIÓN 4: ENTRENAR MODELO RLS (MANUAL)
# ============================================
def entrenar_modelo_rls(X_train, y_train):
    """
    Entrena el modelo de Regresión Lineal Simple MANUALMENTE.
    
    La ecuación de la RLS es: y = mx + b
    
    Fórmulas matemáticas:
    - m (pendiente) = Σ[(xi - x̄)(yi - ȳ)] / Σ[(xi - x̄)²]
    - b (intercepto) = ȳ - m * x̄
    
    Donde:
    - x̄ = promedio de X
    - ȳ = promedio de Y
    - xi, yi = valores individuales
    
    Parámetros:
    -----------
    X_train : array
        Datos de entrenamiento (variable independiente)
    y_train : array
        Datos de entrenamiento (variable dependiente)
    
    Retorna:
    --------
    m, b : float
        Pendiente e intercepto del modelo
    """
    print("\n" + "="*60)
    print("🤖 ENTRENAMIENTO DEL MODELO (Implementación Manual)")
    print("="*60)
    
    # Calcular los promedios
    x_promedio = np.mean(X_train)
    y_promedio = np.mean(y_train)
    
    # Calcular la pendiente (m)
    # m = Σ[(xi - x̄)(yi - ȳ)] / Σ[(xi - x̄)²]
    numerador = np.sum((X_train - x_promedio) * (y_train - y_promedio))
    denominador = np.sum((X_train - x_promedio) ** 2)
    m = numerador / denominador
    
    # Calcular el intercepto (b)
    # b = ȳ - m * x̄
    b = y_promedio - (m * x_promedio)
    
    print(f"\n✅ Modelo entrenado exitosamente")
    print(f"\n📐 Ecuación de la recta:")
    print(f"   Temperatura = {m:.4f} × Humedad + {b:.4f}")
    print(f"\n   - Pendiente (m): {m:.4f}")
    print(f"   - Intercepto (b): {b:.4f}")
    print(f"\n💡 Interpretación:")
    if m > 0:
        print(f"   → Por cada 1% de aumento en humedad, la temperatura aumenta {abs(m):.4f}°C")
    else:
        print(f"   → Por cada 1% de aumento en humedad, la temperatura disminuye {abs(m):.4f}°C")
    
    return m, b


# ============================================
# FUNCIÓN 5: HACER PREDICCIONES
# ============================================
def predecir(X, m, b):
    """
    Realiza predicciones usando la ecuación de la recta.
    
    y_pred = m * X + b
    
    Parámetros:
    -----------
    X : array
        Valores de entrada (humedad)
    m : float
        Pendiente
    b : float
        Intercepto
    
    Retorna:
    --------
    y_pred : array
        Predicciones
    """
    return m * X + b


# ============================================
# FUNCIÓN 6: EVALUAR MODELO
# ============================================
def evaluar_modelo(y_test, y_pred):
    """
    Evalúa el rendimiento del modelo usando métricas estadísticas.
    
    Métricas utilizadas:
    - R² (R-cuadrado): Mide qué tan bien el modelo explica la variabilidad
    - MSE (Error Cuadrático Medio): Promedio de los errores al cuadrado
    - RMSE (Raíz del MSE): Error promedio en las mismas unidades que Y
    - MAE (Error Absoluto Medio): Promedio de los errores absolutos
    
    Parámetros:
    -----------
    y_test : array
        Valores reales
    y_pred : array
        Predicciones del modelo
    
    Retorna:
    --------
    metricas : dict
        Diccionario con las métricas calculadas
    """
    print("\n" + "="*60)
    print("📊 EVALUACIÓN DEL MODELO")
    print("="*60)
    
    # Calcular R² (Coeficiente de Determinación)
    # R² = 1 - (SS_res / SS_tot)
    # SS_res = Suma de cuadrados de residuos = Σ(yi - ŷi)²
    # SS_tot = Suma total de cuadrados = Σ(yi - ȳ)²
    ss_res = np.sum((y_test - y_pred) ** 2)
    ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    
    # Calcular MSE (Error Cuadrático Medio)
    # MSE = (1/n) * Σ(yi - ŷi)²
    mse = np.mean((y_test - y_pred) ** 2)
    
    # Calcular RMSE (Raíz del MSE)
    rmse = np.sqrt(mse)
    
    # Calcular MAE (Error Absoluto Medio)
    # MAE = (1/n) * Σ|yi - ŷi|
    mae = np.mean(np.abs(y_test - y_pred))
    
    # Mostrar métricas
    print(f"\n📈 Métricas de Rendimiento:")
    print(f"   - R² (Coeficiente de Determinación): {r2:.4f}")
    print(f"     → Interpretación: El modelo explica el {r2*100:.2f}% de la variabilidad")
    print(f"\n   - MSE (Error Cuadrático Medio): {mse:.4f}")
    print(f"   - RMSE (Raíz del Error Cuadrático Medio): {rmse:.4f}°C")
    print(f"     → Interpretación: Error promedio de ±{rmse:.2f}°C")
    print(f"\n   - MAE (Error Absoluto Medio): {mae:.4f}°C")
    
    # Interpretación del R²
    print(f"\n💡 Interpretación del Modelo:")
    if r2 > 0.7:
        print("   ✅ Excelente ajuste del modelo")
    elif r2 > 0.5:
        print("   ⚠️  Ajuste moderado del modelo")
    else:
        print("   ❌ Ajuste débil - La humedad no predice bien la temperatura")
    
    metricas = {
        'R2': r2,
        'MSE': mse,
        'RMSE': rmse,
        'MAE': mae
    }
    
    return metricas


# ============================================
# FUNCIÓN 7: VISUALIZAR RESULTADOS
# ============================================
def visualizar_resultados(m, b, X_train, y_train, X_test, y_test, y_pred, metricas):
    """
    Crea visualizaciones gráficas del modelo y sus predicciones.
    
    Genera 3 gráficas:
    1. Datos de entrenamiento con línea de regresión
    2. Predicciones vs valores reales (datos de prueba)
    3. Distribución de errores (residuos)
    
    Parámetros:
    -----------
    m, b : float
        Pendiente e intercepto del modelo
    X_train, y_train : arrays
        Datos de entrenamiento
    X_test, y_test : arrays
        Datos de prueba
    y_pred : array
        Predicciones del modelo
    metricas : dict
        Diccionario con métricas de evaluación
    """
    print("\n" + "="*60)
    print("📊 GENERANDO VISUALIZACIONES")
    print("="*60)
    
    # Crear figura con 3 subgráficas
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle('Análisis de Regresión Lineal Simple: Humedad vs Temperatura', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    # ===== GRÁFICA 1: Línea de Regresión con Datos de Entrenamiento =====
    axes[0].scatter(X_train, y_train, alpha=0.5, color='blue', s=30, label='Datos de entrenamiento')
    
    # Crear línea de regresión
    X_line = np.linspace(X_train.min(), X_train.max(), 100)
    y_line = m * X_line + b
    axes[0].plot(X_line, y_line, color='red', linewidth=2, label='Línea de Regresión')
    
    axes[0].set_xlabel('Humedad (%)', fontsize=11, fontweight='bold')
    axes[0].set_ylabel('Temperatura (°C)', fontsize=11, fontweight='bold')
    axes[0].set_title('Modelo de Regresión Lineal', fontsize=12, fontweight='bold')
    axes[0].legend(loc='best')
    axes[0].grid(True, alpha=0.3)
    
    # Añadir ecuación a la gráfica
    ecuacion = f'T = {m:.3f}H + {b:.3f}'
    axes[0].text(0.05, 0.95, ecuacion, transform=axes[0].transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # ===== GRÁFICA 2: Predicciones vs Valores Reales =====
    axes[1].scatter(y_test, y_pred, alpha=0.6, color='green', s=40)
    
    # Línea diagonal perfecta (predicción = valor real)
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    axes[1].plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Predicción perfecta')
    
    axes[1].set_xlabel('Temperatura Real (°C)', fontsize=11, fontweight='bold')
    axes[1].set_ylabel('Temperatura Predicha (°C)', fontsize=11, fontweight='bold')
    axes[1].set_title('Predicciones vs Valores Reales', fontsize=12, fontweight='bold')
    axes[1].legend(loc='best')
    axes[1].grid(True, alpha=0.3)
    
    # Añadir R² a la gráfica
    r2_text = f'R² = {metricas["R2"]:.4f}\nRMSE = {metricas["RMSE"]:.2f}°C'
    axes[1].text(0.05, 0.95, r2_text, transform=axes[1].transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    
    # ===== GRÁFICA 3: Distribución de Errores (Residuos) =====
    residuos = y_test - y_pred
    axes[2].hist(residuos, bins=30, color='purple', alpha=0.7, edgecolor='black')
    axes[2].axvline(x=0, color='red', linestyle='--', linewidth=2, label='Error = 0')
    
    axes[2].set_xlabel('Error (Residuo) en °C', fontsize=11, fontweight='bold')
    axes[2].set_ylabel('Frecuencia', fontsize=11, fontweight='bold')
    axes[2].set_title('Distribución de Errores', fontsize=12, fontweight='bold')
    axes[2].legend(loc='best')
    axes[2].grid(True, alpha=0.3, axis='y')
    
    # Añadir estadísticas de los residuos
    stats_text = f'Media: {residuos.mean():.3f}°C\nDesv. Est.: {residuos.std():.3f}°C'
    axes[2].text(0.65, 0.95, stats_text, transform=axes[2].transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    
    # Ajustar el espaciado entre gráficas
    plt.tight_layout()
    
    # Guardar la figura
    nombre_archivo = 'grafica_regresion_lineal.png'
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    print(f"\n✅ Gráfica guardada como: {nombre_archivo}")
    
    # Mostrar la gráfica
    plt.show()
    print("✅ Visualizaciones generadas exitosamente")


# ============================================
# FUNCIÓN 8: HACER PREDICCIONES PERSONALIZADAS
# ============================================
def hacer_predicciones_ejemplo(m, b):
    """
    Realiza predicciones de ejemplo con valores específicos de humedad.
    
    Parámetros:
    -----------
    m, b : float
        Pendiente e intercepto del modelo
    """
    print("\n" + "="*60)
    print("🔮 PREDICCIONES DE EJEMPLO")
    print("="*60)
    
    # Valores de humedad para predecir
    humedades_ejemplo = [30, 40, 50, 60, 70]
    
    print("\n📋 Predicciones de Temperatura según Humedad:")
    print("-" * 50)
    print(f"{'Humedad (%)':<15} {'Temperatura Predicha (°C)':<30}")
    print("-" * 50)
    
    for humedad in humedades_ejemplo:
        # Hacer predicción usando la ecuación y = mx + b
        temperatura_pred = m * humedad + b
        print(f"{humedad:<15} {temperatura_pred:<30.2f}")
    
    print("-" * 50)


# ============================================
# FUNCIÓN PRINCIPAL
# ============================================
def main():
    """
    Función principal que ejecuta todo el flujo del análisis.
    """
    print("\n" + "="*60)
    print("🌡️  PREDICCIÓN DE TEMPERATURA MEDIANTE RLS")
    print("   Datos de Sensores Ambientales - Firebase")
    print("   VERSIÓN SIMPLIFICADA (Sin sklearn)")
    print("="*60)
    
    # Ruta al archivo JSON (en la misma carpeta)
    ruta_json = r'C:\Users\emisa\Documents\UNIVERSIDAD\5to Semestre\Administración Bases de Datos\RLS_Datos-Historicos\Datos-Historicos.json'
    
    try:
        # PASO 1: Cargar datos
        df = cargar_datos_json(ruta_json)
        
        # PASO 2: Análisis exploratorio
        analisis_exploratorio(df)
        
        # PASO 3: Preparar datos para RLS
        X_train, X_test, y_train, y_test = preparar_datos_rls(df)
        
        # PASO 4: Entrenar modelo (manual)
        m, b = entrenar_modelo_rls(X_train, y_train)
        
        # PASO 5: Hacer predicciones
        y_pred = predecir(X_test, m, b)
        
        # PASO 6: Evaluar modelo
        metricas = evaluar_modelo(y_test, y_pred)
        
        # PASO 7: Visualizar resultados
        visualizar_resultados(m, b, X_train, y_train, X_test, y_test, y_pred, metricas)
        
        # PASO 8: Hacer predicciones de ejemplo
        hacer_predicciones_ejemplo(m, b)
        
        print("\n" + "="*60)
        print("✅ ANÁLISIS COMPLETADO EXITOSAMENTE")
        print("="*60)
        
    except FileNotFoundError:
        print(f"\n❌ ERROR: No se encontró el archivo '{ruta_json}'")
        print("   Asegúrate de que el archivo esté en la ruta correcta.")
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")


# ============================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================
if __name__ == "__main__":
    main()
