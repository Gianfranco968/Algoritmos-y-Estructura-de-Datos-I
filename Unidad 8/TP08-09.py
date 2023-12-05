"""
-----------------------------------------------------------------------------------------------
Título: DICCIONARIO RECORTADO

Fecha: 04/12/23

Autor: Gianfranco Mazzei

Descripción: Desarrollar una función eliminarClaves() que reciba como parámetros un diccionario y una lista de claves. La función debe 
eliminar del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor que indique 
si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento.

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

def eliminarClaves(diccionario,lista):
    verificar = 1
    for claves in range(len(lista)):
        del diccionario[lista[claves]]
    return diccionario, verificar


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

diccionario = {43442055:'Gianfranco', 43254054: 'Julieta', 38243589: 'Fernando', 42059455: 'Oscar'}
lista = [43254054,42059455]

#-------------------------------------------------
# Procesos
#-------------------------------------------------

diccionario, verificar = eliminarClaves(diccionario,lista)

if verificar == 1:
    print("Operación exitosa!")
    print(diccionario)

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

