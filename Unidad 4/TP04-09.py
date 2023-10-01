"""
-----------------------------------------------------------------------------------------------
Título: FUNCIÓN ELIMINAR SUBCADENA

Fecha: 30/09/2023

Autor: Gianfranco Mazzei

Descripción: Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de 
caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la 
misma. Escribir una función para cada uno de los siguientes casos:
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
def eliminarSubcadenaRebanada(cadena, posicion):
    longitud = len(cadena[posicion:])
    print("Utilizando rebanadas -->","Posicion:",posicion, "Caracteres:",longitud)
    print(cadena[0:posicion])

def eliminarSubcadena(cadena, posicion):
    contador = 0
    aumento = 0
    lista = []
    aux = []
    eliminado = []
    if contador >= 0 and contador < 3:
        for valores in range(0,len(cadena)):
            contador += 1
            lista.append(cadena[valores])
        contador = 0
        
        for i in range(len(lista)):
            if i < posicion:
                aux.append(lista[i])
            elif i >= posicion:
                eliminado.append(lista[i])
        
        longitud = len(eliminado)

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

conRebanadas = eliminarSubcadenaRebanada(cadena,posicion)
sinRebanadas = eliminarSubcadena(cadena,posicion)

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

