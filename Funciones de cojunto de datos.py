from collections import Counter
import math


# Función para calcular la Media
def calcular_media(datos):
    return sum(datos) / len(datos)

# Función para calcular la Mediana
def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos)
    mitad = n // 2
    
    if n % 2 == 0:  # Si el número de elementos es par
        return (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2
    else:  # Si es impar
        return datos_ordenados[mitad]

# Función para calcular la Moda
def calcular_moda(datos):
    contador = Counter(datos)  # Contar las ocurrencias de cada valor
    moda, frecuencia = contador.most_common(1)[0]  # Obtener el valor más común
    return moda

# Función para calcular la Varianza
def calcular_varianza(datos):
    media = calcular_media(datos)
    return sum((x - media) ** 2 for x in datos) / (len(datos) - 1)

# Función para calcular la Desviación Estándar
def calcular_desviacion_estandar(datos):
    return math.sqrt(calcular_varianza(datos))

# Función para calcular el Coeficiente de Variación
def calcular_coeficiente_variacion(datos):
    media = calcular_media(datos)
    desviacion_estandar = calcular_desviacion_estandar(datos)
    return (desviacion_estandar / media) * 100  # Expresado en porcentaje

# Función para calcular la Normalización Z
def calcular_normalizacion_z(datos):
    media = calcular_media(datos)
    desviacion_estandar = calcular_desviacion_estandar(datos)
    return [(x - media) / desviacion_estandar for x in datos]

# Datos de ejemplo
datos = [10, 12, 23, 23, 16, 23, 21, 16, 3,8 ,15 ,15 ,21]

# Calculamos cada una de las medidas
media = calcular_media(datos)
mediana = calcular_mediana(datos)
moda = calcular_moda(datos)
varianza = calcular_varianza(datos)
desviacion_estandar = calcular_desviacion_estandar(datos)
coeficiente_variacion = calcular_coeficiente_variacion(datos)
normalizacion_z = calcular_normalizacion_z(datos)

(media, mediana, moda, varianza, desviacion_estandar, coeficiente_variacion, normalizacion_z)


print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Varianza: {varianza}")
print(f"Desviación Estándar: {desviacion_estandar}")
print(f"Coeficiente de Variación: {coeficiente_variacion}")
print(f"Normalización Z: {normalizacion_z}")
