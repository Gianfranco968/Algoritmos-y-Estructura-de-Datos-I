"""
-----------------------------------------------------------------------------------------------
Título: VERIFICAR ORDEN DE ELEMENTOS

Fecha: 1/9/2023

Autor: Gianfranco Mazzei

Descripción: Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente 
o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
además un programa para verificar el comportamiento de la función.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def verificarOrdenamientoLista(lista):
    ordenada = []
    
    for x in range(len(lista)):
        ordenada.append(lista[x])
        ordenada.sort()
        
    if lista == ordenada:
        return True
    else:
        return False

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

lista = ["a","b","c","e","d"]


#-------------------------------------------------
# Procesos
#-------------------------------------------------

if verificarOrdenamientoLista(lista) == True:
    print("True, la lista está ordenada de manera ascendiente")
else:
    print("False, la lista está ordenada de manera descendente")


#-------------------------------------------------
# Resultados
#-------------------------------------------------




