"""
-----------------------------------------------------------------------------------------------
Título: DICCIONARIO DE LIBRERÍA

Fecha: 05/12/23

Autor: Gianfranco Mazzei

Descripción: Una librería almacena su lista de precios en un diccionario. Diseñar un programa para crearlo, incrementar los precios de 
los cuadernos en un 15%, imprimir un listado con todos los elementos de la lista de precios e indicar cuál es el ítem más 
costoso que venden en el comercio.

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

diccionario = {}
listaPrecios = []
listaProductos = []
productoMasCostoso = ""
variable = 'CUADERNOS'

#-------------------------------------------------
# Procesos
#-------------------------------------------------

while True:
    producto = input("Ingrese el producto [finalizar con -1]: ").upper()
    if producto != "-1":
        listaProductos.append(producto)
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                listaPrecios.append(precio)
                break
            except ValueError:
                print("ERROR --> Ingrese un precio válido")
    else:
        break

diccionario = dict(zip(listaProductos,listaPrecios))

if variable in diccionario:
    aumento = diccionario.get(variable) * 15 / 100
    montoTotal = aumento + diccionario.get(variable)
    diccionario[variable] = montoTotal

listaPreciosActualizados = list(diccionario.values())

precioProductoMasCostoso = max(listaPreciosActualizados)

for maximo in range(len(listaPreciosActualizados)):
    if listaPreciosActualizados[maximo] == precioProductoMasCostoso:
        productoMasCostoso = listaProductos[maximo]

print(diccionario)   
print(listaPreciosActualizados)
print("El producto más costoso que se vende es -->",productoMasCostoso)


#-------------------------------------------------
# Resultados
#-------------------------------------------------
...

