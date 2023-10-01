"""
-----------------------------------------------------------------------------------------------
Título: PALABRAS DE FRASE ORDENADAS

Fecha: 30/09/2023

Autor: Gianfranco Mazzei

Descripción: Escribir una función que reciba como parámetro una cadena de caracteres en la que las palabras se encuentran separadas 
por uno o más espacios. Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre 
cada una.

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
def fraseOrdenada(cadena):
    lista = []
    aux = []
    contador = 0
    aumento = 0
    if contador >= 0 and contador < 3:
        for valores in range(0,len(cadena)):
            contador += 1
            lista.append(cadena[valores])
        contador = 0
        
    lista.sort()
    
    for vacio in lista:
        if vacio != " ":
            aux.append(vacio)
            
        aumento = len(aux)
    
    for i in range(1,len(aux) + aumento,2):
        aux.insert(i," ")
        aumento += 1
    print("Palabras ordenadas alfabéticamente de la palabra -->",cadena)
    for elementos in aux:
        print(elementos, end="")


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

cadena = "hola como estas"


#-------------------------------------------------
# Procesos
#-------------------------------------------------

fraseOrdenada(cadena)

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

