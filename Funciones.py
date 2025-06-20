from Inputs import *
def calcular_promedios_participantes(matriz_puntaje:list,cantidad_jurados:int,cantidad_participantes:int) -> list:
    #Calcula el promedio de un grupo de participantes en base a la calificacion de una cantidad de jueces
    #Crea la lista para devolver los promedios
    lista_promedios_participante = crear_array(cantidad_participantes,0)
    #Recorre la matriz donde se guardaron los puntajes
    for fil in range(len(lista_promedios_participante)):
        #Cada vez que cambia de fila reinicia el acumulador (cada fila representa un participante diferente)
        acumulador = 0
        for col in range(cantidad_jurados):
            #Pasa secuencialmente por cada columna sumando todas, de una misma fila
            acumulador += matriz_puntaje[fil][col]
        #Cuando tiene la suma de la nota de cada juez, para el mismo participante, la divide por la cantidad de jueces
        #Guarda ese promedio en el indice correspondiente al numero de participante
        lista_promedios_participante[fil]= acumulador / cantidad_jurados
    #Devuelve la lista, donde los indices coinciden con la lista nombres
    return lista_promedios_participante

def calcular_promedio_jurado(matriz_puntaje:list,cantidad_participantes:int,cantidad_jurados:int) -> list:
    #Calcula y guarda en una lista los promedios de cada jurado
    #Crea la lista que va a devolver
    lista_promedios_jurado = crear_array (cantidad_jurados,0)
    #Recorre la matriz donde se guardaron los puntajes
    for col in range(cantidad_jurados):
        acumulador = 0
        for fil in range(cantidad_participantes):
            acumulador += matriz_puntaje[fil][col]
        lista_promedios_jurado[col] = acumulador / cantidad_participantes
        
    return lista_promedios_jurado

def filtrar_promedios(lista_promedios:list,lista_nombres:list,criterio:float) -> bool:
    #Filtra una lista de valores segun un criterio dado y los imprime en pantalla
    bandera = False
    for i in range(len(lista_promedios)):
        #Compara los promedios con el criterio seleccionado
        if lista_promedios[i] < criterio:
            #Sí el valor es menor que el criterio, imprime su nombre y promedio en pantalla
            print(f"{lista_nombres[i]} tiene de promedio menos de {criterio}.\nSu promedio es {lista_promedios[i]}")
            bandera = True
    if bandera == False:
        #Mensaje de error
        print(f"Ningun participante tiene menos de {criterio} promedio")

    return bandera

def mostrar_matriz(matriz:list,lista_nombres:list,lista_promedios_participante:list) -> None:
    for fil in range(len(matriz)):
        #Muestra una lista ordenada con el nombre, votos de cada juez y promedio
        print(f"NOMBRE PARTICIPANTE: {lista_nombres[fil]}")
        for col in range(len(matriz[fil])):
            print(f"VOTO JUEZ {col+1}: {matriz[fil][col]}")
        print(f"PROMEDIO: {lista_promedios_participante[fil]}")

def comparar_jurados_estricto (lista_promedios_jurado:list,cantidad_jurados:int) -> bool:
    #Compara el promedio de los jurados para determinar cual es mas bajo
    #Le asigna a una variable auxiliar el valor del primer elemento de la lista
    comparado = lista_promedios_jurado[0]
    #Usa otro variable auxiliar para guardar el indice en el que se encuentra el promedio mas bajo
    num = 0
    #Recorre la lista de promedios comparandolos con el primer valor y reemplazando el valor de la variable temporal a medida que encuentra valores más bajos dentro de la lista
    for i in range(cantidad_jurados):
        if lista_promedios_jurado[i] < comparado:
            #Al encontrar un valor más bajo, le asigna ese valor a la variable auxiliar
            comparado = lista_promedios_jurado[i]
            #Guarda el indice en donde encontro este valor
            num = i
    #Por pantalla usa las dos variables auxiliares para mostrar el numero de jurado y el promedio correspondiente
    print(f"El jurado mas estricto es el {num+1} con {comparado} de promedio")
    
    return True

def comparar_jurados_generoso (lista_promedios_jurado:list,cantidad_jurados:int) -> bool:
    #Compara el promedio de los jurados para determinar cual es más alto
    #Le asigna a una variable auxiliar el valor del primer elemento de la lista
    comparado = lista_promedios_jurado[0]
    #Usa otro variable auxiliar para guardar el indice en el que se encuentra el promedio mas bajo
    num = 0
    #Recorre la lista de promedios comparandolos con el primer valor y reemplazando el valor de la variable temporal a medida que encuentra valores más altos dentro de la lista
    for i in range(cantidad_jurados):
        if lista_promedios_jurado[i] > comparado:
            #Al encontrar un valor más bajo, le asigna ese valor a la variable auxiliar
            comparado = lista_promedios_jurado[i]
            #Guarda el indice en donde encontro este valor
            num = i
    #Por pantalla usa las dos variables auxiliares para mostrar el numero de jurado y su promedio correspondiente
    print(f"El jurado mas generoso es el {num+1} con {comparado} de promedio")
    
    return True

def encontrar_promedios_iguales(lista_promedios_participante: list, lista_nombres: list, cantidad_participantes: int) -> bool:
    # Encuentra y muestra por pantalla los promedios que son iguales en la lista dada
    # Inicializa las variables que va a usar
    encontrados = False
    promedios_ya_revisados = crear_array(cantidad_participantes, 0)
    contador_revisados = 0
    posiciones = crear_array(cantidad_participantes, 0)  # Array para guardar posiciones
    # Comparar cada promedio con los demás
    for i in range(cantidad_participantes):
        promedio_actual = lista_promedios_participante[i]
        # Verificar si ya fue revisado
        ya_revisado = False
        for k in range(contador_revisados):
            if promedio_actual == promedios_ya_revisados[k]:
                ya_revisado = True
                break
        if ya_revisado == True:
            continue
        # Contar cuántas veces aparece este promedio y guardar posiciones
        contador = 0
        for j in range(cantidad_participantes):
            if lista_promedios_participante[j] == promedio_actual:
                posiciones[contador] = j  # Guardar la posición real (sin +1)
                contador = contador + 1
        # Si aparece más de una vez, mostrarlo
        if contador > 1:
            encontrados = True
            mensaje = f"Promedio {promedio_actual} aparece {contador} veces en participantes: "
            # Construir la cadena con los nombres de los participantes
            for p in range(contador):
                if p > 0:
                    mensaje = mensaje + ", "
                mensaje = mensaje + f"{lista_nombres[posiciones[p]]}"
            print(mensaje)
        # Agregar a la lista de ya revisados
        promedios_ya_revisados[contador_revisados] = promedio_actual
        contador_revisados = contador_revisados + 1
    # En caso de no haber repeticiones en la lista, lo muestra por pantalla
    if encontrados == False:
        print("NO SE ENCONTRARON PROMEDIOS IGUALES")
    
    return encontrados

def ordenar_nombres_alfabeticamente(lista_nombres:list) -> list:
    #Ordena un array de nombres alfabéticamente
    #Crear una copia del array para no modificar el original
    nombres_ordenados = lista_nombres[:]
    #Recorre la lista original en todo su largo
    for i in range(len(lista_nombres)):
        for j in range(len(lista_nombres)-i-1):
            # Comparar los nombres
            if nombres_ordenados[j] > nombres_ordenados[j + 1]:
                # Intercambiar la posicion usando variables temporales
                temp = nombres_ordenados[j]
                nombres_ordenados[j] = nombres_ordenados[j + 1]
                nombres_ordenados[j + 1] = temp
    
    return nombres_ordenados


def calcular_mejores_promedios(lista_promedios_participante: list, cantidad_participantes: int) -> tuple:
    #Recibe una lista de promedios y devuelve los 3 mejores (más altos) y sus índices originales.
    #Crear lista de índices para rastrear posiciones originales
    indices_originales = crear_array(cantidad_participantes,0)  # Crear una lista del tamaño de participantes llena de ceros
    for i in range(len(indices_originales)):
        #Llena esta lista con los indices de menor a mayor
        indices_originales[i] = i
    #Ordenar de mayor a menor usando algoritmo de selección
    #Intercambiamos tanto los valores como los índices
    for i in range(len(lista_promedios_participante)):
        #Encontrar el índice del elemento más grande en la parte no ordenada
        max_i = i
        j = i + 1  # Empezar desde la siguiente posición
        while j < len(lista_promedios_participante):
            if lista_promedios_participante[j] > lista_promedios_participante[max_i]:
                max_i = j
            j = j + 1 
        #Intercambiar elementos en ambas listas usando variables auxiliares
        temporal_valor = lista_promedios_participante[i]
        lista_promedios_participante[i] = lista_promedios_participante[max_i]
        lista_promedios_participante[max_i] = temporal_valor
        temporal_indice = indices_originales[i]
        indices_originales[i] = indices_originales[max_i]
        indices_originales[max_i] = temporal_indice
    #Devolver los 3 mejores valores y sus índices originales (ya están ordenados)
    mejores_tres = [lista_promedios_participante[0], lista_promedios_participante[1], lista_promedios_participante[2]]
    indice_referencia = [indices_originales[0], indices_originales[1], indices_originales[2]]
    
    return mejores_tres, indice_referencia

def buscar(lista_nombres:list,matriz:list,nombre_buscado:str,cantidad_jurados:int,cantidad_participantes:int) -> bool:
    #Busca un nombre pedido previamente ignorando mayusculas y minusculas
    encontrado = False    
    #Convertir el nombre buscado a minúsculas para comparar
    nombre_buscado_minus = nombre_buscado.lower()
    #Buscar ignorando mayúsculas/minúsculas
    for i in range(len(lista_nombres)):
        if lista_nombres[i].lower() == nombre_buscado_minus:
            encontrado = True
            nombre_original = lista_nombres[i]
            indice = i
            break
    #Mostrar resultado
    if encontrado == True:
        lista_promedios_participante = calcular_promedios_participantes(matriz,cantidad_jurados,cantidad_participantes)
        #Muestra el nombre buscado y su ficha
        print(f"¡{nombre_original} encontrado!\nFICHA DEL PARTICIPANTE:\nNOMBRE: {lista_nombres[indice]}")
        for col in range(len(matriz[indice])):
            #Muestra los votos de cada juez y el promedio del participante
            print(f"VOTO JUEZ {col+1}: {matriz[indice][col]}")
        print(f"PROMEDIO: {lista_promedios_participante[indice]}")
    else:
        #Si no se encuentra el nombre buscado, lo informa por pantalla
        print(f"El nombre {nombre_buscado} no se encuentra en la lista")
    
    return encontrado