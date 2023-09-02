"""
-----------------------------------------------------------------------------------------------
Título: AZAR Y ELEMENTOS IMPARES

Fecha: 1/9/2023

Autor: Gianfranco Mazzei

Descripción: Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera que sean 
impares. El proceso deberá realizarse utilizando listas por comprensión. Imprimir las dos listas por pantalla.

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random



#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------





#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------




#-------------------------------------------------
# Procesos
#-------------------------------------------------

listaAleatorio = [random.randint(1,100) for x in range(20)]
listaImpar = [listaAleatorio[n] for n in range(len(listaAleatorio)) if listaAleatorio[n] % 2]

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print(listaAleatorio)
print(listaImpar)


