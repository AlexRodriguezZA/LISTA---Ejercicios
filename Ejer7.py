from listas import Lista
# Implementar los algoritmos necesarios para resolver las siguientes tareas:
# a. concatenar dos listas, una atrás de la otra;
# b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
# c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
# d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.

Lista1 = Lista()
lista2 = Lista()
ListaNueva = Lista()

cargarlista1 = [1, 2, 3, 4, 5, 6]
cargarlista2 = [3, 4, 5, 6, 7, 8]
# Cargamos lista 1
for e in cargarlista1:
    Lista1.insertar(e)

# Cargamos lista 2
for e in cargarlista2:
    lista2.insertar(e)


# Punto B
contadorElementoRepLista = 0;
for i in range(Lista1.tamanio()):
    verificador1 = 0
    dato1 = Lista1.obtenerElemento(i)
    for j in range(lista2.tamanio()):
        dato2 = lista2.obtenerElemento(j)
        if (dato1 != dato2):
            verificador1 += 1;
        else:
            contadorElementoRepLista += 1 #Para contar los elementos repetidos en la lista
    if (verificador1 == lista2.tamanio()):
        ListaNueva.insertar(dato1)

for x in range(lista2.tamanio()):
    verificador2 = 0
    dato2 = lista2.obtenerElemento(x)
    for z in range(Lista1.tamanio()):
        dato1 = Lista1.obtenerElemento(z)
        if (dato2 != dato1):
            verificador2 += 1;
    if (verificador2 == Lista1.tamanio()):
        ListaNueva.insertar(dato2)
print(ListaNueva.barrido())


# Punto A
# cargamos las dos listas en una
for i in range(Lista1.tamanio()):
    Lista1.insertar(lista2.obtenerElemento(i))
#Punto c
print("La cantidad de elementos repetidos en la listas es de --> ",contadorElementoRepLista)
#Punto d

while (not lista2.lista_Vacia()):
    datoEliminar = lista2.obtenerElemento(0)
    print("Dato eliminado-> ",datoEliminar)
    lista2.eliminar(datoEliminar)

