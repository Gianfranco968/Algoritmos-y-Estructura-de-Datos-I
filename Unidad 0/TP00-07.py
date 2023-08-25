"""
-----------------------------------------------------------------------------------------------
Título: AUMENTO DE LÍMITES DE TARJETAS

Fecha: 17/08/2023

Autor: Gianfranco Mazzei

Descripción: Escribir un programa que, ingresado el precio de lista de un producto, muestre cuanto
le costará al cliente según todas las opciones de pago disponibles (si es en cuotas además del
precio final debe mostrar el valor de cada cuota). Los descuentos o recargos según las formas de
pago son los siguientes:
    En efectivo aplicar 10% de descuento
    Tarjeta 1 pago mantener el precio de lista
    Tarjeta 3 pagos recargar 5%
    Tarjeta 6 pagos recargar 10%
    Tarjeta 12 pagos recargar 15%
Una vez mostrados los valores, el algoritmo debe esperar un nuevo ingreso, y sólo debe finalizar
si se ingresa un precio de 0 pesos (en dicho caso debe terminar sin calcular nada). Se pide usar
un tipo de bucle que evite tener que escribir el input dos veces

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

precioEfectivo = 0
precioTarjetaUnPago = 0
precioTarjetaTresPagos = 0
precioTarjetaSeisPagos = 0
precioTarjetaDocePagos = 0
precioProducto = 0
contador = 0


#-------------------------------------------------
# Procesos
#-------------------------------------------------

while contador == 0:
    precioProducto = int(input("Introducir el precio del producto [finalizar introduciendo 0]: "))
    if precioProducto != 0:
        precioEfectivo = precioProducto - (precioProducto * 10 / 100)
        precioTarjetaUnPago = precioProducto
        precioTarjetaTresPagos = precioProducto + (precioProducto * 5 / 100)
        precioTarjetaSeisPagos = precioProducto + (precioProducto * 10 / 100)
        precioTarjetaDocePagos = precioProducto + (precioProducto * 15 / 100)
    else:
        contador += 1
        break
#-------------------------------------------------
# Resultados
#-------------------------------------------------
    print("El precio en efectivo es:",precioEfectivo)
    print("El precio en 1 cuota con tarjeta es:",precioTarjetaUnPago)
    print("El precio en 3 cuotas con tarjeta es:",precioTarjetaTresPagos)
    print("El precio en 6 cuotas con tarjeta es:",precioTarjetaSeisPagos)
    print("El precio en 12 cuotas con tarjeta es:",precioTarjetaDocePagos)

