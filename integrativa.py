
lista_pueblo=["Mapuche", "Aymara", "Rapa Nui", "Lican Antai", "Quechua", "Colla", "Diaguita", "Kawèsqar", "Yagan", "Otro", "Ignorado"]
lista_poblacion=[1745147, 156754, 9399, 30369, 33868, 20744, 88474, 3448, 1600, 28115, 67874]


def MostrarDatos():
    print("\n:::..[ PUEBLOS ORIGINARIOS DE CHILE ]..:::\n")
    print("PUEBLO       HABITANTES\n")
    for i in range(len(lista_pueblo)):
        mostrarPueblos= print(lista_pueblo[i]," ---> ",lista_poblacion[i])
    return mostrarPueblos

def avg_poblacion(poblacion):
    porcentajeTotal= lambda x: x/(len(poblacion))
    suma= 0
    for i in range(len(poblacion)):
        suma+= (poblacion[i])
    print("\n:::..[ PROMEDIO ]..:::\n")
    mostrarPorcentaje=print("-> El pomedio total de los pueblos originarios de chile es:\n", "-->",round(porcentajeTotal(suma),2),"%")
    return mostrarPorcentaje

def min_poblacion(poblacion, pueblo):
    poblacionMinima= poblacion[0]
    for i in range(len(poblacion)):
        if poblacion[i]<poblacionMinima:
            poblacionMinima= poblacion[i]
            nombrePoblacion= pueblo[i]
            lista_min=[nombrePoblacion, poblacionMinima]
    mostrarMinima = print("* Poblacion con menos habitantes: ", lista_min[0], "\n*Cantida de habitantes: ", lista_min[1])
    return mostrarMinima

def max_poblacion(poblacion, pueblo):
    poblacionMaxima= 0
    for i in range(len(poblacion)):
        if poblacion[i]>poblacionMaxima:
            poblacionMaxima=poblacion[i]
            nombrePoblacion= pueblo[i]
        lista_max=[nombrePoblacion, poblacionMaxima]
    print("\n:::...[ ESTADISTICAS ]...:::\n")
    mostrarEstadisticas= print("* Poblacion con mas habitantes: ", lista_max[0], "\n* Cantidad de habitantes: ", lista_max[1])
    return mostrarEstadisticas

def hab_porcentaje(poblacion):
    calculoPorcentajes = lambda p: (p*100)/sumaTotal
    sumaTotal= 0
    lista_porcentajes=[]
    for i in poblacion:
        sumaTotal+= i
    for i in poblacion:
        lista_porcentajes.append(round(calculoPorcentajes(i),2))
    print("\n:::...[ PORCENTAJE DE LOS PUEBLOS ]...:::\n")
    for i in range(len(poblacion)):
        mostrarPorcentajeI= print(lista_pueblo[i], " ---> ", lista_porcentajes[i],"%")
    return mostrarPorcentajeI

def sum_poblacion(poblacion):
    sumaPoblacion= 0
    for i in range(len(poblacion)):
        sumaPoblacion+= poblacion[i]    
    print("\n:::..[ POBLACION TOTAL ]..:::\n")
    mostrarPoblacionTotal = print("\n-> Cantidad total de habitantes: ", sumaPoblacion)
    return mostrarPoblacionTotal

def OrdenDeDatos(comparacion):
    """
La funcion OrdenDeDatos(comparacion)
retornara el nombre y numero de habitantes de mayor a menor o de menor a mayor 
de los pueblos originarios de chile al pasar una cadena de texto igua a "Mayor" o "Menor" 
como parametro segun el orden en el que necesitemos ver los datos

la funcion evalua cada elemento de la lista lista_poblacion para encontrar la poblacion mayor o menor
y el indice en el que este se encuentra, reservando los valores en las variables correspondiente
max_val y max_index para luego comprobar el valor obtenido con las subsiguientes vueltas del ciclo for,
durante el recorrido del ciclo for, la variable especial que definimos para guardar el dato mayor o menor y el 
indice ira guardando y/o remplazando su valor cada vez que se encuentre un numero mayor o menor (segun
el parametro que le pasemos a nuestra funcion para que ordene los datos segun lo indiquemos)
al que ya posee y se quedara con ese ultimo valor

terminado el recorrido del ciclo for ya nuestras variables max_val y max_index contendran el valor mayor o menor
y el indcice donde este se encuentra dentro de nuestra lista lista_poblacion y en la variable x que contiene una 
lista vacia, se iran almacenando los indice obtenido, que serviran para ir aumentando el rango de la lista
para que nuestro ciclo while pueda parar, y a su vez usar los indices de x para comprobar en las vueltas 
siguientes si ese indice de lista_poblacion ya fue evaluado y no repetir su coprobacion, si el indice ya fue 
evaluado, el ciclo for pasa a su siguiente vuelta y evalua el indice siguiente, si el indice en el que vaya 
el recorrido comprueba que no esta en x pasara ha evaluar ese indice para saber si el valor que esta en 
lista_poblacion[indice que este evaluando] es el mayor o menor y hacer el proceso explicado anteriormente. 

al terminar el ciclo while, se retorna una variable valor (definida dentro del while), que contiene la impresion 
de los datos de lista_poblacion y lista_pueblo con max_index como su indice, (Recordando que max_index contiene
los indice ordenandos de los datos mayores o menores de las listas)
"""
    lista_index=[]
    while len(lista_index) < len(lista_poblacion):
        max_value= 0
        max_index=0
        for i in range(len(lista_poblacion)):
            if i in lista_index:
                None
            else:
                if comparacion == "Mayor":
                    if lista_poblacion[i]> max_value:
                        max_value= lista_poblacion[i]
                        max_index=i
                elif comparacion == "Menor":
                    if i == 0:
                        max_value = lista_poblacion[i]
                    elif lista_poblacion[i]< max_value:
                        max_value= lista_poblacion[i]
                        max_index=i
        lista_index.append(max_index)   
        ordenDatos= print(lista_poblacion[max_index],"\n",lista_pueblo[max_index],"\n")
    return ordenDatos
#******************************************************************************************************
opcion_menu = 1
while opcion_menu !=0:
    print("\n        ============ [ MENU ] ============ \n")
    print("* 1) Mostrar dato de los pueblos originarios de chile")
    print("* 2) Mostrar poblacion total")
    print("* 3) Mostrar promedio de todos los pueblos")
    print("* 4) Estadisticas de la poblacion")
    print("* 5) Mostrar porcentaje que representa cada poblacion")
    print("* 6) Mostra datos de manera ordenada")
    print("* 0) Opcion para salir\n")
    
    opcion_menu= int(input("\n--> Elige una opcion del menu: "))
    
    if opcion_menu==1:
        MostrarDatos()
   
    elif opcion_menu== 2:
        sum_poblacion(lista_poblacion)
    
    elif opcion_menu== 3:
        avg_poblacion(lista_poblacion)

    elif opcion_menu== 4:
        max_poblacion(lista_poblacion,lista_pueblo)
        print()
        min_poblacion(lista_poblacion, lista_pueblo)

    elif opcion_menu== 5:
        hab_porcentaje(lista_poblacion)

    elif opcion_menu==6:
        sub_menu= 1
        while sub_menu!=0:
            print("\n¿En que orden desea ver los datos?\n")
            print("* 1) De mayor a menor")
            print("* 2) De menor a mayor")
            print("* 0) Menu anterior")
            sub_menu= int(input("\nElije una opcion: \n"))
            if sub_menu==1:
                print("======[ DATOS DE MAYOR A MENOR ]======\n")
                OrdenDeDatos("Mayor")
            elif sub_menu== 2:
                print("======[ DATOS DE MENOR A MAYOR ]======\n")
                OrdenDeDatos("Menor")
            elif sub_menu==0:
                None
            elif sub_menu !=0:
                print("Solo puedes entre la opcion 1, 2 y 0")

    elif opcion_menu == 0:
        print("Usted ha salido del menu principal")
        
    else:
        print("Opcion no valida, ¡Ingrese una opcion del menu!")