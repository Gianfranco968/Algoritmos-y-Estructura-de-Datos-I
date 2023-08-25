"""
-----------------------------------------------------------------------------------------------
Título: AUMENTO DE LÍMITES DE TARJETAS

Fecha: 17/08/2023

Autor: Gianfranco Mazzei

Descripción: Un banco necesita establecer los nuevos límites de crédito de sus tarjetas. Las de
tipo 1 aumentarán un 25%; las de tipo 2 aumentarán un 35%; las de tipo 3 aumentarán un 40%, y
las de cualquier otro tipo aumentarán un 50%. Desarrollar un algoritmo para calcular el nuevo
límite según el límite actual y el tipo de tarjeta del cliente

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
...



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables
#-------------------------------------------------

limiteActual = 0
nuevoLimite = 0
tipoTarjeta = 0


#-------------------------------------------------
# Procesos
#-------------------------------------------------

limiteActual = int(input("Introducir el límite actual: "))
tipoTarjeta = int(input("Introducir el tipo de tarjeta [1,2,3]: "))

if tipoTarjeta == 1:
    nuevoLimite = 25 * limiteActual / 100 + limiteActual
elif tipoTarjeta == 2:
    nuevoLimite = 35 * limiteActual / 100 + limiteActual
elif tipoTarjeta == 3:
    nuevoLimite = 40 * limiteActual / 100 + limiteActual
else:
    nuevoLimite = 50 * limiteActual / 100 + limiteActual

#-------------------------------------------------
# Resultados
#-------------------------------------------------
print("El nuevo límite es:",nuevoLimite)

