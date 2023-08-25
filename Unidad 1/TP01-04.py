"""
-----------------------------------------------------------------------------------------------
Título: BILLETES SEGÚN VUELTO

Fecha: 24/08/2023

Autor: Gianfranco Mazzei

Descripción: Un comercio de electrodomésticos necesita para su línea de cajas un programa que le
indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números
enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes
de cada denominación deben ser entregados al cliente como vuelto, de tal forma que se minimice
la cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1.
Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de
$317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete
de $20, 1 billete de $10 y 3 billetes de $1.

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

def calcularCambio(num1, num2):
    billetes_quinientos = 0
    billetes_cien = 0
    billetes_cincuenta = 0
    billetes_veinte = 0
    billetes_diez = 0
    billetes_cinco = 0
    billetes_uno = 0
    devolucion = num2 - num1
    print("El vuelto es:")
    while devolucion != 0:
        if devolucion >= 500:
            billetes_quinientos = devolucion // 500
            print(billetes_quinientos,"billetes de $500")
            devolucion = devolucion % 500

        if devolucion >= 100 and devolucion < 500:
            billetes_cien = devolucion // 100
            print(billetes_cien,"billetes de $100")
            devolucion = devolucion % 100
            
        if devolucion >= 50 and devolucion < 100:
            billetes_cincuenta = devolucion // 50
            print(billetes_cincuenta,"billetes de $50")
            devolucion = devolucion % 50
        
        if devolucion >= 20 and devolucion < 50:
            billetes_veinte = devolucion // 20
            print(billetes_veinte,"billetes de $20")
            devolucion = devolucion % 20
            
        if devolucion >= 10 and devolucion < 20:
            billetes_diez = devolucion // 10
            print(billetes_diez,"billetes de $10")
            devolucion = devolucion % 10
            
        if devolucion >= 5 and devolucion < 10:
            billetes_cinco = devolucion // 5
            print(billetes_cinco,"billetes de $5")
            devolucion = devolucion % 5
        
        if devolucion >= 1 and devolucion < 5:
            billetes_uno = devolucion // 1
            print(billetes_uno,"billetes de $1")
            devolucion = devolucion % 1

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------



#-------------------------------------------------
# Procesos
#-------------------------------------------------

totalCompra = int(input("Introducir el total de la compra: "))
dineroRecibido = int(input("Introducir con cuanto paga: "))

if totalCompra > dineroRecibido:
    print("El dinero recibido es INSUFICIENTE")
else:
    calcularCambio(totalCompra,dineroRecibido)


#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

