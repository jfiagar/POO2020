print("Bienvenido a la Base de datos de Estudiantes") #Saludo :v


CM=input("Ingrese el código de la Materia: ") #Código de la materia
NM=input("Ingrese el Nombre de la materia: ")# Nombre de la materia
CF=input("Ingrese el Código facultad que dicta la Materia: ")# Código facultad que la dicta
CD=input("Ingrese el Código departamento que dicta la Materia: ")# Código departamento que la dicta
CC=input("Ingrese la Cantidad de créditos de la Materia: ")# Cantidad de créditos
CMA=input("Ingrese el Código de la materia anterior obligatoria en el plan de estudios: ")# Código materia anterior obligatoria en el plan de estudios
dict = {"CM" : CM, "NM" : NM, "CF" : CF,"CD":CD,"CC":CC,"CMA":CMA}
f = open("dict.txt","a")
f.write( str(dict)+"\n" )
f.close()
with open('dict.txt', 'r') as dict_file:
    dict_text = dict_file.read()
    print(dict_text)

# #CREAR LA BASE DE DATOS DE ESTUDIANTES
# basedatosESTUDIANTES=open ("BDE.txt","a")  #Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
#
# baseDatos.close()