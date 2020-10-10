# import operator
#
# valores = {5: 20000, 3: 90000, 4: 15000,8:2}
# valores_ord = dict(sorted(valores.items(), key=operator.itemgetter(0)))
# print(valores_ord)  # {4: 15000, 5: 20000, 3: 90000}
# f = open("BD-Materias.txt", "r")
# for linea in f:
#     linea=linea.rstrip()
#     print(type(linea))
#     print(linea)
# f.close()
with open('BD-Materias.txt') as file:
    nuevalista1 = []
    nuevalista2 = []
    nuevalista3 = []
    nuevalista4 = []
    nuevalista5 = []
    nuevalista6 = []
    nuevalista7 = []

    for line in file:
        IN,CM,NM,CF,CD,CC,CMA = line.strip().split(';')
        nuevalista1.append(int(IN[3:]))
        nuevalista2.append(CM[3:])
        nuevalista3.append(NM[3:])
        nuevalista4.append(CF[3:])
        nuevalista5.append(CD[3:])
        nuevalista6.append(CC[3:])
        nuevalista7.append(CMA[4:])

print(nuevalista1)
print(nuevalista2)
dic=dict(zip(nuevalista1,nuevalista2))
print(dic)
import operator

valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
print(valores_ord)  # {4: 15000, 5: 20000, 3: 90000}

val= list(valores_ord.keys())
print(val)

for indices in val:
    listaordenada="IN:"+str(indices)+";""CM:"+ nuevalista2[indices-1] + ";"+ "NM:"+ nuevalista3[indices-1] + ";" + "CF:"+ nuevalista4[indices-1] + ";" + "CD:" + nuevalista5[indices-1]+ ";"+ "CC:"+nuevalista6[indices-1]+ ";"+"CMA:"+nuevalista7[indices-1]
    print(listaordenada)