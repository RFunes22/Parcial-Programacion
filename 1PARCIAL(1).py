# import os
# from funciones import *
def calcular_promedios_participantes(matriz_puntaje:list,lista_promedios_participantes:list,cantidad_jurados:int) -> list:
    for fil in range(len(matriz_puntaje)):
        acumulador = 0
        for col in range(len(matriz_puntaje[fil])):
            acumulador += matriz_puntaje[fil][col]
        lista_promedios_participante[fil]= acumulador / cantidad_jurados
    
    return lista_promedios_participante

def calcular_promedio_jurado(matriz_puntaje:list,lista_promedios_jurado:list,cantidad_participantes:int) -> bool:
      for col in range(len(matriz_puntaje[fil])):
            acumulador = 0
            for fil in range(len(matriz_puntaje)):
                acumulador += matriz_puntaje[fil][col]
            lista_promedios_jurado[col] = acumulador / cantidad_participantes 
      for i in range(len(lista_promedios_jurado)):
            print(f"PROMEDIO DEL JUEZ {i+1}: {lista_promedios_jurado[i]}")

      return True

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

def cargar_puntaje(matriz_puntaje:list) -> bool:
    if type(matriz_puntaje) == list and len(matriz_puntaje) > 0:
        retorno = True
        for fil in range(len(matriz_puntaje)):
            for col in range(len(matriz_puntaje[fil])):
                #Pedir el dato
                puntaje = int(input(f"Ingrese el puntaje del juez numero {col + 1} para {list_nombres[fil]}: "))
                #Verificacion del dato
                while puntaje < 1 or puntaje > 10:
                    print("Puntaje ingresada fuera de rango (debe estar entre 1 y 10)")
                    puntaje = int(input(f"Ingrese nuevamente el puntaje del juez numero {col + 1} para {lista_nombres[fil]}: "))
                #Guardarlo en la matriz
                matriz_puntaje[fil][col] = puntaje
    else:
        retorno = False
    
    return retorno


def filtrar_promedios(lista_promedios:list,criterio:float) -> bool:
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

def mostrar_matriz(matriz:list) -> None:
    for fil in range(len(matriz)):
        #Muestra una lista ordenada con el nombre, votos de cada juez y promedio
        print(f"NOMBRE PARTICIPANTE: {lista_nombres[fil]}")
        for col in range(len(matriz[fil])):
            print(f"VOTO JUEZ {col+1}: {matriz[fil][col]}")
        print(f"PROMEDIO: {lista_promedios_participante[fil]}")

lista_nombres = crear_array (2,0)
lista_promedios_participante = crear_array(2,0)
lista_promedios_jurado = crear_array (3,0)
matriz_puntaje = crear_matriz(2,3,0)
opcion = 100000
acumulador = 0

while opcion != 0:
    print("MENU DE OPCIONES")
    print("1) Cargar los nombres de los participantes\n2)Cargar los puntajes\n3)Mostrar los puntajes\n4)Mostrar participantes con promedio menor a 4"
    "\n5)Mostrar participantes con promedio menor a 8\n6)Mostrar promedio de cada Juez\n7)Mostrar Juez mas estricto\n8)Mostrar Juez mas generoso\n" \
    "9)Mostrar participantes con el mismo promedio\n10)Buscar participante por nombre\n0)Salir")
    opcion = int(input("Su opcion: "))
    while type(opcion) != int:
        opcion = int(input("ERROR\nOpcion incorrecta\nReingrese su opcion (1-10): "))
    if opcion == 1:
        list_nombres = cargar_nombres(lista_nombres,2)
        bandera_nombres = True
    elif opcion == 2:
        cargar_puntaje(matriz_puntaje)
        bandera_puntaje = True
    elif (opcion == 3):
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        calcular_promedios_participantes(matriz_puntaje,lista_promedios_participante,3)
        mostrar_matriz(matriz_puntaje)
    elif opcion == 4:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        filtrar_promedios(lista_promedios_participante,4)
    elif opcion == 5:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        filtrar_promedios(lista_promedios_participante,8)
    elif opcion == 6:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        calcular_promedio_jurado(matriz_puntaje,lista_promedios_jurado,2)
        
