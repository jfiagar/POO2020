#
# with open("BD-Materias.txt","r") as file:
#     listatotal=[]
#     for lineas in file:
#         lineas=lineas.strip().split(";")
#         listatotal.append(lineas)
#
# Tabla = """\
# +-----------------------------------------------------------------------------------------------------------------------------------------------------------+
# | Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |
# |-----------------------------------------------------------------------------------------------------------------------------------------------------------|\
# """
#
# print(Tabla)
# for fila in listatotal:
#     if len(fila[2])<19:
#         a,b,c,d,e,f,g=fila
#         stringdetabla="|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a,b,c,d,e,f,g)
#         stringdetabla=stringdetabla
#         print(stringdetabla)
#     else:
#         a, b, c, d, e, f, g = fila
#         stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c[0:19]+"-", d, e, f, g)
#         stringdetabla = stringdetabla
#         print(stringdetabla)
#         stringdetabla="|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" "," ", c[19:38], " ", " ", " ", " ")
#         print(stringdetabla)
# print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------+")
#
# palabra="3"
# indicador = False
# lista_ME=[]
# with open("BD-Materias.txt","r") as file:
#     for linea in file:
#         linea=linea.strip().split(";")
#         for items in linea:
#             if palabra== items:
#                 indicador=True
#         if indicador:
#             lista_ME.append(linea)
#             print(lista_ME)
#             indicador = False
# Tabla = """\
# +-----------------------------------------------------------------------------------------------------------------------------------------------------------+
# | Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |
# |-----------------------------------------------------------------------------------------------------------------------------------------------------------|\
# """
#
# print(Tabla)
# for fila in lista_ME:
#     if len(fila[2])<19:
#         a,b,c,d,e,f,g=fila
#         stringdetabla="|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a,b,c,d,e,f,g)
#         stringdetabla=stringdetabla
#         print(stringdetabla)
#     else:
#         a, b, c, d, e, f, g = fila
#         stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c[0:19]+"-", d, e, f, g)
#         stringdetabla = stringdetabla
#         print(stringdetabla)
#         stringdetabla="|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" "," ", c[19:38], " ", " ", " ", " ")
#         print(stringdetabla)
# print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------+")
#
# import basededatosMATERIAS as BDM
#
#
# BDM.mainBDM()
import operator
with open('BD-Materias.txt', "r") as file:
    listaIN = []
    listaCM = []
    listaNM = []
    listaCF = []
    listaCD = []
    listaCC = []
    listaCMA = []

    for line in file:
        IN1, CM1, NM1, CF1, CD1, CC1, CMA1 = line.strip().split(';')
        listaIN.append(int(IN1))
        listaCM.append(int(CM1))
        listaNM.append(NM1)
        listaCF.append(CF1)
        listaCD.append(CD1)
        listaCC.append(CC1)
        listaCMA.append(CMA1)


dic = dict(zip(listaIN, listaCM))

valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))


val = list(valores_ord.keys())

with open("BD-Materias-ORDENADA.txt", "w") as file:
    for indices in val:
        listaordenada = str(indices) + ";" + str(listaCM[indices - 1]) + ";" + listaNM[indices - 1] + ";" + listaCF[indices - 1] + ";" + listaCD[indices - 1] + ";" + listaCC[indices - 1] + ";" + listaCMA[indices - 1]
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