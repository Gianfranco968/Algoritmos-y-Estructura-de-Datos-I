"""
-----------------------------------------------------------------------------------------------
Título: ELEMENTOS REPETIDOS

Fecha: 1/9/2023

Autor: Gianfranco Mazzei

Descripción: Escribir funciones para:

a. Generar una lista de 50 números aleatorios del 1 al 100.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no 
debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin 
importar el orden.

Combinar estas tres funciones en un mismo programa.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
listaAleatoria = []
def numerosAleatorios():
    for i in range(50):
        numeros = random.randint(1,100)
        listaAleatoria.append(numeros)
    print(listaAleatoria)
numerosAleatorios()

def numerosRepetidos(listaAleatoria):
    numeros = set()
    
    for elemento in listaAleatoria:
        if elemento in numeros:
            return True
        numeros.add(elemento)

segundaLista = []
contador = 0
def numerosUnicos(listaAleatoria):
    numeros = set()
    
    for elemento in listaAleatoria:
        if elemento in numeros:
            contador = 0
        else:
            contador = 1
            segundaLista.append(elemento)
        numeros.add(elemento)
        contador = 0
        
    print(segundaLista)
numerosUnicos(listaAleatoria)

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------



#-------------------------------------------------
# Procesos
#-------------------------------------------------

if numerosRepetidos(listaAleatoria) == True:
    print(True)
    

#-------------------------------------------------
# Resultados
#-------------------------------------------------


