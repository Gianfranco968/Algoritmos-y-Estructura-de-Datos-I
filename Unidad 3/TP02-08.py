"""
-----------------------------------------------------------------------------------------------
Título: LISTA NORMALIZADA

Fecha: 1/9/2023

Autor: Gianfranco Mazzei

Descripción: Escribir una función que reciba una lista de números enteros como parámetro y la normalice, es decir que todos sus 
elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar
también un programa que permita verificar el comportamiento de la función. Por ejemplo, normalizar([1, 1, 2]) debe 
devolver [0.25, 0.25, 0.50].

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def normalizarLista(lista):
    suma = 0
    for x in range(len(lista)):
        suma += lista[x]
    
    for valores in range(len(lista)):
        division = lista[valores] / suma
        lista[valores] = division
    return lista


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

lista = [1,1,3]

#-------------------------------------------------
# Procesos
#-------------------------------------------------

if normalizarLista(lista):
    print(lista)


#-------------------------------------------------
# Resultados
#-------------------------------------------------



