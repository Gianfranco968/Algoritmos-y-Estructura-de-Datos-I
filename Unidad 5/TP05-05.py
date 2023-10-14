"""
-----------------------------------------------------------------------------------------------
Título: INDEX CON MANEJADOR DE EXCEPCIONES

Fecha: 14/10/2023

Autor: Gianfranco Mazzei

Descripción: El método index permite buscar un elemento dentro de una lista, devolviendo la posición que éste ocupa. Sin embargo, 
si el elemento no pertenece a la lista se produce una excepción de tipo ValueError. Desarrollar un programa que cargue 
una lista con números enteros ingresados a través del teclado (terminando con -1) y permita que el usuario ingrese el 
valor de algunos elementos para visualizar la posición que ocupan, utilizando el método index. Si el número no pertenece 
a la lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el proceso al tercer error detectado. 
No utilizar el operador in durante la búsqueda.

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

lista = []
maximosIntentos = 3
contador = 0

#-------------------------------------------------
# Procesos
#-------------------------------------------------
while True:
    elemento = input("Introduce un elemento para la lista (finalizar con '-1'): ")
    if elemento == "-1":
        break
    else:
        lista.append(elemento)

print("Lista:", lista)

while contador < maximosIntentos:
    try:
        usuario = input("Introduce un elemento a buscar: ")
        posicion = lista.index(usuario)
        print("El valor",usuario,"está en la posición:",posicion)
        break
    except ValueError:
        print("ERROR --> Elemento no encontrado. Inténtalo de nuevo.")
        contador += 1
else:
    print("Se agotaron los 3 intentos")

#-------------------------------------------------
# Resultados
#-------------------------------------------------


