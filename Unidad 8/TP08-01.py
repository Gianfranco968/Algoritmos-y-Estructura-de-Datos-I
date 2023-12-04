"""
-----------------------------------------------------------------------------------------------
Título: FECHA CORTA A EXTENDIDA

Fecha: 04/12/23

Autor: Gianfranco Mazzei

Descripción: Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena 
de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12,10,17) devuelve "12 de octubre 
de 2017". Escribir también un programa para verificar su comportamiento.

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
def fechaExtendida(tupla):
    fechaCompleta = ""
    
    meses = ('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    
    if int(tupla[0]) <= 31 and int(tupla[1]) <= 12:
        fechaCompleta = str(tupla[0]) + " " + "de" + " " + str(meses[int(tupla[1])-1]) + " " + "de" + " " + "20" + str(tupla[2])
    else:
        print("ERROR --> Fecha inválida")
        
    return fechaCompleta


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

dia = input("Ingrese el día: ")
mes = input("Ingrese el mes: ")
año = int(input("Ingrese el año: "))

tupla = (dia, mes, año)

fechaCompleta = fechaExtendida(tupla)


#-------------------------------------------------
# Resultados
#-------------------------------------------------
print(fechaCompleta)

