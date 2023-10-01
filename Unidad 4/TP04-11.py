"""
-----------------------------------------------------------------------------------------------
Título: REEMPLAZO DE PALABRA

Fecha: 01/10/2023

Autor: Gianfranco Mazzei

Descripción: Desarrollar una función para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres y 
devolver la cadena obtenida y un entero con la cantidad de reemplazos realizados. Tener en cuenta que sólo deben 
reemplazarse palabras completas, y no fragmentos de palabras. Escribir también un programa para verificar el 
comportamiento de la función.

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
def reemplazoPalabra(cadena,reemplazo,nueva):
    listaReemplazo = []
    palabras = cadena.split()
    cantidadReemplazos = 0
    
    for palabra in palabras:
        if palabra == reemplazo:
            listaReemplazo.append(nueva)
            cantidadReemplazos += 1
        else:
            listaReemplazo.append(palabra)
    
    for elementos in listaReemplazo:
        print(elementos, end=" ")
    
    print("\n")
    print("Cantidad de reemplazos:",cantidadReemplazos)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

cadena = "Hola como estas"
reemplazo = "estas"
nueva = "vivis"


#-------------------------------------------------
# Procesos
#-------------------------------------------------

reemplazoPalabra(cadena,reemplazo,nueva)

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

