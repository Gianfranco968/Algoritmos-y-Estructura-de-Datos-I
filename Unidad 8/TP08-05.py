"""
-----------------------------------------------------------------------------------------------
Título: PALABRAS ÚNICAS

Fecha: 04/12/23

Autor: Gianfranco Mazzei

Descripción: Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de 
cada una. Finalmente mostrar las palabras ordenadas según su longitud.

Pendientes: NO TERMINADO!!!!

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
...


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def eliminarRepetidos(frase,conjunto):
    cadena = ""
    contador = 0
    lista = []
    
    for linea in frase:
        cadena += linea
     
    cadena = cadena.split(" ")
    
    for x in range(len(cadena)):
        if contador <= 1:
            if cadena[x] in conjunto:
                contador += 1
            lista.append(cadena[x])
            
        if contador >= 2:
            lista.remove(cadena[x])
            contador = 0
    
    for i in lista:
        print(i, end=" ")

        
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

conjunto = {'hola','uade','algoritmos','facultad'}

#-------------------------------------------------
# Procesos
#-------------------------------------------------

frase = input("Ingrese una frase: ")
eliminarRepetidos(frase, conjunto)

#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

