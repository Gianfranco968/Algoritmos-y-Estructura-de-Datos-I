"""
-----------------------------------------------------------------------------------------------
Título: ELEMENTOS ELIMINADOS

Fecha: 1/9/2023

Autor: Gianfranco Mazzei

Descripción: Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista de 
palabras a eliminar y la lista resultante.

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

listaOriginal = ["UADE","Licenciatura","Ingeniería","Programación"]
listaSecundaria = ["UADE","Programación","Tecnicatura","Labs"]
listaEliminar = []
listaResultante = []


#-------------------------------------------------
# Procesos
#-------------------------------------------------

for palabra in range(len(listaOriginal)):
    if listaOriginal[palabra] in listaSecundaria:
        listaEliminar.append(listaOriginal[palabra])
    else:
        listaResultante.append(listaOriginal[palabra])
    
    if not listaSecundaria[palabra] in listaOriginal:
        listaResultante.append(listaSecundaria[palabra])

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print(listaOriginal)
print(listaSecundaria)
print(listaEliminar)
print(listaResultante)
