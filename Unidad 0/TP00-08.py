"""
-----------------------------------------------------------------------------------------------
Título: AUMENTO DE LÍMITES DE TARJETAS

Fecha: 17/08/2023

Autor: Gianfranco Mazzei

Descripción: Realizar un programa que solicite la carga de las temperaturas de todos los días de
enero y al finalizar devuelva la temperatura promedio, máxima y mínima del mes.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
...



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------

temperaturaEnero = 0
temperaturaPromedio = 0
temperaturaMinima = 999
temperaturaMaxima = -999
contador = 0

suma = 0


#-------------------------------------------------
# Procesos
#-------------------------------------------------

while contador <= 31:
    temperaturaEnero = int(input("Introducir la temperatura del dia: "))
    if temperaturaEnero < temperaturaMinima:
        temperaturaMinima = temperaturaEnero
        contador += 1
    if temperaturaEnero > temperaturaMaxima:
        temperaturaMaxima = temperaturaEnero
        contador += 1
    suma += temperaturaEnero

temperaturaPromedio = suma / 31

#-------------------------------------------------
# Resultados
#-------------------------------------------------
print("La temperatura máxima fue:",temperaturaMaxima)
print("La temperatura mínima fue:",temperaturaMinima)
print("El promedio fue:",temperaturaPromedio)

