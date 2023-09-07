"""
-----------------------------------------------------------------------------------------------
Título: REGISTRO DE VISITAS DE SOCIOS

Fecha: 07/09/2023

Autor: Gianfranco Mazzei

Descripción: Resolver el siguiente problema, utilizando funciones: 
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se ingresa el número de socio de cinco 
dígitos hasta ingresar un cero como fin de carga.

Se solicita:

a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola vez en el informe).
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los registros de 
entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron.

Pendientes: ¡¡¡¡¡INCOMPLETO - ARREGLARR!!!!!

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def cantidadDeIngresos(socio,listaSocios):
    cantidad = listaSocios.count(socio)
    return cantidad

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

listaSocios = []
contador = 0

#-------------------------------------------------
# Procesos
#-------------------------------------------------

while True:
    numeroDeSocio = int(input("Introducir el número de socio [longitud 5 digitos]{finalizar con 0}: "))
    if numeroDeSocio >= 10000 and numeroDeSocio <= 99999:
        listaSocios.append(numeroDeSocio)
    elif numeroDeSocio == 0:
        break
    
for numeros in range(len(listaSocios)):
    socio = listaSocios[numeros]
    if cantidadDeIngresos(socio,listaSocios) and contador == 0:
        cantidad = cantidadDeIngresos(socio,listaSocios)
        contador += 1
        if cantidad == 1:
            print("El socio con número:",socio,"ingresó",cantidad,"vez")
        else:
            print("El socio con número:",socio,"ingresó",cantidad,"veces")
        contador = 0
#-------------------------------------------------
# Resultados
#-------------------------------------------------


