"""
-----------------------------------------------------------------------------------------------
Título: AUMENTO DE LÍMITES DE TARJETAS

Fecha: 17/08/2023

Autor: Gianfranco Mazzei

Descripción: Realizar un programa donde se vayan ingresando las calificaciones de los alumnos de
un curso. Luego de ingresar la calificación del último alumno, se ingresará un -1 para terminar
la carga. El programa informará entonces la calificación promedio del curso.

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
# Inicialización de variables
#-------------------------------------------------

calificacionAlumno = 0
sumador = 0
contador = 0
promedioTotal = 0


#-------------------------------------------------
# Procesos
#-------------------------------------------------

while True:
    calificacionAlumno = int(input("Introducir la calificacion del alumno [Introducir -1 para finalizar]: "))
    if calificacionAlumno != -1:
        sumador += calificacionAlumno
        contador += 1
    else:
        break

promedioTotal = sumador / contador
    

#-------------------------------------------------
# Resultados
#-------------------------------------------------
print("El promedio de la clase es de: ", promedioTotal)

