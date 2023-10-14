"""
-----------------------------------------------------------------------------------------------
Título: MES NÚMERO A TEXTO CON MANEJADOR DE EXCEPCIONES

Fecha: 14/10/2023

Autor: Gianfranco Mazzei

Descripción: Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo número se recibe como 
parámetro. Los nombres de los meses deberán obtenerse de una lista de cadenas de caracteres inicializada dentro de la 
función. Devolver una cadena vacía si el número de mes es inválido. La detección de meses inválidos deberá realizarse a 
través de excepciones.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def calcularMes(numero):
    try:
        numero = int(numero)
        listaMes = ['ENERO','FEBRERO','MARZO', 'ABRIL', 'MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']
        if numero > 0 and numero < 13:
            salida = listaMes[numero-1]
            return salida
        else:
            raise ValueError
            return []
    except ValueError:
        return []
        
    
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------



#-------------------------------------------------
# Procesos
#-------------------------------------------------

numero = input("Introducir el número de un mes: ")
salida = calcularMes(numero)

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print(salida)
