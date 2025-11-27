# 🚀 INSTRUCCIONES RÁPIDAS DE USO

## ⚡ Ejecución Rápida (3 pasos)

### 1. Activar el entorno virtual
```powershell
.\venv\Scripts\Activate.ps1
```

### 2. Ejecutar el programa
```powershell
python prediccion_rls_simple.py
```

### 3. Ver resultados
- La gráfica se guarda automáticamente como `grafica_regresion_lineal.png`
- Todas las métricas se muestran en la consola

---

## 📊 Resultados que obtendrás

### ✅ Métricas del Modelo
- **R² = 0.6352** → El modelo explica el 63.52% de la variabilidad
- **RMSE = 3.37°C** → Error promedio de ±3.37 grados
- **MAE = 2.68°C** → Error absoluto medio

### 📐 Ecuación obtenida
```
Temperatura = -0.2368 × Humedad + 32.5309
```

**Interpretación**: Por cada 1% de aumento en la humedad, la temperatura disminuye aproximadamente 0.24°C

### 📈 Gráficas generadas
1. **Línea de Regresión**: Muestra cómo el modelo ajusta los datos
2. **Predicciones vs Reales**: Compara las predicciones con valores reales
3. **Distribución de Errores**: Histograma de los residuos del modelo

---

## 🔧 Solución de Problemas Comunes

### ❌ Error: "No se puede ejecutar scripts en este sistema"
**Solución**: Ejecuta esto primero:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### ❌ Error: "No se encontró el archivo JSON"
**Solución**: Verifica que `Datos-Historicos.json` esté en la misma carpeta

### ❌ Error: "ModuleNotFoundError"
**Solución**: Reinstala las dependencias:
```powershell
pip install numpy pandas matplotlib
```

---

## 📝 ¿Qué hace el programa?

1. **Carga** 4032 registros del archivo JSON de Firebase
2. **Analiza** estadísticas de temperatura y humedad
3. **Entrena** un modelo de Regresión Lineal Simple (implementación manual)
4. **Evalúa** el modelo con métricas estadísticas (R², MSE, RMSE, MAE)
5. **Genera** gráficas profesionales en formato PNG
6. **Muestra** predicciones de ejemplo y ecuación final

---

## 🎯 Características del Proyecto

✅ **Implementación manual** de RLS (sin sklearn, más simple y rápida)  
✅ **Código completamente comentado** línea por línea  
✅ **Métricas completas** de evaluación (R², MSE, RMSE, MAE)  
✅ **Gráficas profesionales** con matplotlib (3 visualizaciones)  
✅ **Predicciones de ejemplo** incluidas  
✅ **Lógica simple** y fácil de entender  
✅ **Documentación organizada** en carpeta dedicada  

---

## 📞 Notas Importantes

- El programa tarda ~5-10 segundos en ejecutarse
- La gráfica se guarda automáticamente antes de mostrarse
- Los datos se dividen en 80% entrenamiento y 20% prueba
- La relación encontrada es **inversa**: a mayor humedad, menor temperatura

---

**¡Listo para usar! 🎉**
