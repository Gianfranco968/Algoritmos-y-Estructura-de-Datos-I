"""
-----------------------------------------------------------------------------------------------
Título: COBRO Y VUELTO

Fecha: 17/08/2023

Autor: Gianfranco Mazzei

Descripción: Escribir un programa básico de caja, donde se ingrese el precio total de la compra,
luego se ingrese el monto con el cual el cliente abona la compra, y finalmente informe con un
mensaje si no es suficiente con lo que abonó o, caso contrario, informe el vuelto que se le debe
dar al cliente.

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

montoTotal = 0
montoCliente = 0
vueltoCliente = 0
faltanteCliente = 0

#-------------------------------------------------
# Procesos
#-------------------------------------------------

montoTotal = int(input("Introducir el monto total de la compra: "))
montoCliente = int(input("Introducir el monto del cliente: "))
if montoTotal > montoCliente:
    faltanteCliente = montoTotal - montoCliente
    print("El cliente no pagó lo suficiente, por ende, debe abonar",faltanteCliente,"$")
elif montoTotal < montoCliente:
    vueltoCliente = montoCliente - montoTotal
    print("Se le debe devolver al cliente el monto",vueltoCliente,"$")
else:
    print("El cliente pagó con lo suficiente")

#-------------------------------------------------
# Resultados
#-------------------------------------------------


