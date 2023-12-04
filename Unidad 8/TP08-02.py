"""
-----------------------------------------------------------------------------------------------
Título: DESCOMPOSICIÓN DE EMAIL

Fecha: 04/12/23

Autor: Gianfranco Mazzei

Descripción: Desarrollar un programa que utilice una función que reciba como parámetro una cadena de caracteres conteniendo una 
dirección de correo electrónico y devuelva una tupla con las distintas partes que componen dicha dirección. Ejemplo: 
alguien@uade.edu.ar -> (alguien, uade, edu, ar)

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

def direccion(correo):
    usuario = ""
    institucion = ""
    dominio = ""
    pais = ""
    cadenaAux = ""
    lista = []
    listaAux = []
    
    correo = list(correo)
    
    for indice in correo:
        if indice != "@":
            correo = indice.replace("."," ")
        if indice == "@":
            correo = indice.replace("@"," ")
        lista += correo
    
    for x in range(len(lista)):
        if lista[x] != " ":
            cadenaAux += lista[x]
        else:
            cadenaAux += " "
            
    cadenaAux = cadenaAux.split(" ")
    
    tupla = (cadenaAux[0], cadenaAux[1], cadenaAux[2], cadenaAux[3])
    
    return tupla
        
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

correo = input("Ingresar una dirección de correo: ")
tupla = direccion(correo)

#-------------------------------------------------
# Resultados
#-------------------------------------------------

print(tupla)

