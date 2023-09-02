"""
-----------------------------------------------------------------------------------------------
Título: MATERIAS CURSANDO

Fecha: 1/9/2023

Autor: Gianfranco Mazzei

Descripción: Escribí un programa donde se declare dentro del mismo código una lista con todas las
materias que estás cursado en la facultad (no es necesario cargarla con input). A continuación,
programar un bucle para listar por pantalla dichas materias, cada materia en una línea.

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
listaMaterias = []
primerMateria = "Sistemas de Información II"
segundaMateria = "Sistemas Operativos"
tercerMateria = "Matemática Discreta"
cuartaMateria = "Algoritmos y Estructuras de Datos I"
quintaMateria = "Testing de Aplicaciones"


#-------------------------------------------------
# Procesos
#-------------------------------------------------
listaMaterias.append(primerMateria)
listaMaterias.append(segundaMateria)
listaMaterias.append(tercerMateria)
listaMaterias.append(cuartaMateria)
listaMaterias.append(quintaMateria)

for materias in listaMaterias:

#-------------------------------------------------
# Resultados
#-------------------------------------------------
    print(materias)
