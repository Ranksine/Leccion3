# Ejercicio estaciones
"""
mes = int(input('Porporciona mes del año (1-12): '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Mes incorrecto'
print(f'Para el mes {mes} la estación es: {estacion}')
"""

# Ejercicio etapas de la vida según la edad
"""
edad = int(input('Proporciona tu edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increible...'
elif 10 <= edad < 20:
    mensaje = 'Muchos cambios y mucho estudio...'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo...'
else:
    mensaje = 'Etapa de vida no reconocida'

print(f'Tu edad es: {edad}, {mensaje}')
"""

"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menos a 6: imprimir una F
Cualquier otro valor debe imprimir: Valor incorrecto
Por ejemplo:
Proporciona un valor entre 0 y 10: 9
A
"""
numero = float(input('Proporciona un valor entre 0 y 10: '))
mensaje = 'La calificación del alumno es: '

if numero >= 9 and numero <= 10:
    mensaje += 'A'
elif 9 > numero >= 8:
    mensaje += 'B'
elif 8 > numero >= 7:
    mensaje += 'C'
elif 7 > numero >= 6:
    mensaje += 'D'
elif 6 > numero >= 0:
    mensaje += 'F'
else:
    mensaje = 'Valor incorrecto'

print(mensaje)