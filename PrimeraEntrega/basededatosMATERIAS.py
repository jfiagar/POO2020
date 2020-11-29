import os               #El módulo "os" nos permite acceder a funcionalidades dependientes del Sistema Operativo. en este caso lo usamos para limpiar la consola
import os.path          # submódulo path (os.path) el cual nos permite acceder a ciertas funcionalidades relacionadas con los nombres de las rutas de archivos y directorios
import operator         #Importa la libreria Operator

def menu_principalBDM():
    borrarPantalla()                                    # Borra los valores de la consola, limpia la consola
    print("Bienvenido a la Base de datos de Materias")          # Saludo :v
    print("MENÚ PRINCIPAL")                                 # Imprime Menú principal
    print("\t[0]  Entrar a la base de datos (Ver CATÁLOGO DE ASIGNATURAS)")                 # Imprime la primera opción
    print("\t[1]  Ingresar Materias a la base de datos")      # Imprime la segunda opción
    print("\t[2]  Salir del programa")                        # Imprime la tercera opción

def menu_mostrarbase():        #Funcion usada para mostrar el menu de la base de datos
    borrarPantalla()  # Borra los valores de la consola de windows, limpia la consola
    print("CATÁLOGO DE ASIGNATURAS\n")
    print("[0]  Ver la base de datos actual COMPLETA")  # Imprime la primera opción
    print("[1]  Ver la base de datos ordenada por un valor")  # Imprime la segunda opción
    print("[2]  Buscar un valor específico en la base de datos")  # Imprime la tercera opción
    print("[3]  Volver al menú principal")  # Imprime la cuarta opción
    print("[4]  Salir (Volver al Menu SIA)")  # Imprime la quinta opción

def menu_opcionesBDM():       #Función usada para imprimir las opciones de volver al menu o salir
    print("[0]  Volver al menú principal")  # Imprime la primera opción
    print("[1]  Salir (Volver al Menu SIA)")  # Imprime la segunda opción

def menu_opcionesBDMOrdenada():          #Funcion usada para imprimir las opciones del Menu de ordenamiento
    print("[1]  Ordenar por Código de materia")  # Imprime la primera opción
    print("[2]  Ordenar por Nombre de materia")  # Imprime la segunda opción
    print("[3]  Ordenar por Código de facultad")  # Imprime la tercera opción
    print("[4]  Ordenar por Código de departamento")  # Imprime la cuarta opción
    print("[5]  Ordenar por Cantidad de créditos")  # Imprime la quinta opción
    print("[6]  Ordenar por Código de materia anterior")  # Imprime la sexta opción
    print("[7]  Volver al menú principal")    # Imprime la septima opción
    print("[8]  Salir (Volver al Menu SIA)")  # Imprime la octava opción

def menu_opcionesBDMOrdenadaalfa():   #Función usada para imprimir las opciones entre ordenamiento Alfabetico
    print("[1]  Ordenar alfabéticamente [A->Z]")  # Imprime la primera opción
    print("[2]  Ordenar alfabéticamente [Z->A]")  # Imprime la Segunda opción

def menu_opcionesBDMOrdenadanum():    #Función usada para imprimir las opciones entre ordenamiento Numérico
    print("[1]  Ordenar numéricamente [0->9]")  # Imprime la primera opción
    print("[2]  Ordenar numéricamente [9->0]")  # Imprime la Segunda opción

def borrarPantalla():                       #Definimos la función estableciendo el nombre de Borrar pantalla
    if os.name == "posix":              #Verifica si el sistema operativo es Unix/Linux/MacOS/BSD
        os.system ("clear")             #Si el sistema es Unix/Linux/MacOS/BSD limpia la consola con la función system clear
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":        #Verifica si el sistema operativo es Windows, o sistemas desarrollados por Microsoft
        os.system ("cls")                       #Si el sistema es DOS/Windows limpia la consola con la función system cls


class Materia:
    def __init__(self):
        self.__CM =  ""
        self.__NM = ""
        self.__CF = ""
        self.__CD = ""
        self.__CC = ""
        self.__CMA = ""
    def getCM(self):
        return self.__CM
    def getNM(self):
        return self.__NM
    def getCF(self):
        return self.__CF
    def getCD(self):
        return self.__CD
    def getCC(self):
        return self.__CC
    def getCMA(self):
        return self.__CMA

    def setCM(self):
        comprobado = True
        while comprobado == True:
            CM = input("Ingrese el Código de la Materia: ")  # Código de la materia
            if len(CM) <= 9:
                self.__CM=CM
                comprobado = False
            else:
                print("El texto es demasiado grande, intentelo de nuevo")

    def setNM(self):
        comprobado = True
        while comprobado == True:
            NM = input("Ingrese el Nombre de la materia: ")  # Nombre de la materia
            if len(NM) <= 100:
                self.__NM = NM
                comprobado = False
            else:
                print("El texto es demasiado grande, intentelo de nuevo")
    def setCF(self):
        comprobado = True
        while comprobado == True:
            CF = input("Ingrese el Código facultad que dicta la Materia: ")  # Código facultad que la dicta
            if len(CF) <= 5:
                self.__CF=CF
                comprobado = False
            else:
                print("El texto es demasiado grande, intentelo de nuevo")

    def setCD(self):
        comprobado = True
        while comprobado == True:
            CD = input("Ingrese el Código departamento que dicta la Materia: ")  # Código departamento que la dicta
            if len(CD) <= 5:
                self.__CD=CD
                comprobado = False
            else:
                print("El texto es demasiado grande, intentelo de nuevo")
    def setCC(self):
        comprobado = True
        while comprobado == True:
            CC = input("Ingrese la Cantidad de créditos de la Materia: ")  # Cantidad de créditos
            if len(CC) <= 2 and CC.isnumeric():
                self.__CC=CC
                comprobado = False
            else:
                print("El texto es demasiado grande o no es un número, intentelo de nuevo")
    def setCMA(self):
        comprobado = True
        while comprobado == True:
            CMA = input(
                "Ingrese el Código de la materia anterior obligatoria en el plan de estudios: ")  # Código materia anterior obligatoria en el plan de estudios
            with open('BD-Materias.txt') as file:
                listaCMB = []
                for line in file:
                    listamaterias = line.strip().split(';')
                    CMB = listamaterias[1]
                    listaCMB.append(CMB)
            if CMA in listaCMB:
                if len(CMA) <= 9:
                    self.__CMA=CMA
                    comprobado = False
                else:
                    print("El texto es demasiado grande, intentelo de nuevo")
            elif CMA == "":
                self.__CMA = CMA
                comprobado = False
            else:
                print("La materia de prerequisito no está en la base de datos")


def mainBDM():   #Función Principal de la Base de datos de Materias
    while True:        #Ciclo while inicializado en True para que el programa no cierre a menos que se lo pida
        menu_principalBDM()            #Llama a la funcion menu principal imprimiendo el menu principal
        opcion_elegida = input("Ingrese el número de la opción: ")      #Solicita una opcion y la almacena como string
        if opcion_elegida == "0":          #Condicion dada por la variable "Opcion elegida"

            if os.path.isfile("BD-Materias.txt"):       # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
                menu_mostrarbase()             #Funcion para mostrar el menu de la base de datos
                opcion2 = input("Ingrese el número de la opción: ")   #Solicita una opcion y la almacena como string
                if opcion2 == "0":              #Condicion dada por la variable "Opcion2"
                    with open("BD-Materias.txt", "r") as file:       # el metodo with  abre el archivo de la base de datos de materias como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                        listatotal = []       #Crea una lista llamada listatotal
                        for lineas in file:           #Recorre cada linea en el archivo usando un ciclo for
                            lineas = lineas.strip().split(";")         #con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                            listatotal.append(lineas)     #se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados

                    Tabla = "\+-----------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |\n|-----------------------------------------------------------------------------------------------------------------------------------------------------------|"
 # Crea un string para las primeras casillas de la tabla
                    print(Tabla)  #Imprime ese string
                    for fila in listatotal:         #Para cada lista en la lista total realiza el codigo siguiente:
                        if len(fila[2]) < 20:       #Si la longitud del item 2 de la lista es menor a 20 entra al ciclo, esto se hace para verificar si la palabra cabe en la celda
                            a, b, c, d, e, f, g = fila         #Desempaqueta las variables de la lista en varias variables llamadas a,b,c, etc que en realidad serían a=Indice, b= Codidog de la materia, C= Nombre. etc--
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c, d, e, f,g)    # Usando el metodo format crea un string con los valores de las variables almacenadas y los centra segun el valor, por ejemplo "^8" lo centra a 8 espacios a izquierda y derecha
                            print(stringdetabla)    #imprime cada string, o sea cada fila de la tabla y continua el ciclo para la siguiente fila
                        else:
                            a, b, c, d, e, f, g = fila     # entra a esta parte si el Nombre de la Materia es muy largo, y hace el mismo procedimiento ya explicado desempaquetando y almacenando las variables
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b,c[0:19] + "-",d, e, f, g)       #con el metodo format pone las varibales, y en el caso de la variable del nombre de la amteria imprime los primeros 19 caracteres mas un guion

                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" ", " ",c[19:38]," ", " ", " "," ")  #Imprime la siguiente parte que faltó del Nombre de la materia
                            print(stringdetabla)

                elif opcion2 == "1":         #Condicion dada por la variable "Opcion2"

                    with open('BD-Materias.txt', "r") as file:      # el metodo with  abre el archivo de la base de datos de materias como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                        listaIN = []            #Se crean listas para almacenar cada variable de la base de datos, el indice, el codigo de la materia, el nombre, etc..
                        listaCM = []
                        listaNM = []
                        listaCF = []
                        listaCD = []
                        listaCC = []
                        listaCMA = []

                        for line in file:  #Recorre la base de datos linea por linea
                            IN1, CM1, NM1, CF1, CD1, CC1, CMA1 = line.strip().split(';')    #Desempaqueta las variables de la lista en varias variables Indice,  Codidog de la materia, Nombre. etc--
                            listaIN.append(int(IN1))        #Almacena el valor del indice en la lista y lo convierte en un Int para asegurar que sea un numero y que el ordenamiento sea correcto
                            listaCM.append(CM1)             #Almacena el codigo de la materia en la lista de codigos de materia "listaCM"
                            listaNM.append(NM1)             #Almacena el nombre de la materia en la lista de nombres de la materia
                            listaCF.append(CF1)             # """""""""
                            listaCD.append(CD1)
                            listaCC.append(CC1)
                            listaCMA.append(CMA1)
                    menu_opcionesBDMOrdenada()         #Imprime el menu de opciones de ordenamiento
                    opcion3 = input("Ingrese el número de la opción: ")        #Solicita una opcion y la almacena como string

                    if opcion3 == "1":        #Condicion dada por la variable "Opcion3"
                        dic = dict(zip(listaIN, listaCM))          #con el metodo zip une las dos listas, la de indices con las del codigo, y luego con el metodo dict lo convierte en diccionario,  dando por ejemplo "Indice: codigo de materia"
                        menu_opcionesBDMOrdenadanum()         #Imprime el menu de ordenamiento numerico dado que los codigos de materia son principalmente numericos
                        opcion4 = input("Ingrese el número de la opción: ")          #Solicita una opcion y la almacena como string
                        if opcion4 == "1":                               #Condicion dada por la variable "Opcion4"
                            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))           #Usando la libreria operator , la funcion sorted y la funcion dict, crea un diccionario ordenado ascendentemente por las Key del diccionario
                        elif opcion4 == "2":
                            valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
                            valores_ord.reverse()                                                  #hace el mismo procedimiento anterior pero lo pone al reves, ordenandolo descendentemente
                            valores_ord = dict(valores_ord)
                        else:
                            print("Opción no valida")
                            break

                    elif opcion3 == "2":            #Explicacion en la parte de arriba, lo unico que cambia es la lista usada, usando en ese caso el nombre de la materia
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
                    print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------+")

                elif opcion2 == "2":         #Condicion dada por la variable "Opcion2"
                    palabra = input("Ingrese el valor a buscar:")         #Solicita una palabra para buscar y la alamacena como string
                    indicador = False                #Inicializa el indicador en False
                    lista_ME = []                      #Crea una lista de Materias Encontradas
                    with open("BD-Materias.txt", "r") as file:               #Abre el archivo en modo lectura con el metodo with, llamando al archivo file , ejecutando el codigo anidado cuando el archivo este abierto y cuando termina cierra el archivo
                        for linea in file:               #Recorre cada linea del archivo usando un ciclo For
                            linea = linea.strip().split(";")          #con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                            for items in linea:             #Recorre cada item de la lista creada llamada linea
                                if palabra == items:                  #Comprueba si la palabra almacenada es igual al item de la lista
                                    indicador = True                   #Indicador de materia encontrada puesto en TRUE
                            if indicador:                            #Si el indicador es verdadero
                                lista_ME.append(linea)            #Almacena en la lista de materias encontradas la lista total de la linea del archivo
                                indicador = False                       #Vuelve a poner el indicador en False
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
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            menu_opcionesBDM()
            opcion2 = input("\n Ingrese el número de la opción: ")
            if opcion2 == "0":
                continue
            elif opcion2 == "1":
                print("Saliendo...")
                break
            else:
                print("Opción no valida")



        elif opcion_elegida == "1":

            mi_materia=Materia()
            mi_materia.setCM()
            mi_materia.setNM()
            mi_materia.setCF()
            mi_materia.setCD()
            mi_materia.setCC()
            mi_materia.setCMA()

            diccionario = mi_materia.getCM() + ";" + mi_materia.getNM() + ";" + mi_materia.getCF() + ";" + mi_materia.getCD() + ";" + mi_materia.getCC() + ";" + mi_materia.getCMA()  # Creación del diccionario de la materia

            if not os.path.isfile("BD-Materias.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
                BDM = open("BD-Materias.txt","w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                numerodematerias = 1  # Establece el número de materias en 1
                BDM.write(str(numerodematerias) + ";" + str(diccionario) + "\n")  # Escribe los datos de la primera materia
                BDM.close()  # Cierra el archivo

                with open('ContadorBD-Materias.txt','w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(numerodematerias))  # Escribe los datos  iniciales del numero de materias en la abse de datos
                print("¡Materia almacenada con éxito!")


            else:  # Si el archivo ya existe se entra a esta condicion
                with open('ContadorBD-Materias.txt','r') as file:  # Abre el archivo del contador de materias en modo lectura
                    numerodematerias = file.read()  # Almacena el numero de materias leyendo el archivo
                numerodematerias = int(numerodematerias) + 1  # Como se hizo una adición a la base de datos de materias entonces se aumenta el contador en 1

                with open("BD-Materias.txt","a") as file:  # Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(numerodematerias) + ";" + str(diccionario) + "\n")  # Escribe los datos de la siguiente materia

                with open('ContadorBD-Materias.txt','w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(numerodematerias))  # Actualiza el archivo sobreescribiendo el valor del numero de materias es decir borra los datos del archivo anterior y escribe de nuevo
                print("¡Materia almacenada con éxito!")

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

