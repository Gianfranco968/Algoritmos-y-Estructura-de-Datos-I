"""
-----------------------------------------------------------------------------------------------
Título: TABLA DE N

Fecha: 04/12/23

Autor: Gianfranco Mazzei

Descripción: Escribir una función que reciba un número entero N y devuelva un diccionario con la tabla de multiplicar de N del 1 al 12. 
Escribir también un programa para probar la función.

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

def tablaMultiplicar(N):
    listaValores = []
    listaContenido = []
    diccionario = {}
    
    for valores in range(1,13):
        resultado = N * valores
        listaValores.append(str(N) + " x " + str(valores))
        listaContenido.append(resultado)
    
    diccionario = dict(zip(listaValores, listaContenido))
    
    return diccionario

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------
...


#-------------------------------------------------
# Procesos
#-------------------------------------------------

while True:
    try:
        N = int(input("Ingrese un número entero: "))
        diccionario = tablaMultiplicar(N)
        break
    except ValueError:
        print("ERROR --> El número ingresado no es entero, ingrese nuevamente")

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print(diccionario)
