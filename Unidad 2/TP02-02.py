"""
-----------------------------------------------------------------------------------------------
Título: MES NÚMERO A TEXTO

Fecha: 1/9/2023

Autor: Gianfranco Mazzei

Descripción: Escribir una función que reciba un número de mes y devuelva una cadena con el nombre del mes.
Probar la función desde un programa principal con un input para la entrada del número de mes, luego la llamada a la 
función con dicho número como argumento, y finalmente un print de lo que la función devuelve.

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
def devolverMes(num1):
    if num1 == 1:
        return "Enero"
    elif num1 == 2:
        return "Febrero"
    elif num1 == 3:
        return "Marzo"
    elif num1 == 4:
        return "Abril"
    elif num1 == 5:
        return "Mayo"
    elif num1 == 6:
        return "Junio"
    elif num1 == 7:
        return "Julio"
    elif num1 == 8:
        return "Agosto"
    elif num1 == 9:
        return "Septiembre"
    elif num1 == 10:
        return "Octubre"
    elif num1 == 11:
        return "Noviembre"
    elif num1 == 12:
        return "Diciembre"


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

listaMes = []

#-------------------------------------------------
# Procesos
#-------------------------------------------------

mes = int(input("Introducir el número de un mes: "))

listaMes.append(devolverMes(mes))

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print(listaMes)

