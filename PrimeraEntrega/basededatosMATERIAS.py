import os.path
import os

def menu_principalBDM():
    os.system('cls')  # NOTA para windows tienes que cambiar clear por cls
    print("Bienvenido a la Base de datos de Materias")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal
    print("[0]  Ver la base de datos actual")  # Imprime la primera opción
    print("[1]  Ingresar Materias a la base de datos")  # Imprime la segunda opción
    print("[2]  Salir del programa")  # Imprime la tercera opción


def menu_opcionesBDM():
    print("[0]  Volver al menú principal")  # Imprime la primera opción
    print("[1]  Salir del programa")  # Imprime la segunda opción


while True:
    menu_principalBDM()
    opcion_elegida = input("Ingrese el número de la opción: ")
    if opcion_elegida == "0":
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        if not os.path.isfile("BD-Materias.txt"):
            print("Aún no existe una Base de datos")
        else:
            with open("BD-Materias.txt", "r") as file:
                print(file.read())
        print(
            "----------------------------------------------------------------------------------------------------------------------------------------------------------------")
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
        dict = {"CM": CM, "NM": NM, "CF": CF, "CD": CD, "CC": CC, "CMA": CMA}  # Creación del diccionario de la materia

        if not os.path.isfile(
                "BD-Materias.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
            BDM = open("BD-Materias.txt",
                       "w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
            numerodematerias = 1  # Establece el número de materias en 1
            BDM.write(str(dict) + "\n")  # Escribe los datos de la primera materia
            BDM.close()  # Cierra el archivo

            with open('ContadorBD-Materias.txt',
                      'w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                file.write(
                    str(numerodematerias))  # Escribe los datos  iniciales del numero de materias en la abse de datos


        else:  # Si el archivo ya existe se entra a esta condicion
            with open("BD-Materias.txt",
                      "a") as file:  # Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
                file.write(str(dict) + "\n")  # Escribe los datos de la siguiente materia

            with open('ContadorBD-Materias.txt',
                      'r') as file:  # Abre el archivo del contador de materias en modo lectura
                numerodematerias = file.read()  # Almacena el numero de materias leyendo el archivo
            numerodematerias = int(
                numerodematerias) + 1  # Como se hizo una adición a la base de datos de materias entonces se aumenta el contador en 1

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



