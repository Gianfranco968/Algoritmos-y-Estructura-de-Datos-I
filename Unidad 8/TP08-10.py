"""
-----------------------------------------------------------------------------------------------
Título: VOCALES POR PALABRA

Fecha: 04/12/23

Autor: Gianfranco Mazzei

Descripción: Crear una función contarvocales(), que reciba una palabra y cuente cuántas letras "a" contiene, cuántas "e", cuántas "i", 
etc. Devolver un diccionario con los resultados. Desarrollar un programa para leer una frase e invocar a la función por 
cada palabra que contenga la misma. Imprimir cada palabra y la cantidad de vocales hallada.

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

def contarVocales(palabra):
    letras = []
    listaVocales = ['a','e','i','o','u']
    listaValores = []
    diccionario = {}
    A = 0
    E = 0
    I = 0
    O = 0
    U = 0
    
    for linea in palabra:
        letras += linea.split(" ")
    
    for x in range(len(letras)):
        if letras[x] == "a":
            A += 1
        elif letras[x] == "e":
            E += 1
        elif letras[x] == "i":
            I += 1
        elif letras[x] == "o":
            O += 1
        elif letras[x] == "u":
            U += 1
            
    listaValores.append(A)
    listaValores.append(E)
    listaValores.append(I)
    listaValores.append(O)
    listaValores.append(U)
    
    diccionario = dict(zip(listaVocales, listaValores))
    return diccionario

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

palabra = []

#-------------------------------------------------
# Procesos
#-------------------------------------------------

frase = input("Ingrese una frase: ")

palabra = frase.split(" ")

for cantidad in range(len(palabra)):
    diccionario = contarVocales(palabra[cantidad])
    print(palabra[cantidad],"-->",diccionario)

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

