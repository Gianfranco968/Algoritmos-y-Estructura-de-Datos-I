"""
-----------------------------------------------------------------------------------------------
Título: CLAVES PARA VALOR

Fecha: 05/12/23

Autor: Gianfranco Mazzei

Descripción: Escribir una función buscarClave() que reciba como parámetros un diccionario y un valor, y devuelva una lista de claves 
que apunten ("mapeen") a ese valor en el diccionario. Comprobar el comportamiento de la función mediante un programa 
apropiado.

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

def buscarClave(diccionario,valor):
    listaDelValor = []
    listaValores = list(diccionario.values())
    listaClaves = list(diccionario.keys())
    
    for valores in range(len(listaValores)):
        if listaValores[valores] == valor:
            listaDelValor.append(listaClaves[valores])
            
    return listaDelValor

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

diccionario = {43442055:'Gianfranco', 18226322: 'Jorge', 23356731: 'Manuel', 54243255: 'Jorge'}
valor = 'Jorge'

#-------------------------------------------------
# Procesos
#-------------------------------------------------

listaDelValor = buscarClave(diccionario,valor)

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print("El valor",valor,"tiene asignado dicha lista -->",listaDelValor)
