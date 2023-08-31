"""
-----------------------------------------------------------------------------------------------
Título: FECHA VÁLIDA

Fecha: 24/08/2023

Autor: Gianfranco Mazzei

Descripción: Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha válida (día, mes, año). Devolver True o False según la fecha sea
correcta o no. Realizar también un programa para verificar el comportamiento de la función.

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
                
def fechaValida(num1,num2,num3):
    if num3 % 4 == 0 and num3 % 100 != 0 or num3 % 400 == 0:
        if num3 <= 2023 and num3 > 0:
            if num2 == 1 or num2 == 3 or num2 == 5 or num2 == 7 or num2 == 8 or num2 == 10 and num2 == 12:
                if num1 <= 31 and num1 >= 0:
                    return True
                else:
                    return False
            if num2 == 4 or num2 == 6 or num2 == 9 or num2 == 11:
                if num1 <= 30 and num1 >= 0:
                    return True
                else:
                    return False
            if num2 == 2:
                if num3 % 4 == 0:
                    if num1 <= 29 and num1 >= 0:
                        return True
                    else:
                        return False
                else:
                    if num1 <= 28 and num1 >= 0:
                        return True
                    else:
                        return False
        else:
            return False
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
dia = int(input("Introducir un dia: "))
mes = int(input("Introducir un mes: "))
anio = int(input("Introducir un año: "))
fechaValida(dia,mes,anio)
if fechaValida(dia,mes,anio) == True:
    print("La fecha introducida es válida")
else:
    print("La fecha introducida es Erronea")

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

