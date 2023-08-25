"""
-----------------------------------------------------------------------------------------------
Título: CAJONES DE NARANJAS

Fecha: 24/08/2023

Autor: Gianfranco Mazzei

Descripción: Resolver el siguiente problema diseñando y utilizando funciones: Un productor frutihortícola desea contabilizar sus 
cajones de naranjas según el peso para poder cargar el camión de reparto. La empresa cuenta con N camiones, y cada
uno puede transportar hasta media tonelada (500 kilogramos). En un cajón caben 100 naranjas con un peso entre 200 y 
300 gramos cada una. Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como
jugo. Se solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos cajones se 
pueden llenar, cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del 
camión no debe ser inferior al 80%; en caso contrario el camión no será despachado por su alto costo

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def calcularNaranjaIndicada():
    peso = random.randint(150,350)
    if peso >= 200 and peso <= 300:
        return "correcto",peso
    else:
        return "incorrecto", 0
    
def calcularCapacidadCamion(num):
    pesoMaximo = 500000
    pesoMinimo = pesoMaximo * 80 // 100
    if num >= pesoMinimo:
        cantidadCamiones = (num + pesoMaximo - 1) // pesoMaximo
        return cantidadCamiones
    else:
        return 0

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

naranjasIndicadas = 0
naranjasDeJugo = 0
pesoNaranjas = 0
cantidadDeCajones = 0
cantidadDeCamiones = 0


#-------------------------------------------------
# Procesos
#-------------------------------------------------

naranjasCosechadas = int(input("Introducir la cantidad de naranjas cosechadas: "))

for x in range(naranjasCosechadas):
    resultado, peso = calcularNaranjaIndicada()
    if resultado == "correcto":
        naranjasIndicadas += 1
        pesoNaranjas += peso
    elif resultado == "incorrecto":
        naranjasDeJugo += 1
        
if naranjasIndicadas <= 100 and naranjasIndicadas > 0:
    cantidadDeCajones += 1
    
if naranjasIndicadas // 100:
    cantidadDeCajones += naranjasIndicadas // 100

cantidadDeCamiones = calcularCapacidadCamion(pesoNaranjas)

sobrantes = naranjasCosechadas - (cantidadDeCajones * 100 + naranjasDeJugo)

if sobrantes <= 0:
    sobrantes = 0

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print("Cantidad de cajones que se pueden llenar:",cantidadDeCajones)
print("Cantidad de naranjas para jugo:",naranjasDeJugo)
print("Cantidad de sobrantes:",sobrantes)
print("Cantidad de camiones necesarios:",cantidadDeCamiones)


