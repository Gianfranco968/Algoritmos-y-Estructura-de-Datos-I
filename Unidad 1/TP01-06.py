"""
-----------------------------------------------------------------------------------------------
Título: CONCATENAR BÁSICO

Fecha: 24/08/2023

Autor: Gianfranco Mazzei

Descripción: Desarrollar una función que reciba como parámetros dos números enteros positivos y
devuelva el número que resulte de concatenar ambos valores. Por ejemplo, si recibe 1234 y 567
debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase, ni
tampoco concatenar strings mediante la conversión de número a cadena.

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def concatenarDosNumeros(num1,num2):
    num2_digitos = 1
    contador = num2
    while contador > 9:
        contador //= 10
        num2_digitos += 1
    
    multiplicador = 10 ** num2_digitos
    resultado = num1 * multiplicador
    resultado += num2
    print(resultado) 
        
    

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------



#-------------------------------------------------
# Procesos
#-------------------------------------------------
numeroA = int(input("Introducir un número: "))
numeroB = int(input("Introducir otro número: "))
concatenarDosNumeros(numeroA,numeroB)

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

