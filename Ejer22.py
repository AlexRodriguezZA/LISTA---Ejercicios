from listas import Lista;
#Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
#colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
#actividades enumeradas a continuación:
#a. listado ordenado por nombre y por especie;
#b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
#c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
#d. mostrar los Jedi de especie humana y twi'lek;
#e. listar todos los Jedi que comienzan con A;
#f. mostrar los Jedi que usaron sable de luz de más de un color;
#g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
#h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

jedis = Lista()
jedisSpecies = Lista();
padawanYoda = []
padawanLuke = []
jediHuman = []
jeditwi_lek = []
jedisA = []
sableMasDeUncolor = []
sableAmarilloVioleta = []
padawansJinWindu = []

file = open("jedis.txt");

lineas = file.readlines()
lineas.pop(0)
for linea in lineas:
    jedi = linea.split(';')
    jedi_data = {}
    jedi_data['name'] = jedi[0].title()
    jedi_data['rank'] = jedi[1]
    jedi_data['species'] = jedi[2]
    jedi_data['master'] = jedi[3].split('/')
    jedi_data['lightsaber_color'] = jedi[4].split('/')
    jedi_data['homeworld'] = jedi[5]
    jedi_data['birth_year'] = jedi[6]
    jedi_data['height'] = float(jedi[7].split('\n')[0])
    if(len(jedi) > 8):
        jedi_data['to_darkside'] = jedi[8]
        jedi_data['come_lightside'] = jedi[9]
    jedis.insertar(jedi_data, 'name')
    jedisSpecies.insertar(jedi_data,"species")
file.close()

#punto a
print("Listado por Nombre")
for i in range(jedis.tamanio()):
    jedi = jedis.obtenerElemento(i)
    if jedi["name"][0]  == "A" in jedi["name"]:
        jedisA.append(jedi)

    if "luke skywalker" in jedi["master"]:
        padawanLuke.append(jedi["name"])
    elif "yoda" in jedi["master"]:
        padawanYoda.append(jedi["name"])
    
    if "Qui-Gon Jin" in jedi["master"] or "Mace Windu" in jedi["master"]:
        padawansJinWindu.append(jedi["name"])

    if "human" in jedi["species"]:
        jediHuman.append(jedi["name"])
    elif jedi["species"] == "twi'lek":
        jeditwi_lek.append(jedi["name"]) 

    if len(jedi["lightsaber_color"])>1:
        sableMasDeUncolor.append(jedi["name"])  

    if "yellow" in jedi["lightsaber_color"] or "purple" in jedi["lightsaber_color"]:
        sableAmarilloVioleta.append(jedi["name"])
    print(jedi["name"])

print("\nListado por Especie")
for i in range(jedisSpecies.tamanio()):
    jedisSpe = jedisSpecies.obtenerElemento(i)
    print(jedisSpe["species"])

#punto b
print(">>Ahsoka Tano")
posAhsokaTano = jedis.busqueda("Ahsoka Tano","name")
if posAhsokaTano>-1:
    print(jedis.obtenerElemento(posAhsokaTano))
print(">>Kit Fisto")
posKitFisto = jedis.busqueda("Kit Fisto","name")
if posKitFisto>-1:
    print(jedis.obtenerElemento(posKitFisto))

#punto c
print("\nLos padawan de luke son")
for p in padawanLuke:
    print(p)

print("\nLos padawan de yoda son")
for p in padawanYoda:
    print(p)

#punto d
print("\nJeids humanos")
for j in jediHuman:
    print(j)
print("\nJeids Twi'lek")
for j in jeditwi_lek:
    print(j)

#punto e
print("\nLos jedis que comienza con A")
for p in jedisA:
    print(p["name"])

#punto f
print("\nLos jedi que usaron mas de un sable de color son:")
for p in sableMasDeUncolor:
    print(p)

#punto g
print("\nLos jedi que usaron amarillo o violeta:")
for i in sableAmarilloVioleta:
    print(i)

#punto h
print("\nLos padawans de Qui-Gon Jin y Mace Windu :")
if len(padawansJinWindu)==0:
    print("-No tuvieron padawans")
else:
    for i in padawansJinWindu:
        print(i)