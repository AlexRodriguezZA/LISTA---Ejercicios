from listas import Lista;
#Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.

ListaNodos = Lista()

Elementos = [1,2,3,4,5,6,7,8,9,0]

for nodos in Elementos:
    ListaNodos.insertar(nodos);

print(">>La lista tiene una cantidad de ",ListaNodos.tamanio()," nodos")

