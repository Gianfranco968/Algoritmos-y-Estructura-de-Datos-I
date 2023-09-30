"""
-----------------------------------------------------------------------------------------------
Título: CONTRASEÑAS INTERCALADAS

Fecha: 30/09/2023

Autor: Gianfranco Mazzei

Descripción: Los números de claves de dos cajas fuertes están intercalados dentro de un número entero llamado "clave maestra", cuya 
longitud no se conoce. Realizar un programa para obtener ambas claves, donde la primera se construye con los dígitos 
ubicados en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en posiciones pares. Los dígitos 
se numeran desde la izquierda. Ejemplo: Si clave maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.

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
claveMaestra = "18293"


#-------------------------------------------------
# Procesos
#-------------------------------------------------

print("Clave N°1:")
for par in range(len(claveMaestra)):
    if par % 2 == 0:
        print(claveMaestra[par], end="")
print("\n")
print("Clave N°2:")
for impar in range(len(claveMaestra)):
    if impar % 2 != 0:
        print(claveMaestra[impar], end="")

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

