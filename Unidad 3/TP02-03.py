"""
-----------------------------------------------------------------------------------------------
Título: ELEMENTOS NUMÉRICOS

Fecha: 1/9/2023

Autor: Gianfranco Mazzei

Descripción: Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento 
imprimiendo la lista luego de invocar a cada función:

a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar 
de dos dígitos.
b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la 
función lo recibe como parámetro.


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
    



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

listaAzar = []
sumatoria = 0


#-------------------------------------------------
# Procesos
#-------------------------------------------------

longitud = random.randint(10,99)

for x in range(longitud):
    numeros = random.randint(1000,9999)
    listaAzar.append(numeros)
print(listaAzar,"\n")
    
for elementos in range(len(listaAzar)):
    sumatoria += listaAzar[elementos]
print("La sumatoria de todos los elementos de la lista es:",sumatoria,"\n")

valor = int(input("Introducir el valor que desea eliminar: "))

for x in range(0,len(listaAzar)-1):
    if listaAzar[x] == valor:
        listaAzar.pop(x)
print(listaAzar)

    
    
#-------------------------------------------------
# Resultados
#-------------------------------------------------



