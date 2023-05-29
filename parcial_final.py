import json
import re


def imprimir_dato(dato:str)->str:
    """
    muestra por consola el dato pasado
    resive un dato en string
    devuelve un string
    """
    return print(dato)


def leer_archivo(ruta_archivo:str)->list:
    """
    abre y lee un archivo de datos
    recibe la ruta del archivo
    devuelve una lista
    """
    with  open(ruta_archivo,"r") as archivo:
        lista = json.load(archivo)
        return lista["jugadores"]
    
ruta =r"C:\Users\Usuario\OneDrive\Escritorio\Parcial Programacion\dt.json"
lista_jugadores = leer_archivo(ruta)


def menu_opciones()->str:
    """
    contiene un menu de opciones 
    no recibe nada
    devueve el muenu 
    """
    menu ="\n\
MENU: \n\
1-Mostrar lista de nombre y posion de jugadores\n\
2-Mostrar estadisticas de jugador seleccionado \n\
3-Exportar archivo de las estadisticas del jugador selecc.\n\
4-Mostrar logros de jugador ingresando su nombre\n\
5-Mostrar el promedio de puntos por partido del equipo y de cada jugador ordenado alfaveticamente\n\
6-Mostrar si un jugador es Miembro de Salon de la Fama del Balocesto ingresadndo su nombre\n\
7-Mostrar el jugador con mayor rebotes totales\n\
8-Mostrar el jugador con el mayor porcentaje de tiros de campo.\n\
9-Mostrar el jugador con la mayor cantidad de asistencias totales.\n\
10-Ingresar un valor y mostrar los jugadores que han promediadomás puntos por partido que ese valor.\n\
11-Ingresar un valor y mostrar los jugadores que han promediadomás rebotes por partido que ese valor.\n\
12-Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.\n\
13-Mostrar el jugador con la mayor cantidad de robos totales.\n\
14-Mostrar el jugador con la mayor cantidad de bloqueos totales.\n\
15-Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.\n\
16-Mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.\n\
17-Mostrar el jugador con la mayor cantidad de logros obtenidos\n\
18-Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.\n\
19-Mostrar el jugador con la mayor cantidad de temporadas jugadas\n\
20-Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a\n\
ese valor.\n\
45-volver al menu anterior"
    return menu


def pedir_opciones()->str:
    """
    pide al usurio que ingrese un valor, verifica que el valor sea un strig numerico
    llama  a dos funcione para mostrar por terminal un menu
    no recibe nada
    devuelve el valor validado
    """
    imprimir_dato(menu_opciones())
    flag = False
    while(True):
        numero_ingresado = input("\ningrese la opcion deseada: ")
        if re.match(r"[aA-zZ]+|^[!@#$%^&*()_+.-]+$",numero_ingresado): # descarta letras y simbolos
            print("Error: ingrese solo numeros")
        elif re.match(r"^([1-9]{1}|1[0-9]{1}|20|23|45)$",numero_ingresado):
            flag = True
        else:
            print("Error: numero exdido")
        break
    if flag == True:
        return numero_ingresado
    

def control_funciones(lista:list):
    """
    controla e inicializa las funciones del programa
    llama a otra funcion para obtener opciones para machearlos
    resive una lista de datos
    no retorna nada
    """
    while(True):
        opciones = pedir_opciones()
        match(opciones):
            case "1":
                mostrar_jugadores_pocision(lista,"posicion")
            case "2":
                mostrar_estadisticas(lista,True)
            case "3":
                exportar_archivo_csv_estadisticas(lista)
            case "4":
                buscar_jugador_nombre_logros(lista)
            case "5":
                calcular_mostrar_promedio_puntos_partido_del_equipo_y_ordenar_nombre_alfabeticamente(lista_jugadores,"asc","nombre","promedio_puntos_por_partido")
            case "6":
                mostrar_miembro_del_salon_de_la_fama(lista,"Miembro del Salon de la Fama del Baloncesto")
            case "7":
                calcular_mayor_estadisticas(lista,"rebotes_totales")
            case "8":
                calcular_mayor_estadisticas(lista,"porcentaje_tiros_de_campo")
            case "9":
                calcular_mayor_estadisticas(lista,"asistencias_totales")
            case "10":
                calcular_mostrar_jugadores_por_valor_ingresado(lista,"promedio_puntos_por_partido")
            case "11":
                calcular_mostrar_jugadores_por_valor_ingresado(lista,"promedio_rebotes_por_partido")
            case "12":
                calcular_mostrar_jugadores_por_valor_ingresado(lista,"promedio_asistencias_por_partido")
            case "13":
                calcular_mayor_estadisticas(lista,"robos_totales")
            case "14":
                calcular_mayor_estadisticas(lista,"bloqueos_totales")
            case "15":
                calcular_mostrar_jugadores_por_valor_ingresado(lista,"porcentaje_tiros_libres")
            case "16":
                calcular_mostrar_promedio_excluyendo_jugador_menor_cantidad_puntos_partido(lista,"promedio_puntos_por_partido")
            case "17":
                calcular_jugador_mas_logros(lista_jugadores,"logros")
            case "18":
                calcular_mostrar_jugadores_por_valor_ingresado(lista,"porcentaje_tiros_triples")
            case "19":
                calcular_mayor_estadisticas(lista,"temporadas")
            case "20":
                ingresar_valor_mostrar_jugadores_ordenados_por_posición(lista_jugadores,"posicion","porcentaje_tiros_de_campo","asc")
            case "45":
                break

def menu_jugadores(lista:list):
    """
    itera sobre la lista, para optener los nombres y agrega un numero a cada nombre
    muestra por terminal los nombres
    recibe una lista de datos
    no devuelve nada
    """
    contador = 0
    for jugador in lista:
        contador += 1
        texto_salida = "{0}-{1}".format(contador,jugador["nombre"])
        imprimir_dato(texto_salida)


def validar_numero()->float:
    """
    pide al usurio que ingrese un valor, verifica que el valor sea un valor numerico
    castea el valor a float
    no recibe nada
    retorna el valor
    """
    while(True):
        numero_ingresado = input("Ingrese un valor: ") 
        if re.search(r"^([1-9]+)$",numero_ingresado):
            numero_casteado = float(numero_ingresado)
            return numero_casteado
        else:
            imprimir_dato("ingrese el numero del menu")


def validar_texto()->str:
    """
    pide al usurio que ingrese un valor, verifica que el valor sea un valor alfabetico
    no recibe nada
    retorna el valor
    """
    while(True):
        texto_ingresado = input("> ")
        if re.search(r"^[aA-zZ ]+$",texto_ingresado):
            return texto_ingresado
        else:
            imprimir_dato("ingrese solo texto")


def obtener_lista_estadisticas(lista:list)->list:
    """
    itera sobre una lista para obtener una lista de diccionarios y nombres
    agrega los nombres a los diccionarios
    recibe un alista
    retorna una lista de diccionarios
    """
    lista_copia_madre= lista[:]
    lista_datos_jugadores = []
    for jugador in lista_copia_madre:
        lista_datos_jugadores.append(jugador["estadisticas"])
        jugador["estadisticas"]["nombre"] = jugador["nombre"]      
    return lista_datos_jugadores


def obtener_cadena_texto_separada_capitalizadas(texto:str)->str:
    """
    formatea una cadena de texto, reemplaza un signo por un espacio
    recibe una cadena texto
    retorna el texto formateado
    """
    formatear = texto.replace("_"," ").capitalize()
    return formatear


def mostrar_obtener_nombre_clave(jugador:dict,clave:str):
    """
    obtiene la clave y nombre de un diccionario de un jugador
    llama a otra funcion para mostrar por terminal el nombre y la clave fromateada
    recibe un diccionario y una clave
    no retorna nada
    """
    clave_formateada = obtener_cadena_texto_separada_capitalizadas(clave)
    imprimir_dato("Nombre: {0}|{1}: {2}".format(jugador["nombre"] ,clave_formateada,jugador[clave]))


def calcular_mostrar_jugadores_por_valor_ingresado(lista:list,clave:str):
    """
    llama a dos funciones para obtener una lista y un valor
    itera sobre una lista para obtener un clave y lo compara con un valor ingresado
    llama a otra funcuion para mostrar la clave y nombre por terminal mayores al valor ingresado
    recibe una lista y una clave 
    no retorna nada
    """
    lista_copia = obtener_lista_estadisticas(lista)
    valor_ingresado = validar_numero()
    for jugador in lista_copia:
        if jugador[clave] > valor_ingresado:
            mostrar_obtener_nombre_clave(jugador,clave)
        else:
            imprimir_dato("numero exede los datos de los jugadores")


def suma_datos_de_estadisticas(lista:list,clave:str)->float:
    """
    itera sobre un alista para obtener una clave y sumarla 
    recibe una lista de datos y un clave como texto
    retorna la suma de las claves
    """
    suma = 0
    for jugadores in lista:
        suma += jugadores[clave]
    return suma


def formatear_numeros_flotantes(numero:float)->float:
    """
    formatea numeros flotantes mostrando solo dos numeros despues de la coma
    recibe un valor flotante
    retorna un valor flotante
    """
    return round(numero, 2)


def calcular_promedio_datos_de_estadisticas(lista:list,clave:str)->float:
    """
    calcula el promedio y llama otra funcion para obtneer las claves sumadas
    y lo divide por el indice total de la lista
    recibe un alista de diccionarios y una clave 
    retorna el resultado del calculo
    """
    divisor = len(lista)
    dividendo = suma_datos_de_estadisticas(lista,clave)
    producto = dividendo / divisor
    return formatear_numeros_flotantes(producto)


def calcular_mayor_estadisticas(lista:list,clave:str):
    """
    itera sobre una lista de diccionarios, compara y calcula la clave mayor de los diccionarios
    muestra por terminal el nombre y la  clave obtenida
    recibe una lista de diccionarios y un clave a buscar
    no retorna nada
    """
    lista_copia = obtener_lista_estadisticas(lista)
    mayor = None
    for jugador in lista_copia:
        if mayor == None or jugador[clave] > mayor:
            mayor = jugador[clave]
            nombre = jugador["nombre"]
    mostrar_obtener_nombre_clave(jugador,clave)


def calcular_menor_estadisticas(lista:list,clave:str)->float: 
    """
    itera sobre una lista de diccionarios, compara y calcula la clave menor de los diccionarios
    muestra por terminal el nombre y la  clave obtenida
    recibe una lista de diccionarios y un clave a buscar
    retorna la clave menor
    """
    lista_estadisticas = obtener_lista_estadisticas(lista)
    menor = None
    for jugador in  lista_estadisticas:
        if menor == None or jugador[clave] < menor:
            menor = jugador[clave]
            nombre = jugador["nombre"]
    return menor

def ordenar_listas(lista:list,ordenar_clave:str,orden:str)->list:
    """
    itera sobre una lista y ordena sus claves de manera ascendente o descente 
    recibe un alista de datos, la clave a ordenar y el orden para ordenar
    retorna la lista ordenada
    """
    rango = len(lista) -1
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        for indice in range(rango):
            if orden == "asc" and lista[indice][ordenar_clave] > lista[indice+1][ordenar_clave] \
            or orden == "desc" and lista[indice][ordenar_clave] < lista[indice+1][ordenar_clave]:
                lista[indice],lista[indice+1] = lista[indice+1],lista[indice]
                flag_swap = True
    return lista
    

def mostrar_jugadores_pocision(lista:list,clave:str):
    """
    itera sobre una lista y obtiene las claves, llama a otra funcion para mostrar 
    el nombre y la clave por la terminal
    recibe una lista de diccionarios y una clave
    no retorna nada
    """
    for jugador in lista:
        mostrar_obtener_nombre_clave(jugador,clave)
  

def mostrar_estadisticas(lista:list,mostrar_mensaje:bool)->list:
    """
    llama a dos funciones para obtener un valor e imprimir un menu
    itera sobre la lista para obtner un lista y un nombre
    muestra por terminal los elemtos de la lista y el nombre guarda la lista obtenida
    recibe una lista y un valor booleano
    retorna la lista obtenida y nombre
    """
    menu_jugadores(lista)
    numero_ingresado = validar_numero()
    lista_estadisticas = []
    dicc = {}
    for indice in range(len(lista)):
        if indice == numero_ingresado -1:
            jugador_elegido =  lista[indice]["estadisticas"]
            nombre = lista[indice]["nombre"]
    for clave,valor in jugador_elegido.items():
        formateo = obtener_cadena_texto_separada_capitalizadas(clave)
        salida = "{0}: {1}".format(formateo,valor)
        if mostrar_mensaje:
            imprimir_dato(salida)
        dicc[formateo] = valor
    lista_estadisticas.append(dicc)
    lista_a_exportar = lista_estadisticas[:]
    return lista_a_exportar,nombre


def exportar_archivo_csv_estadisticas(lista:list):
    """
    llama a otra funcion parta obtner la lista, nombre y formatea los elementos de la lista a estring 
    y exporta la lista en un archivo csv con el nombre obtenido
    recibe una lista
    no retorna nada
    """
    lista_a_exporortar,nombre_jugador = mostrar_estadisticas(lista,False)
    claves = lista_a_exporortar[0].keys()
    texto_claves = ','.join(claves)  
    texto_valores = ''
    formatear_nombre = nombre_jugador.replace(" ","_")
    nombre_archivo = "{0}_estadisticas.csv".format(formatear_nombre)
    for diccionario in lista_a_exporortar:
        valores = [str(diccionario[clave]) for clave in claves]  
        texto_valores += ','.join(valores) + '\n'  
    obtener_formato_csv = texto_claves + '\n' + texto_valores

    with open(nombre_archivo, "w") as archivo:
        archivo.write(obtener_formato_csv)


def buscar_jugador_nombre_logros(lista:list):
    """
    itera sobre una lista de diccionarios para obtener clave y nombre 
    imprime en la terminal el nombre y la clave obtenida
    recibe uns lista de diccionarios
    no retorna nada
    """
    imprimir_dato("ingrese nombre del jugador a buscar")
    nombre_obtenido = validar_texto()
    nombre_validado = nombre_obtenido.title()
    for jugador in lista:
        if jugador["nombre"] == nombre_validado:
            logros = jugador["logros"]
            formateo = "\n".join((elemento)for elemento in logros)
            imprimir_dato(formateo)
        

def calcular_mostrar_promedio_puntos_partido_del_equipo_y_ordenar_nombre_alfabeticamente(lista:list,orden:str,ordenar_clave:str,clave:str):
    """
    llama a 3 funciones para obtener un lista de diccionarios,clave,nombres, calcula el promedio de las claves de la lista
    y muestra por la terminal el promedio total y los promedios de los jugadores en orden alfabetico
    recibe una lista, un strig para el orden, la clave a ordenar y la clave a calcular
    no retorna nada
    """
    lista_copia = obtener_lista_estadisticas(lista)
    proemdio = calcular_promedio_datos_de_estadisticas(lista_copia,clave)
    mensaje = "El promedio del equipo es: {0}\nPromedio de los jugadores:".format(proemdio)
    imprimir_dato(mensaje)
    lista_ordenada = ordenar_listas(lista_copia,ordenar_clave,orden)
    for jugadores in lista_ordenada: 
        mostrar_obtener_nombre_clave(jugadores,clave)


def mostrar_miembro_del_salon_de_la_fama(lista:list,clave_logro:str):
    """
    itera sobre una lista para obtener el nombre y saber si coincide con la clave recibida
    y lo muestra por la terminal 
    no retorna nada
    """
    flag = True
    imprimir_dato("Ingrese nombre del jugador")
    nombre_ingresado = validar_texto()
    nombre_validado = nombre_ingresado.title()
    for jugador in lista:
        obtener_logros = jugador["logros"]
        for logro in obtener_logros:
            if jugador["nombre"] == nombre_validado and logro == clave_logro :
                imprimir_dato("si es miembro del Salon de la Fama del Baloncesto")
                flag = True
            else:
                flag = False
    if flag == False:
        imprimir_dato("no es mioembro del Salon de la Fama del Baloncesto")


def calcular_mostrar_promedio_excluyendo_jugador_menor_cantidad_puntos_partido(lista:list,clave:str):
    """
    calcula la clave con menor valor de la lista recibida
    itera sobre una lista de diccionarios para calcular la clave recibida de los diccionarios
    muestra el promedio de las claves exluyendo a la clave menor
    recibe una lista de diccionarios y una clave como parametro
    no retorna nada
    """
    lista_estadisticas = obtener_lista_estadisticas(lista)
    valor_jugador_excluido = calcular_menor_estadisticas(lista,clave)
    for jugador in lista_estadisticas:
        if jugador[clave] == valor_jugador_excluido:
            lista_estadisticas.remove(jugador)
    promedio = calcular_promedio_datos_de_estadisticas(lista_estadisticas,clave)
    mensaje = "El promedio del equipo del equipo exluyendo al jugador con la menor cantidad de puntos por partido es: {0} Pts.".format(promedio)
    imprimir_dato(mensaje)


def calcular_jugador_mas_logros(lista:list,clave:str):
    """
    itera sobre una lista de diccionarios y busca la clave y nombre, calcula el len de las listas
    dentro de los diccionarios y busca el mayor, muestra al nombre que coincida con el diccionario
    recibe una listade diccionarios y una clave como parametro
    no retorna nada
    """
    mayor = None
    for jugador in lista:
        if mayor == None or len(jugador[clave]) > mayor:
            mayor = len(jugador[clave])
            mostrar_jugador = "Nombre: {0}|Jugador con mayor logros obtenidos".format(jugador["nombre"])
            imprimir_dato(mostrar_jugador)


def ingresar_valor_mostrar_jugadores_ordenados_por_posición(lista,clave_ordenar,clave,orden):
    """
    llama a dos funciones para calcular las claves mayor al valor ingresado
    ordena la lista alfabeticamente segun la posicion
    recibe una lista de diccionarios, un strig para el orden, la clave a ordenar y la clave a calcular
    no retorna nada
    """
    lista_ordenada_posicion = ordenar_listas(lista,orden)
    calcular_mostrar_jugadores_por_valor_ingresado(lista_ordenada_posicion,clave)

control_funciones(lista_jugadores)