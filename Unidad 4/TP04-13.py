"""
-----------------------------------------------------------------------------------------------
Título: BARAJA ESPAÑOLA

Fecha: 01/10/2023

Autor: Gianfranco Mazzei

Descripción: Escribir un programa para crear mediante listas por comprensión los naipes de la baraja española de 48 cartas. La lista 
debe contener cadenas de caracteres. Ejemplo: ["1 de Oros", "2 de Oros"... ]. Imprimir la lista por pantalla. (investigar en 
internet el tema “python listas por comprensión producto cartesiano de dos listas”)

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
def cartasNaipes(palos, figuras):
    print("Cantidad de cartas 48")
    listaUno = [[(d,e) ] for d in palos[0] for e in palos[1]]
    for item in listaUno:
        print(item)
    listaDos = [[(a,b) ] for a in figuras[0] for b in figuras[1]]
    for item in listaDos:
        print(item)


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

palos = [[1,2,3,4,5,6,7,8,9],["oro","copa","espada","basto"]]
figuras = [[10,11,12],["rey","caballo","caballero","sota"]]

#-------------------------------------------------
# Procesos
#-------------------------------------------------

cartasNaipes(palos, figuras)

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

