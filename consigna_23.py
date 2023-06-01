def calcular_jugador_posicion_ranking(lista):
    lista_estadisticas = obtener_lista_estadisticas(lista)
    lista_ranking = []
    
    for indice in range(len(lista_estadisticas)):
        jugador = lista_estadisticas[indice]
        puntaje = {"nombre": jugador["nombre"], "puntos_totales": 1, "rebotes_totales": 1, "asistencias_totales": 1,"robos_totales": 1}
        for i in range(len(lista_estadisticas)):
            if indice != i:
                comparar_persona = lista_estadisticas[i]
                
                if jugador["puntos_totales"] < comparar_persona["puntos_totales"]:
                    puntaje["puntos_totales"] += 1
                
                if jugador["rebotes_totales"] < comparar_persona["rebotes_totales"]:
                    puntaje["rebotes_totales"] += 1
                
                if jugador["asistencias_totales"] < comparar_persona["asistencias_totales"]:
                    puntaje["asistencias_totales"] += 1

                if jugador["robos_totales"] < comparar_persona["robos_totales"]:
                    puntaje["robos_totales"] += 1

        lista_ranking.append(puntaje)
    claves = lista_ranking[0].keys()
    texto_claves = ','.join(claves)  
    texto_separado = texto_claves.replace("_"," ")
    texto_valores = ''
    nombre_archivo = "ranking_estadisticas.csv"
    for diccionario in lista_ranking:
        valores = [str(diccionario[clave]) for clave in claves]  
        texto_valores += ','.join(valores) + '\n'  
    obtener_formato_csv = texto_separado + '\n' + texto_valores

    with open(nombre_archivo, "w") as archivo:
        archivo.write(obtener_formato_csv)

calcular_jugador_posicion_ranking(lista_jugadores)