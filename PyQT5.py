import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QColorDialog, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QColor

class Interfaz(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        etiqueta = QLabel('Ingresa tu nombre:')
        self.campo_nombre = QLineEdit()
        

        boton_enviar = QPushButton('Enviar')
        boton_enviar.clicked.connect(self.mostrar_mensaje)
        boton_enviar.setFixedSize(100, 30)
        
        boton_cambiar_color = QPushButton('Cambiar Color')
        boton_cambiar_color.clicked.connect(self.cambiar_color)
        boton_cambiar_color.setFixedSize(120, 30)
        
        boton_color_aleatorio = QPushButton('Color Aleatorio')
        boton_color_aleatorio.clicked.connect(self.color_aleatorio)
        boton_color_aleatorio.setFixedSize(120, 30)
        
        # Crear un layout horizontal para los botones y espaciadores
        layout_botones = QHBoxLayout()
        espaciador_izquierdo = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        espaciador_derecho = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        layout_botones.addItem(espaciador_izquierdo)
        layout_botones.addWidget(boton_enviar)
        layout_botones.addWidget(boton_cambiar_color)
        layout_botones.addWidget(boton_color_aleatorio)
        layout_botones.addItem(espaciador_derecho)
        
        # Crear un layout vertical y agregar los widgets
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(etiqueta)
        layout_principal.addWidget(self.campo_nombre)
        layout_principal.addLayout(layout_botones)
        

        self.setLayout(layout_principal)
        

        self.setWindowTitle('Ingreso de Nombre')
        self.resize(400, 300)
        
        self.show()

    def mostrar_mensaje(self):
        nombre = self.campo_nombre.text()
        if nombre:
            QMessageBox.information(self, 'Mensaje', f'¡Hola, {nombre}!')
        else:
            QMessageBox.warning(self, 'Advertencia', 'Por favor, ingresa un nombre.')

    def cambiar_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f'background-color: {color.name()};')

    def color_aleatorio(self):
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.setStyleSheet(f'background-color: {color.name()};')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Interfaz()
    sys.exit(app.exec_())