import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon
from windows.UI import UI_janela_inicial, UI_janela_admin
from imports.BancoDeDados import BD_add_conta

cont = 0

class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_janela_inicial.Ui_Janela_login()
        self.ui.setupUi(self)
        # add imagens
        self.ui.btn_criar_2.setIcon(QIcon('img\\login.png'))
        self.ui.img_contas.setPixmap(QPixmap('img\\contas.png'))
        self.ui.img_criar.setPixmap(QPixmap('img\\add_contas.png'))
        self.setWindowIcon(QIcon('img\\icon_login.ico'))

        # btn cadastrar
        self.ui.btn_criar_2.clicked.connect(self.cadastro)

    def contas_salvas(self):
        pass


    def cadastro(self):
        if self.ui.input_nome_2.text().isnumeric() or self.ui.input_sobrenome_2.text().isnumeric() or len(
                self.ui.input_nome_2.text()) < 2 or len(self.ui.input_sobrenome_2.text()) < 2:
            self.ui.input_saida.setStyleSheet('color:red;font: 87 italic 10pt "Segoe UI Black";')
            self.ui.input_saida.setText('Cadastro invalído!')
        else:
            try:
                db.inserir_conta(self.ui.input_nome_2.text(), self.ui.input_sobrenome_2.text())
            except:
                self.ui.input_saida.setStyleSheet('color:yellow;font: 87 italic 10pt "Segoe UI Black";')
                self.ui.input_saida.setText('Conta já cadastrada!')
            else:
                self.cont += 1
                self.ui.input_saida.setStyleSheet('color:green;font: 87 italic 10pt "Segoe UI Black";')
                self.ui.input_saida.setText('Cadastro concluído!')

                # mostrando nome da conta
                nome_completo = f'{str(self.ui.input_nome_2.text()).capitalize()} {str(self.ui.input_sobrenome_2.text()).capitalize()}'
                if len(nome_completo) > 10:
                    nome_completo = f'{str(self.ui.input_nome_2.text()).capitalize()} {str(self.ui.input_sobrenome_2.text()).capitalize()[0]}'

                # limpando os campos de textos
                self.ui.input_nome_2.setText('')
                self.ui.input_sobrenome_2.setText('')

                if self.cont == 1:
                    # revelando o botões das contas
                    self.ui.btn_entrar_1.setEnabled(True)
                    self.ui.btn_apagar_1.setEnabled(True)
                    self.ui.nome_conta_1.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_1.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_1.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_1.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 2:
                    # revelando o botões das contas
                    self.ui.btn_entrar_2.setEnabled(True)
                    self.ui.btn_apagar_2.setEnabled(True)
                    self.ui.nome_conta_2.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_2.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_2.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_2.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 3:
                    # revelando o botões das contas
                    self.ui.btn_entrar_3.setEnabled(True)
                    self.ui.btn_apagar_3.setEnabled(True)
                    self.ui.nome_conta_3.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_3.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_3.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_3.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 4:
                    # revelando o botões das contas
                    self.ui.btn_entrar_4.setEnabled(True)
                    self.ui.btn_apagar_4.setEnabled(True)
                    self.ui.nome_conta_4.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_4.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_4.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_4.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 5:
                    # revelando o botões das contas
                    self.ui.btn_entrar_5.setEnabled(True)
                    self.ui.btn_apagar_5.setEnabled(True)
                    self.ui.nome_conta_5.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_5.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_5.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_5.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 6:
                    # revelando o botões das contas
                    self.ui.btn_entrar_6.setEnabled(True)
                    self.ui.btn_apagar_6.setEnabled(True)
                    self.ui.nome_conta_6.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_6.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_6.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_6.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 7:
                    # revelando o botões das contas
                    self.ui.btn_entrar_7.setEnabled(True)
                    self.ui.btn_apagar_7.setEnabled(True)
                    self.ui.nome_conta_7.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_7.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_7.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_7.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 8:
                    # revelando o botões das contas
                    self.ui.btn_entrar_8.setEnabled(True)
                    self.ui.btn_apagar_8.setEnabled(True)
                    self.ui.nome_conta_8.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_8.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_8.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_8.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 9:
                    # revelando o botões das contas
                    self.ui.btn_entrar_9.setEnabled(True)
                    self.ui.btn_apagar_9.setEnabled(True)
                    self.ui.nome_conta_9.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_9.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_9.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_9.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 10:
                    # revelando o botões das contas
                    self.ui.btn_entrar_10.setEnabled(True)
                    self.ui.btn_apagar_10.setEnabled(True)
                    self.ui.nome_conta_10.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_10.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_10.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_10.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 11:
                    # revelando o botões das contas
                    self.ui.btn_entrar_11.setEnabled(True)
                    self.ui.btn_apagar_11.setEnabled(True)
                    self.ui.nome_conta_11.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_11.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_11.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_11.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 12:
                    # revelando o botões das contas
                    self.ui.btn_entrar_12.setEnabled(True)
                    self.ui.btn_apagar_12.setEnabled(True)
                    self.ui.nome_conta_12.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_12.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_12.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_12.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 13:
                    # revelando o botões das contas
                    self.ui.btn_entrar_13.setEnabled(True)
                    self.ui.btn_apagar_13.setEnabled(True)
                    self.ui.nome_conta_13.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_13.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_13.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_13.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 14:
                    # revelando o botões das contas
                    self.ui.btn_entrar_14.setEnabled(True)
                    self.ui.btn_apagar_14.setEnabled(True)
                    self.ui.nome_conta_14.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_14.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_14.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_14.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 15:
                    # revelando o botões das contas
                    self.ui.btn_entrar_15.setEnabled(True)
                    self.ui.btn_apagar_15.setEnabled(True)
                    self.ui.nome_conta_15.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_15.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_15.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_15.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 16:
                    # revelando o botões das contas
                    self.ui.btn_entrar_16.setEnabled(True)
                    self.ui.btn_apagar_16.setEnabled(True)
                    self.ui.nome_conta_16.setText(nome_completo)

                    ######

                    # botoes

                    ######
                    self.ui.btn_entrar_16.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_16.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_16.setStyleSheet('background-color:#6c6c6c')


class TelaAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_janela_admin.Ui_Janela_admin()
        self.ui.setupUi(self)

        # btn mostrar senha
        self.ui.input_senha.setEchoMode(QLineEdit.Password)
        self.ui.mostrarS.pressed.connect(self.view_senha)
        self.ui.mostrarS.clicked.connect(self.block_senha)

        # add imagens
        self.ui.cadastrar.setIcon(QIcon('img\\entrar.png'))
        self.ui.mostrarS.setIcon(QIcon('img\\mostrarsenha.png'))
        self.ui.imgS.setPixmap(QPixmap('img\\cadiado.ico'))
        self.setWindowIcon(QIcon('img\\icon2.ico'))

    def view_senha(self):
        return self.ui.input_senha.setEchoMode(QLineEdit.Normal)

    def block_senha(self):
        return self.ui.input_senha.setEchoMode(QLineEdit.Password)


T = True


class JuntandoTelas:
    def __init__(self):
        # config window admin
        self.tela_admin = TelaAdmin()
        self.tela_admin.ui.cadastrar.clicked.connect(self.open_ini)

        # config window inicial
        self.tela_inicial = TelaInicial()

    def escrever_admin_bd(self):
        banco = BD_add_conta.BD()
        senha_atual = str(self.tela_admin.ui.input_senha.text())
        banco.inserir_admin(senha_atual)

    def open_ini(self):
        self.escrever_admin_bd()
        self.tela_inicial.show()
        self.tela_admin.close()


if __name__ == '__main__':
    go = QApplication(sys.argv)
    w = JuntandoTelas()
    db = BD_add_conta.BD()

    if db.verificar_admin():
        w.tela_inicial.show()
        go.exec_()
    else:
        w.tela_admin.show()
        go.exec_()
