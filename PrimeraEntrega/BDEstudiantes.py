import os.path
import os
import operator

def menu_principalBDM():
    os.system('cls')  # Borra los valores de la consola de windows, limpia la consola
    print("Bienvenido a la Base de datos de Estudiantes")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal
    print("[0]  Entrar a la base de datos")  # Imprime la primera opción
    print('[1]  Ingresar info. Estudiantes a la base de datos')  # Imprime la segunda opción
    print("[2]  Salir del programa")  # Imprime la tercera opción

def menu_mostrarbase():
    os.system('cls')  # Borra los valores de la consola de windows, limpia la consola
    print("[0]  Ver la base de datos actual COMPLETA")  # Imprime la primera opción
    print("[1]  Ver la base de datos ordenada por un valor")  # Imprime la segunda opción
    print("[2]  Buscar un valor específico en la base de datos")  # Imprime la segunda opción
    print("[3]  Volver al menú principal")  # Imprime la primera opción
    print("[4]  Salir del programa")  # Imprime la tercera opción

def menu_opcionesBDM():
    print("[0]  Volver al menú principal")  # Imprime la primera opción
    print("[1]  Salir del programa")  # Imprime la segunda opción

def menu_opcionesBDMOrdenada():
    print("[1]  Oredenar por Documento de identidad")  # Imprime la primera opción
    print("[2]  Oredenar por Nombre")  # Imprime la primera opción
    print("[3]  Oredenar por Apellido")  # Imprime la primera opción
    print("[4]  Oredenar por Código  plan  de  estudios  al  que  pertenece")  # Imprime la primera opción
    print("[5]  Oredenar por Calidad  de estudiante")  # Imprime la primera opción
    print("[6]  Oredenar por PAPA actual")  # Imprime la primera opción
    print("[7]  Volver al menú principal")
    print("[8]  Salir del programa")  # Imprime la segunda opción

def menu_opcionesBDMOrdenadaalfa():
    print("[1]  Oredenar alfabéticamente [A->Z]")  # Imprime la primera opción
    print("[2]  Oredenar alfabéticamente [Z->A]")  # Imprime la primera opción

def menu_opcionesBDMOrdenadanum():
    print("[1]  Oredenar numéricamente [0->9]")  # Imprime la primera opción
    print("[2]  Oredenar numéricamente [9->0]")  # Imprime la primera opción


def mainBDE():
    while True:
        menu_principalBDM()
        opcion_elegida = input("Ingrese el número de la opción: ")
        if opcion_elegida == "0":
            print(
                "----------------------------------------------------------------------------------------------------------------------------------------------------------------")
            if os.path.isfile("BD-Estudiantes.txt"):
                menu_mostrarbase()
                opcion2 = input("Ingrese el número de la opción: ")
                if opcion2 == "0":
                    with open("BD-Estudiantes.txt", "r") as file:
                        print(file.read())
                elif opcion2 == "1":

                    with open('BD-Estudiantes.txt', "r") as file:
                        listaIN = []
                        listaDI = []
                        listaN = []
                        listaA = []
                        listaCP = []
                        listaCE = []
                        listaPA = []

                        for line in file:
                            IN, DI, N, A, CP, CE, PA = line.strip().split(';')
                            listaIN.append(int(IN))
                            listaDI.append(DI)
                            listaN.append(N)
                            listaA.append(A)
                            listaCP.append(CP)
                            listaCE.append(CE)
                            listaPA.append(PA)
                    menu_opcionesBDMOrdenada()
                    opcion3 = input("Ingrese el número de la opción: ")

                    if opcion3 == "1":
                        dic = dict(zip(listaDI, listaDI))
                        menu_opcionesBDMOrdenadanum()
                        opcion4 = input("Ingrese el número de la opción: ")
                        if opcion4 == "1":
                            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
                        elif opcion4 == "2":
                            valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
                            valores_ord.reverse()
                            valores_ord = dict(valores_ord)
                        else:
                            print("Opción no valida")

                    elif opcion3 == "2":
                        dic = dict(zip(listaIN, listaN))
                        menu_opcionesBDMOrdenadaalfa()
                        opcion4 = input("Ingrese el número de la opción: ")
                        if opcion4 == "1":
                            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
                        elif opcion4 == "2":
                            valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
                            valores_ord.reverse()
                            valores_ord = dict(valores_ord)
                        else:
                            print("Opción no valida")
                    elif opcion3 == "3":
                        dic = dict(zip(listaIN, listaA))
                        menu_opcionesBDMOrdenadanum()
                        opcion4 = input("Ingrese el número de la opción: ")
                        if opcion4 == "1":
                            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
                        elif opcion4 == "2":
                            valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
                            valores_ord.reverse()
                            valores_ord = dict(valores_ord)
                        else:
                            print("Opción no valida")
                    elif opcion3 == "4":
                        dic = dict(zip(listaIN, listaCP))
                        menu_opcionesBDMOrdenadanum()
                        opcion4 = input("Ingrese el número de la opción: ")
                        if opcion4 == "1":
                            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
                        elif opcion4 == "2":
                            valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
                            valores_ord.reverse()
                            valores_ord = dict(valores_ord)
                        else:
                            print("Opción no valida")
                    elif opcion3 == "5":
                        dic = dict(zip(listaIN, listaCE))
                        menu_opcionesBDMOrdenadanum()
                        opcion4 = input("Ingrese el número de la opción: ")
                        if opcion4 == "1":
                            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
                        elif opcion4 == "2":
                            valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
                            valores_ord.reverse()
                            valores_ord = dict(valores_ord)
                        else:
                            print("Opción no valida")
                    elif opcion3 == "6":
                        dic = dict(zip(listaIN, listaPA))
                        menu_opcionesBDMOrdenadanum()
                        opcion4 = input("Ingrese el número de la opción: ")
                        if opcion4 == "1":
                            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
                        elif opcion4 == "2":
                            valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
                            valores_ord.reverse()
                            valores_ord = dict(valores_ord)
                        else:
                            print("Opción no valida")
                    elif opcion2 == "7":
                        continue
                    elif opcion2 == "8":
                        break
                    else:
                        print("Opción no valida")

                    val = list(valores_ord.keys())

                    with open("BD-Estudiantes-ORDENADA.txt", "w") as file:
                        for indices in val:
                            listaordenada = str(indices) + ";" + listaDI[indices - 1] + ";" + listaN[
                                indices - 1] + ";" + listaA[indices - 1] + ";" + listaCP[indices - 1] + ";" + listaCE[
                                                indices - 1] + ";" + listaPA[indices - 1]
                            file.write(listaordenada + "\n")
                elif opcion2 == "2":
                    palabra = input("Ingrese el valor a buscar:")
                    indicador = False
                    lista_ME = []
                    with open("BD-Estudiantes.txt", "r") as file:
                        for linea in file:
                            linea = linea.strip().split(";")
                            for items in linea:
                                if palabra == items:
                                    indicador = True
                            if indicador:
                                lista_ME.append(linea)
                                indicador = False
                    Tabla = "+-----------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |\n|-----------------------------------------------------------------------------------------------------------------------------------------------------------|"

                    print(Tabla)
                    for fila in lista_ME:
                        if len(fila[2]) < 19:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c, d, e, f,
                                                                                                       g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b,
                                                                                                       c[0:19] + "-",
                                                                                                       d, e, f, g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" ", " ",
                                                                                                       c[19:38],
                                                                                                       " ", " ", " ",
                                                                                                       " ")
                            print(stringdetabla)
                    print(
                        "+-----------------------------------------------------------------------------------------------------------------------------------------------------------+")
                elif opcion2 == "3":
                    continue
                elif opcion2 == "4":
                    break
                else:
                    print("Opción no valida")
            else:
                print("Aún no existe una Base de datos")
            print(
                "----------------------------------------------------------------------------------------------------------------------------------------------------------------")
            menu_opcionesBDM()
            opcion2 = input("Ingrese el número de la opción: ")
            if opcion2 == "0":
                continue
            elif opcion2 == "1":
                print("Saliendo...")
                break
            else:
                print("Opción no valida")



        elif opcion_elegida == "1":
            DI = input("Ingrese el Documento de Identidad: ")  # Código de la materia
            N = input("Ingrese el Nombre: ")  # Nombre de la materia
            A = input("Ingrese el Apellido: ")  # Código facultad que la dicta
            CP = input("Ingrese el Codigo del plan de estudio: ")  # Código departamento que la dicta
            CE = input(
                "Ingrese la calidad de estudiante (matriculado [M], graduado [G], perdida de cupo [P]): ")  # Cantidad de créditos
            PA = input(
                "Ingrese el PAPA actual: ")  # Código materia anterior obligatoria en el plan de estudios
            diccionario = DI + ";" + N + ";" + A + ";" + CP + ";" + CE + ";" + PA  # Creación del diccionario de la materia

            if not os.path.isfile(
                    "BD-Estudiantes.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
                BDM = open("BD-Estudiantes.txt",
                           "w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                numerodeestudiantes = 1  # Establece el número de materias en 1
                BDM.write(str(numerodeestudiantes) + ";" + str(dict) + "\n")  # Escribe los datos de la primera materia
                BDM.close()  # Cierra el archivo

                with open('ContadorBD-Estudiantes.txt',
                          'w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(
                        numerodeestudiantes))  # Escribe los datos  iniciales del numero de materias en la abse de datos


            else:  # Si el archivo ya existe se entra a esta condicion
                with open('ContadorBD-Estudiantes.txt',
                          'r') as file:  # Abre el archivo del contador de materias en modo lectura
                    numerodeestudiantes = file.read()  # Almacena el numero de materias leyendo el archivo
                numerodeestudiantes = int(
                    numerodeestudiantes) + 1  # Como se hizo una adición a la base de datos de materias entonces se aumenta el contador en 1

                with open("BD-Estudiantes.txt",
                          "a") as file:  # Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
                    file.write(
                        str(numerodeestudiantes) + ";" + str(dict) + "\n")  # Escribe los datos de la siguiente materia

                with open('ContadorBD-Estudiantes.txt',
                          'w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(
                        numerodeestudiantes))  # Actualiza el archivo sobreescribiendo el valor del numero de materias es decir borra los datos del archivo anterior y escribe de nuevo
            menu_opcionesBDM()
            opcion2 = input("Ingrese el número de la opción: ")
            if opcion2 == "0":
                continue
            elif opcion2 == "1":
                print("Saliendo...")
                break
            else:
                print("Opción no valida")

        elif opcion_elegida == "2":
            print("Saliendo...")
            break
        else:
            print("Opción no valida")

