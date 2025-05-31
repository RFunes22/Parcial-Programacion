import os
from Funciones import *
lista_nombres = crear_array (5,0)
lista_promedios_participante = crear_array(5,0)
lista_promedios_jurado = crear_array (3,0)
matriz_puntaje = crear_matriz(5,3,0)
opcion = 100000
acumulador = 0
bandera_nombres = False
bandera_puntaje = False
while opcion != 0:
    print("MENU DE OPCIONES")
    print("1) Cargar los nombres de los participantes\n2)Cargar los puntajes\n3)Mostrar los puntajes\n4)Mostrar participantes con promedio menor a 4"
    "\n5)Mostrar participantes con promedio menor a 8\n6)Mostrar promedio de cada Juez\n7)Mostrar Juez mas estricto\n8)Mostrar Juez mas generoso\n" \
    "9)Mostrar participantes con el mismo promedio\n10)Buscar participante por nombre\n0)Salir")
    opcion = int(input("Su opcion: "))
    while type(opcion) != int:
        opcion = int(input("ERROR\nOpcion incorrecta\nReingrese su opcion (1-10): "))
    if opcion == 1:
        lista_nombres = cargar_nombres(lista_nombres,5)
        bandera_nombres = True
    elif opcion == 2:
        matriz_puntaje = cargar_puntaje(matriz_puntaje,lista_nombres)
        bandera_puntaje = True
    elif (opcion == 3):
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        lista_promedios_participante= calcular_promedios_participantes(matriz_puntaje,lista_promedios_participante,3)

        mostrar_matriz(matriz_puntaje,lista_nombres,lista_promedios_participante)
    elif opcion == 4:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        filtrar_promedios(lista_promedios_participante,lista_nombres,4)
    elif opcion == 5:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        filtrar_promedios(lista_promedios_participante,lista_nombres,8)
    elif opcion == 6:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        calcular_promedio_jurado(matriz_puntaje,lista_promedios_jurado,5)
    elif opcion == 7:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        calcular_promedio_jurado(matriz_puntaje,lista_promedios_jurado,5)
        comparar_jurados_estricto(lista_promedios_jurado)
    elif opcion == 8:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        calcular_promedio_jurado(matriz_puntaje,lista_promedios_jurado,5)
        comparar_jurados_generoso(lista_promedios_jurado)
    elif opcion == 9:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        lista_promedios_participante= calcular_promedios_participantes(matriz_puntaje,lista_promedios_participante,3)
        encontrar_promedios_iguales(lista_promedios_participante,lista_nombres)