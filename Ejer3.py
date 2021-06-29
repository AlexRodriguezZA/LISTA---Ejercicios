from listas import Lista;
#Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
#una que contenga los números pares y otra para los números impares.

listaNumeros = Lista();
listaPar = Lista();
listaImpar = Lista();

ArrayNumeros = [1,2,3,4,5,6,7,8,9,10]

print("Lista Completa:")
for n in ArrayNumeros:
    print(n)
    listaNumeros.insertar(n);

for i in range(listaNumeros.tamanio()):
    if (listaNumeros.obtenerElemento(i) % 2 == 0):
        listaPar.insertar(listaNumeros.obtenerElemento(i))
    else:
        listaImpar.insertar(listaNumeros.obtenerElemento(i))

print("\nLista Par:")
listaPar.barrido()
print("\nLista Impar:")
listaImpar.barrido()
