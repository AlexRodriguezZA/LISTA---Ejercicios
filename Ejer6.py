from listas import Lista
#Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
#casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias 
#para poder realizar las siguientes actividades:

#a. eliminar el nodo que contiene la información de Linterna Verde;
#b. mostrar el año de aparición de Wolverine;
#c. cambiar la casa de Dr. Strange a Marvel;
#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
#“traje” o “armadura”;
#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
#sea anterior a 1963;
#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
#g. mostrar toda la información de Flash y Star-Lord;
#h. listar los superhéroes que comienzan con la letra B, M y S;
#i. determinar cuántos superhéroes hay de cada casa de comic.

ListaHeroes = Lista()

Heroes = [
    {"Name":"Iron Man","AnioAparicion":1968,"CasaComic":"Marvel","Bio":"Iron man Es personaje que tiene una armadura la cual evolucina a medida que pasn los años"},
    {"Name":"Linterna verde","AnioAparicion":1938,"CasaComic":"DC","Bio":"Linterna Verde, traje verde, Es personaje que tiene un anillo el cual le permite crear objetos"},
    {"Name":"Capitana Marvel","AnioAparicion":1950,"CasaComic":"Marvel","Bio":"cap marvel Es personaje que tiene un traje brilloso y tiene poderes cosmicos"},
    {"Name":"Dr strange","AnioAparicion":1928,"CasaComic":"Marvel","Bio":"dr  strange Es personaje que tiene habilidades mágicas"},
    {"Name":"Mujer Maravilla","AnioAparicion":1918,"CasaComic":"DC","Bio":"Mujer maravilla"},
    {"Name":"Flash","AnioAparicion":1978,"CasaComic":"DC","Bio":"corre rapido el weon"},
    {"Name":"Star Lord","AnioAparicion":1918,"CasaComic":"Marvel","Bio":"novio de gamora"},
    {"Name":"Wolverine","AnioAparicion":1956,"CasaComic":"Marvel","Bio":"lobezno en espanña"},
]



#Cargamos los personajes

for h in Heroes:
    ListaHeroes.insertar(h,"Name")

#Punto a
ListaHeroes.eliminar("Linterna verde","Name")

#punto b
wolverineAnio = ListaHeroes.obtenerElemento(ListaHeroes.busqueda("Wolverine","Name"))
print("El año de aparicion de wolverine es en --> ",wolverineAnio["AnioAparicion"])

#punto c
DrStrangeModificacion = ListaHeroes.obtenerElemento(ListaHeroes.busqueda("Dr strange","Name"))
DrStrangeModificacion["CasaComic"] = "DC";


#punto d
palabraClave1 = "traje"
palabraClave2 = "armadura"
for i in range(ListaHeroes.tamanio()):
    datoHeroe = ListaHeroes.obtenerElemento(i)
    if(palabraClave1 in datoHeroe["Bio"]):
        print("biografia", datoHeroe["Name"])
    if (palabraClave2 in datoHeroe["Bio"]):
        print("biografia", datoHeroe["Name"])


#punto e and #punto g
for i in range(ListaHeroes.tamanio()):
    datoHeroe = ListaHeroes.obtenerElemento(i)
    if(datoHeroe["Name"]=="Flash") or (datoHeroe["Name"]=="Star Lord"):
        print(datoHeroe)
    if (datoHeroe["AnioAparicion"] < 1968):
        print("Heroe anterior a 1963 -->",datoHeroe["Name"]," ",datoHeroe["CasaComic"])

#punto f
capMarvel = ListaHeroes.obtenerElemento(ListaHeroes.busqueda("Capitana Marvel","Name"))
MujerMaravilla = ListaHeroes.obtenerElemento(ListaHeroes.busqueda("Mujer Maravilla","Name"))
print("\nLa mujer maravilla pertenece a la casa de --> ",MujerMaravilla["CasaComic"])
print("\nLa cap Marvel pertenece a la casa de --> ",capMarvel["CasaComic"])

#punto H and punto I
contadorMarvel = 0;
contadorDC = 0;
print("\nHeroes que empiezan con B, M o S")
for i in range(ListaHeroes.tamanio()):
    datoHeroe = ListaHeroes.obtenerElemento(i)
    if (datoHeroe["CasaComic"]=="Marvel"):
        contadorMarvel += 1;
    else:
        contadorDC += 1
    if(datoHeroe["Name"][0] == "B") or (datoHeroe["Name"][0] == "M") or (datoHeroe["Name"][0] == "S"):
        print(datoHeroe["Name"])

print("\nContadores de casa de comic")
print("MARVEL -->",contadorMarvel)
print("DC -->",contadorDC)

print(ListaHeroes.barrido())

