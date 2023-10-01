"""
-----------------------------------------------------------------------------------------------
Título: PUNTO CADA 3 DÍGITOS

Fecha: 30/09/2023

Autor: Gianfranco Mazzei

Descripción: Escribir una función que reciba una cadena que contiene un número entero de muchos dígitos y devuelva una cadena con 
el mismo número, pero con los puntos de las separaciones de miles. Por ejemplo, si recibe 1234567890, debe devolver 
1.234.567.890

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
# Inicialización de variables y entrada de datos
#-------------------------------------------------

cadena = "1234567890"
contador = 0
aumento = 0
lista = []

#-------------------------------------------------
# Procesos
#-------------------------------------------------

if contador >= 0 and contador < 3:
    for valores in range(0,len(cadena)):
        contador += 1
        lista.append(cadena[valores])
    contador = 0

if len(lista) % 3 == 0:
    aumento = (len(lista) // 3) - 1
else:
    aumento = (len(lista) // 3)

lista = lista[::-1]

for i in range(3,len(lista) + aumento,4):
    lista.insert(i,".")
    aumento += 1

lista = lista[::-1]

for elementos in lista:
    print(elementos,end="")
#-------------------------------------------------
# Resultados
#-------------------------------------------------


