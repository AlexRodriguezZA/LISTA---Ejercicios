from listas import Lista;
#Utilizando una lista doblemente enlazada, cargar una palabra carácter a carácter, y determinar
# si la misma es un palíndromo, sin utilizar ninguna estructura auxiliar.

listaPaliendromo = Lista();

palabra = "nuequen"

for p in palabra:
    print(p)
    listaPaliendromo.insertar(p)

for i in range(listaPaliendromo.tamanio()):
    pass
