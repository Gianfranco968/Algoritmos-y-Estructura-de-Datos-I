"""
-----------------------------------------------------------------------------------------------
Título: SIMULACRO 2DO PARCIAL - 2C23
Fecha: 29/11/23
Autor: Gianfranco Mazzei
Descripción: PDF
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORTADOS
#----------------------------------------------------------------------------------------------

import random

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def agregarAmigoAlSorteo(path):
    ## Desarrolla aquí el código ##
    ## Esta función permite agregar un amigo al archivo
    ## (el string a almacenar debe quedar así "nombre;apellido;dni;num1;num2;num3;num4;num5;num6")
    cadenaCaracter = ""
    contador = 0
    
    usuario = input("Dime el nombre de tu amigo... ")
    apellido = input("Dime su apellido... ")
    digitos = validarEntero("Dime su DNI... ","El valor no es un entero!")
    
    cadenaCaracter = usuario + ";" + apellido + ";" + str(digitos) + ";"
    
    while contador < 6:
        digitos = validarEntero("Dime el número elegido... ","El valor no es un entero!")
        if contador < 5:
            cadenaCaracter += str(digitos) + ";"
            contador += 1
        else:
            cadenaCaracter += str(digitos)
            contador += 1
            
    archivo = open(path, mode="a", encoding="utf-8")
    
    archivo.write(cadenaCaracter)
    
    archivo.close()


def validarEntero(mensajePedido, mensajeError):
    ## Desarrolla aquí el código ##
    ## Esta función se utilizará en las funciones agregarAmigosAlSorteo y repartirPozo
    ## para validar que los valores ingresados (dni y numeros elegidos en el primer caso y monto en el segundo) sean enteros
    ## utilizar un manejador de excepciones 
    ## No es necesario validar que el número jugado esté entre 0 y 90, asumiremos que el usuario siempre ingresa correctamente esos números
    while True:
        try:
            digitos = int(input(mensajePedido))
            return digitos
        except ValueError:
            print(mensajeError)
    

def realizarSorteo(path):
    ## Desarrolla aquí el código ##
    contador = 0
    numerosSorteados = []
    listaGanadores = []
    listaAleatorios = sortearNumeros()
    numerosSorteados = listaAleatorios
    
    archivo = open(path, mode="r", encoding="utf-8")
    
    for linea in archivo:
        campos = linea.replace("\n","").split(";")
        
        for indice in range(3,len(campos)):
            if int(campos[indice]) in numerosSorteados:
                contador += 1
                
        if contador >= 2:
            cadena = campos[0] + " " + campos[1]
            listaGanadores.append(cadena)
            
        contador = 0
    
    return numerosSorteados, listaGanadores
        
        
def sortearNumeros():
    ## Desarrolla aquí el código ##
    ## Esta función crea una lista de 6 números aleatorios distintos
    contador = 0
    aux = 0
    listaAleatorios = []
    
    while contador < 6:
        aleatorio = random.randint(0,90)
        if aleatorio not in listaAleatorios:
            listaAleatorios.append(aleatorio)
            contador += 1
        
    return listaAleatorios


def repartirPozo(listaGanadores):
    ## Desarrolla aquí el código ##
    ## Utilizar un manejador de excepciones si el pozo es vacante
    mensajePedido = "Ingrese un monto total de apuestas válido: "
    mensajeError = "El monto no es un número, intente de nuevo."
    monto = validarEntero("Ingrese un monto total de apuestas válido: ", "Error, introducir un valor válido!")
    try:
        if len(listaGanadores) == 0:
            print("Pozo Vacante!")
            
        for cantidad in range(len(listaGanadores)):
            divisionMonto = monto / len(listaGanadores)
            print(listaGanadores[cantidad] + "ganó $ " + str(divisionMonto))
    except ZeroDivisionError:
        print("Pozo Vacante!")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
#----------------------------------------------------------------------------------------------

numerosSorteados = []
listaGanadores = []
path = "C:/Users/gianf/Desktop/amigos.txt" # IMPORTANTE!!!!! usa esta variable string para el path completo del archivo amigos.txt

# Bloque de menú
#----------------------------------------------------------------------------------------------

while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Cargar Amigo al sorteo")
        print("[2] Sortear!")
        print("[3] Mostrar ganadores!")
        print("[0] Salir del programa")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in ("0","1","2","3"): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para continuar.")

    if opcion == "0": # Opción salir del programa
        exit()

    elif opcion == "1":   # Opción Cargar Amigo al sorteo
        agregarAmigoAlSorteo(path)
        
    elif opcion == "2":   # Sortear!
        numerosSorteados, listaGanadores = realizarSorteo(path)
        print('Números sorteados: ', numerosSorteados)
        print('Ganadores: ', listaGanadores)

    elif opcion == "3":   # Vaciar lista de amigos
        if len(numerosSorteados) > 0:
            repartirPozo(listaGanadores)
        else:
            print("Primero realice el sorteo!")

    print()
    input("Presione ENTER para continuar.")
