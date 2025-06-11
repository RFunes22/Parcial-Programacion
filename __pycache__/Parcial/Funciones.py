def calcular_promedio_jurado(matriz_puntaje:list,cantidad_participantes:int) -> list:
    #Calcula los promedios individuales de cada jurado
    lista_promedios_jurado = []
      #Recorre la matriz por columnas
    for col in range(len(matriz_puntaje[fil])):
        #Empieza reiniciando el contador cuando cambia de columna
        acumulador = 0
        #Recorre toda la columna 0 de todas las filas y cambia a la columna 1 y repite el proceso
        for fil in range(len(matriz_puntaje)):
            acumulador += matriz_puntaje[fil][col]
        #Guarda el promedio de cada juez en una lista
        lista_promedios_jurado[col] = acumulador / cantidad_participantes
    
    return lista_promedios_jurado

def cargar_nombres(lista_nombres:list,cantidad_nombres:int) -> list:
      #Carga, verifica y guarda en una lista, una cantidad de nombres dada
      for i in range(cantidad_nombres):
            bandera = False
            while bandera == False:
                  #Pide el dato
                  lista_nombres[i] = input(f"Ingrese el nombre del participante {i+1}: ")
                  valor = lista_nombres[i]
                  #Recorre el str guardado en la posicion i de la lista de nombres
                  for p in range(len(valor)):
                        #Verifica que tenga mas de 3 digitos
                        if len(valor) >= 3:
                              valor_caracter = 0                              
                              valor_caracter = valor[p]
                              valor_caracter = ord(valor_caracter)
                              bandera = True
                              #Verifica que el valor ascii de los caracteres sean validos
                              if valor_caracter >= 123 or valor_caracter <= 64:
                                    #Mensaje de error
                                    print(f"ERROR\n{valor} no es un nombre valido. Para que cargar correctamente el nombre, este debe contener solo letras y espacio")
                                    bandera = False
                        else:
                              #Mensaje de error
                              print(f"ERROR\n{valor} no es un nombre valido. Para que cargar correctamente el nombre, este debe contener solo letras y espacio")
                              bandera = False
      if bandera == True:
            #Confirmacion de carga exitosa
            print("Los nombres fueron cargados correctamente")
      
      return lista_nombres

def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    #Sirve para crear una matriz
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
        
    return matriz

def crear_array(cantidad_elementos:float,valor_inicial:any) -> list:
    array = [valor_inicial] * cantidad_elementos
    
    return array

def cargar_puntaje(matriz_puntaje:list,lista_nombres:list) -> list:
    for fil in range(len(matriz_puntaje)):
        for col in range(len(matriz_puntaje[fil])):
            #Pedir el dato
            puntaje = int(input(f"Ingrese el puntaje del juez numero {col + 1} para {lista_nombres[fil]}: "))
            #Verificacion del dato
            while puntaje < 1 or puntaje > 10:
                print("Puntaje ingresada fuera de rango (debe estar entre 1 y 10)")
                puntaje = int(input(f"Ingrese nuevamente el puntaje del juez numero {col + 1} para {lista_nombres[fil]}: "))
            #Guardarlo en la matriz
            matriz_puntaje[fil][col] = puntaje
       
    return matriz_puntaje


def filtrar_promedios(lista_promedios:list,lista_nombres:list,criterio:float) -> bool:
    for i in range(len(lista_promedios)):
        #Compara los promedios con el criterio seleccionado
        if lista_promedios[i] < criterio:
            bandera = True
            #Sí el participante tiene menos puntaje que el criterio, imprime su nombre en  pantalla
            print(f"{lista_nombres[i]} tiene de promedio menos de {criterio}, tiene {lista_promedios[i]} como promedio")
        else:
            bandera = False

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

def calcular_promedios_participantes(matriz_puntaje:list,cantidad_jurados:int) -> list:
    #Calcula y guarda en una lista los promedios de los participantes
    lista_promedios_participante = []
    #Recorre el la matriz con los puntajes por fila
    for fil in range(3):
        acumulador = 0
    #Recorre la primer fila, suma todos los valores y los divide por la cantidad de jurados que hayamos ingresado
        for col in range(len(matriz_puntaje[fil])):
            acumulador += matriz_puntaje[fil][col]
        #Guarda los promedios en una lista
        lista_promedios_participante[fil]= acumulador / cantidad_jurados
    
    #Devuelve la lista donde el indice 0 corresponde al primer participantes, el 1 al segundo y asi sucesivamente
    return lista_promedios_participante

def encontrar_promedios_iguales(lista_promedios_participante:list,lista_nombres) -> bool:
    # Encuentra y muestra los promedios que son iguales en el array    
    encontrados = False
    promedios_ya_revisados = []    
    # Comparar cada promedio con los demás
    for i in range(5):
        promedio_actual = lista_promedios_participante[i]        
        # Verificar si ya revisamos este promedio
        ya_revisado = False
        for revisado in promedios_ya_revisados:
            if promedio_actual == revisado:
                ya_revisado = True
                break
        
        if ya_revisado == True:
            continue
        # Contar cuántas veces aparece este promedio
        contador = 0
        posiciones = []
        
        for j in range(5):
            if lista_promedios_participante[j] == promedio_actual:
                contador += 1
                posiciones = posiciones + [j+1]
        # Si aparece más de una vez, mostrarlo
        if contador > 1:
            encontrados = True
            print(f"Promedio {promedio_actual} aparece {contador} veces con el participante: {lista_nombres[posiciones]}")
        # Agregar a la lista de ya revisados
        promedios_ya_revisados = promedios_ya_revisados + [promedio_actual]
    
    # Mostrar resultado final
    if encontrados == False:
        print("NO SE ENCONTRARON PROMEDIOS IGUALES")
        print("Todos los promedios son diferentes")

    return True