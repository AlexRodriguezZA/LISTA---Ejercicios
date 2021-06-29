from listas import Lista;
#Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
#Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con
#la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un
#algoritmo que permita realizar la siguientes actividades:
#a. mostrar los alumnos ordenados alfabéticamente por apellido;
#b. indicar los alumnos que no desaprobaron ningún parcial;
#c. determinar los alumnos que tienen promedio mayor a 8,89;
#d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
#e. mostrar el promedio de cada uno de los alumnos;
#f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
#g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
#h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
#i. mostrar todos los alumnos que rindieron en el año 2020;
#j. debe modificar el TDA para implementar lista de lista.

ListaAlumno = Lista()
AlumnosNoDesaprobados = []
AlumnosPromediosMayores = []
Alumnos2020 = []
Alumnos = [
    {"Nombre":"Alex","Apellido":"Rodriguez","ListaParciales":Lista()},

    {"Nombre":"Eugenia","Apellido":"Santamaria","ListaParciales":Lista()},

    {"Nombre":"Dimas","Apellido":"Lelasquez","ListaParciales":Lista()},

    {"Nombre":"luciano","Apellido":"Arriondo","ListaParciales":Lista()}
]

datosAlex = [
    {"Materia":"Algoritmo y Datos","Nota":6.7,"Fecha":"15/05/2021"},
    {"Materia":"Ingenieria de SW","Nota":6.7,"Fecha":"10/05/2020"}
]
datosEuge = [
    {"Materia":"Bases de datos","Nota":9.7,"Fecha":"10/03/2021"},
    {"Materia":"Mat discretas","Nota":10,"Fecha":"10/05/2020"}
]
datosDimas = [
    {"Materia":"Estadisticas","Nota":10,"Fecha":"14/08/2021"},
    {"Materia":"Algoritmo y Datos","Nota":4,"Fecha":"10/05/2022"}
]
datosLuciano = [
    {"Materia":"Estadisticas","Nota":10,"Fecha":"14/08/2021"},
    {"Materia":"Mat discretas","Nota":6.7,"Fecha":"10/05/2022"}
]
#Cargamos los alumnos:
for alumno in Alumnos:
    ListaAlumno.insertar(alumno,"Nombre")

#Cargamos los parciales a los alumnos:
pos = ListaAlumno.busqueda("Alex","Nombre")
if pos>-1:
    alex = ListaAlumno.obtenerElemento(pos)
    for parcial in datosAlex:
        alex["ListaParciales"].insertar(parcial,"Materia")

poslu = ListaAlumno.busqueda("luciano","Nombre")
if pos>-1:
    luciano = ListaAlumno.obtenerElemento(poslu)
    for parcial in datosLuciano:
        luciano["ListaParciales"].insertar(parcial,"Materia")

poseu = ListaAlumno.busqueda("Eugenia","Nombre")
if pos>-1:
    Eugenia = ListaAlumno.obtenerElemento(poseu)
    for parcial in datosEuge:
        Eugenia["ListaParciales"].insertar(parcial,"Materia")

posdi = ListaAlumno.busqueda("Dimas","Nombre")
if pos>-1:
    Dimas = ListaAlumno.obtenerElemento(posdi)
    for parcial in datosDimas:
        Dimas["ListaParciales"].insertar(parcial,"Materia")
        pos = ListaAlumno.busqueda("Sofia","Nombre")



#Punto a
print(ListaAlumno.barrido())
#alumnosBuscado = str(input("Ingrese un alumnos que desee ver su porcentaje"))
#punto b
contadorAprobadoBasesDeDatos = 0;
#RECORRER LISTAS DE ALUMNOS
for i in range(ListaAlumno.tamanio()):
    aprobado=False;
    contador = 0;
    Promedios = 0;
    acumuladorPromedio=0;
    alumnito = ListaAlumno.obtenerElemento(i)
    if (alumnito["Apellido"][0] == "L"):
        #punto d
        print("Empieza con L --> ",alumnito)

    #RECORRER LISTAS DE MATERIAS DE CADA ALUMNO
    for j in range(alumnito["ListaParciales"].tamanio()):
        MateriaAlumnito = alumnito["ListaParciales"].obtenerElemento(j)
        if (MateriaAlumnito["Fecha"][6:] == "2020"):
            Alumnos2020.append(alumnito)
        #punto g
        #if (alumnito["Nombre"]==alumnosBuscado):
           # pass#calcular el procentaje
        #punto f    
        if (MateriaAlumnito["Materia"]=="Algoritmo y Datos"):
            print(alumnito["Nombre"]," estudia ", "Algoritmo y Datos")
        acumuladorPromedio = MateriaAlumnito["Nota"] + acumuladorPromedio;
        
        if (MateriaAlumnito["Materia"] == "Bases de datos" and MateriaAlumnito["Nota"]>6 ):
            contadorAprobadoBasesDeDatos += 1

        if (MateriaAlumnito["Nota"]>6):
            contador+=1; #Punto b
    if (contador == alumnito["ListaParciales"].tamanio()):
        AlumnosNoDesaprobados.append(alumnito)

    Promedios = acumuladorPromedio / alumnito["ListaParciales"].tamanio();
    #punto e
    print("Promedio de ",alumnito["Nombre"]," es ",Promedios)
    if (Promedios > 8.89):
        AlumnosPromediosMayores.append(alumnito)

print("Los alumnos que desaprobarin ninguna materia son -->" )
for n in AlumnosNoDesaprobados:
    print(n["Nombre"])

#punto c
print("\nLos alumnos con promedios mayores a 8.89 son -->" )
for a in AlumnosPromediosMayores:
    print(a["Nombre"])
print("\nLos alumnos que aprobaron Bases de datos son --> ", contadorAprobadoBasesDeDatos )

print("\nLos alumnos que rindieron en 2020 -->" )
for i in Alumnos2020:
    print(i["Nombre"])







    


