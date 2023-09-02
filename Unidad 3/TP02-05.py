"""
-----------------------------------------------------------------------------------------------
Título: ELEMENTOS AL CUADRADO

Fecha: 1/9/2023

Autor: Gianfranco Mazzei

Descripción: Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. 
Luego se solicita imprimir los últimos 10 valores de la lista.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def numeroCuadrado(num1):
    cuadrado = num1 ** 2
    return cuadrado


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------
listaCuadrado = []


#-------------------------------------------------
# Procesos
#-------------------------------------------------

numero = int(input("Introducir un número: "))

for x in range(1,numero+1):
    listaCuadrado.append(numeroCuadrado(x))

for i in range(-10,len(listaCuadrado)):
    if i <= -1:
        print(listaCuadrado[i],end=" ")

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print("\n")
print(listaCuadrado)

