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

palabra="Programación orientada a objetos"
indicador = False
with open("BD-Materias.txt","r") as file:
    for linea in file:
        linea=linea.strip().split(";")
        for items in linea:
            if palabra== items:
                indicador=True
        if indicador:
            print("linea encontrada"+str(linea))
            indicador = False
        print(linea)
