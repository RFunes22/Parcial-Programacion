def verificar_dato(nombre: str, caracteres_minimos: int) -> str:
    # Verifica si un dato str es más largo que un criterio dado y si contiene solo letras y espacio
    bandera = False
    while bandera == False:
        # Verificar longitud mínima
        if len(nombre) < caracteres_minimos:
            print(f"ERROR\n{nombre} no es un nombre válido (Debe tener al menos {caracteres_minimos} caracteres)")
            nombre = input("Ingrese nuevamente el nombre: ")
            continue
        # Verificar que no esté vacío
        if len(nombre) == 0:
            print(f"ERROR\n'{nombre}' no es un nombre válido (No puede estar vacío)")
            nombre = input("Ingrese nuevamente el nombre: ")
            continue
        # Verificar caracteres válidos
        caracter_invalido = False
        for caracter in nombre:
            es_espacio = False
            es_mayuscula = False
            es_minuscula = False
            valor_ascii = ord(caracter)
            # Verificar si es letra mayúscula (A-Z: 65-90)
            if valor_ascii >= 65 and valor_ascii <= 90:
                es_mayuscula = True
            # Verificar si es letra minúscula (a-z: 97-122)
            if valor_ascii >= 97 and valor_ascii <= 122:
                es_minuscula = True
            # Verificar si es espacio (32)
            if valor_ascii == 32:
                es_espacio = True
            if es_mayuscula == False and es_minuscula == False and es_espacio == False:
                print(f"ERROR\n'{nombre}' no es un nombre válido (Debe contener solo letras o espacio)")
                nombre = input("Ingrese nuevamente el nombre: ")
                caracter_invalido = True
                break
        if not caracter_invalido:
            bandera = True
    
    return nombre

def verificar_opcion(opcion:int, caracter_maximo) -> int:
    bandera = False
    while bandera == False:
        opcion_aux = str(opcion)
        bandera = True
        for p in range(len(opcion_aux)):
            #Verifica que la variable ingresada tenga menos de los digitos dados
            if len(opcion) <= caracter_maximo:
                valor_caracter = 0
                valor_caracter = opcion_aux[p]
                valor_caracter = ord(valor_caracter)
                bandera = True
                #Verifica que el valor ascii de los caracteres sean validos
                if valor_caracter < 48 or valor_caracter > 57:
                        #Mensaje de error
                    opcion = input("ERROR\nOpcion incorrecta (contiene caracteres invalidos)\nReingrese su numero: ")
                    bandera = False
            else:
                #Mensaje de error
                opcion = input(f"ERROR\nOpcion incorrecta (tiene mas de {caracter_maximo} caracteres)\nReingrese su numero: ")
                bandera = False
    
    return opcion

def cargar_puntaje(lista_nombres:list,cantidad_jurados:int,cantidad_participantes:int) -> list:
    #Carga secuencialmente los puntajes en una matriz creada con ese propósito
    #Crea una matriz donde cada fila es un participante y cada calumna es un jurado.
    matriz_puntaje = crear_matriz(cantidad_participantes,cantidad_jurados,0)
    bandera = True
    #Carga secuencial
    for fil in range(cantidad_participantes):
        for col in range(cantidad_jurados):
            #Pedir el dato
            puntaje = input(f"Ingrese el puntaje del juez numero {col + 1} para {lista_nombres[fil]}: ")
            #Verificacion del dato
            puntaje = verificar_opcion(puntaje,2)
            #Reconoce el caracter nulo
            while len(puntaje) == 0 :
                puntaje = input(f"ERROR\nPuntaje invalido\nIngrese el puntaje del juez numero {col + 1} para {lista_nombres[fil]}: ")
                puntaje = verificar_opcion(puntaje,2)
            puntaje = int(puntaje)
            matriz_puntaje[fil][col] = int(puntaje)

    return matriz_puntaje

def crear_array(cantidad_elementos:float,valor_inicial:any) -> list:
    # GENERAL
    # Crea una lista con las especificaciones indicadas
    array = [valor_inicial] * cantidad_elementos
    
    return array

def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    #Sirve para crear una matriz con las especificaciones indicadas
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
        
    return matriz

def cargar_nombres(cantidad_nombres:int) -> list:
    #Devuelve una lista con: Una cantidad indicada (en el llamado de la funcion) de nombres verificados (mediante la funcion verificar_dato)
    #Crea la lista a devolver
    lista_nombres = crear_array (cantidad_nombres,0)
    #Carga secuencialmente la lista con los nombre
    print("INGRESANDO NOMBRE DE LOS PARTICIPANTES")
    for i in range(cantidad_nombres):
            bandera = False
            #Usa un sistema de banderas para comprobar que el dato ya haya sido verificado
            while bandera == False:
                #Pide el dato
                lista_nombres[i] = input(f"Ingrese el nombre {i+1}: ")
                nombre = lista_nombres[i]
                #Verifica el Dato
                verificado = verificar_dato(nombre,3)
                #Guarda el nombre una vez verificado y pone en True la bandera para poder pasar al siguiente indice en la lista de nombres
                lista_nombres[i] = verificado
                bandera  = True
    #Devuelve la lista completa con los nombres ya verificados
    return lista_nombres