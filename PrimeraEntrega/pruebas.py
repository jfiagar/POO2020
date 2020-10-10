import operator

def menu_opcionesBDMOrdenada():
    print("[1]  Oredenar por Código de materia")  # Imprime la primera opción
    print("[2]  Oredenar por Nombre de materia")  # Imprime la primera opción
    print("[3]  Oredenar por Código de facultad")  # Imprime la primera opción
    print("[4]  Oredenar por Código de departamento")  # Imprime la primera opción
    print("[5]  Oredenar por Cantidad de créditos")  # Imprime la primera opción
    print("[6]  Oredenar por Código de materia anterior")  # Imprime la primera opción
    print("[7]  Volver al menú principal")
    print("[8]  Salir del programa")  # Imprime la segunda opción

def menu_opcionesBDMOrdenadaalfa():
    print("[1]  Oredenar alfabéticamente [A->Z]")  # Imprime la primera opción
    print("[2]  Oredenar alfabéticamente [Z->A]")  # Imprime la primera opción

def menu_opcionesBDMOrdenadanum():
    print("[1]  Oredenar numéricamente [0->9]")  # Imprime la primera opción
    print("[2]  Oredenar numéricamente [9->0]")  # Imprime la primera opción



with open('BD-Materias.txt') as file:
    listaIN = []
    listaCM = []
    listaNM = []
    listaCF = []
    listaCD = []
    listaCC = []
    listaCMA = []

    for line in file:
        IN,CM,NM,CF,CD,CC,CMA = line.strip().split(';')
        listaIN.append(int(IN[3:]))
        listaCM.append(CM[3:])
        listaNM.append(NM[3:])
        listaCF.append(CF[3:])
        listaCD.append(CD[3:])
        listaCC.append(CC[3:])
        listaCMA.append(CMA[4:])
menu_opcionesBDMOrdenada()
opcion3 = input("Ingrese el número de la opción: ")

if opcion3=="1":
    dic=dict(zip(listaIN,listaCM))
    menu_opcionesBDMOrdenadaalfa()
    opcion4 = input("Ingrese el número de la opción: ")
    if opcion4=="1":
        valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
    elif opcion4=="2":
        valores_ord = sorted(dic.items(), key=operator.itemgetter(1))
        valores_ord.reverse()
        valores_ord = dict(valores_ord)
    else:
        print("Opción no valida")

elif opcion3=="2":
    dic=dict(zip(listaIN,listaNM))
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
elif opcion3=="3":
    dic=dict(zip(listaIN,listaCF))
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
elif opcion3=="4":
    dic=dict(zip(listaIN,listaCD))
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
elif opcion3=="5":
    dic=dict(zip(listaIN,listaCC))
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
elif opcion3=="6":
    dic=dict(zip(listaIN,listaCMA))
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
# elif opcion2=="7":
#     continue
# elif opcion2=="8":
#     break
else:
    print("Opción no valida")


print(valores_ord)  # {4: 15000, 5: 20000, 3: 90000}

val= list(valores_ord.keys())
print(val)
with open("BD-Materias-ORDENADA.txt","w") as file:
    for indices in val:
        listaordenada="IN:"+str(indices)+";""CM:"+ listaCM[indices-1] + ";"+ "NM:"+ listaNM[indices-1] + ";" + "CF:"+ listaCF[indices-1] + ";" + "CD:" + listaCD[indices-1]+ ";"+ "CC:"+listaCC[indices-1]+ ";"+"CMA:"+listaCMA[indices-1]
        file.write(listaordenada+"\n")
        print(listaordenada)
