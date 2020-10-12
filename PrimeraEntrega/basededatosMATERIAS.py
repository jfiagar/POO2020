import os.path
import os
import operator

def menu_principalBDM():
    os.system('cls')  # Borra los valores de la consola de windows, limpia la consola
    print("Bienvenido a la Base de datos de Materias")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal
    print("[0]  Entrar a la base de datos")  # Imprime la primera opción
    print("[1]  Ingresar Materias a la base de datos")  # Imprime la segunda opción
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
    print("[1]  Oredenar por Código de materia")  # Imprime la primera opción
    print("[2]  Oredenar por Nombre de materia")  # Imprime la primera opción
    print("[3]  Oredenar por Código de facultad")  # Imprime la primera opción
    print("[4]  Oredenar por Código de departamento")  # Imprime la primera opción
    print("[5]  Oredenar por Cantidad de créditos")  # Imprime la primera opción
    print("[6]  Oredenar por Código de materia anterior")  # Imprime la primera opción
    print("[7]  Volver al menú principal")
    print("[8]  Salir del programa")  # Imprime la segunda opción

def menu_opcionesBDMOrdenadaalfa():
    print("[1]  Oredenar alfabéticamente [A->Z]")  # Imprime la primera opción
    print("[2]  Oredenar alfabéticamente [Z->A]")  # Imprime la primera opción

def menu_opcionesBDMOrdenadanum():
    print("[1]  Oredenar numéricamente [0->9]")  # Imprime la primera opción
    print("[2]  Oredenar numéricamente [9->0]")  # Imprime la primera opción




while True:
    menu_principalBDM()
    opcion_elegida = input("Ingrese el número de la opción: ")
    if opcion_elegida == "0":
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        if os.path.isfile("BD-Materias.txt"):
            menu_mostrarbase()
            opcion2 = input("Ingrese el número de la opción: ")
            if opcion2=="0":
                with open("BD-Materias.txt", "r") as file:
                    print(file.read())
            elif opcion2=="1":

                with open('BD-Materias.txt') as file:
                    listaIN = []
                    listaCM = []
                    listaNM = []
                    listaCF = []
                    listaCD = []
                    listaCC = []
                    listaCMA = []

                    for line in file:
                        IN, CM, NM, CF, CD, CC, CMA = line.strip().split(';')
                        listaIN.append(int(IN))
                        listaCM.append(CM)
                        listaNM.append(NM)
                        listaCF.append(CF)
                        listaCD.append(CD)
                        listaCC.append(CC)
                        listaCMA.append(CMA)
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
                elif opcion2 == "7":
                    continue
                elif opcion2 == "8":
                    break
                else:
                    print("Opción no valida")

                val = list(valores_ord.keys())

                with open("BD-Materias-ORDENADA.txt", "w") as file:
                    for indices in val:
                        listaordenada = str(indices) + ";"+ listaCM[indices - 1] + ";"  + listaNM[indices - 1] + ";" + listaCF[indices - 1] + ";" + listaCD[indices - 1] + ";"  + listaCC[indices - 1] + ";"  + listaCMA[indices - 1]
                        file.write(listaordenada + "\n")
            elif opcion2=="2":
                print("ingrese :v")
            elif opcion2=="3":
                continue
            elif opcion2=="4":
                break
            else:
                print("Opción no valida")
        else:
            print("Aún no existe una Base de datos")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        menu_opcionesBDM()
        opcion2 = input("Ingrese el número de la opción: ")
        if opcion2 == "0":
            continue
        elif opcion2=="1":
            print("Saliendo...")
            break
        else:
            print("Opción no valida")



    elif opcion_elegida == "1":
        CM = input("Ingrese el código de la Materia: ")  # Código de la materia
        NM = input("Ingrese el Nombre de la materia: ")  # Nombre de la materia
        CF = input("Ingrese el Código facultad que dicta la Materia: ")  # Código facultad que la dicta
        CD = input("Ingrese el Código departamento que dicta la Materia: ")  # Código departamento que la dicta
        CC = input("Ingrese la Cantidad de créditos de la Materia: ")  # Cantidad de créditos
        CMA = input(
            "Ingrese el Código de la materia anterior obligatoria en el plan de estudios: ")  # Código materia anterior obligatoria en el plan de estudios
        dict = CM + ";" + NM + ";" +  CF + ";" + CD+ ";"+ CC+ ";"+CMA  # Creación del diccionario de la materia

        if not os.path.isfile("BD-Materias.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
            BDM = open("BD-Materias.txt","w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
            numerodematerias = 1  # Establece el número de materias en 1
            BDM.write(str(numerodematerias)+";"+str(dict) + "\n")  # Escribe los datos de la primera materia
            BDM.close()  # Cierra el archivo

            with open('ContadorBD-Materias.txt','w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                file.write(str(numerodematerias))  # Escribe los datos  iniciales del numero de materias en la abse de datos


        else:  # Si el archivo ya existe se entra a esta condicion
            with open('ContadorBD-Materias.txt','r') as file:  # Abre el archivo del contador de materias en modo lectura
                numerodematerias = file.read()  # Almacena el numero de materias leyendo el archivo
            numerodematerias = int(numerodematerias) + 1  # Como se hizo una adición a la base de datos de materias entonces se aumenta el contador en 1

            with open("BD-Materias.txt","a") as file:  # Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
                file.write(str(numerodematerias)+";"+str(dict) + "\n")  # Escribe los datos de la siguiente materia

            with open('ContadorBD-Materias.txt','w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                file.write(str(numerodematerias))  # Actualiza el archivo sobreescribiendo el valor del numero de materias es decir borra los datos del archivo anterior y escribe de nuevo
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