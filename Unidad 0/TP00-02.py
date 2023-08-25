"""
-----------------------------------------------------------------------------------------------
Título: Asientos de conferencia

Fecha: 17/08/2023

Autor: Gianfranco Mazzei

Descripción: Realizar un programa que permita ingresar la cantidad de inscriptos a una
conferencia y la cantidad de asientos disponibles en el auditorio. Se debe indicar si alcanzan
los asientos. Si los asientos no alcanzan, indicar cuantos faltan para que todos los inscriptos
puedan sentarse.

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
cantidadInscriptos = 0
cantidadAsientos = 0
cantidadAsientosRestantes = 0


#-------------------------------------------------
# Procesos
#-------------------------------------------------

cantidadInscriptos = int(input("Introducir la cantidad de inscriptos: "))
cantidadAsientos = int(input("Introducir la cantidad de asientos: "))
if cantidadAsientos >= cantidadInscriptos:
    print("Los asientos alcanzan para todos")
else:
    cantidadAsientosRestantes = cantidadInscriptos - cantidadAsientos
    print("Faltan",cantidadAsientosRestantes,"asientos para el resto de inscriptos")
    
#-------------------------------------------------
# Resultados
#-------------------------------------------------


