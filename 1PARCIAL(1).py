import os
from Funciones import *
lista_nombres = crear_array (5,0)
lista_promedios_participante = crear_array(5,0)
lista_promedios_jurado = crear_array (3,0)
matriz_puntaje = crear_matriz(5,3,0)
opcion = 1
acumulador = 0
bandera_nombres = False
bandera_puntaje = False
while opcion != 0:
    print("MENU DE OPCIONES")
    print("1) Cargar los nombres de los participantes\n2)Cargar los puntajes\n3)Mostrar los puntajes\n4)Mostrar participantes con promedio menor a 4"
    "\n5)Mostrar participantes con promedio menor a 8\n6)Mostrar promedio de cada Juez\n7)Mostrar Juez mas estricto\n8)Mostrar Juez mas generoso\n" \
    "9)Mostrar participantes con el mismo promedio\n10)Buscar participante por nombre\n11)TOP 3 mejores promedios\n12)Ordenar nombres alfabeticamente\n0)Salir")
    opcion = int(input("Su opcion: "))
    while type(opcion) != int:
        opcion = int(input("ERROR\nOpcion incorrecta\nReingrese su opcion (1-12): "))
    if opcion == 1:
        lista_nombres = cargar_nombres(lista_nombres,5)
        bandera_nombres = True
        print("Enter para continuar")
        input()
    elif opcion == 2:
        matriz_puntaje = cargar_puntaje(matriz_puntaje,lista_nombres)
        bandera_puntaje = True
        print("Enter para continuar")
        input()
    elif (opcion == 3):
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        lista_promedios_participante= calcular_promedios_participantes(matriz_puntaje,lista_promedios_participante,3)

        mostrar_matriz(matriz_puntaje,lista_nombres,lista_promedios_participante)
        print("Enter para continuar")
        input()
    elif opcion == 4:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        filtrar_promedios(lista_promedios_participante,lista_nombres,4)
        print("Enter para continuar")
        input()
    elif opcion == 5:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        filtrar_promedios(lista_promedios_participante,lista_nombres,8)
        print("Enter para continuar")
        input()
    elif opcion == 6:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        calcular_promedio_jurado(matriz_puntaje,lista_promedios_jurado,5)
        for i in range(len(lista_promedios_jurado)):
            print(f"PROMEDIO DEL JUEZ {i+1}: {lista_promedios_jurado[i]}")
        print("Enter para continuar")
        input()
    elif opcion == 7:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        calcular_promedio_jurado(matriz_puntaje,lista_promedios_jurado,5)
        comparar_jurados_estricto(lista_promedios_jurado)
        print("Enter para continuar")
        input()
    elif opcion == 8:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        calcular_promedio_jurado(matriz_puntaje,lista_promedios_jurado,5)
        comparar_jurados_generoso(lista_promedios_jurado)
        print("Enter para continuar")
        input()
    elif opcion == 9:
        while bandera_nombres == False and bandera_puntaje == False:
            print("No se cargaron los nombres y puntajes de los participantes")
            break
        lista_promedios_participante=calcular_promedios_participantes(matriz_puntaje,lista_promedios_participante,3)
        encontrar_promedios_iguales(lista_promedios_participante,lista_nombres)
        print("Enter para continuar")
        input()
    elif opcion == 12:
        nombres_ordenados = ordenar_nombres_alfabeticamente(lista_nombres,5)
        print("Nombres Ordenados alfabeticamente:")
        for i in range(len(nombres_ordenados)):
            print(f"{nombres_ordenados[i]}")
        print("Enter para continuar")
        input()
    elif opcion == 11:
        mejores_tres = top_3_promedios(lista_promedios_participante)
        for i in range(len(lista_promedios_participante)):
            print(f"{lista_promedios_participante[i]}")
        print("Enter para continuar")
        input()
    elif opcion == 10:
        nombre_buscado = input("Ingrese el nombre que quiere buscar: ")
        while type(nombre_buscado) != str:
            print("Nombre no valido. Ingrese nuevamente")
            nombre_buscado = input("Ingrese el nombre que quiere buscar: ")
        buscar (lista_nombres,lista_promedios_participante,nombre_buscado)
print("SALIENDO DEL PROGRAMA")