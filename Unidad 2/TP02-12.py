"""
-----------------------------------------------------------------------------------------------
Título: ATENCION DE PACIENTES EN CLÍNICA

Fecha: 1/9/2023

Autor: Gianfranco Mazzei

Descripción: Resolver el siguiente problema, diseñando las funciones a utilizar:

Una clínica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se anuncia en la recepción 
indicando su número de afiliado (número entero de 4 dígitos) y además indica si viene por una urgencia (ingresando un 
0) o con turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita:

a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en 
el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por 
urgencia. Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado

Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def calculoPacientes(num1,num2,lista1,lista2):
    if num2 == 0:
        lista1.append(num1)
    elif num2 == 1:
        lista2.append(num1)

def mostrarListados(listaUrgencia, listaTurno):
    print("Pacientes atendidos por urgencia:")
    for paciente in listaUrgencia:
        print(paciente)
    print("\nPacientes atendidos por turno:")
    for paciente in listaTurno:
        print(paciente)

def buscarPaciente(usuario, listaUrgencia, listaTurno):
    atendidoPorTurno = listaTurno.count(usuario)
    atendidoPorUrgencia = listaUrgencia.count(usuario)
    return atendidoPorTurno, atendidoPorUrgencia

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

paciente = 0
listaUrgencia = []
listaTurno = []

#-------------------------------------------------
# Procesos
#-------------------------------------------------

while True:
    recepcion = int(input("Introducir su número de afiliado [4 digitos] {para finalizar introducir -1}: "))
    if recepcion == -1:
        break
    estado = int(input("Si es por urgencia introducir 0, si tiene turno 1: "))
    if recepcion >= 1000 and recepcion <= 9999:
        calculoPacientes(recepcion, estado, listaUrgencia, listaTurno)
        
while True:
    usuario = int(input("Introducir el número de afiliado que desea buscar [4 dígitos] {Finalizar -1}: "))
    if usuario == -1:
        break
    atendidoPorTurno, atendidoPorUrgencia = buscarPaciente(usuario, listaUrgencia, listaTurno)
    print(f"El paciente",usuario, "fue atendido",atendidoPorTurno, "veces por Turno")
    print(f"El paciente",usuario, "fue atendido",atendidoPorUrgencia, "veces por Urgencia")

#-------------------------------------------------
# Resultados
#-------------------------------------------------

mostrarListados(listaUrgencia, listaTurno)





