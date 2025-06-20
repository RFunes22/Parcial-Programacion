import os
from Funciones import *
from Inputs import *
#Inicializacion de las variables
cantidad_jurados = 3 #Para facilitar el testeo la cantidad de jurados se expresa en forma de variable
cantidad_participantes = 5 #IDEM con los participantes
bandera_error = False
bandera = False
opcion = 1 #Se inicia en 1 para evitar el 0 que sale del menu
bandera_nombres = False
bandera_puntaje = False
#Inicio del menu de opciones
while opcion != 0:
    if bandera_error == False or bandera == True:
        print("MENU DE OPCIONES")
        print("1) Cargar los nombres de los participantes\n2)Cargar los puntajes\n3)Mostrar los puntajes\n4)Mostrar participantes con promedio menor a 4"
        "\n5)Mostrar participantes con promedio menor a 8\n6)Mostrar promedio de cada Juez\n7)Mostrar Juez mas estricto\n8)Mostrar Juez mas generoso\n" \
        "9)Mostrar participantes con el mismo promedio\n10)Buscar participante por nombre\n11)TOP 3 mejores promedios\n12)Ordenar nombres alfabeticamente\n0)Salir")
        opcion = input("Su opcion: ")
        opcion = verificar_opcion(opcion,2)
        while len(opcion) == 0:
            opcion = input("ERROR\nOpcion incorrecta (no es un numero)\nReingrese su opcion (1-12): ")
            opcion = verificar_opcion(opcion,2)
        opcion = int(opcion)
    bandera = False
    while opcion > 12 or opcion < 0:
        opcion = input("ERROR\nOpcion incorrecta (fuera de rango)\nReingrese su opcion (1-12): ")
    if opcion == 1:
        lista_nombres = cargar_nombres(cantidad_participantes)
        print("Los nombres fueron cargados correctamente")
        bandera_nombres = True
        bandera = True
        print("Enter para continuar")
        input()
    elif opcion == 2:
        if bandera_nombres == False:
            while opcion != 1:
                print("No se cargaron los nombres")
                opcion = input("Ingrese 1 para cargar nombre: ")
                opcion = int(verificar_opcion(opcion,2))
            bandera_error = True
        else:
            matriz_puntaje = cargar_puntaje(lista_nombres,cantidad_jurados,cantidad_participantes)
            bandera_puntaje = True
            print("Los puntajes fueron cargados correctamente")
            bandera = True
            print("Enter para continuar")
            input()
        bandera_puntaje = True
    elif opcion == 3:
        if bandera_nombres == False or bandera_puntaje == False:
            while opcion != 1 and opcion != 2:
                print("No se cargaron los nombres y puntajes de los participantes")
                opcion = input("Ingrese 1 para cargar los nombres o 2 para cargar los puntajes: ")
                opcion = int(verificar_opcion(opcion,2))
            bandera_error = True
        else:
            lista_promedios_participante= calcular_promedios_participantes(matriz_puntaje,cantidad_jurados,cantidad_participantes)
            mostrar_matriz(matriz_puntaje,lista_nombres,lista_promedios_participante)
            print("Enter para continuar")
            bandera = True
            input()
    elif opcion == 4:
        if bandera_nombres == False or bandera_puntaje == False:
            while opcion != 1 and opcion != 2:
                print("No se cargaron los nombres y puntajes de los participantes")
                opcion = input("Ingrese 1 para cargar nombre o 2 para cargar puntajes: ")
                opcion = int(verificar_opcion(opcion,2))
            bandera_error = True
        else:
            lista_promedios_participante= calcular_promedios_participantes(matriz_puntaje,cantidad_jurados,cantidad_participantes)
            filtrar_promedios(lista_promedios_participante,lista_nombres,4)
            print("Enter para continuar")
            bandera = True
            input()
    elif opcion == 5:
        if bandera_nombres == False or bandera_puntaje == False:
            while opcion != 1 and opcion != 2:
                print("No se cargaron los nombres y puntajes de los participantes")
                opcion = input("Ingrese 1 para cargar nombre o 2 para cargar puntajes: ")
                opcion = int(verificar_opcion(opcion,2))
            bandera_error = True
        else:
            lista_promedios_participante= calcular_promedios_participantes(matriz_puntaje,cantidad_jurados,cantidad_participantes)
            filtrar_promedios(lista_promedios_participante,lista_nombres,8)
            print("Enter para continuar")
            bandera = True
            input()
    elif opcion == 6:
        if bandera_nombres == False or bandera_puntaje == False:
            while opcion != 1 and opcion != 2:
                print("No se cargaron los nombres y puntajes de los participantes")
                opcion = input("Ingrese 1 para cargar nombre o 2 para cargar puntajes: ")
                opcion = int(verificar_opcion(opcion,2))
            bandera_error = True
        else:
            lista_promedios_jurado = calcular_promedio_jurado(matriz_puntaje,cantidad_participantes,cantidad_jurados)
            for i in range(len(lista_promedios_jurado)):
                print(f"PROMEDIO DEL JURADO {i+1}: {lista_promedios_jurado[i]}")
            print("Enter para continuar")
            bandera = True
            input()
    elif opcion == 7:
        if bandera_nombres == False or bandera_puntaje == False:
            while opcion != 1 and opcion != 2:
                print("No se cargaron los nombres y puntajes de los participantes")
                opcion = input("Ingrese 1 para cargar nombre o 2 para cargar puntajes: ")
                opcion = int(verificar_opcion(opcion,2))
            bandera_error = True
        else:
            lista_promedios_jurado = calcular_promedio_jurado(matriz_puntaje,cantidad_participantes,cantidad_jurados)
            comparar_jurados_estricto(lista_promedios_jurado,cantidad_jurados)
            print("Enter para continuar")
            bandera = True
            input()
    elif opcion == 8:
        if bandera_nombres == False or bandera_puntaje == False:
            while opcion != 1 and opcion != 2:
                print("No se cargaron los nombres y puntajes de los participantes")
                opcion = input("Ingrese 1 para cargar nombre o 2 para cargar puntajes: ")
                opcion = int(verificar_opcion(opcion,2))
            bandera_error = True
        else:
            lista_promedios_jurado = calcular_promedio_jurado(matriz_puntaje,cantidad_participantes,cantidad_jurados)
            comparar_jurados_generoso(lista_promedios_jurado,cantidad_jurados)
            print("Enter para continuar")
            bandera = True
            input()
    elif opcion == 9:
        if bandera_nombres == False or bandera_puntaje == False:
            while opcion != 1 and opcion != 2:
                print("No se cargaron los nombres y puntajes de los participantes")
                opcion = input("Ingrese 1 para cargar nombre o 2 para cargar puntajes: ")
                opcion = int(verificar_opcion(opcion,2))
            bandera_error = True
        else:
            lista_promedios_participante=calcular_promedios_participantes(matriz_puntaje,cantidad_jurados,cantidad_participantes)
            encontrar_promedios_iguales(lista_promedios_participante,lista_nombres,cantidad_participantes)
            print("Enter para continuar")
            bandera = True
            input()
    elif opcion == 12:
        if bandera_nombres == False or bandera_puntaje == False:
            while opcion != 1 and opcion != 2:
                print("No se cargaron los nombres y puntajes de los participantes")
                opcion = input("Ingrese 1 para cargar nombre o 2 para cargar puntajes: ")
                opcion = int(verificar_opcion(opcion,2))
            bandera_error = True
        else:
            nombres_ordenados = ordenar_nombres_alfabeticamente(lista_nombres)
            print("Nombres Ordenados alfabeticamente:")
            for i in range(len(nombres_ordenados)):
                print(f"{nombres_ordenados[i]}")
            print("Enter para continuar")
            bandera = True
            input()
    elif opcion == 11:
        if bandera_nombres == False or bandera_puntaje == False:
            while opcion != 1 and opcion != 2:
                print("No se cargaron los nombres y puntajes de los participantes")
                opcion = input("Ingrese 1 para cargar nombre o 2 para cargar puntajes: ")
                opcion = int(verificar_opcion(opcion))
            bandera_error = True
        else:
            lista_promedios_participante = calcular_promedios_participantes(matriz_puntaje,cantidad_jurados,cantidad_participantes)
            mejores_tres, indice_referencia = calcular_mejores_promedios(lista_promedios_participante,cantidad_participantes)
            print("TOP 3 MEJORES PROMEDIOS")
            for i in range(len(mejores_tres)):
                print(f"{lista_nombres[indice_referencia[i]]}")
                print(f"{mejores_tres[i]}\n")
                
            print("Enter para continuar")
            bandera = True
            input()
    elif opcion == 10:
        if bandera_nombres == False or bandera_puntaje == False:
            while opcion != 1 and opcion != 2:
                print("No se cargaron los nombres y puntajes de los participantes")
                opcion = input("Ingrese 1 para cargar nombre o 2 para cargar puntajes: ")
                opcion = int(verificar_opcion(opcion,2))
            bandera_error = True
        else:
            rebusca = 1
            while rebusca == 1:
                nombre_buscado = input("Ingrese el nombre que quiere buscar: ")
                verificar_dato (nombre_buscado,3)
                buscar(lista_nombres,matriz_puntaje,nombre_buscado,cantidad_jurados,cantidad_participantes)
                rebusca = input("Para buscar nuevamente, ingrese el numero 1. Para salir, ingrese 2: ")
                rebusca = verificar_opcion(rebusca,1)
                while len(rebusca) == 0 :
                    rebusca = input("ERROR\nOpcion incorrecta (no es un numero)\nReingrese su opcion (1 o 2): ")
                    rebusca = verificar_opcion(rebusca,1)
                rebusca = int(rebusca)
            print("Enter para continuar")
            input()
print("SALIENDO DEL PROGRAMA")