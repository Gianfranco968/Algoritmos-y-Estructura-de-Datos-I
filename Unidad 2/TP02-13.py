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

Pendientes: ¡Revisar!

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
numeroFigurado = 0
cantidadDeEliminados = 0

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
    if numeroFigurado != socio:
        if cantidadDeIngresos(socio,listaSocios) and contador == 0:
            cantidad = cantidadDeIngresos(socio,listaSocios)
            contador += 1
            if cantidad == 1:
                print("El socio con número:",socio,"ingresó",cantidad,"vez")
                numeroFigurado = socio
            else:
                print("El socio con número:",socio,"ingresó",cantidad,"veces")
                numeroFigurado = socio
            contador = 0
           
print("Registros de entrada antes de pedir la/s baja/s:",listaSocios,"\n")

while True:
    baja = int(input("Introducir el número de socio para realizar la baja [longitud 5 digitos]{finalizar con 0}: "))
    if baja >= 10000 and baja <= 99999:
        for socio in range(len(listaSocios)):
            if baja in listaSocios:
                listaSocios.remove(baja)
                cantidadDeEliminados += 1
    elif baja == 0:
        break
 
#-------------------------------------------------
# Resultados
#-------------------------------------------------

print("Registros de entrada luego de la/s baja/s:",listaSocios)
print("La cantidad de ingresos eliminados fueron:",cantidadDeEliminados)

