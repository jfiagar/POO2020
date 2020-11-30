import os               #El módulo "os" nos permite acceder a funcionalidades dependientes del Sistema Operativo. en este caso lo usamos para limpiar la consola
import os.path          # submódulo path (os.path) el cual nos permite acceder a ciertas funcionalidades relacionadas con los nombres de las rutas de archivos y directorios
import operator         #Importa la libreria Operator


def menu_principalBDM():
    borrarPantalla()  # Borra los valores de la consola, limpia la consola
    print("Bienvenido a la Base de datos de Materias")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal
    print("[1]  Ingresar Materias Aprobadas")  # Imprime la tercera opción
    print("[2]  Mostrar Base de datos de Materias Aprobadas")
    print("[3]  Salir del programa")  # Imprime la cuarta opción


def menu_mostrarbase():
    borrarPantalla()  # Borra los valores de la consola, limpia la consola
    print("[0]  Ver la base de datos actual COMPLETA")  # Imprime la primera opción
    print("[1]  Ver la base de datos ordenada por un valor")  # Imprime la segunda opción
    print("[2]  Buscar un valor específico en la base de datos")  # Imprime la segunda opción
    print("[3]  Ver la base de datos por estudiante") # Imprime la esta opción
    print("[4]  Volver al menú principal")  # Imprime la primera opción
    print("[5]  Salir del programa")  # Imprime la tercera opción


def menu_opcionesBDM():
    print("[0]  Volver al menú principal")  # Imprime la primera opción
    print("[1]  Salir del programa")  # Imprime la segunda opción


def menu_opcionesBDMOrdenada():
    print("[1]  Oredenar por Código de materia")  # Imprime la primera opción
    print("[2]  Oredenar por Identificacion del estudiante")  # Imprime la primera opción

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

class MateriaAprobada:
    def __init__(self):
        self.__CodigoM =  ""
        self.__ID = ""

    def getCodigoM(self):
        return self.__CodigoM
    def getID(self):
        return self.__ID


    def setCodigoM(self):
        
        comprobado = True
        while comprobado == True:
            CodigoM = input("Ingrese el código de la Materia: ")  # Código de la materia
            Contcm = len(CodigoM)
            with open('BD-Materias.txt') as file:
                listaCMB = []
                for line in file:
                    listamaterias = line.strip().split(';')
                    CMB = listamaterias[1]
                    listaCMB.append(CMB)
            if CodigoM not in listaCMB:
                print("La materia no está en la base de datos")
            elif Contcm >= 12 or Contcm < 5 or not CodigoM.isnumeric():  # Comprobación de caracteres
                a = True
                while a :
                    print("El código superó el límite o el minímo de caracteres, o no ingresó un número")
                    CodigoM = input("Ingrese el código de la Materia: ")
                    if CodigoM <= 12 and CodigoM.isnumeric():
                        a = False
            else:
                comprobado = False
        self.__CodigoM = CodigoM

    def setID(self):
        comprobado = True
        while comprobado == True:
            ID = input("Ingrese el Documento de Identidad: ")  # Código de la materia

            with open('BD-Estudiantes.txt') as file:
                listaCMB = []
                for line in file:
                    listamaterias = line.strip().split(';')
                    CMB = listamaterias[1]
                    listaCMB.append(CMB)
            if ID not in listaCMB:
                print("El documento del estudiante no se encuentra en la base de datos")
            
            else: 
                if len(ID) < 12 and ID.isnumeric() and not "":
                    self.__ID = ID
                    comprobado = False
                else:
                    print("El número es demasiado grande o no es un número, intentelo de nuevo")

def mainBDMAntigua():
    while True:
        menu_principalBDM()
        opcion_elegida = input("Ingrese el número de la opción: ")

        if opcion_elegida == "1":
            mi_materiaaprobada=MateriaAprobada()
            mi_materiaaprobada.setCodigoM()
            mi_materiaaprobada.setID()

            diccionario = mi_materiaaprobada.getCodigoM() + ";" + mi_materiaaprobada.getID()  # Creación de la info de la materia
            if not os.path.isfile("BD-Materias-Antigua.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
                BDM = open("BD-Materias-Antigua.txt","w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                numerodematerias = 1  # Establece el número de materias en 1
                BDM.write(
                    str(numerodematerias) + ";" + str(diccionario) + "\n")  # Escribe los datos de la primera materia
                BDM.close()  # Cierra el archivo

                with open('ContadorBD-Materias-Antigua.txt',
                          'w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(
                        numerodematerias))  # Escribe los datos  iniciales del numero de materias en la abse de datos
                print("¡Materia almacenada con éxito!")


            else:  # Si el archivo ya existe se entra a esta condicion
                with open('ContadorBD-Materias-Antigua.txt',
                          'r') as file:  # Abre el archivo del contador de materias en modo lectura
                    numerodematerias = file.read()  # Almacena el numero de materias leyendo el archivo
                numerodematerias = int(
                    numerodematerias) + 1  # Como se hizo una adición a la base de datos de materias entonces se aumenta el contador en 1

                with open("BD-Materias-Antigua.txt",
                          "a") as file:  # Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(numerodematerias) + ";" + str(
                        diccionario) + "\n")  # Escribe los datos de la siguiente materia

                with open('ContadorBD-Materias-Antigua.txt',
                          'w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                    file.write(str(
                        numerodematerias))  # Actualiza el archivo sobreescribiendo el valor del numero de materias es decir borra los datos del archivo anterior y escribe de nuevo
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
            if os.path.isfile(
                    "BD-Materias-Antigua.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
                menu_mostrarbase()  # Funcion para mostrar el menu de la base de datos
                opcion2 = input("Ingrese el número de la opción: ")  # Solicita una opcion y la almacena como string
                if opcion2 == "0":  # Condicion dada por la variable "Opcion2"
                    with open("BD-Materias-Antigua.txt",
                              "r") as file:  # el metodo with  abre el archivo de la base de datos de materias como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                        listatotal = []  # Crea una lista llamada listatotal
                        for lineas in file:  # Recorre cada linea en el archivo usando un ciclo for
                            lineas = lineas.strip().split(
                                ";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                            listatotal.append(
                                lineas)  # se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados

                    Tabla = "+--------------------------------------------------------+\n| Indice | Código de la Materia | Documento de Identidad |\n|--------------------------------------------------------|"
                    # Crea un string para las primeras casillas de la tabla
                    print(Tabla)  # Imprime ese string
                    for fila in listatotal:  # Para cada lista en la lista total realiza el codigo siguiente:
                        a, b, c = fila  # Desempaqueta las variables de la lista en varias variables llamadas a,b,c, etc que en realidad serían a=Indice, b= Codidog de la materia, C= Nombre. etc--
                        stringdetabla = "|{:^8}|{:^22}|{:^24}|".format(a, b,
                                                                       c)  # Usando el metodo format crea un string con los valores de las variables almacenadas y los centra segun el valor, por ejemplo "^8" lo centra a 8 espacios a izquierda y derecha
                        print(
                            stringdetabla)  # imprime cada string, o sea cada fila de la tabla y continua el ciclo para la siguiente fila
                        print("+--------------------------------------------------------+")

                elif opcion2 == "1":  # Condicion dada por la variable "Opcion2"

                    with open('BD-Materias-Antigua.txt',
                              "r") as file:  # el metodo with  abre el archivo de la base de datos de materias como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                        listaIN = []  # Se crean listas para almacenar cada variable de la base de datos, el indice, el codigo de la materia, el nombre, etc..
                        listaCM = []
                        listaNM = []

                        for line in file:  # Recorre la base de datos linea por linea
                            IN1, CM1, NM1 = line.strip().split(';')  # Desempaqueta las variables de la lista en varias variables Indice,  Codidog de la materia, Nombre. etc--
                            listaIN.append(int(
                                IN1))  # Almacena el valor del indice en la lista y lo convierte en un Int para asegurar que sea un numero y que el ordenamiento sea correcto
                            listaCM.append(
                                CM1)  # Almacena el codigo de la materia en la lista de codigos de materia "listaCM"
                            listaNM.append(NM1)  # Almacena el nombre de la materia en la lista de nombres de la materia

                    menu_opcionesBDMOrdenada()  # Imprime el menu de opciones de ordenamiento
                    opcion3 = input("Ingrese el número de la opción: ")  # Solicita una opcion y la almacena como string

                    if opcion3 == "1":  # Condicion dada por la variable "Opcion3"
                        dic = dict(zip(listaIN,
                                       listaCM))  # con el metodo zip une las dos listas, la de indices con las del codigo, y luego con el metodo dict lo convierte en diccionario,  dando por ejemplo "Indice: codigo de materia"
                        menu_opcionesBDMOrdenadanum()  # Imprime el menu de ordenamiento numerico dado que los codigos de materia son principalmente numericos
                        opcion4 = input(
                            "Ingrese el número de la opción: ")  # Solicita una opcion y la almacena como string
                        if opcion4 == "1":  # Condicion dada por la variable "Opcion4"
                            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(
                                1)))  # Usando la libreria operator , la funcion sorted y la funcion dict, crea un diccionario ordenado ascendentemente por las Key del diccionario
                        elif opcion4 == "2":
                            valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
                            valores_ord.reverse()  # hace el mismo procedimiento anterior pero lo pone al reves, ordenandolo descendentemente
                            valores_ord = dict(valores_ord)
                        else:
                            print("Opción no valida")
                            break

                    elif opcion3 == "2":  # Explicacion en la parte de arriba, lo unico que cambia es la lista usada, usando en ese caso el nombre de la materia
                        dic = dict(zip(listaIN, listaNM))
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

                    with open("BD-Materias-Antigua-ORDENADA.txt", "w") as file:
                        for indices in val:
                            listaordenada = str(indices) + ";" + listaCM[indices - 1] + ";" + listaNM[indices - 1]
                            file.write(listaordenada + "\n")
                    with open("BD-Materias-Antigua-ORDENADA.txt", "r") as file:
                        listatotal = []
                        for lineas in file:
                            lineas = lineas.strip().split(";")
                            listatotal.append(lineas)
                    Tabla = "+--------------------------------------------------------+\n| Indice | Código de la Materia | Documento de Identidad |\n|--------------------------------------------------------|"

                    print(Tabla)
                    for fila in listatotal:  # Para cada lista en la lista total realiza el codigo siguiente:
                        a, b, c = fila  # Desempaqueta las variables de la lista en varias variables llamadas a,b,c, etc que en realidad serían a=Indice, b= Codidog de la materia, C= Nombre. etc--
                        stringdetabla = "|{:^8}|{:^22}|{:^24}|".format(a, b,
                                                                       c)  # Usando el metodo format crea un string con los valores de las variables almacenadas y los centra segun el valor, por ejemplo "^8" lo centra a 8 espacios a izquierda y derecha
                        print(
                            stringdetabla)  # imprime cada string, o sea cada fila de la tabla y continua el ciclo para la siguiente fila
                        print("---------------------------------------------------------+")

                elif opcion2 == "2":  # Condicion dada por la variable "Opcion2"
                    palabra = input(
                        "Ingrese el valor a buscar:")  # Solicita una palabra para buscar y la alamacena como string
                    indicador = False  # Inicializa el indicador en False
                    lista_ME = []  # Crea una lista de Materias Encontradas
                    with open("BD-Materias-Antigua.txt",
                              "r") as file:  # Abre el archivo en modo lectura con el metodo with, llamando al archivo file , ejecutando el codigo anidado cuando el archivo este abierto y cuando termina cierra el archivo
                        for linea in file:  # Recorre cada linea del archivo usando un ciclo For
                            linea = linea.strip().split(
                                ";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                            for items in linea:  # Recorre cada item de la lista creada llamada linea
                                if palabra == items:  # Comprueba si la palabra almacenada es igual al item de la lista
                                    indicador = True  # Indicador de materia encontrada puesto en TRUE
                            if indicador:  # Si el indicador es verdadero
                                lista_ME.append(
                                    linea)  # Almacena en la lista de materias encontradas la lista total de la linea del archivo
                                indicador = False  # Vuelve a poner el indicador en False
                    
                    if lista_ME == []:            
                        print("No se encontró el valor buscado en la base de datos")

                    else:
                        Tabla = "+--------------------------------------------------------+\n| Indice | Código de la Materia | Documento de identidad |\n|--------------------------------------------------------|"

                        print(Tabla)
                        for fila in lista_ME:  # Para cada lista en la lista total realiza el codigo siguiente:
                            a, b, c = fila  # Desempaqueta las variables de la lista en varias variables llamadas a,b,c, etc que en realidad serían a=Indice, b= Codidog de la materia, C= Nombre. etc--
                            stringdetabla = "|{:^8}|{:^22}|{:^24}|".format(a, b,
                                                                        c)  # Usando el metodo format crea un string con los valores de las variables almacenadas y los centra segun el valor, por ejemplo "^8" lo centra a 8 espacios a izquierda y derecha
                            print(
                                stringdetabla)  # imprime cada string, o sea cada fila de la tabla y continua el ciclo para la siguiente fila
                            print("+--------------------------------------------------------+")

                elif opcion2 == "3":
                    CompE = True
                    while CompE:
                        EstR = input("ingrese el documento del estudiante:")
                        with open('BD-Materias-Antigua.txt') as file:
                            listaCMB = []
                            for line in file:
                                listamaterias = line.strip().split(';')
                                CMB = listamaterias[2]
                                listaCMB.append(CMB)
                        if EstR not in listaCMB:
                            print("El estudiante no está en la base de datos, o no tiene materias aprobadas")
                        else:
                            CompE = False
                    
                    MateriasM = []    
                    with open('BD-Materias-Antigua.txt') as file:
                        for line in file:
                            listamaterias = line.strip().split(';')
                            CMB = listamaterias[2]
                            if EstR == CMB:
                                MateriasM.append(listamaterias[1])
                    print(MateriasM)
                    indicador = False  # Inicializa el indicador en False
                    lista_ME = []  # Crea una lista de Materias Encontradas
                    with open("BD-Materias.txt",
                              "r") as file:  # Abre el archivo en modo lectura con el metodo with, llamando al archivo file , ejecutando el codigo anidado cuando el archivo este abierto y cuando termina cierra el archivo
                        for linea in file:  # Recorre cada linea del archivo usando un ciclo For
                            linea = linea.strip().split(
                                ";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                            if linea[1] in MateriasM:  # Recorre la lista par ver si se encuentra el código en la lista de materias
                                indicador = True  # Indicador de materia encontrada puesto en TRUE
                            if indicador:  # Si el indicador es verdadero
                                lista_ME.append(
                                    linea)  # Almacena en la lista de materias encontradas la lista total de la linea del archivo
                                indicador = False  # Vuelve a poner el indicador en False
                    
                            
                    Tabla = "+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n| índice | Documento de identidad | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |\n|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|"
                    BID = EstR
                    print(Tabla)
                    for fila in lista_ME:         #Para cada lista en la lista total realiza el codigo siguiente:
                        if len(fila[2]) < 20:       #Si la longitud del item 2 de la lista es menor a 20 entra al ciclo, esto se hace para verificar si la palabra cabe en la celda
                            a, b, c, d, e, f, g = fila         #Desempaqueta las variables de la lista en varias variables llamadas a,b,c, etc que en realidad serían a=Indice, b= Codidog de la materia, C= Nombre. etc--
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, BID, b, c, d, e, f,g)    # Usando el metodo format crea un string con los valores de las variables almacenadas y los centra segun el valor, por ejemplo "^8" lo centra a 8 espacios a izquierda y derecha
                            print(stringdetabla)    #imprime cada string, o sea cada fila de la tabla y continua el ciclo para la siguiente fila
                        else:
                            a, b, c, d, e, f, g = fila     # entra a esta parte si el Nombre de la Materia es muy largo, y hace el mismo procedimiento ya explicado desempaquetando y almacenando las variables
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, BID, b, c[0:19] + "-", d, e, f, g)       #con el metodo format pone las varibales, y en el caso de la variable del nombre de la amteria imprime los primeros 19 caracteres mas un guion

                            print(stringdetabla)
                            stringdetabla = "|{:^8}|{:^24}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" "," ", " ", c[19:38]," ", " ", " "," ")  #Imprime la siguiente parte que faltó del Nombre de la materia
                            print(stringdetabla)
                            print("+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
             
                elif opcion2 == "4":
                    continue
                elif opcion2 == "5":
                    break
                else:
                    print("Opción no valida")
            else:
                print("Aún no existe una Base de datos")
            menu_opcionesBDM()
            opcion2 = input("\n Ingrese el número de la opción: ")
            if opcion2 == "0":
                continue
            elif opcion2 == "1":
                print("Saliendo...")
                break
            else:
                print("Opción no valida")

        elif opcion_elegida == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no valida")
            print("Saliendo...")
            break

