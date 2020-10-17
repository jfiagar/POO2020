import os.path
import os
import operator

def menu_principalBDM():
    borrarPantalla()  # Borra los valores de la consola de windows, limpia la consola
    print("Bienvenido a la Base de datos de Materias")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal
    print("[0]  Entrar a la base de datos")  # Imprime la primera opción
    print("[1]  Ingresar Materias a la base de datos")  # Imprime la segunda opción
    print("[2]  Salir del programa")  # Imprime la tercera opción

def menu_mostrarbase():
    borrarPantalla()  # Borra los valores de la consola de windows, limpia la consola
    print("[0]  Ver la base de datos actual COMPLETA")  # Imprime la primera opción
    print("[1]  Ver la base de datos ordenada por un valor")  # Imprime la segunda opción
    print("[2]  Buscar un valor específico en la base de datos")  # Imprime la segunda opción
    print("[3]  Volver al menú principal")  # Imprime la primera opción
    print("[4]  Salir del programa")  # Imprime la tercera opción

def menu_opcionesBDM():
    print("[0]  Volver al menú principal")  # Imprime la primera opción
    print("[1]  Salir del programa")  # Imprime la segunda opción

def menu_opcionesBDMOrdenada():
    print("[1]  Ordenar por Código de materia")  # Imprime la primera opción
    print("[2]  Ordenar por Nombre de materia")  # Imprime la primera opción
    print("[3]  Ordenar por Código de facultad")  # Imprime la primera opción
    print("[4]  Ordenar por Código de departamento")  # Imprime la primera opción
    print("[5]  Ordenar por Cantidad de créditos")  # Imprime la primera opción
    print("[6]  Ordenar por Código de materia anterior")  # Imprime la primera opción
    print("[7]  Volver al menú principal")
    print("[8]  Salir del programa")  # Imprime la segunda opción

def menu_opcionesBDMOrdenadaalfa():
    print("[1]  Ordenar alfabéticamente [A->Z]")  # Imprime la primera opción
    print("[2]  Ordenar alfabéticamente [Z->A]")  # Imprime la primera opción

def menu_opcionesBDMOrdenadanum():
    print("[1]  Ordenar numéricamente [0->9]")  # Imprime la primera opción
    print("[2]  Ordenar numéricamente [9->0]")  # Imprime la primera opción

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":\
        os.system ("cls")


def mainBDM():
    while True:
        menu_principalBDM()
        opcion_elegida = input("Ingrese el número de la opción: ")
        if opcion_elegida == "0":

            if os.path.isfile("BD-Materias.txt"):
                menu_mostrarbase()
                opcion2 = input("Ingrese el número de la opción: ")
                if opcion2 == "0":
                    with open("BD-Materias.txt", "r") as file:
                        listatotal = []
                        for lineas in file:
                            lineas = lineas.strip().split(";")
                            listatotal.append(lineas)

                    Tabla = "\+-----------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |\n|-----------------------------------------------------------------------------------------------------------------------------------------------------------|"

                    print(Tabla)
                    for fila in listatotal:
                        if len(fila[2]) < 19:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c, d, e, f,g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b,c[0:19] + "-",d, e, f, g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" ", " ",c[19:38]," ", " ", " "," ")
                            print(stringdetabla)

                elif opcion2 == "1":

                    with open('BD-Materias.txt', "r") as file:
                        listaIN = []
                        listaCM = []
                        listaNM = []
                        listaCF = []
                        listaCD = []
                        listaCC = []
                        listaCMA = []

                        for line in file:
                            IN1, CM1, NM1, CF1, CD1, CC1, CMA1 = line.strip().split(';')
                            listaIN.append(int(IN1))
                            listaCM.append(CM1)
                            listaNM.append(NM1)
                            listaCF.append(CF1)
                            listaCD.append(CD1)
                            listaCC.append(CC1)
                            listaCMA.append(CMA1)
                    menu_opcionesBDMOrdenada()
                    opcion3 = input("Ingrese el número de la opción: ")

                    if opcion3 == "1":
                        dic = dict(zip(listaIN, listaCM))
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
                            break

                    elif opcion3 == "2":
                        dic = dict(zip(listaIN, listaNM))
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
                            break
                    elif opcion3 == "3":
                        dic = dict(zip(listaIN, listaCF))
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
                            break
                    elif opcion3 == "4":
                        dic = dict(zip(listaIN, listaCD))
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
                            break
                    elif opcion3 == "5":
                        dic = dict(zip(listaIN, listaCC))
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
                            break
                    elif opcion3 == "6":
                        dic = dict(zip(listaIN, listaCMA))
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
                            break
                    elif opcion2 == "7":
                        continue
                    elif opcion2 == "8":
                        break
                    else:
                        print("Opción no valida")
                        break

                    val = list(valores_ord.keys())

                    with open("BD-Materias-ORDENADA.txt", "w") as file:
                        for indices in val:
                            listaordenada = str(indices) + ";" + listaCM[indices - 1] + ";" + listaNM[indices - 1] + ";" + listaCF[indices - 1] + ";" + listaCD[indices - 1] + ";" + listaCC[indices - 1] + ";" + listaCMA[indices - 1]
                            file.write(listaordenada + "\n")
                    with open("BD-Materias-ORDENADA.txt", "r") as file:
                        listatotal = []
                        for lineas in file:
                            lineas = lineas.strip().split(";")
                            listatotal.append(lineas)

                    Tabla = "+-----------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |\n|-----------------------------------------------------------------------------------------------------------------------------------------------------------|"

                    print(Tabla)
                    for fila in listatotal:
                        if len(fila[2]) < 19:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c, d, e, f,g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b,c[0:19] + "-",d, e, f, g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" ", " ",c[19:38]," ", " ", " "," ")
                            print(stringdetabla)
                    print(
                        "+-----------------------------------------------------------------------------------------------------------------------------------------------------------+")
                elif opcion2 == "2":
                    palabra = input("Ingrese el valor a buscar:")
                    indicador = False
                    lista_ME = []
                    with open("BD-Materias.txt", "r") as file:
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
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c, d, e, f,g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b,c[0:19] + "-",d, e, f, g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" ", " ",c[19:38]," ", " ", " "," ")
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
            comprobado = True
            while comprobado == True:
                CM = input("Ingrese el código de la Materia: ")  # Código de la materia
                if len(CM) <= 7:
                    comprobado = False
                else:
                    print("El texto es demasiado grande, intentelo de nuevo")
            comprobado = True
            while comprobado == True:
                NM = input("Ingrese el Nombre de la materia: ")  # Nombre de la materia
                if len(NM) <= 100:
                    comprobado = False
                else:
                    print("El texto es demasiado grande, intentelo de nuevo")
            comprobado = True
            while comprobado == True:
                CF = input("Ingrese el Código facultad que dicta la Materia: ")  # Código facultad que la dicta
                if len(CF) <= 4:
                    comprobado = False
                else:
                    print("El texto es demasiado grande, intentelo de nuevo")
            comprobado = True
            while comprobado == True:
                CD = input("Ingrese el Código departamento que dicta la Materia: ")  # Código departamento que la dicta
                if len(CD) <= 3:
                    comprobado = False
                else:
                    print("El texto es demasiado grande, intentelo de nuevo")
            comprobado = True
            while comprobado == True:
                CC = input("Ingrese la Cantidad de créditos de la Materia: ")  # Cantidad de créditos
                if len(CC) <= 2:
                    comprobado = False
                else:
                    print("El texto es demasiado grande, intentelo de nuevo")
            comprobado = True
            while comprobado == True:
                CMA = input(
                    "Ingrese el Código de la materia anterior obligatoria en el plan de estudios: ")  # Código materia anterior obligatoria en el plan de estudios
                if len(CMA) <= 7:
                    comprobado = False
                else:
                    print("El texto es demasiado grande, intentelo de nuevo")

            diccionario = CM + ";" + NM + ";" + CF + ";" + CD + ";" + CC + ";" + CMA  # Creación del diccionario de la materia

            if not os.path.isfile(
                    "BD-Materias.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
                BDM = open("BD-Materias.txt","w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                numerodematerias = 1  # Establece el número de materias en 1
                BDM.write(str(numerodematerias) + ";" + str(diccionario) + "\n")  # Escribe los datos de la primera materia
                BDM.close()  # Cierra el archivo

                with open('ContadorBD-Materias.txt',
                          'w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(
                        numerodematerias))  # Escribe los datos  iniciales del numero de materias en la abse de datos


            else:  # Si el archivo ya existe se entra a esta condicion
                with open('ContadorBD-Materias.txt',
                          'r') as file:  # Abre el archivo del contador de materias en modo lectura
                    numerodematerias = file.read()  # Almacena el numero de materias leyendo el archivo
                numerodematerias = int(
                    numerodematerias) + 1  # Como se hizo una adición a la base de datos de materias entonces se aumenta el contador en 1

                with open("BD-Materias.txt",
                          "a") as file:  # Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
                    file.write(
                        str(numerodematerias) + ";" + str(diccionario) + "\n")  # Escribe los datos de la siguiente materia

                with open('ContadorBD-Materias.txt',
                          'w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(
                        numerodematerias))  # Actualiza el archivo sobreescribiendo el valor del numero de materias es decir borra los datos del archivo anterior y escribe de nuevo
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

