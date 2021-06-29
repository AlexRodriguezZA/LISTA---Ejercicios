from listas import Lista;
#Dada una lista de números enteros eliminar de estas los números primos.

listaEnteros = Lista();
enteros = [1,2,3,4,5,6,7]

def numerosPrimos(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for n in enteros:
    listaEnteros.insertar(n)


for i in range((listaEnteros.tamanio())):
    dato = listaEnteros.obtenerElemento(i)
    print(i)
    if(numerosPrimos(dato) == True):
        listaEnteros.eliminar(dato)  

print(listaEnteros.barrido())
