"""
-----------------------------------------------------------------------------------------------
Título: MAYOR ENTRE TRES NUMEROS

Fecha: 24/08/2023

Autor: Gianfranco Mazzei

Descripción: Desarrollar una función que reciba tres números positivos y devuelva el mayor de
los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto
devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para
ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje 
informativo si éste no existe.

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

def numerosPositivos(num1,num2,num3):
    if num1 > num2:
        if num1 > num3:
            print("El maximo hallado existe y es:",num1)
            return
                
    if num2 > num1:
        if num2 > num3:
            print("El maximo hallado existe y es:",num2)
            return
            
    if num3 > num1:
        if num3 > num2:
            print("El maximo hallado existe y es:",num3)
            return
        
    if num1 == num2:
        print("No existe el máximo hallado")
        
    if num2 == num3:
        print("No existe el máximo hallado")
        
    if num3 == num1:
        print("No existe el máximo hallado")
        
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------
...


#-------------------------------------------------
# Procesos
#-------------------------------------------------

primerNumero = int(input("Introducir un número: "))
segundoNumero = int(input("Introducir un segundo número: "))
tercerNumero = int(input("Introducir un tercer número: "))
numerosPositivos(primerNumero,segundoNumero,tercerNumero)


#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

