from listas import Lista;
#Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad 
# de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
# más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

#las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
#a. obtener la cantidad de Pokémons de un determinado entrenador;
#b. listar los entrenadores que hayan ganado más de tres torneos;
#c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
#d. mostrar todos los datos de un entrenador y sus Pokémos;
#e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
#f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
#(tipo y subtipo);
#g. el promedio de nivel de los Pokémons de un determinado entrenador;
#h. determinar cuántos entrenadores tienen a un determinado Pokémon;
#i. mostrar los entrenadores que tienen Pokémons repetidos;
#j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
#k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenadorcomo del Pokémon deben
# ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos;

ListaEntrenadores = Lista();
EntrenadoresMayor79 = []
GanadoresMasTresTorneos = [];
EntrenadoresPokemonsSubtipos = [];
EntrenadoresQueTieneUnPokemonDeterminado = [];
pokemonsRepetidosDeunEntrenador = []
entrenadoresConPokemonsRepetidos = []
DatosEntrenadores = [
    {"NombreEntrenador":"Alex","TorneosGanados":2,"Ganadas":4,"Perdidas":4,"ListaPokemons":Lista()},

    {"NombreEntrenador":"Mario","TorneosGanados":1,"Ganadas":3,"Perdidas":6,"ListaPokemons":Lista()},

    {"NombreEntrenador":"Juan","TorneosGanados":7,"Ganadas":4,"Perdidas":3,"ListaPokemons":Lista()},

    {"NombreEntrenador":"Ash","TorneosGanados":9,"Ganadas":7,"Perdidas":0,"ListaPokemons":Lista()},
]
PokemonsAlex = [
    {"Nombrepoke":"Tyrantrum","Nivel":5,"Tipo":"tierra","subtipo":"agua"},
    {"Nombrepoke":"marcus","Nivel":2,"Tipo":"fuego","subtipo":"volador"},
    {"Nombrepoke":"ryden","Nivel":8,"Tipo":"tierra","subtipo":"agua"},
]
PokemonsMario = [
    {"Nombrepoke":"Charmander","Nivel":5,"Tipo":"fuego","subtipo":"volador"},
    {"Nombrepoke":"Squirtle","Nivel":2,"Tipo":"agua","subtipo":"volador"},
    {"Nombrepoke":"ryden","Nivel":8,"Tipo":"agua","subtipo":"agua"},
]
PokemonsJuan = [
    {"Nombrepoke":"Bulbasaur","Nivel":9,"Tipo":"agua","subtipo":"veneno"},
    {"Nombrepoke":"Bulbasaur","Nivel":6,"Tipo":"agua","subtipo":"afua"},
    {"Nombrepoke":"Pidgey","Nivel":1,"Tipo":"normal","subtipo":"volador"},
]
PokemonsAsh = [
    {"Nombrepoke":"Pikachu","Nivel":20,"Tipo":"electrico","subtipo":"electrico"},
    {"Nombrepoke":"Charizard","Nivel":8,"Tipo":"fuego","subtipo":"volador"},
    {"Nombrepoke":"Dragonite","Nivel":10,"Tipo":"fuego","subtipo":"planta"},
]
#CARGAMOS LOS ENTRENADORES
for e in DatosEntrenadores:
    ListaEntrenadores.insertar(e,"NombreEntrenador")

#CARGAMOS LOS POKEMONS
pos = ListaEntrenadores.busqueda("Alex","NombreEntrenador")
if (pos != -1):
    alex = ListaEntrenadores.obtenerElemento(pos)
    for p in PokemonsAlex:
        alex["ListaPokemons"].insertar(p,"Nombrepoke")

pos = ListaEntrenadores.busqueda("Mario","NombreEntrenador")
if (pos != -1):
    Mario = ListaEntrenadores.obtenerElemento(pos)
    for p in PokemonsMario:
        Mario["ListaPokemons"].insertar(p,"Nombrepoke")

pos = ListaEntrenadores.busqueda("Juan","NombreEntrenador")
if (pos != -1):
    Juan = ListaEntrenadores.obtenerElemento(pos)
    for p in PokemonsJuan:
        Juan["ListaPokemons"].insertar(p,"Nombrepoke")

pos = ListaEntrenadores.busqueda("Ash","NombreEntrenador")
if (pos != -1):
    Ash = ListaEntrenadores.obtenerElemento(pos)
    for p in PokemonsAsh:
        Ash["ListaPokemons"].insertar(p,"Nombrepoke")

#punto a
MayorGanadorTorneos = 0;
MayorGanadorTorneosPokemonMasFuerte = 0;
entrenadorBuscado = str(input(">>Ingrese el nombre de un entrenador: "))
PokemonRepetido = str(input(">>Ingrese el pokemon que desee buscar para saber si se repite: "))
entrenadorBuscar = str(input(">>Ingrese el nombre de un entrenador X: "))
pokemonBuscar = str(input(">>Ingrese el nombre de un pokemon  Y: "))
verificarPuntoK = 0;
contadorParaSaberRepDeUnPokemon = 0;
#ENTRAMOS A LA LISTA DE ENTRENADORES
for i in range(ListaEntrenadores.tamanio()):
    porcentaje = 0;
    suma_Batallas = 0;
    Entrenador = ListaEntrenadores.obtenerElemento(i)
    suma_Batallas = Entrenador["Ganadas"] + Entrenador["Perdidas"];
    porcentaje = (Entrenador["Ganadas"]/suma_Batallas*100)
    if (porcentaje > 79):
        EntrenadoresMayor79.append(Entrenador)

    #ENTRAMOS A LA LISTA DE POKEMONS
    pokemonsRepetidosDeunEntrenador = [] #PONEMOS LA LISTA EN CERO
    acumuladorNivelMario = 0;
    contadorPokemonsMario= 0;
    for j in range(Entrenador["ListaPokemons"].tamanio()):
        pokemonEntrenador = Entrenador["ListaPokemons"].obtenerElemento(j)
        pokemonsRepetidosDeunEntrenador.append(pokemonEntrenador["Nombrepoke"])
        if Entrenador["NombreEntrenador"] == entrenadorBuscar:
            if pokemonEntrenador["Nombrepoke"] == pokemonBuscar:
                verificarPuntoK += 1; 
        if pokemonEntrenador["Nombrepoke"] == PokemonRepetido:
            contadorParaSaberRepDeUnPokemon +=1
        if pokemonEntrenador["Nombrepoke"] == "Tyrantrum" or pokemonEntrenador["Nombrepoke"] == "Terrakion" or pokemonEntrenador["Nombrepoke"] == "Wingull":
            EntrenadoresQueTieneUnPokemonDeterminado.append(Entrenador)
        if (Entrenador["NombreEntrenador"]=="Mario"):
            acumuladorNivelMario = pokemonEntrenador["Nivel"] + acumuladorNivelMario;
            contadorPokemonsMario +=1;

        if pokemonEntrenador["Tipo"]=="fuego" and pokemonEntrenador["subtipo"]=="planta":
            EntrenadoresPokemonsSubtipos.append(Entrenador)
        elif pokemonEntrenador["Tipo"]=="agua" and pokemonEntrenador["subtipo"]=="volador":
            EntrenadoresPokemonsSubtipos.append(Entrenador)
    
    if Entrenador["ListaPokemons"].tamanio() != len(set(pokemonsRepetidosDeunEntrenador)): #COMPARAMOS PARA SABER SI SE REPITE UN POKEMON
        entrenadoresConPokemonsRepetidos.append(Entrenador) 
    if (Entrenador["NombreEntrenador"]=="Alex"):
        alex = i;

    if (Entrenador["TorneosGanados"]>=MayorGanadorTorneos):
        MayorGanadorTorneos = Entrenador["TorneosGanados"];
        posicionMayorGanadorTorneos = i;

    if (Entrenador["TorneosGanados"]>3): #PUNTO B
        GanadoresMasTresTorneos.append(Entrenador)
    if (Entrenador["NombreEntrenador"] == entrenadorBuscado):
        print("El entrenador ", entrenadorBuscado," tiene la cantidad -> ",Entrenador["ListaPokemons"].tamanio(),"Pokemons")

#punto c
PokeMasPoderoso = 0;
mayor_ganador = ListaEntrenadores.obtenerElemento(posicionMayorGanadorTorneos)
for j in range(mayor_ganador["ListaPokemons"].tamanio()):
    poke = mayor_ganador["ListaPokemons"].obtenerElemento(j)
    if (poke["Nivel"]>=PokeMasPoderoso):
        PokeMasPoderoso=poke["Nivel"]
        nombrepoke = poke["Nombrepoke"];
#punto D --> mostramos los datos de alex
print("\nDatos de ALEX")
Alex = ListaEntrenadores.obtenerElemento(alex)
print(Alex)
print("POKEMONS ALEX:")
for i in range(Alex["ListaPokemons"].tamanio()):
    pokeAlex = Alex["ListaPokemons"].obtenerElemento(i)
    print(pokeAlex)



print("\nEntrenadores que ganaron mas de 3 torneos")
for n in GanadoresMasTresTorneos:
    print(n["NombreEntrenador"])

print("\nEl entrenador que mas torneos gano es -> ",ListaEntrenadores.obtenerElemento(posicionMayorGanadorTorneos)["NombreEntrenador"],
"total-> ",MayorGanadorTorneos)
print("Y su Pokemon Mas poderoso es --> ",nombrepoke )

#punto e
print("\nLos entrenadores con un porcenaje mayor al %79 de torneos ganados son")
for elementos in EntrenadoresMayor79:
    print(elementos["NombreEntrenador"])

#punto f
print("Los entrenadores que tienen pokemons de tipo fuego o agua y subtipo planta y volador son:")
for p in EntrenadoresPokemonsSubtipos:
    print(p["NombreEntrenador"])

#punto g
#UTILIZAMOS A MARIO PARA OBTENER EL PROMEDIO DE NIVELES DE SUS POKEMONS
print("EL promedio de poder de los pokemons de Mario son: ")
print(acumuladorNivelMario/contadorPokemonsMario)

#punto h
print(f"La cantidad de entrenadores que tienen a {PokemonRepetido} es de ->",contadorParaSaberRepDeUnPokemon)

#punto i
print("Los entrenadores con pokemons repetidos son: ")
for p in entrenadoresConPokemonsRepetidos:
    print(p["NombreEntrenador"])
#punto j 
print("Los entrenadores que tiene a tyranum, terrakion o wingull son:")
for p in EntrenadoresQueTieneUnPokemonDeterminado:
    print(p["NombreEntrenador"])

#punto k
if verificarPuntoK>0:
    print(f"EL entrenador {entrenadorBuscar} si tiene al pokemon {pokemonBuscar}")
else:
    print(f"EL entrenador {entrenadorBuscar} NO tiene al pokemon {pokemonBuscar}")







