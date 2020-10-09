import os.path
print("Bienvenido a la Base de datos de Materias") #Saludo :v


CM=input("Ingrese el código de la Materia: ") #Código de la materia
NM=input("Ingrese el Nombre de la materia: ")# Nombre de la materia
CF=input("Ingrese el Código facultad que dicta la Materia: ")# Código facultad que la dicta
CD=input("Ingrese el Código departamento que dicta la Materia: ")# Código departamento que la dicta
CC=input("Ingrese la Cantidad de créditos de la Materia: ")# Cantidad de créditos
CMA=input("Ingrese el Código de la materia anterior obligatoria en el plan de estudios: ")  # Código materia anterior obligatoria en el plan de estudios
dict = {"CM" : CM, "NM" : NM, "CF" : CF,"CD":CD,"CC":CC,"CMA":CMA}  # Creación del diccionario de la materia


if not os.path.isfile("BD-Materias.txt"):    #Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no xiste entonces lo crea
    BDM = open("BD-Materias.txt","w")     #Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
    numerodematerias = 1          #Establece el número de materias en 1
    BDM.write(str(dict)+"\n")   #Escribe los datos de la primera materia
    BDM.close()   #Cierra el archivo
    with open('ContadorBD-Materias.txt', 'w') as file:
        file.write(str(numerodematerias))
else:                                #Si el archivo ya existe se entra a esta condicion
    with open("BD-Materias.txt", "a") as file:
        file.write(str(dict) + "\n")

    with open('ContadorBD-Materias.txt', 'r') as file:
        numerodematerias=file.read()
    numerodematerias=int(numerodematerias)+1
    with open('ContadorBD-Materias.txt', 'w') as file:
        file.write(str(numerodematerias))






