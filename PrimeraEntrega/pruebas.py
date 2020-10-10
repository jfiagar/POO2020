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
    mdict = {}
    for line in file:
        a, b,c,d,e,f,g = line.strip().split(';')
        print(a,b,c,d,e,f,g)