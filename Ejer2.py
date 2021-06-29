from listas import Lista;

#Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

ListaCaracteres = Lista()
vocales = ["a","e","i","o","u"]

frase = "alexDevops"                                                 

print("Frase cargada")
for letra in frase:
    ListaCaracteres.insertar(letra)

print(ListaCaracteres.barrido()) 

tamanioLista = ListaCaracteres.tamanio();
i = 0;
while (i < ListaCaracteres.tamanio()):
    letra = ListaCaracteres.obtenerElemento(i);
    if letra in vocales:
        print(letra)
        ListaCaracteres.eliminar(letra)
        i -= 1;
    else:
        i+=1

    

    


print("Vocales eliminadas")
print(ListaCaracteres.barrido()) 
