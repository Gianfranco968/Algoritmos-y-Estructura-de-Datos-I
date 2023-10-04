"""
-----------------------------------------------------------------------------------------------
Título: PARCIAL 2022 D'AQUINO

Fecha: 03/10/2023

Autor: Gianfranco Mazzei

Descripción:
Crear una cadena con las letras del abecedario. Transformarla  en una lista, en donde
cada letra sea un elemento de la lista abc. Utilizar el método Split.

Ingresar dos valores por teclado que serán las longitudes de dos listas , a y b, (Estos valores
pueden ser iguales o distintos) que se crearán, con valores aleatorios comprendidos entre 10 y 260
y deficientes, y deberán ser cargados a las listas, ej: 15, 27

Ordenar ambas listas de manera ascendente

Unir ambas listas sobre una nueva lista, de manera tal que la nueva lista c tenga la longitud de a más b.

Obtener el código de cada elemento de la lista c, de la siguiente manera:

1 – Si el elemento de la lista es menor a 100,  con el primer dígito, tomar la letra correspondiente de
la lista abc  y concatenarlo con el elemento de la lista original.

2 – Si elemento de la lista es 100 o más, con los dos primeros  dígitos, tomar la letra correspondiente de
la lista abc  y concatenarlo con el elemento de la lista original.

Para poder hacer la concatenación, deberá hacer lo pertinente con cada elemento de la lista c. La lista
deberá quedar, por ej: ‘a15,’b27’……

Mostrar la lista c, en un campo de 10 posiciones, utilizando center, con relleno de guiones.

Número deficiente: Cuando la suma de los divisores, sin el propio número, es menor al número.


Pendientes:

-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def numeroAleatorio(longitud):
    aleatorio = random.randint(10,260)
    return aleatorio

def numeroDeficiente(numero):
    suma = 0
    for divisor in range(1,numero-1):
        if numero % divisor == 0:
            suma += divisor
    if suma < numero:
        return True
    
def ordenarLista(lista1, lista2):
    for x in range(len(lista1)):
        lista2.append(lista1[x])
    return lista2
    
#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
#-------------------------------------------------
# Inicialización de variables y entrada de datos
#-------------------------------------------------

cadena = "abcdefghijklmnopqrstuvwxyz"
listaCadena = []
lista_A = []
lista_B = []
lista_C = []
a = 0
b = 0
aux = 0
contador = 0
centrar = ""

#-------------------------------------------------
# Procesos
#-------------------------------------------------

longitud_A = int(input("Introducir un valor: "))
longitud_B = int(input("Introducir otro valor: "))

while a != longitud_A:
    A = numeroAleatorio(longitud_A)
    if numeroDeficiente(A) == True:
        lista_A.append(A)
        a += 1
        
while b  != longitud_B:
    B = numeroAleatorio(longitud_B)
    if numeroDeficiente(B) == True:
        lista_B.append(B)
        b += 1
    
for j in range(len(cadena.split())):
    if j == 0:
        for i in cadena.split()[j]:
            listaCadena.append(i)
            
lista_A.sort()
lista_B.sort()

ordenarLista(lista_A, lista_C)
ordenarLista(lista_B, lista_C)
lista_C.sort()

for numero in range(len(lista_C)):
    aux = lista_C[numero]
    if aux < 100:
        primerDigito = aux // 10
        for posicion in range(len(listaCadena)):
            if posicion == primerDigito:
                aux = str(aux)
                listaCadena[posicion] = listaCadena[posicion] + aux
    aux = int(aux)
    if aux >= 100:
        dosDigitos = aux // 10
        for posicion in range(len(listaCadena)):
            if posicion == dosDigitos:
                aux = str(aux)
                listaCadena[posicion] = listaCadena[posicion] + aux

for numeros in range(len(lista_C)):
    lista_C[numeros] = str(lista_C[numeros])


for elementos in lista_C:
    elementosCentrados = elementos.center(10,'-')
    centrar += elementosCentrados

        
        
#-------------------------------------------------
# Resultados
#-------------------------------------------------
print(listaCadena)
print(lista_A)
print(lista_B)
print(lista_C)
print(centrar)
