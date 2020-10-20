import basededatosMATERIAS as BDM
import BDMateriasAntigua as BDMA
import inscripcion as INS
import BDEstudiantes as BDE

import os
import os.path
import operator



def menu_principalSIA():
    borrarPantalla()  # Borra los valores de la consola de windows, limpia la consola
    print("Bienvenido al SIA")  # Saludo :v
    print("MENÚ PRINCIPAL")  # Imprime Menú principal
    print("[0]  Entrar a la base de datos de materias Actual")  # Imprime la primera opción
    print("[1]  Entrar a la base de datos de materias Antigua")
    print("[2]  Entrar a la base de datos de Estudiantes")  # Imprime la segunda opción
    print("[3]  Entrar a la base de datos de Docentes")
    print("[4]  Inscribir materias")
    print("[5]  Salir del programa")  # Imprime la tercera opción

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":\
        os.system ("cls")

while True:
    menu_principalSIA()
    opcion_elegida = input("Ingrese el número de la opción: ")
    if opcion_elegida == "0":
        BDM.mainBDM()
    elif opcion_elegida == "1":
        BDMA.mainBDMAntigua()
    elif opcion_elegida=="2":
        BDE.mainBDE()
    # elif opcion_elegida == "3":
    #     BDMD.mainBDMD()
    elif opcion_elegida == "4":
        INS.main_inscripciones()
    elif opcion_elegida == "5":
        break
    else:
        print("Saliendo")