from listas import Lista;
#Se dispone de una lista de canciones de Spotify, de las cuales se sabe su nombre, banda o artista,
#duración y cantidad de reproducciones durante el último mes. Desarrollar un algoritmo que
#permita realizar las siguientes actividades:
#a. obtener la información de la canción más larga;
#b. obtener el TOP 5, TOP 10 y TOP 40 de canciones más escuchadas;
#c. obtener todas las canciones de la banda Arctic Monkeys;
#d. mostrar los nombres de las bandas o artistas que solo son de una palabra.

ListaSpotify = Lista()
ListaTop = Lista()
cantantesUnaPalabra = []
listaCanciones = [
    {"NombreCancion":"Dura","Artista":"Daddy yankke","Duracion":2,"Reproducciones":5000000},
    {"NombreCancion":"levitating","Artista":"Dua Lipa","Duracion":10,"Reproducciones":545600000},
    {"NombreCancion":"titanium","Artista":"David Guetta","Duracion":4,"Reproducciones":10000000},
    {"NombreCancion":"Do I Wanna Know?","Artista":"Arctic Monkeys","Duracion":5,"Reproducciones":346000043},
    {"NombreCancion":"Taste","Artista":"Tyga","Duracion":6,"Reproducciones":10000000000},
]

#cargamos lista
for cancion in listaCanciones:
    ListaSpotify.insertar(cancion,"NombreCancion")
    ListaTop.insertar(cancion,"Reproducciones")


#punto c
cancionMasLarga = 0;
posicionCancionMasLarga = -1;
for i in range(ListaSpotify.tamanio()):
    validarEspacio = 0;
    datoCancion = ListaSpotify.obtenerElemento(i)
    if (datoCancion["Duracion"]>=cancionMasLarga):
        cancionMasLarga = datoCancion["Duracion"];
        posicionCancionMasLarga = i;
    if (" " not in datoCancion["Artista"]):
        validarEspacio += 1;
    if validarEspacio > 0:
        cantantesUnaPalabra.append(datoCancion["Artista"])
            
    
    if (datoCancion["Artista"]=="Arctic Monkeys"):
        print("Canciones los Arctic Monkeys")
        print("-",datoCancion["NombreCancion"])

#punto a

print("\nLa cancion mas larga es -->",ListaSpotify.obtenerElemento(posicionCancionMasLarga)["NombreCancion"])
print("Con una duracion de -->",ListaSpotify.obtenerElemento(posicionCancionMasLarga)["Duracion"]," min.")

#punto b
print("\nTOP 5- Los mas escuchados:")
for i in reversed(range(0,ListaTop.tamanio())):
    dato = ListaTop.obtenerElemento(i)
    print("Song: ",dato["NombreCancion"],"/ Reproducciones- -> ",dato["Reproducciones"])

#punto d
print("Artista con un solo nombre")
for cantante in cantantesUnaPalabra:
    print(cantante)


