"""
-----------------------------------------------------------------------------------------------
Título: REMOVE SOBRE CONJUNTOS

Fecha: 04/12/23

Autor: Gianfranco Mazzei

Descripción: Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al usuario y eliminarlos del conjunto mediante 
el método remove, mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1. 
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.

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
# Inicialización de variables y entrada de datos
#-------------------------------------------------

conjunto = {0,1,2,3,4,5,6,7,8,9}

#-------------------------------------------------
# Procesos
#-------------------------------------------------

while True:
    try:
        usuario = int(input("Ingresa el número a eliminar del conjunto [0 hasta 9] {finalizar con -1}: "))
        if usuario != -1:
            conjunto.remove(usuario)
            print("Se eliminó satisfactoriamente el número",usuario,"del conjunto:",conjunto)
        else:
            break
    except KeyError:
        print("ERROR --> Dicho valor no se encuentra en el conjunto")
    
#-------------------------------------------------
# Resultados
#-------------------------------------------------
...


