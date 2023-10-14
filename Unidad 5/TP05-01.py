"""
-----------------------------------------------------------------------------------------------
Título: CADENAS A REALES CON MANEJADOR DE EXCEPCIONES

Fecha: 12/10/2023

Autor: Gianfranco Mazzei

Descripción: Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos 
valores y devuelva el resultado como un número real. Devolver -1 si alguna de las cadenas no contiene un número válido, 
utilizando manejo de excepciones para detectar el error.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def numerosReales(cadena1, cadena2):
    while True:
        try:
            cadena1 = float(input("Introducir un número real: "))
            cadena2 = float(input("Introducir otro número real: "))
            suma = cadena1 + cadena2
            if cadena1 == float or cadena2 == float:
                raise ValueError
            else:
                print("La suma correspondiente es:",suma)
                
        except ValueError:
            print("-1")
            break
    
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

cadena1 = ""
cadena2 = ""

#-------------------------------------------------
# Procesos
#-------------------------------------------------

numerosReales(cadena1,cadena2)

#-------------------------------------------------
# Resultados
#-------------------------------------------------


