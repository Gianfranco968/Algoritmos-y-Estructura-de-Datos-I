"""
-----------------------------------------------------------------------------------------------
Título: FUNCIÓN TOMAR SUBCADENA

Fecha: 30/09/2023

Autor: Gianfranco Mazzei

Descripción: Desarrollar una función que extraiga una subcadena de una cadena de caracteres, indicando la posición y la cantidad de 
caracteres deseada. Devolver la subcadena como valor de retorno. Escribir también un programa para verificar el 
comportamiento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-7890" extraer la subcadena que 
comienza en la posición 25 y tiene 9 caracteres, resultando la subcadena "4356-7890". Escribir una función para cada uno 
de los siguientes casos:
    A. Utilizando rebanadas
    B. Sin utilizar rebanadas

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
def extraerSubcadenaRebanada(cadena, posicion):
    longitud = len(cadena[posicion:])
    print("Utilizando rebanadas -->","Posicion:",posicion, "Caracteres:",longitud)
    print(cadena[posicion:])

def extraerSubcadena(cadena, posicion):
    aumento = 0
    lista = []
    aux = []
    for valores in range(0,len(cadena)):
        lista.append(cadena[valores])
        
    for i in range(len(lista)):
        if i >= posicion:
            aux.append(lista[i])
        
    longitud = len(aux)

    print("Sin utilizar rebanadas -->","Posicion:",posicion, "Caracteres:",longitud)
    for elementos in aux:
        print(elementos,end="")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

cadena = "El número de télefono es 4356-7890"
posicion = 25

#-------------------------------------------------
# Procesos
#-------------------------------------------------

conRebanadas = extraerSubcadenaRebanada(cadena,posicion)
sinRebanadas = extraerSubcadena(cadena,posicion)

#-------------------------------------------------
# Resultados
#-------------------------------------------------


