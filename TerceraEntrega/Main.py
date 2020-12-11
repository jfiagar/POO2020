from PyQt5 import QtWidgets
from Interfaz import Ui_SIA  # importa nuestro archivo generado

import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_SIA()
        self.ui.setupUi(self)
        self.ui.Datos.hide()
        self.ui.Buscador.hide()
        self.ui.BaseD.hide()
        self.ui.Volver.hide()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
class Persona:

    def __init__(self):
        self.__DI = ""
        self.__N = ""
        self.__A = ""
    def getDI(self):
        return self.__DI
    def getN(self):
        return self.__N
    def getA(self):
        return self.__A
    def setDI(self):
        comprobado = True
        while comprobado == True:
            DI = input("Ingrese el Documento de Identidad: ")  # Código de la materia
            if len(DI) < 12 and DI.isnumeric():
                self.__DI=DI
                comprobado = False
            else:
                print("El número es demasiado grande o no es un número, intentelo de nuevo")
    def setN(self):
        comprobado = True
        while comprobado == True:
            N = input("Ingrese el Nombre: ")  # Nombre de la materia
            if len(N) < 40 and N.isalpha():
                self.__N=N
                comprobado = False
            else:
                print("El texto es demasiado grande o es un número, intentelo de nuevo")
    def setA(self):
        comprobado = True
        while comprobado == True:
            A = input("Ingrese el Apellido: ")  # Código facultad que la dicta
            if len(A) < 40 and A.isalpha():
                self.__A=A
                comprobado = False
            else:
                print("El texto es demasiado grande o es un número, intentelo de nuevo")

class Estudiante(Persona):
    def __init__(self):
        self.__CP = ""
        self.__CE = ""
        self.__PA = ""

    def getCP(self):
        return self.__CP
    def getCE(self):
        return self.__CE
    def getPA(self):
        return self.__PA


    def setCP(self):
        comprobado = True
        while comprobado == True:
            CP = input("Ingrese el Codigo del plan de estudio: ")  # Código departamento que la dicta
            if len(CP) < 14 and CP.isnumeric():
                self.__CP=CP
                comprobado = False
            else:
                print("El texto es demasiado grande o no es un número, intentelo de nuevo")
    def setCE(self):
        comprobado = True
        while comprobado == True:
            CE = input("Ingrese la calidad de estudiante (matriculado [M], graduado [G], perdida de cupo [P]): ")  # Cantidad de créditos
            if CE == "M" or CE == "G" or CE == "P":
                self.__CE=CE
                comprobado = False
            else:
                print("El texto es incorrecto, intentelo de nuevo")
    def setPA(self):
        comprobado = True
        Ed = False
        while comprobado == True:
            PA = input("Ingrese el PAPA actual: ")  # Código materia anterior obligatoria en el plan de estudios
            for a in PA:
                if a == "." or a == ",":
                    Ed = True
            if Ed:
                if len(PA) < 8 and int(PA[0]) < 5 or int(PA[0]) == 5 and int(PA[2]) == 0:
                    self.__PA = PA
                    comprobado = False
                else:
                    print("El texto es demasiado grande o el PAPA se pasa de lo establecido, intentelo de nuevo")
            else:
                if int(PA) < 5 and int(PA) > -1:
                    self.__PA = PA
                    comprobado = False
                else:
                    print("El texto es demasiado grande o el PAPA se pasa de lo establecido, intentelo de nuevo")

diccionario = Ui_SIA.Documentoiden()# + ";" + mi_estudiante.getN() + ";" + mi_estudiante.getA() + ";" + mi_estudiante.getCP() + ";" + mi_estudiante.getCE() + ";" + mi_estudiante.getPA()  # Creación del diccionario de la materia
print("diccionario")
