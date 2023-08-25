"""
-----------------------------------------------------------------------------------------------
Título: FECHA VÁLIDA

Fecha: 24/08/2023

Autor: Gianfranco Mazzei

Descripción: Una persona desea llevar el control de los gastos realizados al viajar en el
subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas
decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función que reciba
como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el total gastado
en viajes. Realizar también un programa para verificar el comportamiento de la función.

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
totalGastado = 0

def cantidadDeViajes(cant1):
    if cant1 >= 1 and cant1 <= 20:
        pasaje = 40
        totalGastado = pasaje * cant1
        print("El total gastado en los viajes es: $",totalGastado)
    if cant1 >= 21 and cant1 <= 30:
        pasaje = 40 - (20 * 40 / 100)
        totalGastado = pasaje * cant1
        print("El total gastado en los viajes es: $",totalGastado)
    if cant1 >= 31 and cant1 <= 30:
        pasaje = 40 - (30 * 40 / 100)
        totalGastado = pasaje * cant1
        print("El total gastado en los viajes es: $",totalGastado)
    if cant1 >= 41:
        pasaje = 40 - (40 * 40 / 100)
        totalGastado = pasaje * cant1
        print("El total gastado en los viajes es: $",totalGastado)
    
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------
...


#-------------------------------------------------
# Procesos
#-------------------------------------------------

viajes = int(input("Introducir la cantidad de viajes: "))
cantidadDeViajes(viajes)


#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

