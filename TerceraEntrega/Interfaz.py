# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import os.path
from PyQt5.QtWidgets import QTableWidgetItem
import operator


class Persona: #Declaración de clase para el guardado de datos 

    def __init__(self):
        self.__DI = "" #Documento de identidad
        self.__N = ""   #Nombre
        self.__A = ""   #Apellido
    def getDI(self):    #Encapsulamiento
        return self.__DI #Obtener documento
    def getN(self):
        return self.__N  #Obtener el nombre
    def getA(self):
        return self.__A  #Obtener el apellido

    def setDI(self,DI):
        self.__DI=DI   #Dar valor al Documento
                
    def setN(self,N):
        self.__N=N      #Dar valor al Nombre
        
    def setA(self,A):
        self.__A=A     #Dar valor al Apellido
        
class Estudiante(Persona): # Declaracion de clase que hereda atributos de persona
    def __init__(self):
        self.__CP = ""          #Codigo de plan de estudios
        self.__CE = ""          #Calidad de estudiante
        self.__PA = ""          #PAPA

    def getCP(self):  #Encapsulamiento
        return self.__CP    #Obtener Codigo
    def getCE(self):
        return self.__CE    #Obtener Calidad de estudiante
    def getPA(self):
        return self.__PA    #Obtener PAPA


    def setCP(self,CP):
        self.__CP=CP       #Dar valor a Codigo 

    def setCE(self,CE):
        self.__CE=CE      #Dar valor a Calidad de estudiante
               
    def setPA(self,PA):
        self.__PA = PA     #Dar valor a PAPA

class Ui_SIA(object): #Interfaz PyQt5
    def setupUi(self, SIA):
        SIA.setObjectName("SIA")
        SIA.setEnabled(True)
        SIA.resize(762, 495)
        SIA.setMouseTracking(False)
        SIA.setStyleSheet("background-color: rgb(118, 35, 47);") #Color rojo
        self.centralwidget = QtWidgets.QWidget(SIA)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)#Boton salir
        self.pushButton_4.setGeometry(QtCore.QRect(340, 440, 111, 41))
        self.pushButton_4.setBaseSize(QtCore.QSize(9, 0))
        self.pushButton_4.setAutoRepeatDelay(298)
        self.pushButton_4.setObjectName("pushButton_4")
        self.Volver = QtWidgets.QPushButton(self.centralwidget) #Boton volver
        self.Volver.setGeometry(QtCore.QRect(110, 440, 112, 41))
        self.Volver.setObjectName("Volver")
        self.Menu = QtWidgets.QWidget(self.centralwidget)  #Widget Menu
        self.Menu.setGeometry(QtCore.QRect(210, 110, 421, 301))
        self.Menu.setObjectName("Menu")
        self.pushButton = QtWidgets.QPushButton(self.Menu) #Boton ingresar estudiante
        self.pushButton.setGeometry(QtCore.QRect(80, 30, 211, 51))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Menu) #Boton ver base de datos
        self.pushButton_2.setGeometry(QtCore.QRect(80, 90, 211, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.Menu)#Boton buscar
        self.pushButton_3.setGeometry(QtCore.QRect(80, 150, 211, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.Buscador = QtWidgets.QWidget(self.centralwidget)#Widget Buscador
        self.Buscador.setGeometry(QtCore.QRect(25, 20, 711, 391))
        self.Buscador.setObjectName("Buscador")
        self.Buscador.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8 = QtWidgets.QLabel(self.Buscador)#texto buscar en el buscador
        self.label_8.setGeometry(QtCore.QRect(100, 20, 71, 21))
        self.label_8.setObjectName("label_8")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Buscador) #Tabla de visualización del buscador
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(29, 110, 650, 270))
        self.tableWidget_2.setAutoScroll(True)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setTabKeyNavigation(True)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.Buscador) #Line edit del buscador
        self.lineEdit_6.setGeometry(QtCore.QRect(190, 20, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.Buscador) #boton de buscar
        self.pushButton_7.setGeometry(QtCore.QRect(170, 50, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.Datos = QtWidgets.QWidget(self.centralwidget)#Widget Datos
        self.Datos.setEnabled(True)
        self.Datos.setGeometry(QtCore.QRect(150, 50, 471, 361))
        self.Datos.setObjectName("Datos")
        self.PAPA = QtWidgets.QLineEdit(self.Datos)#Para obtener el PAPA
        self.PAPA.setGeometry(QtCore.QRect(280, 210, 113, 20))
        self.PAPA.setObjectName("PAPA")
        self.PAPA.setInputMask("9.9")#Mascara para que solo ingrese numeros float de 0.0 a 5.0
        self.Documento = QtWidgets.QLineEdit(self.Datos)#Para obtener el Documento
        self.Documento.setGeometry(QtCore.QRect(280, 50, 113, 20))
        self.Documento.setObjectName("Documento")
        self.Documento.setInputMask("999999999999")
        self.Documento.setCursorPosition(0)
        self.label_6 = QtWidgets.QLabel(self.Datos)
        self.label_6.setGeometry(QtCore.QRect(40, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Codigo = QtWidgets.QLineEdit(self.Datos)#Para obtener el codigo
        self.Codigo.setGeometry(QtCore.QRect(280, 150, 113, 20))
        self.Codigo.setObjectName("Codigo")
        self.Codigo.setInputMask("99999")#Mascara para ingresar 5 digitos
        self.Guardar = QtWidgets.QPushButton(self.Datos)#boton guardar
        self.Guardar.setGeometry(QtCore.QRect(200, 260, 111, 41))
        self.Guardar.setObjectName("Guardar")
        self.comboBox = QtWidgets.QComboBox(self.Datos)#Combobox de la calidad de estudiante
        self.comboBox.setGeometry(QtCore.QRect(280, 180, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.Datos)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.Datos)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Nombre = QtWidgets.QLineEdit(self.Datos)#Para obtener el Nombre
        self.Nombre.setGeometry(QtCore.QRect(280, 80, 113, 20))
        self.Nombre.setObjectName("Nombre")
        self.Nombre.setMaxLength(20)
        self.label_5 = QtWidgets.QLabel(self.Datos)
        self.label_5.setGeometry(QtCore.QRect(40, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.Datos)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Apellido = QtWidgets.QLineEdit(self.Datos)#Para obtener el apellido
        self.Apellido.setGeometry(QtCore.QRect(280, 110, 113, 20))
        self.Apellido.setObjectName("Apellido")
        self.Apellido.setMaxLength(20)
        self.label = QtWidgets.QLabel(self.Datos)
        self.label.setGeometry(QtCore.QRect(40, 50, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.BaseD = QtWidgets.QWidget(self.centralwidget)
        self.BaseD.setGeometry(QtCore.QRect(25, 20, 711, 391))
        self.BaseD.setObjectName("BaseD")
        self.tableWidget = QtWidgets.QTableWidget(self.BaseD)
        self.tableWidget.setGeometry(QtCore.QRect(29, 110, 650, 270))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item.setBackground(QtGui.QColor(255, 255, 255))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label_7 = QtWidgets.QLabel(self.BaseD)
        self.label_7.setGeometry(QtCore.QRect(100, 30, 81, 31))
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.BaseD)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 30, 221, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_6 = QtWidgets.QPushButton(self.BaseD)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 30, 81, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.BANDERA = QtWidgets.QLabel(self.Datos)#mensaje de advertencia en los datos
        self.BANDERA.setGeometry(QtCore.QRect(10, 1, 550, 30))
        self.BANDERA.hide()
        self.BANDERA.setObjectName("BANDERA")
        self.BANDERA.setStyleSheet('QLabel {color: red;}')
        self.label_9 = QtWidgets.QLabel(self.centralwidget) # Imagen en el inicio
        self.label_9.setGeometry(QtCore.QRect(0, 0, 210, 90))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Imagen1.png"))
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.BANDERA.raise_()
        self.Buscador.raise_()
        self.pushButton_4.raise_()
        self.Volver.raise_()
        self.BaseD.raise_()
        self.Menu.raise_()
        self.Datos.raise_()
        SIA.setCentralWidget(self.centralwidget)
        self.BaseD.setStyleSheet("background-color: rgb(255, 255, 255);")#cambios de colores a botones,fondos y textos
        self.Datos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Volver.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.Guardar.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.pushButton.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.label.setFont(QtGui.QFont('Dominican', 12))
        self.label_2.setFont(QtGui.QFont('Dominican', 12))
        self.label_3.setFont(QtGui.QFont('Dominican', 12))
        self.label_4.setFont(QtGui.QFont('Dominican', 12))
        self.label_5.setFont(QtGui.QFont('Dominican', 12))
        self.label_6.setFont(QtGui.QFont('Dominican', 12))
        self.label_7.setFont(QtGui.QFont('Dominican', 12))
        self.label_8.setFont(QtGui.QFont('Dominican', 12))
        self.pushButton.setFont(QtGui.QFont('Dominican',12))
        self.pushButton_2.setFont(QtGui.QFont('Dominican', 12))
        self.pushButton_3.setFont(QtGui.QFont('Dominican', 12))
        self.pushButton_4.setFont(QtGui.QFont('Dominican', 12))
        self.pushButton_6.setFont(QtGui.QFont('Dominican', 12))
        self.pushButton_7.setFont(QtGui.QFont('Dominican', 12))
        self.pushButton_2.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.pushButton_3.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.pushButton_4.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.pushButton_6.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.pushButton_7.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.comboBox.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.comboBox_2.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.Documento.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.Nombre.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.Apellido.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.Codigo.setStyleSheet("background-color: rgb(212, 215, 221);")
        self.PAPA.setStyleSheet("background-color: rgb(212, 215, 221);")

        self.retranslateUi(SIA)
        self.pushButton.clicked.connect(self.Datos.show)#Eventos de los botones para ocultar, mostar ventanas y ejecutar 
        self.pushButton.clicked.connect(self.Menu.hide)
        self.pushButton_2.clicked.connect(self.Menu.hide)
        self.pushButton_3.clicked.connect(self.Buscador.show)
        self.pushButton_3.clicked.connect(self.Menu.hide)
        self.pushButton_3.clicked.connect(self.Volver.show)
        self.pushButton_2.clicked.connect(self.Volver.show)
        self.pushButton.clicked.connect(self.Volver.show)
        self.Volver.clicked.connect(self.Menu.show)
        self.Volver.clicked.connect(self.Buscador.hide)
        self.Volver.clicked.connect(self.BaseD.hide)
        self.pushButton_2.clicked.connect(self.BaseD.show)
        self.pushButton_2.clicked.connect(self.actua)
        self.Volver.clicked.connect(self.Datos.hide)
        self.Volver.clicked.connect(self.Volver.hide)
        self.pushButton_4.clicked.connect(SIA.close)
        self.Guardar.clicked.connect(self.btnClicked)
        self.pushButton_6.clicked.connect(self.ordenarclick)
        self.pushButton_7.clicked.connect(self.buscarclick)
        QtCore.QMetaObject.connectSlotsByName(SIA)

    def ordenarclick(self): #funcion para ordenar segun el comboBox
        comboBox2=self.comboBox_2.currentText()#obtener lo seleccionado en el combo box

        with open('BD-Estudiantes.txt', "r") as file:#busqueda en la base de datos
                        listaIN = []
                        listaDI = []
                        listaN = []
                        listaA = []
                        listaCP = []
                        listaCE = []
                        listaPA = []

                        for line in file:
                            IN, DI, N, A, CP, CE, PA = line.strip().split(';')
                            listaIN.append(int(IN))
                            listaDI.append(int(DI))
                            listaN.append(N)
                            listaA.append(A)
                            listaCP.append(int(CP))
                            listaCE.append(CE)
                            listaPA.append(float(PA))
        #caso segun la variabe combo box
        if comboBox2=="Documento de identidad":
            dic = dict(zip(listaIN, listaDI))
            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
            val = list(valores_ord.keys())

            with open("BD-Estudiantes-ORDENADA.txt", "w") as file:
                for indices in val:
                    listaordenada = str(indices) + ";" + str(listaDI[indices - 1]) + ";" + listaN[indices - 1] + ";" + listaA[indices - 1] + ";" + str(listaCP[indices - 1]) + ";" + listaCE[indices - 1] + ";" + str(listaPA[indices - 1])
                    file.write(listaordenada + "\n")
            with open("BD-Estudiantes-ORDENADA.txt","r") as file:  # el metodo with  abre el archivo de la base de datos de Estudiantes como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                listatotal = []  # Crea una lista llamada listatotal
                for lineas in file:  # Recorre cada linea en el archivo usando un ciclo for
                    lineas = lineas.strip().split(";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                    listatotal.append(lineas)  # se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados


            with open('BD-Estudiantes-ORDENADA.txt', "r") as file:
                data = []
                for line in file:
                    IN, DI, N, A, CP, CE, PA = line.strip().split(';')
                    data.append((DI, N, A, CP, CE, PA))

        if comboBox2=="Nombre":
            dic = dict(zip(listaIN, listaN))
            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
            val = list(valores_ord.keys())

            with open("BD-Estudiantes-ORDENADA.txt", "w") as file:
                for indices in val:
                    listaordenada = str(indices) + ";" + str(listaDI[indices - 1]) + ";" + listaN[indices - 1] + ";" + listaA[indices - 1] + ";" + str(listaCP[indices - 1]) + ";" + listaCE[indices - 1] + ";" + str(listaPA[indices - 1])
                    file.write(listaordenada + "\n")
            with open("BD-Estudiantes-ORDENADA.txt","r") as file:  # el metodo with  abre el archivo de la base de datos de Estudiantes como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                listatotal = []  # Crea una lista llamada listatotal
                for lineas in file:  # Recorre cada linea en el archivo usando un ciclo for
                    lineas = lineas.strip().split(";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                    listatotal.append(lineas)  # se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados


            with open('BD-Estudiantes-ORDENADA.txt', "r") as file:
                data = []
                for line in file:
                    IN, DI, N, A, CP, CE, PA = line.strip().split(';')
                    data.append((DI, N, A, CP, CE, PA))
                    
        if comboBox2=="Apellido":
            dic = dict(zip(listaIN, listaA))
            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
            val = list(valores_ord.keys())

            with open("BD-Estudiantes-ORDENADA.txt", "w") as file:
                for indices in val:
                    listaordenada = str(indices) + ";" + str(listaDI[indices - 1]) + ";" + listaN[indices - 1] + ";" + listaA[indices - 1] + ";" + str(listaCP[indices - 1]) + ";" + listaCE[indices - 1] + ";" + str(listaPA[indices - 1])
                    file.write(listaordenada + "\n")
            with open("BD-Estudiantes-ORDENADA.txt","r") as file:  # el metodo with  abre el archivo de la base de datos de Estudiantes como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                listatotal = []  # Crea una lista llamada listatotal
                for lineas in file:  # Recorre cada linea en el archivo usando un ciclo for
                    lineas = lineas.strip().split(";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                    listatotal.append(lineas)  # se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados


            with open('BD-Estudiantes-ORDENADA.txt', "r") as file:
                data = []
                for line in file:
                    IN, DI, N, A, CP, CE, PA = line.strip().split(';')
                    data.append((DI, N, A, CP, CE, PA))


        if comboBox2=="Código plan de estudios":
            dic = dict(zip(listaIN, listaCP))
            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
            val = list(valores_ord.keys())

            with open("BD-Estudiantes-ORDENADA.txt", "w") as file:
                for indices in val:
                    listaordenada = str(indices) + ";" + str(listaDI[indices - 1]) + ";" + listaN[indices - 1] + ";" + listaA[indices - 1] + ";" + str(listaCP[indices - 1]) + ";" + listaCE[indices - 1] + ";" + str(listaPA[indices - 1])
                    file.write(listaordenada + "\n")
            with open("BD-Estudiantes-ORDENADA.txt","r") as file:  # el metodo with  abre el archivo de la base de datos de Estudiantes como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                listatotal = []  # Crea una lista llamada listatotal
                for lineas in file:  # Recorre cada linea en el archivo usando un ciclo for
                    lineas = lineas.strip().split(";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                    listatotal.append(lineas)  # se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados


            with open('BD-Estudiantes-ORDENADA.txt', "r") as file:
                data = []
                for line in file:
                    IN, DI, N, A, CP, CE, PA = line.strip().split(';')
                    data.append((DI, N, A, CP, CE, PA))

        if comboBox2=="Calidad de estudiante":
            dic = dict(zip(listaIN, listaCE))
            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
            val = list(valores_ord.keys())

            with open("BD-Estudiantes-ORDENADA.txt", "w") as file:
                for indices in val:
                    listaordenada = str(indices) + ";" + str(listaDI[indices - 1]) + ";" + listaN[indices - 1] + ";" + listaA[indices - 1] + ";" + str(listaCP[indices - 1]) + ";" + listaCE[indices - 1] + ";" + str(listaPA[indices - 1])
                    file.write(listaordenada + "\n")
            with open("BD-Estudiantes-ORDENADA.txt","r") as file:  # el metodo with  abre el archivo de la base de datos de Estudiantes como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                listatotal = []  # Crea una lista llamada listatotal
                for lineas in file:  # Recorre cada linea en el archivo usando un ciclo for
                    lineas = lineas.strip().split(";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                    listatotal.append(lineas)  # se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados


            with open('BD-Estudiantes-ORDENADA.txt', "r") as file:
                data = []
                for line in file:
                    IN, DI, N, A, CP, CE, PA = line.strip().split(';')
                    data.append((DI, N, A, CP, CE, PA))

        if comboBox2=="PAPA actual":
            dic = dict(zip(listaIN, listaPA))
            valores_ord = dict(sorted(dic.items(), key=operator.itemgetter(1)))
            val = list(valores_ord.keys())

            with open("BD-Estudiantes-ORDENADA.txt", "w") as file:
                for indices in val:
                    listaordenada = str(indices) + ";" + str(listaDI[indices - 1]) + ";" + listaN[indices - 1] + ";" + listaA[indices - 1] + ";" + str(listaCP[indices - 1]) + ";" + listaCE[indices - 1] + ";" + str(listaPA[indices - 1])
                    file.write(listaordenada + "\n")
            with open("BD-Estudiantes-ORDENADA.txt","r") as file:  # el metodo with  abre el archivo de la base de datos de Estudiantes como modo lectura, lo abre con el nombre de "file" y ejecuta el codigo siguiente mientras esté abierto, luego cierra el archivo
                listatotal = []  # Crea una lista llamada listatotal
                for lineas in file:  # Recorre cada linea en el archivo usando un ciclo for
                    lineas = lineas.strip().split(";")  # con la función strip quita los saltos de linea "\n", con la función split, divide las palabras segun cuando encuentra un ";" y devuelve una lista, la cual es almacenada en la variable lineas
                    listatotal.append(lineas)  # se agregan las listas creadas a la lista total, creando una lista de listas con los valores separados


            with open('BD-Estudiantes-ORDENADA.txt', "r") as file:
                data = []
                for line in file:
                    IN, DI, N, A, CP, CE, PA = line.strip().split(';')
                    data.append((DI, N, A, CP, CE, PA))
                

        with open('ContadorBD-Estudiantes.txt','r') as file:  # Abre el archivo del contador de materias en modo lectura
            numerodeestudiantes = file.read()  # Almacena el numero de materias leyendo el archivo
        self.tableWidget.setRowCount(int(numerodeestudiantes))
        self.tableWidget.setColumnCount(6)
        row=0
        for tup in data:
             col=0
             for item in tup:
                 cellinfo=QTableWidgetItem(item)
                 self.tableWidget.setItem(row, col, cellinfo)
                 col+=1
             row += 1

    def actua(self):
        with open('BD-Estudiantes.txt', "r") as file:
            data = []
            for line in file:
                IN, DI, N, A, CP, CE, PA = line.strip().split(';')
                data.append((DI, N, A, CP, CE, PA))

        with open('ContadorBD-Estudiantes.txt','r') as file:  # Abre el archivo del contador de materias en modo lectura
            numerodeestudiantes = file.read()  # Almacena el numero de materias leyendo el archivo
        self.tableWidget.setRowCount(int(numerodeestudiantes))
        self.tableWidget.setColumnCount(6)
        row=0
        for tup in data:
             col=0
             for item in tup:
                 cellinfo=QTableWidgetItem(item)
                 self.tableWidget.setItem(row, col, cellinfo)
                 col+=1
             row += 1
        

    def buscarclick(self): #comienza la busqueda 
        Item = self.lineEdit_6.text()#elemento a buscar
        f=0 #contador de filas
        
        with open('BD-Estudiantes.txt', "r") as file:
            data = []
            indicador = False
            for linea in file:
                linea = linea.strip().split(";")
                for palabra in linea:
                    if palabra == Item:
                        indicador = True
                if indicador:
                    IN, DI, N, A, CP, CE, PA = linea
                    data.append((DI, N, A, CP, CE, PA))
                    indicador = False
                    f+=1
                
        self.tableWidget_2.setRowCount(int(f))#generacion de la tabla 
        self.tableWidget_2.setColumnCount(6)
        row=0
        for tup in data:
             col=0
             for item in tup:
                 cellinfo=QTableWidgetItem(item)
                 self.tableWidget_2.setItem(row, col, cellinfo)
                 col+=1
             row += 1


    def btnClicked(self):#guardar los datos en la seccion de ingresar estudiante
        Documento=self.Documento.text()
        Nombre=self.Nombre.text()
        Apellido=self.Apellido.text()
        Codigo=self.Codigo.text()
        PAPA=self.PAPA.text()
        comboBox=self.comboBox.currentText()
        #verificar si exite las bases de datos 
        if not os.path.isfile("BD-Estudiantes.txt"):  # Verificación de que la base de datos exista usando "isfile" de la libreria os.path , si existe el archivo el valor es True, sino False .Por lo tanto si el archivo no existe entonces entra a la condición
            BDM = open("BD-Estudiantes.txt","w")  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
            BDM.close()  # Cierra el archivo
            BDM = open("ContadorBD-Estudiantes.txt","w")# Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
            BDM.close()  # Cierra el archivo
            with open('ContadorBD-Estudiantes.txt','w') as file:# Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                file.write(str(0))
            
        with open("BD-Estudiantes.txt", "r") as file:#comprueba si existe el documento de identidad en la base de datos
            listaCMB = []
            for line in file:
                listamaterias = line.strip().split(';')
                CMB = listamaterias[1]
                listaCMB.append(CMB)
            if Documento in listaCMB:
                self.BANDERA.setText("Documento de identidad ya se encuentra en la base de datos, por favor revise sus datos")#advertencia
                self.BANDERA.show()
            else:
                if Documento!="" and Nombre!="" and Apellido!="" and Codigo!="" and PAPA!="." and comboBox!="": #comprueba de que no existan espacios vacios
                    mi_estudiante = Estudiante()#Instancia el objeto para el guardado de datos 
                    mi_estudiante.setDI(Documento)
                    mi_estudiante.setN(Nombre)
                    mi_estudiante.setA(Apellido)
                    mi_estudiante.setCP(Codigo)
                    mi_estudiante.setCE(comboBox)
                    if float(PAPA)<= 5.0: #comprueba el PAPA sea menor a 5.0
                        mi_estudiante.setPA(PAPA)

                        diccionario = mi_estudiante.getDI() + ";" + mi_estudiante.getN() + ";" + mi_estudiante.getA() + ";" + mi_estudiante.getCP() + ";" + mi_estudiante.getCE() + ";" + mi_estudiante.getPA()  # Creación del diccionario de la materia
                        with open('ContadorBD-Estudiantes.txt','r') as file:  # Abre el archivo del contador de materias en modo lectura
                            numerodeestudiantes = file.read()  # Almacena el numero de materias leyendo el archivo
                        numerodeestudiantes = int(numerodeestudiantes) + 1  # Como se hizo una adición a la base de datos de materias entonces se aumenta el contador en 1
                        with open("BD-Estudiantes.txt","a") as file:  # Abrir archivo en modo adjuntar. Si el archivo no existe, crea un nuevo archivo.
                            file.write(str(numerodeestudiantes) + ";" + str(diccionario) + "\n")  # Escribe los datos de la siguiente materia
                        with open('ContadorBD-Estudiantes.txt','w') as file:  # Este modo abre el archivo para escritura. Si el archivo no existe, crea un nuevo archivo.
                            file.write(str(numerodeestudiantes))
                        self.BANDERA.hide()#Oculta el mensaje de adevertencia si este ya se visualiza en la ventana y todo es correcto
                    else:
                        self.BANDERA.setText("PAPA inválido, por favor revise sus datos")#Advertencia de PAPA superior a 5.0
                        self.BANDERA.show()  
                else:
                    self.BANDERA.setText("Espacios vacios, por favor revise sus datos")#Advertencia de espacio vacios
                    self.BANDERA.show()
        

        #limpia los line edit para ingresar mas datos                        
        self.Documento.clear()
        self.Nombre.clear()
        self.Apellido.clear()
        self.Codigo.clear()
        self.PAPA.clear()


    def retranslateUi(self, SIA):
        _translate = QtCore.QCoreApplication.translate
        SIA.setWindowTitle(_translate("SIA", "MainWindow"))
        self.pushButton_4.setText(_translate("SIA", "Salir "))
        self.Volver.setText(_translate("SIA", "Volver"))
        self.pushButton.setText(_translate("SIA", "Ingresar Estudiante"))
        self.pushButton_2.setText(_translate("SIA", "Ver base de datos Estudiante"))
        self.pushButton_3.setText(_translate("SIA", "Buscar"))
        self.label_8.setText(_translate("SIA", "Buscar por"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("SIA", "Documento de \n"
"identidad"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("SIA", "Nombre"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("SIA", "Apellido"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("SIA", "Código de \n"
"plan de estudio"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("SIA", "Calidad de\n"
"estudiante"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("SIA", "PAPA actual"))
        self.pushButton_7.setText(_translate("SIA", "Buscar"))
        self.label_6.setText(_translate("SIA", "PAPA actual"))
        self.Guardar.setText(_translate("SIA", "Guardar"))
        self.comboBox.setItemText(0, _translate("SIA", ""))
        self.comboBox.setItemText(1, _translate("SIA", "Matriculado"))
        self.comboBox.setItemText(2, _translate("SIA", "Graduado"))
        self.comboBox.setItemText(3, _translate("SIA", "Pérdida de cupo"))
        self.label_3.setText(_translate("SIA", "Código de plan de estudios"))
        self.label_2.setText(_translate("SIA", "Nombre "))
        self.label_5.setText(_translate("SIA", "Apellido"))
        self.label_4.setText(_translate("SIA", "Calidad de estudiante"))
        self.label.setText(_translate("SIA", "Documento de identidad"))
        self.BANDERA.setText(_translate("SIA", "ERROR"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SIA", "Documento de \n"
"identidad"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SIA", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SIA", "Apellido"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SIA", "Código plan \n"
"de estudios "))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SIA", "Calidad de \n"
"estudiante "))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SIA", "PAPA actual"))
        self.label_7.setText(_translate("SIA", "Ordenar por"))
        self.comboBox_2.setItemText(0, _translate("SIA", "Documento de identidad"))
        self.comboBox_2.setItemText(1, _translate("SIA", "Nombre"))
        self.comboBox_2.setItemText(2, _translate("SIA", "Apellido"))
        self.comboBox_2.setItemText(3, _translate("SIA", "Código plan de estudios"))
        self.comboBox_2.setItemText(4, _translate("SIA", "Calidad de estudiante"))
        self.comboBox_2.setItemText(5, _translate("SIA", "PAPA actual"))
        self.pushButton_6.setText(_translate("SIA", "Ordenar"))
        
