"""
-----------------------------------------------------------------------------------------------
Título: RAIZ CUADRADA CON MANEJADOR DE EXCEPCIONES

Fecha: 12/10/2023

Autor: Gianfranco Mazzei

Descripción: La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del módulo math. Escribir un programa que 
utilice esta función para calcular la raíz cuadrada de un número cualquiera ingresado a través del teclado. El programa 
debe utilizar manejo de excepciones para evitar errores si se ingresa un número negativo.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

import math

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def calcularRaiz():
    while True:
        try:
            usuario = float(input("Introducir un valor para calcular su raíz cuadrada: "))
            raiz = math.sqrt(usuario)
            return raiz, usuario
            
        except ValueError:
            print("ERROR --> No se puede calcular la raíz de un número negativo. Tampoco se aceptan letras o símbolos ")
        
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------



#-------------------------------------------------
# Procesos
#-------------------------------------------------

raiz, usuario = calcularRaiz()

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print("La raiz del número",usuario,"es:",raiz)
