"""
-----------------------------------------------------------------------------------------------
Título: RELOJ

Fecha: 30/09/2023

Autor: Gianfranco Mazzei

Descripción: Desarrollar un programa que pida un valor de hora, un valor de minuto, y un valor de segundo. A partir de esos valores 
mostrar un reloj digital en formato de display HH:MM:SS (cada valor siempre en 2 dígitos). El display deberá avanzar cada 
1 segundo como cualquier reloj digital (es decir que cuando los segundos superen los 59 volverán a 00 y se agregará un 
minuto, etc. Y lo mismo entre los minutos y las horas)

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

#-------------------------------------------------
# Procesos
#-------------------------------------------------

hora = int(input("Introducir la hora: "))
minuto = int(input("Introducir el/los minuto/s: "))
segundo = int(input("Introducir el/los segundo/s: "))

lista.append(hora)
lista.append(minuto)
lista.append(segundo)

while True:
    if lista[2] >= 0 and lista[2] <= 58:
        lista[2] += 1
    else:
        if lista[1] >= 0 and lista[1] <= 58:
            lista[2] = 0
            lista[1] += 1
        else:
            if lista[0] >= 0 and lista[0] <= 58:
                lista[1] = 0
                lista[2] = 0
                lista[0] += 1
    print(lista[0], end=":")
    print(lista[1], end=":")
    print(lista[2], end="")
    print("\n")     

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

