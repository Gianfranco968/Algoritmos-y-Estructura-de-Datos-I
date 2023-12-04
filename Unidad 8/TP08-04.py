"""
-----------------------------------------------------------------------------------------------
Título: ÁNGULO ENTRE VECTORES 

Fecha: 04/12/23

Autor: Gianfranco Mazzei

Descripción: En geometría un vector es un segmento de recta orientado que va desde un punto A hasta un punto B. Los vectores en el 
plano se representan mediante un par ordenado de números reales (x, y) llamados componentes. Para representarlos 
basta con unir el origen de coordenadas con el punto indicado en sus componentes.

Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo basta calcular su producto escalar 
y verificar si es igual a 0. Ejemplo:
    A = (2,3) y B = (-3,2) => 2 * (-3) + 3 * 2 = -6 + 6 = 0 => Son ortogonales
    
Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor de verdad indicando si son ortogonales 
o no. Desarrollar también un programa que permita verificar el comportamiento de la función.


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

def vectoresOrtogonales(vector1, vector2):
    if (vector1[0] * vector2[0]) + (vector1[1] * vector2[1]) == 0:
        return True
    else:
        return False
        
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
        primerVectorA = int(input("Ingresar el valor X del primer vector: "))
        break
    except ValueError:
        print("ERROR --> Ingrese nuevamente un valor correcto")

while True:
    try:
        primerVectorB = int(input("Ingresar el valor Y del primer vector: "))
        break
    except ValueError:
        print("ERROR --> Ingrese nuevamente un valor correcto")

vector1 = (primerVectorA, primerVectorB)

while True:
    try:
        segundoVectorA = int(input("Ingresar el valor X del segundo vector: "))
        break
    except ValueError:
        print("ERROR --> Ingrese nuevamente un valor correcto")
        
while True:
    try:
        segundoVectorB = int(input("Ingresar el valor Y del segundo vector: "))
        break
    except ValueError:
        print("ERROR --> Ingrese nuevamente un valor correcto")

vector2 = (segundoVectorA, segundoVectorB)

if vectoresOrtogonales(vector1, vector2) == True:
    print("Los vectores:",vector1,vector2,"son ortogonales")
else:
    print("Los vectores:",vector1,vector2,"NO son ortogonales")

#-------------------------------------------------
# Resultados
#-------------------------------------------------


