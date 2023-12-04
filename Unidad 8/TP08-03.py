"""
-----------------------------------------------------------------------------------------------
Título: FICHAS DOMINÓ

Fecha: 04/12/23

Autor: Gianfranco Mazzei

Descripción: Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas, por ejemplo: 
(3, 4) y (5, 4). La función devuelve True o False. Escribir también un programa para verificar su comportamiento.

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

def fichas(tupla1, tupla2):
    if tupla1[1] == tupla2[0]:
        return True
    if tupla1[0] == tupla2[0]:
        return True
    if tupla1[1] == tupla2[1]:
        return True
    if tupla1[0] == tupla2[1]:
        return True
    else:
        return False
        
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

while True:
    try:
        primerTuplaA = int(input("Ingresar el primer valor de la primer ficha: "))
        
        if primerTuplaA <= 6 and primerTuplaA >= 0:
            break
        else:
            print("ERROR --> Introducir nuevamente valores entre 0 y 6")
    except ValueError:
        print("ERROR --> Introducir nuevamente valores entre 0 y 6")

while True:
    try:
        primerTuplaB = int(input("Ingresar el segundo valor de la primer ficha: "))
        
        if primerTuplaB <= 6 and primerTuplaB >= 0:
            break
        else:
            print("ERROR --> Introducir nuevamente valores entre 0 y 6")
    except ValueError:
        print("ERROR --> Introducir nuevamente valores entre 0 y 6")

tupla1 = (primerTuplaA, primerTuplaB)
        
while True:
    try:
        segundaTuplaA = int(input("Ingresar el primer valor de la segunda ficha: "))

        if segundaTuplaA <= 6 and segundaTuplaA >= 0:
            break
        else:
            print("ERROR --> Introducir nuevamente valores entre 0 y 6")
    except ValueError:
        print("ERROR --> Introducir nuevamente valores entre 0 y 6")
        
while True:
    try:
        segundaTuplaB = int(input("Ingresar el segundo valor de la segunda ficha: "))
        
        if segundaTuplaB <= 6 and segundaTuplaB >= 0:
            break
        else:
            print("ERROR --> Introducir nuevamente valores entre 0 y 6")
    except ValueError:
        print("ERROR --> Introducir nuevamente valores entre 0 y 6")
        
tupla2 = (segundaTuplaA, segundaTuplaB)

print(fichas(tupla1, tupla2)) #IMPRIME POR PANTALLA TRUE OR FALSE {VERIFICACION}

#-------------------------------------------------
# Resultados
#-------------------------------------------------


