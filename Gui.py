import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QGridLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
import ResoursesGUI_rc

class Inpalpe_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("INPALPE_Graficos.ui", self)
        self.setWindowTitle("INPALPE")
        
        self.Agregar.setEnabled(True)
        #self.NOMBRE_BOTON.clicked.connect(self.Fn_Activar) #conecta la funcion con el nombre del boton
        self.Agregar.clicked.connect(self.Fn_Activar_Agregar)
        #self.Agregar.clicked.connect(self.inicializacion)

        self.lineEntry = QLineEdit(self)
        self.qlabel = QLabel(self)

        self.lineEntry.textChanged.connect(self.onChanged)
        self.Actualizar.clicked.connect(self.Fn_Activar_Actualizar)
        self.Eliminar.clicked.connect(self.Fn_Activar_Eliminar)
        self.Mostrar_Lista.clicked.connect(self.Fn_Activar_ImprimirListaCompleta)
        self.Ordenar.clicked.connect(self.Fn_Activar_Ordenar)
        self.Almacenar.clicked.connect(self.Fn_Activar_Almacenar)
        self.Buscar_elemento.clicked.connect(self.Fn_Activar_Consulta_Elemento)
        self.Salir.clicked.connect(self.Fn_Activar_Salir)
    
       
    def Fn_Activar_Agregar(self):
        self.Agregar.setEnabled(True)
        self.Etiqueta.setText("Agregar")
        

    def Fn_Activar_Actualizar(self):
        self.Actualizar.setEnabled(True)
        self.Etiqueta.setText("Actualizar")

    def Fn_Activar_Eliminar(self):
        self.Eliminar.setEnabled(True)
        self.Etiqueta.setText("Eliminar")

    def Fn_Activar_ImprimirListaCompleta(self):
        self.Mostrar_Lista.setEnabled(True)
        self.Etiqueta.setText("Imprimir Lista Completa")

    def Fn_Activar_Ordenar(self):
        self.Ordenar.setEnabled(True)
        self.Etiqueta.setText("Ordenar")

    def Fn_Activar_Almacenar(self):
        self.Almacenar.setEnabled(True)
        self.Etiqueta.setText("Almacenar")

    def Fn_Activar_Consulta_Elemento(self):
        self.Buscar_elemento .setEnabled(True)
        self.Etiqueta.setText("Consulta Elemento")

    def Fn_Activar_Salir(self):
        self.Salir.setEnabled(True)
        self.Etiqueta.setText("Salir")

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    VentanaPrincipal = Inpalpe_GUI()
    VentanaPrincipal.show()
    sys.exit(app.exec_())
    
