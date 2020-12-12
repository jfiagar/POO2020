from PyQt5 import QtWidgets
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

with open('BD-Estudiantes.txt', "r") as file:
    data = []
    for line in file:
        IN, DI, N, A, CP, CE, PA = line.strip().split(';')
        data.append((DI, N, A, CP, CE, PA))

with open('ContadorBD-Estudiantes.txt','r') as file:  # Abre el archivo del contador de materias en modo lectura
    numerodeestudiantes = file.read()  # Almacena el numero de materias leyendo el archivo

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_SIA()
        self.ui.setupUi(self)
        self.ui.Datos.hide()
        self.ui.Buscador.hide()
        self.ui.BaseD.hide()
        self.ui.Volver.hide()
        self.ui.tableWidget.setRowCount(int(numerodeestudiantes))
        self.ui.tableWidget.setColumnCount(6)
        row=0
        for tup in data:
             col=0
             for item in tup:
                 cellinfo=QTableWidgetItem(item)
                 self.ui.tableWidget.setItem(row, col, cellinfo)
                 col+=1
             row += 1


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())


