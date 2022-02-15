from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys
from UI import UI_janela_inicial

class App(QMainWindow, UI_janela_inicial.Ui_Janela_login):
    def __init__(self):
        super(App, self).__init__()
        super().setupUi(self)
        self.setFixedSize(458, 336)
        self.btn_criar_2.clicked.connect(self.cadastro)

        # add img
        #self.fundo.setPixmap(QPixmap('img\\fundo.jpeg'))
        self.btn_criar_2.setIcon(QIcon('..\\img\\login.png'))

    def cadastro(self):
        if self.input_nome_2.text().isnumeric() or self.input_sobrenome_2.text().isnumeric() or len(
                self.input_nome_2.text()) < 2 or len(self.input_sobrenome_2.text()) < 2:
            self.input_saida.setStyleSheet('color:red;font: 87 italic 10pt "Segoe UI Black";')
            self.input_saida.setText('Nome ínvalido!')
        else:
            self.input_saida.setStyleSheet('color:green;font: 87 italic 10pt "Segoe UI Black";')
            self.input_saida.setText('Cadastro concluído!')


if __name__ == '__main__':
    go = QApplication(sys.argv)
    app = App()
    app.show()
    go.exec_()
