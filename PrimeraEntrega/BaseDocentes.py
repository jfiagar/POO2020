import os               #El módulo "os" nos permite acceder a funcionalidades dependientes del Sistema Operativo. en este caso lo usamos para limpiar la consola
import os.path          # submódulo path (os.path) el cual nos permite acceder a ciertas funcionalidades relacionadas con los nombres de las rutas de archivos y directorios
import operator         #Importa la libreria Operator

def menu_principalBDD():
    borrarPantalla()  # Borra los valores de la consola, limpia la consola
    print("Bienvenido a la Base de datos de Docentes")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal
    print("\t[0]  Entrar a la base de datos de DOCENTES")  # Imprime la primera opción
    print("\t[1]  Ingresar información a la base de datos")  # Imprime la segunda opción
    print("\t[2]  Salir del Modulo de la Base de datos de Docentes")  # Imprime la tercera opción

def menu_mostrarbase():
    borrarPantalla()  # Borra los valores de la consola, limpia la consola
    print("[0]  Ver la base de datos actual completa")  # Imprime la primera opción
    print("[1]  Ver la base de datos ordenada por un valor")  # Imprime la segunda opción
    print("[2]  Buscar un valor específico en la base de datos")  # Imprime la segunda opción
    print("[3]  Volver al menú principal")  # Imprime la primera opción
    print("[4]  Salir")  # Imprime la tercera opción

def menu_opcionesBDD():
    print("[0]  Volver al menú principal")  # Imprime la primera opción
    print("[1]  Salir\n")  # Imprime la segunda opción

def menu_opcionesBDDingresar():
    print("[0]  Ingresar nuevo Docente")  # Imprime la primera opción
    print("[1]  Ingresar nueva materia a Docente\n")  # Imprime la segunda opción

def menu_opcionesBDDOrdenada():
    print("[1]  Ordenar por Número de documento de identidad")  # Imprime la primera opción
    print("[2]  Ordenar por Nombre")  # Imprime la primera opción
    print("[3]  Ordenar por Apellido")  # Imprime la primera opción
    print("[4]  Ordenar por Código de materia que dicta")  # Imprime la primera opción
    print("[5]  Ordenar por Día de clase")  # Imprime la primera opción
    print("[6]  Ordenar por Hora de clase")  # Imprime la primera opción
    print("[7]  Ordenar por Número de horas dictadas")  # Imprime la primera opción
    print("[8]  Volver al menú principal")
    print("[9]  Salir\n")  # Imprime la segunda opción

def menu_opcionesBDDordenadaalfa():
    print("[1]  Ordenar alfabéticamente [A->Z]")  # Imprime la primera opción
    print("[2]  Ordenar alfabéticamente [Z->A]\n")  # Imprime la primera opción

def menu_opcionesBDDordenadanum():
    print("[1]  Ordenar numéricamente [0->9]")  # Imprime la primera opción
    print("[2]  Ordenar numéricamente [9->0]\n")  # Imprime la primera opción

def borrarPantalla():                       #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":              #Verifica si el sistema operativo es Unix/Linux/MacOS/BSD
        os.system ("clear")             #Si el sistema es Unix/Linux/MacOS/BSD limpia la consola con la función system clear
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":        #Verifica si el sistema operativo es Windows, o sistemas desarrollados por Microsoft
        os.system ("cls")                       #Si el sistema es DOS/Windows limpia la consola con la función system cls

def Comprobacion(dato,longitud,texto):#Función para comprobar si la longitud y el tipo de dato corresponde
    if texto:
        a = dato.isalpha()
    else:
        a = dato.isdigit()
    if len(dato) <= longitud:
        if a:
            return True
        else:
            print("Carácteres no válido")
            return False
    else:
        print("El dato ingresado es demasiado grande, por favor inténtelo de nuevo")
        return False

def ComprobarEsp(dato,longitud,texto,comparar,parametro,mensaje):#Función para comprobar si la longitud y el tipo de dato corresponde, ademas de comparar el dato con parametro e imprimir un mensaje cuando este no se cumple
    if texto:
        a = dato.isalpha()
    else:
        a = dato.isdigit()
    if len(dato) <= longitud:
        if a:
            if comparar in parametro:
                return True
            else:
                print(mensaje)
                return False
        else:
            print("Carácteres no válido")
            return False
    else:
        print("El dato ingresado es demasiado grande, por favor inténtelo de nuevo")
        return False

def mostrartabla(listatotal):
    Tabla = "+----------------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Numero de documento  |        Nombre        |       Apellido       |Código de materia que dicta|        Dia        |        Hora        |   Duración  |\n|----------------------------------------------------------------------------------------------------------------------------------------------------------------|"

    print(Tabla)
    for fila in listatotal:
        a, b, c, d, e, f, g, h = fila
        e = e.strip().split("-")
        f = f.strip().split("-")
        g = g.strip().split("-")
        h = h.strip().split("-")
        if len(e) == 1:
            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^22}|{:^27}|{:^19}|{:^20}|{:^13}|".format(a, b, c, d, e[0], f[0], g[0], h[0])
            stringdetabla = stringdetabla
            print(stringdetabla)
        else:
            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^22}|{:^27}|{:^19}|{:^20}|{:^13}|".format(a, b, c, d, e[0], f[0], g[0], h[0])
            stringdetabla = stringdetabla
            print(stringdetabla)
            for i in range(1, len(e)):
                stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^22}|{:^27}|{:^19}|{:^20}|{:^13}|".format(" ", " ", " ", " ", e[i], f[i], g[i], h[i])
                print(stringdetabla)
    print(
        "+----------------------------------------------------------------------------------------------------------------------------------------------------------------+")

def listasordenarytexto(lista): #ordenar y pone en texto las casillas con mas de un dato
    for i in range(len(lista)):
        lista[i] = lista[i].strip().split("-")
    for i in range(len(lista)):
        lista[i] = sorted(lista[i])
    for i in range(len(lista)):
        a = lista[i]
        listatexto = ""
        for j in range(len(a)):
            if j == (len(a) - 1):
                listatexto = listatexto + a[j]
            else:
                listatexto = listatexto + a[j] + "-"
        lista[i] = listatexto
    return lista

class Persona:
    def __init__(self):
        self.__ID = ""
        self.__N = ""
        self.__A = ""

    def getID(self):
        return self.__ID
    def getN(self):
        return self.__N
    def getA(self):
        return self.__A

    def setID(self):
        comprobar = False
        while not comprobar:
            ID = input("Ingrese el número de documento de indentidad del Docente: ")  # Número de documento del Docente
            comprobar = Comprobacion(ID, 10, False)
        self.__ID = ID

    def setN(self):
        comprobar = False
        while not comprobar:
            N = input("Ingrese el nombre: ")  # Nombre del Docente
            comprobar = Comprobacion(N, 50, True)
        self.__N = N

    def setA(self):
        comprobar = False
        while not comprobar:
            A = input("Ingrese el apellido: ")  # Apellido del Docente
            comprobar = Comprobacion(A, 50, True)
        self.__A = A

class Docente(Persona):
    def __init__(self):
        self.__CM = ""
        self.__DC = ""
        self.__HC = ""
        self.__DH = ""

    def getCM(self):
        return self.__CM
    def getDC(self):
        return self.__DC
    def getHC(self):
        return self.__HC
    def getDH(self):
        return self.__DH


    def setCM(self):
        comprobar = False
        while not comprobar:
            CM = input("Ingrese el código de la materia que dicta: ")  # Código de la materia que dicta
            with open('BD-Materias.txt') as file:
                listaCMB = []
                for line in file:
                    listamaterias = line.strip().split(';')
                    CMB = listamaterias[1]
                    listaCMB.append(CMB)
            if CM in listaCMB:
                comprobar = True
            else:
                print("La materia no se encuentra en la base de datos")
        self.__CM = CM

    def setDC(self):
        comprobar = False
        while not comprobar:
            DC = input("Ingrese el día que se dicta la clase (L,M,C,J,V): ")  # Día de que se dicta la materia
            comprobar = ComprobarEsp(DC, 1, True, DC, ("L", "M", "C", "J", "V"),"Dia no válido,por favor ingresar uno válido (L,M,C,J,V)")
        self.__DC = DC

    def setHC(self):
        comprobar = False
        while not comprobar:
            HC = input(
                "Ingrese la hora que se dicta la clase (Si la clase es a las 7 am ingrese 700): ")  # Hora que se dicta la materia
            comprobar = ComprobarEsp(HC, 4, False, int(HC), range(700, 2000),
                                     "La hora esta fuera del horario permitido, desde las 700 hasta las 2000")
        self.__HC = HC

    def setDH(self):
        comprobar = False
        while not comprobar:
            DH = input("Ingrese la cantidad de horas dictadas: ")  # Cantidad de horas dictadas
            comprobar = ComprobarEsp(DH, 1, False, int(HC) + int(DH) * 100, range(700, 2001), "La duración esta fuera del horario permitido, desde las 700 hasta las 2000")
        self.__DH = DH

def baseDocentes():
    while True:
        menu_principalBDD()
        opcion_elegida = input("Ingrese el número de la opción: ")
        if opcion_elegida == "0":
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
            if os.path.isfile("BD-Docentes.txt"):
                menu_mostrarbase()
                opcion2 = input("Ingrese el número de la opción: ")
                if opcion2=="0":
                    with open("BD-Docentes.txt", "r") as file:
                        listatotal = []
                        for lineas in file:
                            lineas = lineas.strip().split(";")
                            listatotal.append(lineas)
                    mostrartabla(listatotal)
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
                        listaCM = listasordenarytexto(listaCM)
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
                        listaDC = listasordenarytexto(listaDC)
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
                        listaHC = listasordenarytexto(listaHC)
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
                        listaCH = listasordenarytexto(listaCH)
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

                    mostrartabla(listatotal)

                elif opcion2=="2":
                    palabra = input("Ingrese el valor a buscar:")
                    indicador = False
                    lista_DE = []
                    with open("BD-Docentes.txt", "r") as file:
                        for linea in file:
                            linea = linea.strip().split(";")
                            for items in linea:
                                if palabra == items:
                                    indicador = True
                            if indicador:
                                lista_DE.append(linea)
                                indicador = False
                    mostrartabla(lista_DE)
                elif opcion2=="3":
                    continue
                elif opcion2=="4":
                    break
                else:
                    print("Opción no valida")
            else:
                print("Aún no existe una Base de datos")
            print("\n")
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
            if opcion2 == "0":

                mi_docente=Docente()
                mi_docente.setID()
                mi_docente.setN()
                mi_docente.setA()
                mi_docente.setCM()
                mi_docente.setDC()
                mi_docente.setHC()
                mi_docente.setDH()


                docente = mi_docente.getID() + ";" + mi_docente.getN() + ";" + mi_docente.getA() + ";" + mi_docente.getCM() + ";" + mi_docente.getDC() + ";" + mi_docente.getHC() + ";" + mi_docente.getDH()  # Creación del diccionario con el docente

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
            elif opcion2 == "1":
                comprobar = False
                while not comprobar:
                    palabra = input("Ingrese documento de identidad del Docente:")
                    indicador = False
                    lista_D = []
                    with open("BD-Docentes.txt", "r") as file:#Verifica si el docente existe en la base de datos de docentes
                        for linea in file:
                            linea = linea.strip().split(";")
                            for items in linea:
                                if palabra == items:
                                    indicador = True
                                    lista_D=linea
                    if indicador == True:
                        comprobar = True
                    else:
                        print("Docente no se encuentra en la base de datos")
                comprobar = False
                while comprobar==False:
                    materia = input("Ingrese el Código de la materia que dicta: ")  # Código de la materia que dicta
                    with open('BD-Materias.txt') as file:#Verifica si La materia esta en la base de datos
                        listaCMB = []
                        for line in file:
                            listamaterias = line.strip().split(';')
                            CMB = listamaterias[1]
                            listaCMB.append(CMB)
                    if materia in listaCMB:
                        comprobar = True
                    else:
                        comprobar = False
                        print("La materia no se encuentra en la base de datos")
                comprobar = False
                while not comprobar:
                    dia = input("Ingrese el dia de clase:")
                    comprobar = ComprobarEsp(dia, 1, True, dia, ("L", "M", "C", "J", "V"), "Dia no válido,por favor ingresar uno válido (L,M,C,J,V)")
                comprobar = False
                f = lista_D[5].strip().split("-")#Convertir en lista los dias almacenados con string en la base de datos para facilitar las comprobaciones
                g = lista_D[6].strip().split("-")#Convertir en lista las horas almacenados con string en la base de datos para facilitar las comprobaciones
                h = lista_D[7].strip().split("-")#Convertir en lista las duraciones almacenados con string en la base de datos para facilitar las comprobaciones
                while not comprobar:
                    hora = input("Ingrese la hora de clase(Si la clase es a las 7 am ingrese 700):")
                    comprobar2=False
                    if ComprobarEsp(hora, 4, False, int(hora), range(700, 2000), "La hora esta fuera del horario permitido, desde las 700 hasta las 2000"):#Comprueba la longitud y el tipo de dato, ademas de que este entre las 700 y las 2000
                        for i in range(len(g)):
                            if int(hora) not in range(int(g[i]),int(g[i])+(int(h[i])*100)-1):#Comprueba que la hora no coincidad con otra clase
                                comprobar2 = True
                            else:
                                if int(hora) not in range(int(g[i]), int(g[i]) + (int(h[i]) * 100) - 1) and dia in f:#Si exite una hora en la lista comprueba el dia ingresado sea diferente con la concidencia
                                    comprobar2 = True
                                else:
                                    comprobar2 = False
                        if comprobar2:#si la comprobacion es exitosa continua o si no muestra porque no se puede continuar
                            comprobar = True
                        else:
                            print("El horario coincide con otra materia")
                comprobar = False
                while not comprobar:
                    comprobar2 = False
                    duracion = input("Ingrese la duración de la clase:")
                    if ComprobarEsp(duracion, 1, False, int(hora)+int(duracion)*100, range(700, 2001), "La duración esta fuera del horario permitido, desde las 700 hasta las 2000"):#Comprueba de la longitud y el tipo de dato sean correctos y la duracion de la clase no se salga del horario
                        for i in range(len(g)):
                            if (int(hora)+int(duracion)*100)-1 not in range(int(g[i]), int(g[i]) + (int(h[i]) * 100) - 1):#Comprueba que la duracion no coincidad con otra clase
                                comprobar2 = True
                            else:
                                if int(hora) not in range(int(g[i]), int(g[i]) + (int(h[i]) * 100) - 1) and dia in f:#Si exite una duracion en la lista comprueba el dia ingresado sea diferente con la concidencia
                                    comprobar2 = True
                                else:
                                    comprobar2 = False
                        if comprobar2:#si la comprobacion es exitosa continua o si no muestra porque no se puede continuar
                            comprobar = True
                        else:
                            print("El horario coincide con otra materia")

                lista_M=[]
                with open("BD-Docentes.txt", "r") as file:
                    for linea in file:
                        linea = linea.strip().split(";")
                        for items in linea:
                            if palabra == items:#Guarda la materia añadida al docente en dato tipo string para exportar a la base de datos
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

