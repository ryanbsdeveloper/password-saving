from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon
from UI import UI_janela_admin, UI_janela_inicial
import sys


class Admin(QMainWindow, UI_janela_admin.Ui_MainWindow):
    def __init__(self):
        super(Admin, self).__init__()
        super().setupUi(self)
        self.input_senha.setEchoMode(QLineEdit.Password)
        self.mostrarS.pressed.connect(self.view_senha)
        self.mostrarS.clicked.connect(self.block_senha)
        self.cadastrar.clicked.connect(self.btn_cadastrar)

        # add img
        self.cadastrar.setIcon(QIcon('..\\img\\entrar.png'))
        self.mostrarS.setIcon(QIcon('..\\img\\mostrarsenha.png'))
        self.imgS.setPixmap(QPixmap('..\\img\\cadiado.ico'))
        self.setWindowIcon(QIcon('..\\img\\icon2.ico'))

    def view_senha(self):
        return self.input_senha.setEchoMode(QLineEdit.Normal)

    def block_senha(self):
        return self.input_senha.setEchoMode(QLineEdit.Password)

    def btn_cadastrar(self):
        self.hide()


if __name__ == '__main__':
    go = QApplication(sys.argv)
    window = Admin()
    window.show()
    go.exec_()
