import os.path
import os
import operator

def menu_principalBDD():
    os.system('clear')  # Borra los valores de la consola de windows, limpia la consola
    print("Bienvenido a la Base de datos de Docentes")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal
    print("[0]  Entrar a la base de datos")  # Imprime la primera opción
    print("[1]  Ingresar información a la base de datos")  # Imprime la segunda opción
    print("[2]  Salir del programa")  # Imprime la tercera opción

def menu_mostrarbase():
    os.system('clear')  # Borra los valores de la consola de windows, limpia la consola
    print("[0]  Ver la base de datos actual completa")  # Imprime la primera opción
    print("[1]  Ver la base de datos ordenada por un valor")  # Imprime la segunda opción
    print("[2]  Buscar un valor específico en la base de datos")  # Imprime la segunda opción
    print("[3]  Volver al menú principal")  # Imprime la primera opción
    print("[4]  Salir del programa")  # Imprime la tercera opción

def menu_opcionesBDD():
    print("[0]  Volver al menú principal")  # Imprime la primera opción
    print("[1]  Salir del programa")  # Imprime la segunda opción

def menu_opcionesBDDingresar():
    print("[0]  Ingresar nuevo Docente")  # Imprime la primera opción
    print("[1]  Ingresar nueva materia a Docente")  # Imprime la segunda opción

def menu_opcionesBDDOrdenada():
    print("[1]  Ordenar por Número de documento de identidad")  # Imprime la primera opción
    print("[2]  Ordenar por Nombre")  # Imprime la primera opción
    print("[3]  Ordenar por Apellido")  # Imprime la primera opción
    print("[4]  Ordenar por Código de materia que dicta")  # Imprime la primera opción
    print("[5]  Ordenar por Día de clase")  # Imprime la primera opción
    print("[6]  Ordenar por Hora de clase")  # Imprime la primera opción
    print("[7]  Ordenar por Número de horas dictadas")  # Imprime la primera opción
    print("[8]  Volver al menú principal")
    print("[9]  Salir del programa")  # Imprime la segunda opción

def menu_opcionesBDDordenadaalfa():
    print("[1]  Ordenar alfabéticamente [A->Z]")  # Imprime la primera opción
    print("[2]  Ordenar alfabéticamente [Z->A]")  # Imprime la primera opción

def menu_opcionesBDDordenadanum():
    print("[1]  Ordenar numéricamente [0->9]")  # Imprime la primera opción
    print("[2]  Ordenar numéricamente [9->0]")  # Imprime la primera opción



def baseDocentes():
    while True:
        menu_principalBDD()
        opcion_elegida = input("Ingrese el número de la opción: ")
        if opcion_elegida == "0":
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
            if os.path.isfile("BD-Docentes.txt"):
                menu_mostrarbase()
                opcion2 = input("Ingrese el número de la opción: ")
                if opcion2=="0":
                    with open("BD-Docentes.txt", "r") as file:
                        listatotal = []
                        for lineas in file:
                            lineas = lineas.strip().split(";")
                            listatotal.append(lineas)
                    Tabla = "\+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Numero de documento  |        Nombre        |       Apellido       |Código de materia que dicta|        Dia        |        Hora        |   Numero de Horas  |\n|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|"

                    print(Tabla)
                    for fila in listatotal:
                        a, b, c, d, e, f, g, h = fila
                        e = e.strip().split("-")
                        f = f.strip().split("-")
                        g = g.strip().split("-")
                        h = h.strip().split("-")

                        if len(e) <= 1:
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^22}|{:^27}|{:^19}|{:^20}|{:^20}|".format(a, b, c, d, e[0], f[0], g[0], h[0])
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                                stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^22}|{:^27}|{:^19}|{:^20}|{:^20}|".format(a, b, c, d, e[0], f[0], g[0], h[0])
                                stringdetabla = stringdetabla
                                print(stringdetabla)
                                for i in range(1,len(e)):
                                    stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^22}|{:^27}|{:^19}|{:^20}|{:^20}|".format(" ", " ", " ", " ", e[i], f[i], g[i], h[i])
                                    print(stringdetabla)
                    print(
                        "+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+")

                elif opcion2=="1":

                    with open('BD-Docentes.txt') as file:
                        listaIN = []
                        listaID = []
                        listaN = []
                        listaA = []
                        listaCM = []
                        listaDC = []
                        listaHC = []
                        listaCH = []

                        for line in file:
                            IN, ID, N, A, CM, DC, HC, CH = line.strip().split(';')
                            listaIN.append(int(IN))
                            listaID.append(int(ID))
                            listaN.append(N)
                            listaA.append(A)
                            listaCM.append(CM)
                            listaDC.append(DC)
                            listaHC.append(HC)
                            listaCH.append(CH)
                    menu_opcionesBDDOrdenada()
                    opcion3 = input("Ingrese el número de la opción: ")

                    if opcion3 == "1":
                        dic = dict(zip(listaIN, listaID))
                        menu_opcionesBDDordenadanum()
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
                        menu_opcionesBDDordenadaalfa()
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
                        menu_opcionesBDDordenadaalfa()
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
                        dic = dict(zip(listaIN, listaCM))
                        menu_opcionesBDDordenadanum()
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
                        dic = dict(zip(listaIN, listaDC))
                        menu_opcionesBDDordenadaalfa()
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
                        dic = dict(zip(listaIN, listaHC))
                        menu_opcionesBDDordenadanum()
                        opcion4 = input("Ingrese el número de la opción: ")
                        if opcion4 == "1":
                            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
                        elif opcion4 == "2":
                            valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
                            valores_ord.reverse()
                            valores_ord = dict(valores_ord)
                        else:
                            print("Opción no valida")

                    elif opcion3 == "7":
                        dic = dict(zip(listaIN, listaCH))
                        menu_opcionesBDDordenadanum()
                        opcion4 = input("Ingrese el número de la opción: ")
                        if opcion4 == "1":
                            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
                        elif opcion4 == "2":
                            valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
                            valores_ord.reverse()
                            valores_ord = dict(valores_ord)
                        else:
                            print("Opción no valida")

                    elif opcion2 == "8":
                        continue
                    elif opcion2 == "9":
                        break
                    else:
                        print("Opción no valida")

                    val = list(valores_ord.keys())

                    with open("BD-Docentes-ORDENADA.txt", "w") as file:
                        for indices in val:
                            listaordenada = str(indices) + ";" + str(listaID[indices - 1]) + ";" + listaN[indices - 1] + ";" + listaA[indices - 1] + ";" + listaCM[indices - 1] + ";"  + listaDC[indices - 1] + ";"  + listaHC[indices - 1] + ";" + listaCH[indices-1]
                            file.write(listaordenada + "\n")

                    with open("BD-Docentes-ORDENADA.txt", "r") as file:
                        listatotal = []
                        for lineas in file:
                            lineas = lineas.strip().split(";")
                            listatotal.append(lineas)

                    Tabla = "\+-----------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Numero de documento  |        Nombre        |       Apellido       |Código de materia que dicta|        Dia        |        Hora        |   Numero de Horas  |\n|-----------------------------------------------------------------------------------------------------------------------------------------------------------|"

                    print(Tabla)
                    for fila in listatotal:
                        if len(fila[2]) < 19:
                            a, b, c, d, e, f, g, h = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^22}|{:^27}|{:^19}|{:^20}|{:^20}|".format(a, b, c,
                                                                                                              d, e, f,
                                                                                                              g, h)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b,
                                                                                                       c[0:19] + "-",
                                                                                                       d, e, f, g, h)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" ", " ",
                                                                                                       c[19:38],
                                                                                                       " ", " ", " ",
                                                                                                       " ", "")
                            print(stringdetabla)
                    print(
                        "+-----------------------------------------------------------------------------------------------------------------------------------------------------------+")

                elif opcion2=="2":
                    palabra = input("Ingrese el valor a buscar:")
                    indicador = False
                    lista_ME = []
                    with open("BD-Docentes.txt", "r") as file:
                        for linea in file:
                            linea = linea.strip().split(";")
                            for items in linea:
                                if palabra == items:
                                    indicador = True
                            if indicador:
                                lista_ME.append(linea)
                                indicador = False
                    Tabla = "\+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Numero de documento  |        Nombre        |       Apellido       |Código de materia que dicta|        Dia        |        Hora        |   Numero de Horas  |\n|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|"

                    print(Tabla)
                    for fila in lista_ME:
                        a, b, c, d, e, f, g, h = fila
                        e = e.strip().split("-")
                        f = f.strip().split("-")
                        g = g.strip().split("-")
                        h = h.strip().split("-")

                        if len(e) <= 1:
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^22}|{:^27}|{:^19}|{:^20}|{:^20}|".format(a, b, c, d, e[0],
                                                                                                              f[0],
                                                                                                              g[0],
                                                                                                              h[0])
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^22}|{:^27}|{:^19}|{:^20}|{:^20}|".format(a, b, c,
                                                                                                              d, e[0],
                                                                                                              f[0],
                                                                                                              g[0],
                                                                                                              h[0])
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            for i in range(1, len(e)):
                                stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^22}|{:^27}|{:^19}|{:^20}|{:^20}|".format(" ",
                                                                                                                  " ",
                                                                                                                  " ",
                                                                                                                  " ",
                                                                                                                  e[i],
                                                                                                                  f[i],
                                                                                                                  g[i],
                                                                                                                  h[i])
                                print(stringdetabla)
                    print(
                        "+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")

                elif opcion2=="3":
                    continue
                elif opcion2=="4":
                    break
                else:
                    print("Opción no valida")
            else:
                print("Aún no existe una Base de datos")
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
            menu_opcionesBDD()
            opcion2 = input("Ingrese el número de la opción: ")
            if opcion2 == "0":
                continue
            elif opcion2=="1":
                print("Saliendo...")
                break
            else:
                print("Opción no valida")

        elif opcion_elegida == "1":
            menu_opcionesBDDingresar()
            opcion2 = input("Ingrese el número de la opción: ")
            if opcion2=="0":
                comprobar = 0
                ID = input("Ingrese el Número de documento de indentidad del Docente: ")  # Número de documento del Docente
                N = input("Ingrese el Nombre: ")  # Nombre del Docente
                A = input("Ingrese el Apellido: ")  # Apellido del Docente
                while comprobar == 0:
                    CM = input("Ingrese el Código de la Materia que dicta: ")  # Código de la materia que dicta
                    with open('BD-Materias.txt') as file:
                        listaCMB = []
                        for line in file:
                            listamaterias = line.strip().split(';')
                            CMB = listamaterias[1]
                            listaCMB.append(CMB)
                    if CM in listaCMB:
                        comprobar = 1
                    else:
                        comprobar = 0
                        print("La materia no se encuentra en la base de datos")

                DC = input("Ingrese el Día que se dicta la clase: ")  # Día de que se dicta la materia
                HC = input("Ingrese la Hora que se dicta la clase: ")  # Hora que se dicta la materia
                CH = input("Ingrese la Cantidad de horas dictadas: ")  # Cantidad de horas dictadas
                docente = ID + ";" + N + ";" + A + ";" + CM + ";" + DC + ";" + HC + ";" + CH  # Creación del diccionario con el docente

                if not os.path.isfile(
                        "BD-Docentes.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
                    BDM = open("BD-Docentes.txt",
                               "w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    numerodedocentes = 1  # Establece el número de materias en 1
                    BDM.write(
                        str(numerodedocentes) + ";" + str(docente) + "\n")  # Escribe los datos de la primera materia
                    BDM.close()  # Cierra el archivo

                    with open('ContadorBD-Docentes.txt',
                              'w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                        file.write(str(
                            numerodedocentes))  # Escribe los datos  iniciales del numero de materias en la abse de datos


                else:  # Si el archivo ya existe se entra a esta condicion
                    with open('ContadorBD-Docentes.txt','r') as file:  # Abre el archivo del contador de materias en modo lectura
                        numerodedocentes = file.read()  # Almacena el numero de materias leyendo el archivo
                    numerodedocentes = int(numerodedocentes) + 1  # Como se hizo una adición a la base de datos de materias entonces se aumenta el contador en 1
                    with open("BD-Docentes.txt","a") as file:  # Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
                        file.write(str(numerodedocentes) + ";" + str(docente) + "\n")  # Escribe los datos de la siguiente materia
                    with open('ContadorBD-Docentes.txt','w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                        file.write(str(numerodedocentes))  # Actualiza el archivo sobreescribiendo el valor del numero de materias es decir borra los datos del archivo anterior y escribe de nuevo
                menu_opcionesBDD()
                opcion3 = input("Ingrese el número de la opción: ")
                if opcion3 == "0":
                    continue
                elif opcion3 == "1":
                    print("Saliendo...")
                    break
                else:
                    print("Opción no valida")
            elif opcion2=="1":
                comprobar=0
                while comprobar==0:
                    palabra = input("Ingrese documento de identidad del Docente:")
                    indicador = False
                    lista_D = []
                    with open("BD-Docentes.txt", "r") as file:
                        for linea in file:
                            linea = linea.strip().split(";")
                            for items in linea:
                                if palabra == items:
                                    indicador = True
                                    lista_D.append(linea)
                    if indicador== True:
                        comprobar=1
                    else:
                        print("Docente no se encuentra en la base de datos")
                comprobar=0
                while comprobar==0:
                    materia = input("Ingrese el Código de la materia que dicta: ")  # Código de la materia que dicta
                    with open('BD-Materias.txt') as file:
                        listaCMB = []
                        for line in file:
                            listamaterias = line.strip().split(';')
                            CMB = listamaterias[1]
                            listaCMB.append(CMB)
                    if materia in listaCMB:
                        comprobar = 1
                    else:
                        comprobar = 0
                        print("La materia no se encuentra en la base de datos")
                comprobar=0
                while comprobar==0:
                    dia = input("Ingrese el dia de clase:")
                    dias=("L","M","C","J","V")
                    if dia in dias:
                        comprobar=1
                    else:
                        print("Día no valido, es L,M,C,J,V")
                comprobar=0
                while comprobar==0:
                    hora = int(input("Ingrese la hora de clase:"))
                    if int(hora)>=700 and int(hora)<=2000:
                        for i in lista_D:
                            if hora not in range(int(i[6]),int(i[6])+(int(i[7])*100)-1) or dia not in i[5]:
                                comprobar=1
                            else:
                                print("El horario coinceden con otra materia")
                    else:
                        print("La hora esta fuera del horario permitido, es 700 a las 2000")
                comprobar = 0
                while comprobar == 0:
                    duracion = int(input("Ingrese la duración de la clase:"))
                    for i in lista_D:
                        if (hora+duracion*100)-1 not in range(int(i[6]), int(i[6]) + (int(i[7]) * 100) - 1):
                            comprobar=1
                        else:
                            print("El horario coinceden con otra materia")
                lista_M=[]
                with open("BD-Docentes.txt", "r") as file:
                    for linea in file:
                        linea = linea.strip().split(";")
                        for items in linea:
                            if palabra == items:
                                linea[4]=linea[4]+"-"+materia
                                linea[5]=linea[5]+"-"+dia
                                linea[6]=linea[6]+"-"+str(hora)
                                linea[7]=linea[7]+"-"+str(duracion)
                        lista_M.append(linea)

                with open("BD-Docentes.txt", "w") as file:
                    for indices in range(len(lista_M)):
                            a=lista_M[indices]
                            listaG = a[0]+";"+a[1]+";"+a[2]+";"+a[3]+";"+a[4]+";"+a[5]+";"+a[6]+";"+a[7]
                            file.write(listaG + "\n")

            else:
                print("Opción no valida")
        elif opcion_elegida == "2":
            print("Saliendo...")
            break
        else:
            print("Opción no valida")


