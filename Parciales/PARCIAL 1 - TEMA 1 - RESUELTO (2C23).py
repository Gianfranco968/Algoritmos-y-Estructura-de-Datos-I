"""
-----------------------------------------------------------------------------------------------
Título: PARCIAL 1 - TEMA 1 - RESUELTO (2C23)
Fecha: 27/11/23
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

def cargarHorasDeVuelo(baseDeAlumnos, baseDeHoras, baseDeAviones):
    
    tipoDeAlumno = input("Desea cargar horas a un nuevo alumno? [S|N]: ").upper()
    
    if tipoDeAlumno == "S":
        alumnoNuevo = input("Ingrese nombre del nuevo alumno: ").upper()
        baseDeAlumnos.append(alumnoNuevo)
        
        while True:
            avion = input("Ingrese avión [SESSNA|PIPER|PETREL]: ").upper()
            if avion == "SESSNA" or avion == "PIPER" or avion == "PETREL":
                baseDeAviones.append(avion)
                break
            else:
                print("Avión inexistente, vuelva a intentar!")
        
        while True:
            horas = int(input("Ingrese la cantidad de horas de vuelvo [Máximo 8 horas]: "))
            if horas >= 0 and horas <= 8:
                baseDeHoras.append(horas)
                break
            else:
                print("No se admiten más de 8 horas de vuelo, vuelva a intentar!")
    
    if tipoDeAlumno == "N":
        while True:
            alumnoExistente = input("Ingrese nombre del alumno existente: ").upper()
            if alumnoExistente in baseDeAlumnos:
                break
            else:
                print("El alumno no existe o fue mal ingresado, vuelva a intentar!")
        
        while True:
            horas = int(input("Ingrese la cantidad de horas de vuelvo [Máximo 8 horas]: "))
            if horas >= 0 and horas <= 8:
                break
            else:
                print("No se admiten más de 8 horas de vuelo, vuelva a intentar!")
            
        for x in range(len(baseDeAlumnos)):
            if alumnoExistente == baseDeAlumnos[x]:
                posicionAlumnoExistente = x
                break
        
    return baseDeAlumnos, baseDeAviones, baseDeHoras
        

def sortearAlumnoParaExamen(baseDeAlumnos, baseDeHoras, baseDeAviones, alumnosParaExamen):
    listaAlumnosAux = []
    listaHorasAux = []
    listaAvionesAux = []
    
    while True:
        aux = ""
        sumador = 0
        
        posicionSorteo = random.randint(0,len(baseDeAlumnos))
        aux = baseDeAlumnos[posicionSorteo]

        for x in range(len(baseDeAlumnos)):
            if aux == baseDeAlumnos[x]:
                sumador += baseDeHoras[x]
                
        if sumador >= 40:
            nombreSorteado = baseDeAlumnos[posicionSorteo]
            
            for alumno in range(len(baseDeAlumnos)):
                if nombreSorteado != baseDeAlumnos[alumno]:
                    listaAlumnosAux.append(baseDeAlumnos[alumno])
                    listaHorasAux.append(baseDeHoras[alumno])
                    listaAvionesAux.append(baseDeAviones[alumno])
            
            alumnosParaExamen.append("Alumno" + " " + str(nombreSorteado) + " " + "listo para examen de piloto, con" + " " + str(sumador) + " " + "horas de vuelo en avión" + " " + str(baseDeAviones[posicionSorteo]))
            print("El alumno sorteado es:",nombreSorteado)
            break
        
        sumador = 0
        
    baseDeAlumnos = listaAlumnosAux
    baseDeHoras = listaHorasAux
    baseDeAviones = listaAvionesAux
    
    return baseDeAlumnos, baseDeHoras, baseDeAviones, alumnosParaExamen


def consultarCantidadDeVuelos(baseDeAlumnos, baseDeAviones):
    avion = ""
    cantidadDeVuelos = 0

    while True:
        usuario = input("Ingrese nombre del alumno [FIN = Salir]: ").upper()
        if usuario != "FIN":
            if usuario in baseDeAlumnos:
                for x in range(len(baseDeAlumnos)):
                    if usuario == baseDeAlumnos[x]:
                        avion = baseDeAviones[x]
                        cantidadDeVuelos += 1
                print("El alumno" + " " + str(usuario) + " " + "realizó a la fecha un total de" + " " + str(cantidadDeVuelos) + " " + "de vuelos en un" + " " + str(avion)) 
            else:
                print("El alumno no existe o fue mal ingresado, vuelva a intentar!")
        else:
            break


def consultarAlumnosParaExamen(alumnosParaExamen):
    for alumnos in range(len(alumnosParaExamen)):
        print(alumnosParaExamen[alumnos])

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
# Declaración de variables
#----------------------------------------------------------------------------------------------

baseDeAlumnos = ["ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ANDRES" , "JUAN" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ANDRES" , "JUAN" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ANDRES" , "JUAN" , "ROBERTO" , "MARIA" , "JORGE" , "SOLEDAD" , "ROBERTO" , "MARIA" , "JORGE" , "JORGE" , "JORGE" , "MARIA" , "MARIA" , "ROBERTO" , "ROBERTO", "MARIA" , "ROBERTO"]
baseDeHoras = [4 , 7 , 5 , 6 , 3 , 4 , 6 , 5 , 4 , 7 , 4 , 5 , 3 , 3 , 4 , 4 , 5 , 4 , 3 , 5 , 6 , 3 , 4 , 3 , 6 , 4 , 5 , 5 , 4 , 4 , 3 , 6 , 4 , 5 , 5 , 3 , 6 , 5 , 4 , 5 , 4 ]
baseDeAviones = ["CESSNA" , "PETREL" , "PIPER" , "PIPER" , "CESSNA" , "PETREL" , "CESSNA" , "PETREL" , "PIPER" , "PIPER" , "CESSNA" , "PETREL" , "PIPER" , "PIPER" , "CESSNA" , "PETREL" , "CESSNA" , "PETREL" , "PIPER" , "PIPER" , "CESSNA" , "PETREL" , "PIPER" , "PIPER" , "CESSNA" , "PETREL" , "CESSNA" , "PETREL" , "PIPER" , "PIPER" , "CESSNA" , "PETREL" , "PIPER" , "PIPER" , "PIPER" , "PETREL" , "PETREL" , "CESSNA" , "CESSNA", "PETREL" , "CESSNA"]
alumnosParaExamen = ['Alumno SUSANA listo para examen de piloto, con 44 horas de vuelo en avión CESSNA']

# Bloque de menú
#----------------------------------------------------------------------------------------------

while True:
    while True:
        print()
        print("---------------------------")
        print("MENÚ DEL SISTEMA           ")
        print("---------------------------")
        print("[1] Cargar horas de vuelo")
        print("[2] Sortear alumno para examen de piloto")
        print("[3] Consultar horas faltantes para examen")
        print("[4] Consultar alumnos para examen de piloto")
        print("[0] Salir del programa")
        print()
        opcion = input("Seleccione una opción: ")
        if opcion in ("0","1","2","3","4"): # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    if opcion == "0": # Opción salir del programa
        exit()

    elif opcion == "1":   # Cargar horas de vuelo
        baseDeAlumnos, baseDeHoras, baseDeAviones = cargarHorasDeVuelo(baseDeAlumnos[:], baseDeHoras[:], baseDeAviones[:])

    elif opcion == "2":   # Sortear alumno para examen de piloto
        baseDeAlumnos, baseDeHoras, baseDeAviones, alumnosParaExamen = sortearAlumnoParaExamen(baseDeAlumnos[:], baseDeHoras[:], baseDeAviones[:], alumnosParaExamen[:])

    elif opcion == "3":   # Consultar horas faltantes para examen
        # Este código va como ayuda para mostrar los alumnos que hay en la base -----------
        print("\nAlumnos sin sortear:")
        alumnosSinRepetir=[]
        [alumnosSinRepetir.append(e) for e in baseDeAlumnos if e not in alumnosSinRepetir]
        alumnosSinRepetir.sort()
        for alumno in alumnosSinRepetir:
            print(alumno)
        # Fin del código de ayuda ---------------------------------------------------------

        consultarCantidadDeVuelos(baseDeAlumnos[:], baseDeAviones[:])
        
    elif opcion == "4":   # Consultar alumnos para examen de piloto
        consultarAlumnosParaExamen(alumnosParaExamen[:])

    print()
    input("Presione ENTER para continuar.")


