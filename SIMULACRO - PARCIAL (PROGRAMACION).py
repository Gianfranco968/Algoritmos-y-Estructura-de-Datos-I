"""
-----------------------------------------------------------------------------------------------
Título: SIMULACRO PARCIAL 2C23 [PROGRAMACIÓN 1]
Fecha: 28/09/2023
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
def agregarAmigosAlSorteo(_listaDeAmigos, _listaDeApuestas):
    while True:
        usuario = input("Qué amigo desea agregar a la lista? (Introducir 'fin' para finalizar la carga): ")
        
        if usuario != "fin":
            _listaDeAmigos.append(usuario)
        else:
            return _listaDeAmigos, _listaDeApuestas
            break
    
        importe = int(input("Qué importe suma al pozo acumulado?: "))
        _listaDeApuestas.append(importe)

def pozoAcumulado(_listaDeApuestas):
    suma = 0
    for valores in range(len(_listaDeApuestas)):
        suma += _listaDeApuestas[valores]
    return suma

def realizarSorteo(_listaDeAmigos, _listaDeApuestas):
    contador = 1
    aux = []
    if len(_listaDeAmigos) < 4:
        print("Participantes:",_listaDeAmigos)
        print("Al haber menos de 4 partipantes el sorteo no se puede hacer")
    else:  
        for nombres in range(len(_listaDeAmigos)):
            nombres = random.randint(0,len(_listaDeAmigos)-1)
            
            if contador == 1:
                cincuentaPorciento = 50 * pozoAcumulado(_listaDeApuestas) / 100
                aux.append(_listaDeAmigos[nombres])
                contador += 1
                print("Primer puesto:",_listaDeAmigos[nombres])
                continue
                
            elif contador == 2:
                if _listaDeAmigos[nombres] not in aux:
                    treintaPorciento = 30 * pozoAcumulado(_listaDeApuestas) / 100
                    aux.append(_listaDeAmigos[nombres])
                    contador += 1
                    print("Segundo puesto:",_listaDeAmigos[nombres])
                    
            elif contador == 3:
                if _listaDeAmigos[nombres] not in aux:
                    veintePorciento = 20 * pozoAcumulado(_listaDeApuestas) / 100
                    aux.append(_listaDeAmigos[nombres])
                    contador += 1
                    print("Tercer puesto:",_listaDeAmigos[nombres])
            
        _listaDeApuestas.clear()
        _listaDeAmigos.clear()
            
def bajaDeAmigo(_listaDeAmigos, _listaDeApuestas):
    posicion = int(input("Introducir la posición del jugador: "))
    print("La posición del jugador eliminado es:",posicion,", se llama:",_listaDeAmigos[posicion],", y el valor aportado es:",_listaDeApuestas[posicion])
    if posicion >= 0 and posicion <= len(_listaDeAmigos):
        for posicion in range(len(_listaDeAmigos)):
            del _listaDeAmigos[posicion]
            del _listaDeApuestas[posicion]
            return _listaDeAmigos, _listaDeApuestas
    else:
        print("Se introdujo una posición inválida, intente nuevamente")
            
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
#----------------------------------------------------------------------------------------------
_listaDeAmigos = []
_listaDeApuestas = []

# Bloque de menú
#----------------------------------------------------------------------------------------------
while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Cargar amigos al sorteo")
        print("[2] Sortear!")
        print("[3] Dar de baja un amigo")
        print("[4] Subir la apuesta!")
        print("[0] Salir del programa")
        print()
        ultimoItemMenu = 4
        opcion = int(input("Seleccione una opción: "))
        if opcion in range(0,ultimoItemMenu + 1): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == 0: # Opción salir del programa
        exit()

    elif opcion == 1:   # Opción Cargar Amigos al sorteo
        agregarAmigosAlSorteo(_listaDeAmigos, _listaDeApuestas)
        print(_listaDeAmigos)
        print(_listaDeApuestas)
        
    elif opcion == 2:   # Sortear!
        realizarSorteo(_listaDeAmigos, _listaDeApuestas)
        
    elif opcion == 3:   # Dar de baja un amigo
        bajaDeAmigo(_listaDeAmigos, _listaDeApuestas)
        print(_listaDeAmigos)
        print(_listaDeApuestas)
        
    elif opcion == 4:   # Subir la apuesta!
        ...

    print()
    input("Presione ENTER para continuar.")

