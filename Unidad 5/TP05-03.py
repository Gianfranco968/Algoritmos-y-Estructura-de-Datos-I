"""
-----------------------------------------------------------------------------------------------
Título: STOP DE CÓDIGO CON MANEJADOR DE EXCEPCIONES

Fecha: 14/10/2023

Autor: Gianfranco Mazzei

Descripción: Todo programa Python es susceptible de ser interrumpido mediante la pulsación de las teclas Ctrl-C, lo que genera una 
excepción del tipo KeyboardInterrupt. Realizar un programa para imprimir los números enteros entre 1 y 100000, y que 
solicite confirmación al usuario antes de detenerse cuando se presione Ctrl-C.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

        
    
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

numero = 1

#-------------------------------------------------
# Procesos
#-------------------------------------------------

try:
    while True:
        while numero <= 100000:
            print(numero)
            numero += 1
            if numero >= 100000:
                break
        break
except KeyboardInterrupt:
    print("\n")
    usuario = input("Desea finalizar? [ENTER] para finalizar ")
    print("FINALIZADO")

#-------------------------------------------------
# Resultados
#-------------------------------------------------


