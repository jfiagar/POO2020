import os               #El módulo "os" nos permite acceder a funcionalidades dependientes del Sistema Operativo. en este caso lo usamos para limpiar la consola
import os.path          # submódulo path (os.path) el cual nos permite acceder a ciertas funcionalidades relacionadas con los nombres de las rutas de archivos y directorios
import operator         #Importa la libreria Operator


def menu_principalBDM():
    borrarPantalla()  # Borra los valores de la consola, limpia la consola
    print("Bienvenido a la Base de datos de Materias")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal
    print("[0]  Entrar a la base de datos")  # Imprime la primera opción
    print("[1]  Ingresar Materias Aprobadas")  # Imprime la tercera opción
    print("[2]  mostrar materias cursadas")
    print("[3]  Salir del programa")  # Imprime la cuarta opción


def menu_mostrarbase():
    borrarPantalla()  # Borra los valores de la consola, limpia la consola
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
    print("[7]  Oredenar por Estado de Aprobacion")  # Imprime la primera opción
    print("[8]  Volver al menú principal")
    print("[9]  Salir del programa")  # Imprime la segunda opción


def menu_opcionesBDMOrdenadaalfa():
    print("[1]  Oredenar alfabéticamente [A->Z]")  # Imprime la primera opción
    print("[2]  Oredenar alfabéticamente [Z->A]")  # Imprime la primera opción


def menu_opcionesBDMOrdenadanum():
    print("[1]  Oredenar numéricamente [0->9]")  # Imprime la primera opción
    print("[2]  Oredenar numéricamente [9->0]")  # Imprime la primera opción

def borrarPantalla():                       #Definimos la función estableciendo el nombre de Borrar pantalla
    if os.name == "posix":              #Verifica si el sistema operativo es Unix/Linux/MacOS/BSD
        os.system ("clear")             #Si el sistema es Unix/Linux/MacOS/BSD limpia la consola con la función system clear
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":        #Verifica si el sistema operativo es Windows, o sistemas desarrollados por Microsoft
        os.system ("cls")                       #Si el sistema es DOS/Windows limpia la consola con la función system cls



def mainBDMAntigua():
    while True:
        menu_principalBDM()
        opcion_elegida = input("Ingrese el número de la opción: ")
        if opcion_elegida == "0":
            numerodocumento = input("Ingrese el número de documento del estudiante: ")

            if os.path.isfile(numerodocumento+".txt"):
                menu_mostrarbase()
                opcion2 = input("Ingrese el número de la opción: ")
                if opcion2 == "0":
                    with open(numerodocumento+".txt", "r") as file:
                        listatotal = []
                        for lineas in file:
                            lineas = lineas.strip().split(";")
                            listatotal.append(lineas)

                    Tabla = "\+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |Estado de la materia|\n|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|"

                    print(Tabla)
                    for fila in listatotal:
                        if len(fila[2]) < 20:
                            a, b, c, d, e, f, g,h = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|{:^21}|".format(a, b, c, d, e, f,g,h)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g,h = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|{:^21}|".format(a, b,c[0:19] + "-",d, e, f, g,h)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|{:^21}|".format(" ", " ",c[19:38]," ", " ", " "," "," ")
                            print(stringdetabla)

                elif opcion2 == "1":

                    with open(numerodocumento+'.txt', "r") as file:
                        listaIN = []
                        listaCM = []
                        listaNM = []
                        listaCF = []
                        listaCD = []
                        listaCC = []
                        listaCMA = []
                        listaES=[]

                        for line in file:
                            IN1, CM1, NM1, CF1, CD1, CC1, CMA1,ES = line.strip().split(';')
                            listaIN.append(int(IN1))
                            listaCM.append(CM1)
                            listaNM.append(NM1)
                            listaCF.append(CF1)
                            listaCD.append(CD1)
                            listaCC.append(CC1)
                            listaCMA.append(CMA1)
                            listaES.append(ES)
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
                    elif opcion3 == "7":
                        dic = dict(zip(listaIN, listaES))
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
                    elif opcion2 == "8":
                        continue
                    elif opcion2 == "9":
                        break
                    else:
                        print("Opción no valida")
                        break

                    val = list(valores_ord.keys())

                    with open("BD-Materias-Antigua-ORDENADA.txt", "w") as file:
                        for indices in val:
                            listaordenada = str(indices) + ";" + listaCM[indices - 1] + ";" + listaNM[indices - 1] + ";" + listaCF[indices - 1] + ";" + listaCD[indices - 1] + ";" + listaCC[indices - 1] + ";" + listaCMA[indices - 1]
                            file.write(listaordenada + "\n")
                    with open("BD-Materias-Antigua-ORDENADA.txt", "r") as file:
                        listatotal = []
                        for lineas in file:
                            lineas = lineas.strip().split(";")
                            listatotal.append(lineas)

                    Tabla = "+-----------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |Estado de la materia|\n|-----------------------------------------------------------------------------------------------------------------------------------------------------------|"

                    print(Tabla)
                    for fila in listatotal:
                        if len(fila[2]) < 20:
                            a, b, c, d, e, f, g,h = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|{:^22}|".format(a, b, c, d, e, f,g,h)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g,h = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|{:^22}|".format(a, b,c[0:19] + "-",d, e, f, g,h)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|{:^22}|".format(" ", " ",c[19:38]," ", " ", " "," "," ")
                            print(stringdetabla)
                    print(
                        "+-----------------------------------------------------------------------------------------------------------------------------------------------------------+")
                elif opcion2 == "2":
                    palabra = input("Ingrese el valor a buscar:")
                    indicador = False
                    lista_ME = []
                    with open(numerodocumento+".txt", "r") as file:
                        for linea in file:
                            linea = linea.strip().split(";")
                            for items in linea:
                                if palabra == items:
                                    indicador = True
                            if indicador:
                                lista_ME.append(linea)
                                indicador = False
                    Tabla = "+-----------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |Estado de la materia|\n|-----------------------------------------------------------------------------------------------------------------------------------------------------------|"

                    print(Tabla)
                    for fila in lista_ME:
                        if len(fila[2]) < 19:
                            a, b, c, d, e, f, g,h = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|{:^22}|".format(a, b, c, d, e, f,g,h)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g,h = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|{:^22}|".format(a, b,c[0:19] + "-",d, e, f, g,h)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|{:^22}|".format(" ", " ",c[19:38]," ", " ", " "," "," ")
                            print(stringdetabla)
                    print(
                        "+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
                elif opcion2 == "3":
                    continue
                elif opcion2 == "4":
                    break
                else:
                    print("Opción no valida")
            else:
                print("Aún no existe una Base de datos")
            print(
                "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
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
            CodigoM = input("Ingrese el código de la Materia: ")  # Código de la materia

            Contcm = len(CodigoM)

            if Contcm >= 12 or Contcm < 5:  # Comprobación de caracteres
                a = True
                while a == True:
                    print("El código superó el límite o el minímo de caracteres")
                    CodigoM = input("Ingrese el código de la Materia: ")
                    if CodigoM <= 12:
                        a = False

            NombreM = input("Ingrese el Nombre de la materia: ")  # Nombre de la materia
            CodigoF = input("Ingrese el Código facultad que dicta la Materia: ")  # Código facultad que la dicta
            CodigoD = input("Ingrese el Código departamento que dicta la Materia: ")  # Código departamento que la dicta
            CCreditos = input("Ingrese la Cantidad de créditos de la Materia: ")  # Cantidad de créditos
            CMP = input(
                "Ingrese el Código de la materia de la que es prerrequisito en el plan de estudios: ")  # Código materia de la que es prerrequiesito en el plan de estudios
            EM = input("Ingrese el estado de la materia(aprobado(a) o (r)Reprobada): ")  # Estado de la materia
            EST = input(
                "Ingrese el número de documento del estudiante que curso la materia: ")  # El nombre del estudiante
            INFOMateria_A = CodigoM + ";" + NombreM + ";" + CodigoF + ";" + CodigoD + ";" + CCreditos + ";" + CMP + ";" + EM  # Creación de la info de la materia
            EST += ".txt"

            if not os.path.isfile(
                    EST):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
                BDMA = open(EST,
                            "w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                N_materiasAntiguas = 1  # Establece el número de materias en 1
                BDMA.write(
                    str(N_materiasAntiguas) + ";" + str(
                        INFOMateria_A) + "\n")  # Escribe los datos de la primera materia
                BDMA.close()  # Cierra el archivo
                with open('ContadorBD-Materias_Antiguas' + EST,
                          'w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(
                        str(
                            N_materiasAntiguas))  # Escribe los datos  iniciales del numero de materias en la abse de datos


            else:  # Si el archivo ya existe se entra a esta condicion

                RevBD = open(EST, "r")

                cods_r = []
                for a in RevBD:
                    cods_r.append(a.split(";"))

                RevBD.close()

                for i in range(len(cods_r)):
                    j = cods_r[i][1]
                    if j == CodigoM:
                        print("Código de materia inválido")
                        menu_opcionesBDM()
                        Opcion_s = input("Opcón a elegir: ")
                        if Opcion_s == "0":
                            continue
                        elif Opcion_salir == "1":
                            print("Saliendo...")
                        else:
                            print("opción no válida")
                        break


                else:
                    with open('ContadorBD-Materias_Antiguas' + EST,
                              'r') as file:  # Abre el archivo del contador de materias en modo lectura
                        N_materiasA = file.read()  # Almacena el numero de materias leyendo el archivo
                        N_materiasAntiguas = int(
                            N_materiasA) + 1  # Como se hizo una adición a la base de datos de materias entonces se aumenta el contador en 1

                    with open(EST,
                              "a") as file:  # Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
                        file.write(str(N_materiasAntiguas) + ";" + str(
                            INFOMateria_A) + "\n")  # Escribe los datos de la siguiente materia

                    with open('ContadorBD-Materias_Antiguas' + EST,
                              'w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                        file.write(str(
                            N_materiasAntiguas))  # Actualiza el archivo sobreescribiendo el valor del numero de materias es decir borra los datos del archivo anterior y escribe de nuevo

                    menu_opcionesBDM()
                    Opcion_salir = input("Opcón a elegir: ")
                    if Opcion_salir == "0":
                        continue
                    elif Opcion_salir == "1":
                        print("Saliendo...")
                    else:
                        print("opción no válida")

        elif opcion_elegida == "2":
            Archivo = input("Ingrese el número de documento del estudiante: ") + ".txt"
            if not os.path.isfile(Archivo):
                print("El estudiante no tiene historial")
                print("[0]  Volver al menú principal: ")
                opcionNE = input("Ingrese el número de la opción: ")
                if opcionNE == "0":
                    continue
                else:
                    print("Opción no valida")
            else:
                with open(Archivo, "r") as file:
                    listatotal = []
                    for lineas in file:
                        lineas = lineas.strip().split(";")
                        listatotal.append(lineas)

                Tabla = "+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia prerrequisito | Estado de la materia |\n|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|"
                print(Tabla)

                for fila in listatotal:
                    if len(fila[2]) < 20:
                        a, b, c, d, e, f, g, h = fila
                        stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^36}|{:^22}|".format(a, b, c, d, e,
                                                                                                          f,
                                                                                                          g, h)
                        stringdetabla = stringdetabla
                        print(stringdetabla)
                    else:
                        a, b, c, d, e, f, g, h = fila
                        stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^36}|{:^22}|".format(a, b,
                                                                                                          c[0:19] + "-",
                                                                                                          d,
                                                                                                          e, f, g, h)
                        stringdetabla = stringdetabla
                        print(stringdetabla)
                        stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^36}|{:^22}|".format(" ", " ",
                                                                                                          c[19:38], " ",
                                                                                                          " ", " ", " ",
                                                                                                          " ")
                        print(stringdetabla)
                print(
                    "+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")

                print("[0]  Volver al menú principal: ")
                opcionSE = input("Ingrese el número de la opción: ")
                if opcionSE == "0":
                    continue



        elif opcion_elegida == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no valida")
