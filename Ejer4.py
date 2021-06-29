from listas import Lista;
#Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.

listaNum = Lista();

numeros = [1,3,45,6,7,89,87,65,34]

tamanioLista = len(numeros)
for n in numeros:
    listaNum.insertar(n);
    
print(listaNum.barrido())

for i in range(listaNum.tamanio()):
    if (i == tamanioLista-1):
        print("Ingrese un dato mayor a --> ", listaNum.obtenerElemento(i))
        datoNuevo = int(input(">>Ingrese dato: "))
        while (datoNuevo<listaNum.obtenerElemento(i)):
            print("Ingrese un dato mayor a --> ", listaNum.obtenerElemento(i))
            datoNuevo = int(input(">>Ingrese dato: "))
                
        listaNum.insertar(datoNuevo)
        print(">>Dato cargado<<")

print(listaNum.barrido())
