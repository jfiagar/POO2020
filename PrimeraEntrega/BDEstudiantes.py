import os               #El módulo "os" nos permite acceder a funcionalidades dependientes del Sistema Operativo. en este caso lo usamos para limpiar la consola
import os.path          # submódulo path (os.path) el cual nos permite acceder a ciertas funcionalidades relacionadas con los nombres de las rutas de archivos y directorios
import operator         #Importa la libreria Operator

def menu_principalBDM():
    borrarPantalla()  # Borra los valores de la consola, limpia la consola
    print("Bienvenido a la Base de datos de Estudiantes")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal
    print("[0]  Entrar a la base de datos")  # Imprime la primera opción
    print('[1]  Ingresar info. Estudiantes a la base de datos')  # Imprime la segunda opción
    print("[2]  Salir del programa")  # Imprime la tercera opción

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

def borrarPantalla():                       #Definimos la función estableciendo el nombre de Borrar pantalla
    if os.name == "posix":              #Verifica si el sistema operativo es Unix/Linux/MacOS/BSD
        os.system ("clear")             #Si el sistema es Unix/Linux/MacOS/BSD limpia la consola con la función system clear
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":        #Verifica si el sistema operativo es Windows, o sistemas desarrollados por Microsoft
        os.system ("cls")                       #Si el sistema es DOS/Windows limpia la consola con la función system cls

class Persona:
    def __init__(self):
        self.__DI = ""
        self.__N = ""
        self.__A = ""
    def getDI(self):
        return self.__DI
    def getN(self):
        return self.__N
    def getA(self):
        return self.__A
    def setDI(self):
        comprobado = True
        while comprobado == True:
            DI = input("Ingrese el Documento de Identidad: ")  # Código de la materia
            if len(DI) < 12 and DI.isnumeric():
                self.__DI=DI
                comprobado = False
            else:
                print("El número es demasiado grande o no es un número, intentelo de nuevo")
    def setN(self):
        comprobado = True
        while comprobado == True:
            N = input("Ingrese el Nombre: ")  # Nombre de la materia
            if len(N) < 40:
                self.__N=N
                comprobado = False
            else:
                print("El texto es demasiado grande, intentelo de nuevo")
    def setA(self):
        comprobado = True
        while comprobado == True:
            A = input("Ingrese el Apellido: ")  # Código facultad que la dicta
            if len(A) < 40:
                self.__A=A
                comprobado = False
            else:
                print("El texto es demasiado grande, intentelo de nuevo")
class Estudiante(Persona):
    def __init__(self):
        self.__CP = ""
        self.__CE = ""
        self.__PA = ""

    def getCP(self):
        return self.__CP
    def getCE(self):
        return self.__CE
    def getPA(self):
        return self.__PA


    def setCP(self):
        comprobado = True
        while comprobado == True:
            CP = input("Ingrese el Codigo del plan de estudio: ")  # Código departamento que la dicta
            if len(CP) < 14:
                self.__CP=CP
                comprobado = False
            else:
                print("El texto es demasiado grande, intentelo de nuevo")
    def setCE(self):
        comprobado = True
        while comprobado == True:
            CE = input("Ingrese la calidad de estudiante (matriculado [M], graduado [G], perdida de cupo [P]): ")  # Cantidad de créditos
            if len(CE) ==1 and CE.isalpha():
                self.__CE=CE
                comprobado = False
            else:
                print("El texto es incorrecto, intentelo de nuevo")
    def setPA(self):
        comprobado = True
        while comprobado == True:
            PA = input("Ingrese el PAPA actual: ")  # Código materia anterior obligatoria en el plan de estudios
            if len(PA) < 8:
                self.__PA=PA
                comprobado = False
            else:
                print("El texto es demasiado grande, intentelo de nuevo")

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
                    with open("BD-Estudiantes.txt","r") as file:  # el metodo with  abre el archivo de la base de datos de Estudiantes como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                        listatotal = []  # Crea una lista llamada listatotal
                        for lineas in file:  # Recorre cada linea en el archivo usando un ciclo for
                            lineas = lineas.strip().split(";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                            listatotal.append(lineas)  # se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados

                    Tabla = "+----------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Documento de Identidad |        Nombre        |       Apellido       | Código del plan de estudio | Calidad de estudiante | PAPA (actual) |\n|----------------------------------------------------------------------------------------------------------------------------------------------------|"
                    # Crea un string para las primeras casillas de la tabla
                    print(Tabla)  # Imprime ese string
                    for fila in listatotal:  # Para cada lista en la lista total realiza el codigo siguiente:
                        if len(fila[2]) < 20:  # Si la longitud del item 2 de la lista es menor a 20 entra al ciclo, esto se hace para verificar si la palabra cabe en la celda
                            a, b, c, d, e, f, g = fila  # Desempaqueta las variables de la lista en varias variables llamadas a,b,c, etc que en realidad serían a=Indice, b= Codidog de la materia, C= Nombre. etc--
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^28}|{:^23}|{:^15}|".format(a, b, c, d, e, f, g)  # Usando el metodo format crea un string con los valores de las variables almacenadas y los centra segun el valor, por ejemplo "^8" lo centra a 8 espacios a izquierda y derecha
                            print(stringdetabla)  # imprime cada string, o sea cada fila de la tabla y continua el ciclo para la siguiente fila
                        else:
                            a, b, c, d, e, f, g = fila  # entra a esta parte si el Nombre de la Materia es muy largo, y hace el mismo procedimiento ya explicado desempaquetando y almacenando las variables
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^28}|{:^23}|{:^15}|".format(a, b, c[0:19] + "-", d,e, f,g)  # con el metodo format pone las varibales, y en el caso de la variable del nombre de la amteria imprime los primeros 19 caracteres mas un guion
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^28}|{:^23}|{:^15}|".format(" ", " ", c[19:38], " "," ", " ", " ")  # Imprime la siguiente parte que faltó del Nombre de la materia
                            print(stringdetabla)
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
                            listaordenada = str(indices) + ";" + listaDI[indices - 1] + ";" + listaN[indices - 1] + ";" + listaA[indices - 1] + ";" + listaCP[indices - 1] + ";" + listaCE[indices - 1] + ";" + listaPA[indices - 1]
                            file.write(listaordenada + "\n")
                    with open("BD-eSTUDIANTES-ORDENADA.txt","r") as file:  # el metodo with  abre el archivo de la base de datos de Estudiantes como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                        listatotal = []  # Crea una lista llamada listatotal
                        for lineas in file:  # Recorre cada linea en el archivo usando un ciclo for
                            lineas = lineas.strip().split(";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                            listatotal.append(lineas)  # se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados

                    Tabla = "+----------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Documento de Identidad |        Nombre        |       Apellido       | Código del plan de estudio | Calidad de estudiante | PAPA (actual) |\n|----------------------------------------------------------------------------------------------------------------------------------------------------|"
                    # Crea un string para las primeras casillas de la tabla
                    print(Tabla)  # Imprime ese string
                    for fila in listatotal:  # Para cada lista en la lista total realiza el codigo siguiente:
                        if len(fila[2]) < 20:  # Si la longitud del item 2 de la lista es menor a 20 entra al ciclo, esto se hace para verificar si la palabra cabe en la celda
                            a, b, c, d, e, f, g = fila  # Desempaqueta las variables de la lista en varias variables llamadas a,b,c, etc que en realidad serían a=Indice, b= Codidog de la materia, C= Nombre. etc--
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^28}|{:^23}|{:^15}|".format(a, b, c, d, e, f, g)  # Usando el metodo format crea un string con los valores de las variables almacenadas y los centra segun el valor, por ejemplo "^8" lo centra a 8 espacios a izquierda y derecha
                            print(stringdetabla)  # imprime cada string, o sea cada fila de la tabla y continua el ciclo para la siguiente fila
                        else:
                            a, b, c, d, e, f, g = fila  # entra a esta parte si el Nombre de la Materia es muy largo, y hace el mismo procedimiento ya explicado desempaquetando y almacenando las variables
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^28}|{:^23}|{:^15}|".format(a, b, c[0:19] + "-", d,e, f,g)  # con el metodo format pone las varibales, y en el caso de la variable del nombre de la amteria imprime los primeros 19 caracteres mas un guion
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^28}|{:^23}|{:^15}|".format(" ", " ", c[19:38], " "," ", " ", " ")  # Imprime la siguiente parte que faltó del Nombre de la materia
                            print(stringdetabla)

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
                    Tabla = "+----------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Documento de Identidad |        Nombre        |       Apellido       | Código del plan de estudio | Calidad de estudiante | PAPA (actual) |\n|----------------------------------------------------------------------------------------------------------------------------------------------------|"

                    print(Tabla)
                    for fila in lista_ME:
                        if len(fila[2]) < 20:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^28}|{:^23}|{:^15}|".format(a, b, c, d, e, f,g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                        else:
                            a, b, c, d, e, f, g = fila
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^28}|{:^23}|{:^15}|".format(a, b, c[0:19] + "-", d, e, f, g)
                            stringdetabla = stringdetabla
                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^28}|{:^23}|{:^15}|".format(" ", " ", c[19:38], " ", " ", " ", " ")
                            print(stringdetabla)
                elif opcion2 == "3":
                    continue
                elif opcion2 == "4":
                    break
                else:
                    print("Opción no valida")
            else:
                print("Aún no existe una Base de datos")
            print("+----------------------------------------------------------------------------------------------------------------------------------------------------+")
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
            mi_estudiante = Estudiante()
            mi_estudiante.setDI()
            mi_estudiante.setN()
            mi_estudiante.setA()
            mi_estudiante.setCP()
            mi_estudiante.setCE()
            mi_estudiante.setPA()

            diccionario = mi_estudiante.getDI() + ";" + mi_estudiante.getN() + ";" + mi_estudiante.getA() + ";" + mi_estudiante.getCP() + ";" + mi_estudiante.getCE() + ";" + mi_estudiante.getPA()  # Creación del diccionario de la materia

            if not os.path.isfile("BD-Estudiantes.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
                BDM = open("BD-Estudiantes.txt","w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                numerodeestudiantes = 1  # Establece el número de materias en 1
                BDM.write(str(numerodeestudiantes) + ";" + str(diccionario) + "\n")  # Escribe los datos de la primera materia
                BDM.close()  # Cierra el archivo

                with open('ContadorBD-Estudiantes.txt','w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(numerodeestudiantes))  # Escribe los datos  iniciales del numero de materias en la abse de datos


            else:  # Si el archivo ya existe se entra a esta condicion
                with open('ContadorBD-Estudiantes.txt','r') as file:  # Abre el archivo del contador de materias en modo lectura
                    numerodeestudiantes = file.read()  # Almacena el numero de materias leyendo el archivo
                numerodeestudiantes = int(numerodeestudiantes) + 1  # Como se hizo una adición a la base de datos de materias entonces se aumenta el contador en 1

                with open("BD-Estudiantes.txt","a") as file:  # Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
                    file.write(
                        str(numerodeestudiantes) + ";" + str(diccionario) + "\n")  # Escribe los datos de la siguiente materia

                with open('ContadorBD-Estudiantes.txt','w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(numerodeestudiantes))  # Actualiza el archivo sobreescribiendo el valor del numero de materias es decir borra los datos del archivo anterior y escribe de nuevo
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

