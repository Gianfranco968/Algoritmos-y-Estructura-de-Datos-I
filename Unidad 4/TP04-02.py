"""
-----------------------------------------------------------------------------------------------
Título: TEXTO CENTRADO EN PANTALLA

Fecha: 30/09/2023

Autor: Gianfranco Mazzei

Descripción: Leer una cadena de caracteres e imprimirla centrada rellenando a izquierda y derecha con guiones para cubrir toda la 
pantalla. Suponer que la pantalla tiene 80 columnas. En el mismo programa hacer 3 versiones: una sin utilizar facilidades 
de Python, otra usando la facilidad de función o método incorporado, y otra usando la facilidad de f-strings.

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

cadena1 = "hola"
cadena2 = "hola"
cadena3 = "hola"
fillcharCadena2 = "-"
longitudCadena2 = 80

#-------------------------------------------------
# Procesos
#-------------------------------------------------

#Sin utilizar facilidades de Python
letras = len(cadena1)
agregarGuiones = 80 - letras
medio = agregarGuiones // 2
for posicion in range(len(cadena1)):
    if posicion == 3:
        print(cadena1, end="")
        for cantidad in range(medio):
            print("-",end="")
    if posicion == 0:
        for cantidad in range(medio):
            print("-",end="")

#Facilidad de función o método incorporado

print("\n")
cadena2 = cadena2.center(longitudCadena2, fillcharCadena2)
print(cadena2)

#Usando f-strings

print("\n")
print(f"{'hola':-^80}")
#-------------------------------------------------
# Resultados
#-------------------------------------------------


