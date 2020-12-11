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

