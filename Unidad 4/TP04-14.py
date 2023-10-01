"""
-----------------------------------------------------------------------------------------------
Título: VERIFICACIÓN DE DIRECCIÓN DE EMAIL

Fecha: 01/10/2023

Autor: Gianfranco Mazzei

Descripción: Se solicita crear un programa para leer direcciones de correo electrónico y verificar si representan una dirección válida. 
Por ejemplo usuario@dominio.com.ar. Para que una dirección sea considerada válida el nombre de usuario debe poseer 
solamente caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe tener al menos un carácter 
y tiene que finalizar con “.com.ar”

Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mostrar un listado de todos los dominios, sin 
repetirlos y ordenados alfabéticamente, recordando que las direcciones de mail no son case sensitive

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
def direccionEmail(cadena):
    contador = 0
    caracter = "@"
        
    for elemento in cadena:
        if elemento == caracter:
            contador += 1
    
    if contador == 1 and cadena.endswith(".com.ar"):
        print("Es Válido")  
    else:
        print("ERROR --> Introducir una dirección válida")



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------



#-------------------------------------------------
# Procesos
#-------------------------------------------------

cadena = input("Introducir una dirección email: ")
direccionEmail(cadena)

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

