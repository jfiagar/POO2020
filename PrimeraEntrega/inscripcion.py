import os
import os.path

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

def menu_inscripcionmateria():
    print("[1]  Ver catálogo de asignaturas")  # Imprime la primera opción
    print("[2]  Inscribir Materias")  # Imprime la primera opción

def menu_principalINS():
    borrarPantalla()  # Borra los valores de la consola de windows, limpia la consola
    print("Bienvenido al proceso de Auto-Matricula")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal



def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":\
        os.system ("cls")

def main_inscripciones():
    while True:
        menu_principalINS()
        comprobar=0
        while comprobar == 0:
            ID = input("Ingrese su Número de documento: ")  # Código de la materia que dicta
            with open('BD-Estudiantes.txt', "r") as file:
                listaID = []
                for line in file:
                    listalinea = line.strip().split(';')
                    IDB = listalinea[1]
                    listaID.append(IDB)
            if ID in listaID:
                comprobar = 1
            else:
                print("El estudiante NO se encuentra en la Base de datos")
        comprobar=0
        menu_inscripcionmateria()

        opcion_elegida = input("Ingrese el número de la opción: ")
        if opcion_elegida=="1":
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
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c, d, e, f,
                                                                                                       g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b,
                                                                                                       c[0:19] + "-",
                                                                                                       d, e, f,
                                                                                                       g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" ", " ",
                                                                                                       c[19:38],
                                                                                                       " ", " ",
                                                                                                       " ", " ")
                            print(stringdetabla)
                            comprobar=1
                            menu_inscripcionmateria()


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
                            listaordenada = str(indices) + ";" + listaCM[indices - 1] + ";" + listaNM[
                                indices - 1] + ";" + \
                                            listaCF[
                                                indices - 1] + ";" + listaCD[indices - 1] + ";" + listaCC[
                                                indices - 1] + ";" + listaCMA[indices - 1]
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
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c, d, e, f,
                                                                                                       g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b,
                                                                                                       c[0:19] + "-",
                                                                                                       d, e, f,
                                                                                                       g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" ", " ",
                                                                                                       c[19:38],
                                                                                                       " ", " ",
                                                                                                       " ", " ")
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
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c, d, e, f,
                                                                                                       g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b,
                                                                                                       c[0:19] + "-",
                                                                                                       d, e, f,
                                                                                                       g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" ", " ",
                                                                                                       c[19:38],
                                                                                                       " ", " ",
                                                                                                       " ", " ")
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

        elif opcion_elegida=="2":
            while comprobar == 0:
                CM = input("Ingrese El código de la Materia a Inscribir: ")  # Código de la materia
                with open('BD-Materias.txt', "r") as file:
                    listaCM = []
                    for line in file:
                        listalinea = line.strip().split(';')
                        CMB = listalinea[1]
                        listaCM.append(CMB)
                if CM in listaCM:
                    with open(ID+".txt", "r") as file: #Verifica que no inscriba una materia de nuevo
                        listaCMA = []
                        for line in file:
                            listalinea = line.strip().split(';')
                            CMAB = listalinea[1]
                            listaCMA.append(CMAB)
                    if CM in listaCMA:
                        print("Esta materia ya fue cursada")
                    else:
                        indicador = False
                        lista_ME = []
                        with open("BD-Materias.txt", "r") as file:
                            for linea in file:
                                linea = linea.strip().split(";")
                                for items in linea:
                                    if CM == items:
                                        indicador = True
                                if indicador:
                                    prerquisito= items
                                    indicador = False
                        indicador = False

                        variabledecomprobacion2 = prerquisito + ID
                        with open(ID".txt", "r") as file:
                            for linea in file:
                                linea = linea.strip().split(";")
                                variabledecomprobacion=linea[1]+ID
                                if variabledecomprobacion==variabledecomprobacion2:
                                    comprobar=1
                        if comprobar==1:
                            with open("BD-Estudiantes.txt","r") as file:
                                for linea in file:
                                    linea = linea.strip().split(";")
                                    nombre = linea[2]
                                    apellido=linea[3]
                            with open("BD-Materias.txt","r") as file:
                                for linea in file:
                                    linea = linea.strip().split(";")
                                    for items in linea:
                                        if CM=items:
                                            nombremateria = linea[2]
                                            creditosmateria = linea[5]
                            with open("BD-Docentes.txt","r") as file:
                                for linea in file:
                                    linea = linea.strip().split(";")



                            infomateria=ID+";"+nombre+";"+apellido+";"+CM+";"+nombremateria+";"+creditosmateria+";"+nombredocente+";"+apellidodocente+";"+diaclase+";"+horaclase+"\n"
                            if not os.path.isfile(ID + "-inscripcion.txt"):
                                with open(ID + "-inscripcion.txt", "w") as file:
                                    file.write(infomateria)
                            else:
                                with open(ID + "-inscripcion.txt", "a") as file:
                                    file.write(infomateria)

                            print("La Inscricpción ha sido satisfactoria")
                            print("¿Desea continuar inscribiendo?")
                            print("[0]  Continuar inscribiendo")
                            print("[1]  Finalizar inscripicion")
                            opcioninscripcion=input("Ingrese el número de la opción: ")

                            while True:
                                if opcioninscripcion == "0":
                                    comprobar = 0
                                    break
                                elif opcioninscripcion == "1":
                                    comprobar = 1
                                    break
                                else:
                                    print("opcion no valida, volviendo a inscribir materia")
                                    continue




                        else:
                            print("La materia Prerequisito no ha sido aprobada")


                else:
                    print("La materia no existe en la Base de datos")









