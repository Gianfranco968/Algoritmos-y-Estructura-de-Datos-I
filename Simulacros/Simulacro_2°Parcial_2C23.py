"""
-----------------------------------------------------------------------------------------------
Título: SIMULACRO - 2DO PARCIAL 2023
Fecha: 16/11/23
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
    nombre = ""
    dni = 0
    contador = 0
    amigos = open(path, mode="a", encoding="utf-8")
    nombre = input("Introducir el nombre del nuevo usuario: ").upper()
    apellido = input("Introducir el apellido del nuevo usuario: ").upper()
    
    while True:
        try:
            dni = int(input("Introducir el DNI: "))
            break
        except ValueError:
            print("El DNI debe ser ENTERO")
            
    cadenaCaracter = nombre + ";" + apellido + ";" + str(dni)
    
    while contador < 6:
        numero = validarEntero("Introducir un número ENTERO: ","El número debe ser ENTERO")
        cadenaCaracter = cadenaCaracter + ";" + str(numero)
        contador += 1
    
    amigos.write(cadenaCaracter + "\n")
    amigos.close()


def validarEntero(mensajePedido, mensajeError):
    ## Desarrolla aquí el código ##
    ## Esta función se utilizará en las funciones agregarAmigosAlSorteo y repartirPozo
    ## para validar que los valores ingresados (dni y numeros elegidos en el primer caso y monto en el segundo) sean enteros
    ## utilizar un manejador de excepciones 
    ## No es necesario validar que el número jugado esté entre 0 y 90, asumiremos que el usuario siempre ingresa correctamente esos números
    try:
        numero = int(input(mensajePedido))
        return numero
    except ValueError:
        print(mensajeError)
        

def realizarSorteo(path):
    ## Desarrolla aquí el código ##
    numerosSorteados = []
    listaGanadores = []
    contador = 0
    numerosSorteados = sortearNumeros()
    amigos = open(path, mode="r", encoding="utf-8")
    
    for linea in amigos:
        campos = linea.replace("\n","").split(";")
        for datos in range(3,9):
            for numerosSalidos in range(0,6):
                if int(campos[datos]) == numerosSorteados[numerosSalidos]:
                    contador += 1
        if contador >= 2:
            ganador = campos[0] + " " + campos[1]
            listaGanadores.append(ganador)
        contador = 0
    amigos.close()
    
    return numerosSorteados, listaGanadores
    

def sortearNumeros():
    ## Desarrolla aquí el código ##
    ## Esta función crea una lista de 6 números aleatorios distintos
    numerosSorteados = []
    contador = 0
    cantidad = 0
    while cantidad < 6:
        aleatorio = random.randint(0,90)
        contador = 1
        for numeros in range(len(numerosSorteados)):
            if contador != 2:
                if numerosSorteados[numeros] != aleatorio:
                    contador = 1
                else:
                    contador = 2
        if contador == 1:
            numerosSorteados.append(aleatorio)
            cantidad += 1
            contador = 0
    return numerosSorteados


def repartirPozo(listaGanadores):
    ## Desarrolla aquí el código ##
    ## Utilizar un manejador de excepciones si el pozo es vacante
    mensajePedido = "Ingrese un monto total de apuestas válido: "
    mensajeError = "El monto no es un número, intente de nuevo."
    monto = validarEntero(mensajePedido, mensajeError)
    cantidadGanadores = len(listaGanadores)

    try:
       division = monto / cantidadGanadores
       for ganadores in range(len(listaGanadores)):
           print(listaGanadores[ganadores],"ganó $",division)
    except ZeroDivisionError:
        print("Pozo vacante")
        

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
#----------------------------------------------------------------------------------------------

numerosSorteados = []
listaGanadores = []
path = "C:/Users/Gian/Desktop/amigos.txt" # IMPORTANTE!!!!! usa esta variable string para el path completo del archivo amigos.txt

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
