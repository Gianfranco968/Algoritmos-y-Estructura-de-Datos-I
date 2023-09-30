"""
-----------------------------------------------------------------------------------------------
Título: TEMPORIZADOR

Fecha: 30/09/2023

Autor: Gianfranco Mazzei

Descripción: Desarrollar un programa que pida un valor de minuto, y un valor de segundo. A partir de esos valores mostrar un reloj 
digital en formato de display MM:SS (cada valor siempre en 2 dígitos). El display deberá ir en cuenta regresiva cada 1 
segundo hasta llegar a 00:00. Cuando llegue a cero deberá detenerse y mostrar el mensaje “<<<< TIEMPO >>>>”

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

lista = []
contador = 0

#-------------------------------------------------
# Procesos
#-------------------------------------------------
minuto = int(input("Introducir el/los minuto/s: "))
segundo = int(input("Introducir el/los segundo/s: "))

lista.append(minuto)
lista.append(segundo)

while contador == 0:
    if lista[1] > 0 and lista[1] <= 59:
        lista[1] -= 1
    else:
        if lista[0] > 0 and lista[0] <= 59:
            lista[1] = 59
            lista[0] -= 1
    print(lista[0], end=":")
    print(lista[1])

    if lista[1] == 0 and lista[0] == 0:
        contador = 1
        print("<<<<TIEMPO>>>>")

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

