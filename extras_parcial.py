
# 1
def cantidad_jugadores_pocision(lista:list,clave:str):
    """
    calcula veces que se repite una clave en diccionarios de jugadores
    y lo muestra por la terminal
    recibe una lista de diccionarios
    retorna una clave como parametro
    """
    cantidad_posicion = {}
    for jugador in lista:
        obtener_posicion = jugador[clave]
        if obtener_posicion in cantidad_posicion:
            cantidad_posicion[obtener_posicion] += 1
        else:
            cantidad_posicion[obtener_posicion] = 1
    
    for clave,valor in cantidad_posicion.items():
        texto_salida = "{0}: {1}".format(clave,valor)
        imprimir_dato(texto_salida)

# cantidad_jugadores_pocision(lista_jugadores,"posicion")



# 3
def calcular_mejores_estadisticas_jugador(lista:list):
    """
    itera sobre una lista de diccionarios para obtener nombres y valores para mostrar por terminal
    los valores maximos junto al nombre
    recibe una lista de diccionarios 
    no retorna nada
    """
    lista_estadisticas = obtener_lista_estadisticas(lista)
    for jugador in lista_estadisticas:
        pass
    for clave,valor in jugador.items():
        clave_buscar = clave
        calcular_mayor_estadisticas(lista,clave_buscar)
    
# calcular_mejores_estadisticas_jugador(lista_jugadores)

