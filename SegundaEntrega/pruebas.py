# #
# # with open("BD-Materias.txt","r") as file:
# #     listatotal=[]
# #     for lineas in file:
# #         lineas=lineas.strip().split(";")
# #         listatotal.append(lineas)
# #
# # Tabla = """\
# # +-----------------------------------------------------------------------------------------------------------------------------------------------------------+
# # | Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |
# # |-----------------------------------------------------------------------------------------------------------------------------------------------------------|\
# # """
# #
# # print(Tabla)
# # for fila in listatotal:
# #     if len(fila[2])<19:
# #         a,b,c,d,e,f,g=fila
# #         stringdetabla="|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a,b,c,d,e,f,g)
# #         stringdetabla=stringdetabla
# #         print(stringdetabla)
# #     else:
# #         a, b, c, d, e, f, g = fila
# #         stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c[0:19]+"-", d, e, f, g)
# #         stringdetabla = stringdetabla
# #         print(stringdetabla)
# #         stringdetabla="|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" "," ", c[19:38], " ", " ", " ", " ")
# #         print(stringdetabla)
# # print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------+")
# #
# # palabra="3"
# # indicador = False
# # lista_ME=[]
# # with open("BD-Materias.txt","r") as file:
# #     for linea in file:
# #         linea=linea.strip().split(";")
# #         for items in linea:
# #             if palabra== items:
# #                 indicador=True
# #         if indicador:
# #             lista_ME.append(linea)
# #             print(lista_ME)
# #             indicador = False
# # Tabla = """\
# # +-----------------------------------------------------------------------------------------------------------------------------------------------------------+
# # | Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |
# # |-----------------------------------------------------------------------------------------------------------------------------------------------------------|\
# # """
# #
# # print(Tabla)
# # for fila in lista_ME:
# #     if len(fila[2])<19:
# #         a,b,c,d,e,f,g=fila
# #         stringdetabla="|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a,b,c,d,e,f,g)
# #         stringdetabla=stringdetabla
# #         print(stringdetabla)
# #     else:
# #         a, b, c, d, e, f, g = fila
# #         stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c[0:19]+"-", d, e, f, g)
# #         stringdetabla = stringdetabla
# #         print(stringdetabla)
# #         stringdetabla="|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" "," ", c[19:38], " ", " ", " ", " ")
# #         print(stringdetabla)
# # print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------+")
# #
# # import basededatosMATERIAS as BDM
# #
# #
# # BDM.mainBDM()
# import operator
# with open('BD-Materias.txt', "r") as file:
#     listaIN = []
#     listaCM = []
#     listaNM = []
#     listaCF = []
#     listaCD = []
#     listaCC = []
#     listaCMA = []
#
#     for line in file:
#         IN1, CM1, NM1, CF1, CD1, CC1, CMA1 = line.strip().split(';')
#         listaIN.append(int(IN1))
#         listaCM.append(int(CM1))
#         listaNM.append(NM1)
#         listaCF.append(CF1)
#         listaCD.append(CD1)
#         listaCC.append(CC1)
#         listaCMA.append(CMA1)
#
#
# dic = dict(zip(listaIN, listaCM))
#
# valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
#
#
# val = list(valores_ord.keys())
#
# with open("BD-Materias-ORDENADA.txt", "w") as file:
#     for indices in val:
#         listaordenada = str(indices) + ";" + str(listaCM[indices - 1]) + ";" + listaNM[indices - 1] + ";" + listaCF[indices - 1] + ";" + listaCD[indices - 1] + ";" + listaCC[indices - 1] + ";" + listaCMA[indices - 1]
#         file.write(listaordenada + "\n")
# with open("BD-Materias-ORDENADA.txt", "r") as file:
#     listatotal = []
#     for lineas in file:
#         lineas = lineas.strip().split(";")
#         listatotal.append(lineas)
#
# Tabla = "+-----------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Indice | Código de la Materia | Nombre de la Materia | Código de facultad | Código de departamento | Cantidad de créditos | Código de la materia anterior |\n|-----------------------------------------------------------------------------------------------------------------------------------------------------------|"
#
# print(Tabla)
# for fila in listatotal:
#     if len(fila[2]) < 19:
#         a, b, c, d, e, f, g = fila
#         stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b, c, d, e, f,g)
#         stringdetabla = stringdetabla
#         print(stringdetabla)
#     else:
#         a, b, c, d, e, f, g = fila
#         stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(a, b,c[0:19] + "-",d, e, f, g)
#         stringdetabla = stringdetabla
#         print(stringdetabla)
#         stringdetabla = "|{:^8}|{:^22}|{:^22}|{:^20}|{:^24}|{:^22}|{:^31}|".format(" ", " ",c[19:38]," ", " ", " "," ")
#         print(stringdetabla)
# print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------+")
#
# print("""
#          %&&&&&&&&&&&&&&&#               *&&&&              &&&&&       &&&&&     #%%%%              %%%%%     *%%%%%%%%%%%%%%%%%          %%%%%%%%%%%%                      %%%%%
#          %&&&&&&&&&&&&&&&&&&&&*          *&&&&&/            &&&&&       &&&&&     #%%%%%*            %%%%%     *%%%%%%%%%%%%%%%%%      %%%%%%%%%%%%%%%%%%%%                 %%%%%%(
#          %&&&&          *&&&&&&&&        *&&&&&&&           &&&&&       &&&&&     #%%%%%%%           %%%%%     *%%%%%               (%%%%%%%,        ,%%%%%%%#             %%%%%%%%%
#          %&&&&              .&&&&&#      *&&&&&&&&&         &&&&&       &&&&&     #%%%%%%%%%         %%%%%     *%%%%%              %%%%%%                %%%%%%           %%%%%*%%%%%
#          %&&&&                %&&&&&     *&&&& &&&&&%       &&&&&       &&&&&     #%%%%#%%%%%/       %%%%%     *%%%%%             (((((                    %%%%%.        %%%%%  (%%%%/
#          %&&&&                 &&&&&.    *&&&&  #&&&&&.     &&&&&       &&&&&     #%%%%* %%%%%%/     %%%%%     *%%%%%                                       %%%%%       %%%%%.   *%%%%(
#          %&&&&                 .&&&&.    *&&&&    &&&&&&    &&&&&       &&&&&     #%%%%*   %%%%%%    %%%%%     *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%             %%%%%      %%%%%      *%%%%%
#          %&&&&                 &&&&&.    *&&&&      &&&&&&  &&&&&       &&&&&     #%%%%*    .%%%%%%  %%%%%     *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%             %%%%%     %%%%%        (%%%%/
#          %&&&&                /&&&&&     *&&&&       (&&&&&(&&&&&       &&&&&     #%%%%*      ,%%%%%(%%%%%     *%%%%%            ./////                    %%%%%*    %%%%%/         %%%%%(
#          %&&&&               &&&&&&      *&&&&         &&&&&&&&&&       &&&&&     #%%%%*        %%%%%%%%%%     *%%%%%             (%%%%%,                .%%%%%#    %%%%%/           %%%%%%
#          %&&&&            &&&&&&&#       *&&&&           &&&&&&&&       &&&&&     #%%%%*          %%%%%%%%     *%%%%%               %%%%%%%/          *%%%%%%%     %%%%%/             %%%%%/
#          %&&&&&&&&&&&&&&&&&&&&&,         *&&&&             &&&&&&       &&&&&     #%%%%*           .%%%%%%     *%%%%%                 %%%%%%%%%%%%%%%%%%%%%%      %%%%%/               %%%%%(
#          %&&&&&&&&&&&&&&&&&              *&&&&              (&&&&       &&&&&     #%%%%*             %%%%%     *%%%%%                     %%%%%%%%%%%%%%         %%%%%/                 %%%%%%
# """)
ID="123456789"
with open(ID + "-inscripcion.txt", "r") as file:
    listatotal = []  # Crea una lista llamada listatotal
    for lineas in file:  # Recorre cada linea en el archivo usando un ciclo for
        lineas = lineas.strip().split(";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
        listatotal.append(lineas)  # se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados

Tabla = "\+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n| Documento de Identidad |        Nombre        |       Apellido       | Código de la Materia |  Nombre de la Materia  | Créditos |  Nombre del Docente  | Apellido del Docente | Dias de Clase | Hora de Clase |\n|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|"
# Crea un string para las primeras casillas de la tabla
print(Tabla)  # Imprime ese string
for fila in listatotal:  # Para cada lista en la lista total realiza el codigo siguiente:
    if len(fila[4]) < 20:  # Si la longitud del item 2 de la lista es menor a 20 entra al ciclo, esto se hace para verificar si la palabra cabe en la celda
        a, b, c, d, e, f, g, h, i, j = fila  # Desempaqueta las variables de la lista en varias variables llamadas a,b,c, etc que en realidad serían a=Indice, b= Codidog de la materia, C= Nombre. etc--
        stringdetabla = "|{:^24}|{:^22}|{:^22}|{:^22}|{:^24}|{:^10}|{:^22}|{:^22}|{:^15}|{:^15}|".format(a, b, c, d, e,f, g, h, i,j)  # Usando el metodo format crea un string con los valores de las variables almacenadas y los centra segun el valor, por ejemplo "^8" lo centra a 8 espacios a izquierda y derecha
        print(
            stringdetabla)  # imprime cada string, o sea cada fila de la tabla y continua el ciclo para la siguiente fila
    else:
        a, b, c, d, e, f, g, h, i, j = fila  # entra a esta parte si el Nombre de la Materia es muy largo, y hace el mismo procedimiento ya explicado desempaquetando y almacenando las variables
        stringdetabla = "|{:^24}|{:^22}|{:^22}|{:^22}|{:^24}|{:^10}|{:^22}|{:^22}|{:^15}|{:^15}|".format(a, b, c, d, e[0:19] + "-", f, g, h,i,j)  # con el metodo format pone las varibales, y en el caso de la variable del nombre de la amteria imprime los primeros 19 caracteres mas un guion

        print(stringdetabla)
        stringdetabla = "|{:^24}|{:^22}|{:^22}|{:^22}|{:^24}|{:^10}|{:^22}|{:^22}|{:^15}|{:^15}|".format(" ", " ", " ", " ", e[19:38], " ", " "," ", " "," ")  # Imprime la siguiente parte que faltó del Nombre de la materia
        print(stringdetabla)
print("+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n")
