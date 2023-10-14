"""
-----------------------------------------------------------------------------------------------
Título: ADIVINAR NÚMERO CON MANEJADOR DE EXCEPCIONES

Fecha: 14/10/2023

Autor: Gianfranco Mazzei

Descripción: Escribir un programa que juegue con el usuario a adivinar un número. El programa debe generar un número al azar entre 
1 y 500 y el usuario debe adivinarlo. Para eso, cada vez que se introduce un valor se muestra un mensaje indicando si el 
número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga adivinarlo, se debe imprimir en 
pantalla la cantidad de intentos que le tomó hallar el número. Si el usuario introduce algo que no sea un número se 
mostrará un mensaje en pantalla y se lo contará como un intento más.

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


    
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-----------------------------------------------

intentos = 0

#-------------------------------------------------
# Procesos
#-------------------------------------------------
aleatorio = random.randint(1,500)

while True:
    try:
        usuario = int(input("Introducir el número para hallar: "))
        
        if usuario != int(usuario):
            raise ValueError
        if usuario > aleatorio:
            intentos += 1
            print("El número es MENOR al ingresado")
        elif usuario < aleatorio:
            intentos += 1
            print("El número es MAYOR al ingresado")
        elif usuario == aleatorio:
            intentos += 1
            print("HAS ENCONTRADO EL NÚMERO:",aleatorio)
            print("Cantidad de intentos ---->",intentos)
            break
        
    except ValueError:
        print("ERROR --> Dicho valor introducido no es un número, intente nuevamente")
        intentos += 1
#-------------------------------------------------
# Resultados
#-------------------------------------------------


