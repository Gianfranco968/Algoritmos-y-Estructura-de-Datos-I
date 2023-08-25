"""
-----------------------------------------------------------------------------------------------
Título: AUMENTO DE LÍMITES DE TARJETAS

Fecha: 17/08/2023

Autor: Gianfranco Mazzei

Descripción: En un mercado los clientes pueden comprar sólo una unidad de cada producto. Realizar
un programa que pida uno por uno los precios de los productos comprados por el cliente, y que al
ingresar un precio igual a cero muestre el total que debe abonar por la compra y la cantidad de
productos comprados.

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

precioProducto = 0
cantidadProductos = 0
totalPrecio = 0


#-------------------------------------------------
# Procesos
#-------------------------------------------------

while True:
    precioProducto = int(input("Introducir el precio del producto [Para finalizar introducir 0]: "))
    if precioProducto != 0:
        cantidadProductos += 1
        totalPrecio += precioProducto
    else:
        break

#-------------------------------------------------
# Resultados
#-------------------------------------------------
print("El monto total es:",totalPrecio)
print("La cantidad de productos comprados:",cantidadProductos)

