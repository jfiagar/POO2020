from PyQt5 import QtWidgets#importa librerias PyQt5
from PyQt5.QtWidgets import QTableWidgetItem
from Interfaz import Ui_SIA  # importa nuestro archivo generado
import sys
import os


if not os.path.isfile("BD-Estudiantes.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
    BDM = open("BD-Estudiantes.txt","w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
    BDM.close()  # Cierra el archivo
    BDM = open("ContadorBD-Estudiantes.txt","w")# Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
    BDM.close()  # Cierra el archivo
    with open('ContadorBD-Estudiantes.txt','w') as file:# Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
        file.write(str(0))

with open('BD-Estudiantes.txt', "r") as file:#Abre la base de datos de estudiantes en modo lectura
    data = []
    for line in file:#Ciclo para recorrer cada linea del archivo
        IN, DI, N, A, CP, CE, PA = line.strip().split(';') #Guarda en variables cada que encuentra un punto y coma
        data.append((DI, N, A, CP, CE, PA))# une estas variables en la lista data

with open('ContadorBD-Estudiantes.txt','r') as file:  # Abre el archivo del contador de estudiantes en modo lectura
    numerodeestudiantes = file.read()  # Almacena el numero de materias leyendo el archivo

class mywindow(QtWidgets.QMainWindow):#Declaracion de la ventana principal
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_SIA()
        self.ui.setupUi(self)
        self.ui.Datos.hide()#oculta el widget de Datos
        self.ui.Buscador.hide() #oculta el widget de Buscador
        self.ui.BaseD.hide()#oculta el widget de Base de datos
        self.ui.Volver.hide()#oculta el boton de volver
        self.ui.tableWidget.setRowCount(int(numerodeestudiantes)) #genera las filas donde se visualiza la base de datos
        self.ui.tableWidget.setColumnCount(6)#genera las columnas donde se visualiza la tabla de datos 
        row=0
        for tup in data: #ciclo para visualizar los datos en la tabla generada
             col=0
             for item in tup:
                 cellinfo=QTableWidgetItem(item)
                 self.ui.tableWidget.setItem(row, col, cellinfo)
                 col+=1
             row += 1


app = QtWidgets.QApplication([])
application = mywindow()#Instancia del objeto
application.show() # motrar la ventana principal
sys.exit(app.exec()) #matener la ventana


