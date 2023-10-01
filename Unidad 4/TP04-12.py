"""
-----------------------------------------------------------------------------------------------
Título: VOCALES ARRIBA

Fecha: 30/09/2023

Autor: Gianfranco Mazzei

Descripción: Se está desarrollando una importante app para tratamiento de texto y nos piden que desarrollemos una función para una 
de las opciones de la app. La función consiste en poner en mayúscula todas las vocales de una frase, por ejemplo, si la 
función recibe el texto “frase de prueba para el nuevo programa de tratamiento de texto” debe devolver “frAsE dE prUEbA 
pArA El nUEvO prOgrAmA dE trAtAmIEntO dE tExtO”. Probar la función desde un programa principal

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
def vocalesMayusculas(cadena):
    vocales = ["a","e","i","o","u"]
    mayuscula = ""
    lista = []
    listaNueva = []
    
    for valores in range(0,len(cadena)):
        lista.append(cadena[valores])
    
    for letras in range(len(lista)):
        if lista[letras] in vocales:
            mayuscula = lista[letras].upper()
            listaNueva.append(mayuscula)
        else:
            listaNueva.append(lista[letras])
            
    for elementos in listaNueva:
        print(elementos, end=" ")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

cadena = "frase de prueba para el nuevo programa de tratamiento de texto"

#-------------------------------------------------
# Procesos
#-------------------------------------------------

vocalesMayusculas(cadena)

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

