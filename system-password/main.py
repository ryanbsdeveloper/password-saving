import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from windows.UI import UI_janela_inicial, UI_janela_apagar, UI_janela_sites
from imports.BancoDeDados import BD_add_conta
from imports.modules import ctrlC, geraCriptografia


class TelaSites(QMainWindow):
    def __init__(self, NomeDaTabela=''):
        super(TelaSites, self).__init__()
        self.nomeDaTabela = NomeDaTabela
        self.ui = UI_janela_sites.Ui_janela_sites()
        self.ui.setupUi(self)
        self.cont = 1
        self.db = BD_add_conta.BD()
        self.db.nome_da_tabela = NomeDaTabela

        # fechando janelas
        self.ui.input.close()
        self.ui.registro_1.close()
        self.ui.registro_2.close()
        self.ui.registro_3.close()
        self.ui.registro_4.close()
        self.ui.registro_5.close()
        self.ui.registro_6.close()
        self.ui.registro_7.close()
        self.ui.registro_8.close()
        self.ui.registro_9.close()
        self.ui.registro_10.close()
        self.ui.registro_11.close()
        self.ui.registro_12.close()
        self.ui.registro_13.close()
        self.ui.registro_14.close()
        self.ui.registro_15.close()
        self.ui.registro_16.close()
        self.ui.registro_17.close()
        self.ui.registro_18.close()
        self.ui.registro_19.close()
        self.ui.registro_20.close()

        # add imagens
        self.setWindowIcon(QIcon('img\\icon2.ico'))
        self.ui.btn_voltar.setIcon(QIcon('img\\voltar'))
        self.ui.btn_fechar_input.setIcon(QIcon('img\\x.png'))
        self.ui.btn_fechar_input.setIcon(QIcon('img\\x.png'))
        self.ui.button_copiar_site_1.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_2.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_3.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_4.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_5.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_6.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_7.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_8.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_9.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_10.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_11.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_12.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_13.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_14.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_15.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_16.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_17.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_18.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_19.setIcon(QIcon('img\\copiar.png'))
        self.ui.button_copiar_site_20.setIcon(QIcon('img\\copiar.png'))

        # botões
        self.ui.btn_fechar_input.clicked.connect(self.ui.input.close)
        self.ui.btn_salvar_registro.clicked.connect(self.registrar)
        self.ui.btn_voltar.clicked.connect(self.close)


        # mostrando registros na GUI
        self.db.carregar_registros()
        for v in self.db.lista_registro:
            if self.cont == 1:
                self.ui.registro_1.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[0]['site']
                senha_na_bd = self.db.lista_registro[0]['senha']
                email_na_bd = self.db.lista_registro[0]['email']

                # excluindo registro
                self.ui.button_deletar_registro_1.clicked.connect(
                    self.apagar_registro_1)

                # mostra na tela
                self.ui.qual_site_1.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_1.setText(site_na_bd)
                self.ui.text_senha_1.setText(senha_na_bd)
                self.ui.text_email_1.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_1.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 2:
                self.ui.registro_2.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[1]['site']
                senha_na_bd = self.db.lista_registro[1]['senha']
                email_na_bd = self.db.lista_registro[1]['email']

                # excluindo registro
                self.ui.button_deletar_registro_2.clicked.connect(
                    self.apagar_registro_2)

                # mostra na tela
                self.ui.qual_site_2.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_2.setText(site_na_bd)
                self.ui.text_senha_2.setText(senha_na_bd)
                self.ui.text_email_2.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_2.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 3:
                self.ui.registro_3.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[2]['site']
                senha_na_bd = self.db.lista_registro[2]['senha']
                email_na_bd = self.db.lista_registro[2]['email']

                # excluindo registro
                self.ui.button_deletar_registro_3.clicked.connect(
                    self.apagar_registro_3)

                # mostra na tela
                self.ui.qual_site_3.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_3.setText(site_na_bd)
                self.ui.text_senha_3.setText(senha_na_bd)
                self.ui.text_email_3.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_3.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 4:
                self.ui.registro_4.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[3]['site']
                senha_na_bd = self.db.lista_registro[3]['senha']
                email_na_bd = self.db.lista_registro[3]['email']

                # excluindo registro
                self.ui.button_deletar_registro_4.clicked.connect(
                    self.apagar_registro_4)

                # mostra na tela
                self.ui.qual_site_4.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_4.setText(site_na_bd)
                self.ui.text_senha_4.setText(senha_na_bd)
                self.ui.text_email_4.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_4.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 5:
                self.ui.registro_5.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[4]['site']
                senha_na_bd = self.db.lista_registro[4]['senha']
                email_na_bd = self.db.lista_registro[4]['email']

                # excluindo registro
                self.ui.button_deletar_registro_5.clicked.connect(
                    self.apagar_registro_5)

                # mostra na tela
                self.ui.qual_site_5.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_5.setText(site_na_bd)
                self.ui.text_senha_5.setText(senha_na_bd)
                self.ui.text_email_5.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_5.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 6:
                self.ui.registro_6.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[5]['site']
                senha_na_bd = self.db.lista_registro[5]['senha']
                email_na_bd = self.db.lista_registro[5]['email']

                # excluindo registro
                self.ui.button_deletar_registro_6.clicked.connect(
                    self.apagar_registro_6)

                # mostra na tela
                self.ui.qual_site_6.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_6.setText(site_na_bd)
                self.ui.text_senha_6.setText(senha_na_bd)
                self.ui.text_email_6.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_6.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 7:
                self.ui.registro_7.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[6]['site']
                senha_na_bd = self.db.lista_registro[6]['senha']
                email_na_bd = self.db.lista_registro[6]['email']

                # excluindo registro
                self.ui.button_deletar_registro_7.clicked.connect(
                    self.apagar_registro_7)

                # mostra na tela
                self.ui.qual_site_7.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))
                self.ui.text_site_7.setText(site_na_bd)
                self.ui.text_senha_7.setText(senha_na_bd)
                self.ui.text_email_7.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_7.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 8:
                self.ui.registro_8.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[7]['site']
                senha_na_bd = self.db.lista_registro[7]['senha']
                email_na_bd = self.db.lista_registro[7]['email']

                # excluindo registro
                self.ui.button_deletar_registro_8.clicked.connect(
                    self.apagar_registro_8)

                # mostra na tela
                self.ui.qual_site_8.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_8.setText(site_na_bd)
                self.ui.text_senha_8.setText(senha_na_bd)
                self.ui.text_email_8.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_8.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 9:
                self.ui.registro_9.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[8]['site']
                senha_na_bd = self.db.lista_registro[8]['senha']
                email_na_bd = self.db.lista_registro[8]['email']

                # excluindo registro
                self.ui.button_deletar_registro_9.clicked.connect(
                    self.apagar_registro_9)

                # mostra na tela
                self.ui.qual_site_9.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_9.setText(site_na_bd)
                self.ui.text_senha_9.setText(senha_na_bd)
                self.ui.text_email_9.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_9.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 10:
                self.ui.registro_10.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[9]['site']
                senha_na_bd = self.db.lista_registro[9]['senha']
                email_na_bd = self.db.lista_registro[9]['email']

                # excluindo registro
                self.ui.button_deletar_registro_10.clicked.connect(
                    self.apagar_registro_10)

                # mostra na tela
                self.ui.qual_site_10.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_10.setText(site_na_bd)
                self.ui.text_senha_10.setText(senha_na_bd)
                self.ui.text_email_10.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_10.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 11:
                self.ui.registro_11.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[10]['site']
                senha_na_bd = self.db.lista_registro[10]['senha']
                email_na_bd = self.db.lista_registro[10]['email']

                # excluindo registro
                self.ui.button_deletar_registro_11.clicked.connect(
                    self.apagar_registro_11)

                # mostra na tela
                self.ui.qual_site_11.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_11.setText(site_na_bd)
                self.ui.text_senha_11.setText(senha_na_bd)
                self.ui.text_email_11.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_11.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 12:
                self.ui.registro_12.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[11]['site']
                senha_na_bd = self.db.lista_registro[11]['senha']
                email_na_bd = self.db.lista_registro[11]['email']

                # excluindo registro
                self.ui.button_deletar_registro_12.clicked.connect(
                    self.apagar_registro_12)

                # mostra na tela
                self.ui.qual_site_12.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_12.setText(site_na_bd)
                self.ui.text_senha_12.setText(senha_na_bd)
                self.ui.text_email_12.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_12.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 13:
                self.ui.registro_13.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[12]['site']
                senha_na_bd = self.db.lista_registro[12]['senha']
                email_na_bd = self.db.lista_registro[12]['email']

                # excluindo registro
                self.ui.button_deletar_registro_13.clicked.connect(
                    self.apagar_registro_13)

                # mostra na tela
                self.ui.qual_site_13.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_13.setText(site_na_bd)
                self.ui.text_senha_13.setText(senha_na_bd)
                self.ui.text_email_13.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_13.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 14:
                self.ui.registro_14.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[13]['site']
                senha_na_bd = self.db.lista_registro[13]['senha']
                email_na_bd = self.db.lista_registro[13]['email']

                # excluindo registro
                self.ui.button_deletar_registro_14.clicked.connect(
                    self.apagar_registro_14)

                # mostra na tela
                self.ui.qual_site_14.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_14.setText(site_na_bd)
                self.ui.text_senha_14.setText(senha_na_bd)
                self.ui.text_email_14.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_14.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 15:
                self.ui.registro_15.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[14]['site']
                senha_na_bd = self.db.lista_registro[14]['senha']
                email_na_bd = self.db.lista_registro[14]['email']

                # excluindo registro
                self.ui.button_deletar_registro_15.clicked.connect(
                    self.apagar_registro_15)

                # mostra na tela
                self.ui.qual_site_15.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_15.setText(site_na_bd)
                self.ui.text_senha_15.setText(senha_na_bd)
                self.ui.text_email_15.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_15.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 16:
                self.ui.registro_16.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[15]['site']
                senha_na_bd = self.db.lista_registro[15]['senha']
                email_na_bd = self.db.lista_registro[15]['email']

                # excluindo registro
                self.ui.button_deletar_registro_16.clicked.connect(
                    self.apagar_registro_16)

                # mostra na tela
                self.ui.qual_site_16.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_16.setText(site_na_bd)
                self.ui.text_senha_16.setText(senha_na_bd)
                self.ui.text_email_16.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_16.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 17:
                self.ui.registro_17.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[16]['site']
                senha_na_bd = self.db.lista_registro[16]['senha']
                email_na_bd = self.db.lista_registro[16]['email']

                # excluindo registro
                self.ui.button_deletar_registro_17.clicked.connect(
                    self.apagar_registro_17)

                # mostra na tela
                self.ui.qual_site_17.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_17.setText(site_na_bd)
                self.ui.text_senha_17.setText(senha_na_bd)
                self.ui.text_email_17.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_17.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 18:
                self.ui.registro_18.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[17]['site']
                senha_na_bd = self.db.lista_registro[17]['senha']
                email_na_bd = self.db.lista_registro[17]['email']

                # excluindo registro
                self.ui.button_deletar_registro_18.clicked.connect(
                    self.apagar_registro_18)

                # mostra na tela
                self.ui.qual_site_18.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_18.setText(site_na_bd)
                self.ui.text_senha_18.setText(senha_na_bd)
                self.ui.text_email_18.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_18.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 19:
                self.ui.registro_19.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[18]['site']
                senha_na_bd = self.db.lista_registro[18]['senha']
                email_na_bd = self.db.lista_registro[18]['email']

                # excluindo registro
                self.ui.button_deletar_registro_19.clicked.connect(
                    self.apagar_registro_19)

                # mostra na tela
                self.ui.qual_site_19.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_19.setText(site_na_bd)
                self.ui.text_senha_19.setText(senha_na_bd)
                self.ui.text_email_19.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_19.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            elif self.cont == 20:
                self.ui.registro_20.show()
                self.db.nome_da_tabela = self.nomeDaTabela

                # dados na bd
                self.db.carregar_registros()
                site_na_bd = self.db.lista_registro[19]['site']
                senha_na_bd = self.db.lista_registro[19]['senha']
                email_na_bd = self.db.lista_registro[19]['email']

                # excluindo registro
                self.ui.button_deletar_registro_20.clicked.connect(
                    self.apagar_registro_20)

                # mostra na tela
                self.ui.qual_site_20.setPixmap(
                    QPixmap(self.set_icon(site_na_bd)))

                self.ui.text_site_20.setText(site_na_bd)
                self.ui.text_senha_20.setText(senha_na_bd)
                self.ui.text_email_20.setText(email_na_bd)

                # botao copiar
                self.ui.button_copiar_site_20.clicked.connect(
                    lambda: ctrlC.CtrlC(senha_na_bd))

            self.cont += 1

    def registrar(self):
        site = self.ui.input_site.text()
        senha = self.ui.input_senha.text().replace(' ', '')
        email = self.ui.input_email.text().replace(' ', '')

        if site == '' and senha == '':
            self.ui.input.show()
            # estilo
            self.ui.input.setStyleSheet(
                'color: rgb(255, 88, 88);border-radius:15px;background-color: rgb(34, 34, 34);')

            self.ui.input_texto.setText('Site e senha inválidos!')
            self.ui.verifica_site.setPixmap(QPixmap('img\\erro.png'))
            self.ui.verifica_senha.setPixmap(QPixmap('img\\erro.png'))

            self.ui.input_site.setStyleSheet("QLineEdit{\n"
                                             "    color: white;\n"
                                             "    background-color:rgb(31, 31, 31);\n"
                                             "    border-radius:10px;\n"
                                             "    border: 2px solid rgb(255, 88, 88);\n"
                                             "    padding: 1px 15px\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:hover{\n"
                                             "    color: rgb(135, 135, 135);\n"
                                             "    border: 2px solid white;\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus{\n"
                                             "    border: 2px solid rgb(85, 85, 255);\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "}")
            self.ui.input_senha.setStyleSheet("QLineEdit{\n"
                                              "    color: white;\n"
                                              "    background-color:rgb(31, 31, 31);\n"
                                              "    border-radius:10px;\n"
                                              "    border: 2px solid rgb(255, 88, 88);\n"
                                              "    padding: 1px 15px\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:hover{\n"
                                              "    color: rgb(135, 135, 135);\n"
                                              "    border: 2px solid white;\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:focus{\n"
                                              "    border: 2px solid rgb(85, 85, 255);\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "}")

        elif site == '':
            self.ui.input_senha.setStyleSheet("QLineEdit{\n"
                                              "    color: white;\n"
                                              "    background-color:rgb(31, 31, 31);\n"
                                              "    border-radius:10px;\n"
                                              "    border: 2px solid;\n"
                                              "    padding: 1px 15px\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:hover{\n"
                                              "    color: rgb(135, 135, 135);\n"
                                              "    border: 2px solid white;\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:focus{\n"
                                              "    border: 2px solid rgb(85, 85, 255);\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "}")

            # estilo
            self.ui.input.setStyleSheet(
                'color:rgb(255, 88, 88);border-radius:15px;background-color: rgb(34, 34, 34);')
            self.ui.input_site.setStyleSheet("QLineEdit{\n"
                                             "    color: white;\n"
                                             "    background-color:rgb(31, 31, 31);\n"
                                             "    border-radius:10px;\n"
                                             "    border: 2px solid rgb(255, 88, 88);\n"
                                             "    padding: 1px 15px\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:hover{\n"
                                             "    color: rgb(135, 135, 135);\n"
                                             "    border: 2px solid white;\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus{\n"
                                             "    border: 2px solid rgb(85, 85, 255);\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "}")

            self.ui.input.show()
            self.ui.input_texto.setText('Site invalido!')
            self.ui.verifica_site.setPixmap(QPixmap('img\\erro.png'))

        elif senha == '':
            self.ui.input_site.setStyleSheet("QLineEdit{\n"
                                             "    color: white;\n"
                                             "    background-color:rgb(31, 31, 31);\n"
                                             "    border-radius:10px;\n"
                                             "    border: 2px solid;\n"
                                             "    padding: 1px 15px\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:hover{\n"
                                             "    color: rgb(135, 135, 135);\n"
                                             "    border: 2px solid white;\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus{\n"
                                             "    border: 2px solid rgb(85, 85, 255);\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "}")
            self.ui.verifica_site.setPixmap(QPixmap('img\\valido.png'))

            # estilo
            self.ui.input.setStyleSheet(
                'color: rgb(255, 88, 88);border-radius:15px;background-color: rgb(34, 34, 34);')
            self.ui.input_senha.setStyleSheet("QLineEdit{\n"
                                              "    color: white;\n"
                                              "    background-color:rgb(31, 31, 31);\n"
                                              "    border-radius:10px;\n"
                                              "    border: 2px solid rgb(255, 88, 88);\n"
                                              "    padding: 1px 15px\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:hover{\n"
                                              "    color: rgb(135, 135, 135);\n"
                                              "    border: 2px solid white;\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:focus{\n"
                                              "    border: 2px solid rgb(85, 85, 255);\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "}")

            self.ui.input.show()
            self.ui.input_texto.setText('Senha invalída!')
            self.ui.verifica_senha.setPixmap(QPixmap('img\\erro.png'))

        elif len(senha) < 4:
            self.ui.verifica_site.setPixmap(QPixmap('img\\valido.png'))
            self.ui.input_site.setStyleSheet("QLineEdit{\n"
                                             "    color: white;\n"
                                             "    background-color:rgb(31, 31, 31);\n"
                                             "    border-radius:10px;\n"
                                             "    border: 2px solid;\n"
                                             "    padding: 1px 15px\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:hover{\n"
                                             "    color: rgb(135, 135, 135);\n"
                                             "    border: 2px solid white;\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus{\n"
                                             "    border: 2px solid rgb(85, 85, 255);\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "}")

            # estilo
            self.ui.input.setStyleSheet(
                "color: rgb(255, 255, 127);border-radius:15px;background-color: rgb(34, 34, 34);")
            self.ui.input_senha.setStyleSheet("QLineEdit{\n"
                                              "    color: white;\n"
                                              "    background-color:rgb(31, 31, 31);\n"
                                              "    border-radius:10px;\n"
                                              "    border: 2px solid rgb(255, 255, 127);\n"
                                              "    padding: 1px 15px\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:hover{\n"
                                              "    color: rgb(135, 135, 135);\n"
                                              "    border: 2px solid white;\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:focus{\n"
                                              "    border: 2px solid rgb(85, 85, 255);\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "}")

            self.ui.input.show()
            self.ui.input_texto.setText('Senha Fraca!')
            self.ui.verifica_senha.setPixmap(QPixmap('img\\perigo.png'))

        else:
            self.ui.verifica_site.setPixmap(QPixmap('img\\valido.png'))
            self.ui.verifica_senha.setPixmap(QPixmap('img\\valido.png'))
            # registro adicionado

            self.ui.input_site.setStyleSheet("QLineEdit{\n"
                                             "    color: white;\n"
                                             "    background-color:rgb(31, 31, 31);\n"
                                             "    border-radius:10px;\n"
                                             "    border: 2px solid;\n"
                                             "    padding: 1px 15px\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:hover{\n"
                                             "    color: rgb(135, 135, 135);\n"
                                             "    border: 2px solid white;\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus{\n"
                                             "    border: 2px solid rgb(85, 85, 255);\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "}")
            self.ui.input_senha.setStyleSheet("QLineEdit{\n"
                                              "    color: white;\n"
                                              "    background-color:rgb(31, 31, 31);\n"
                                              "    border-radius:10px;\n"
                                              "    border: 2px solid;\n"
                                              "    padding: 1px 15px\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:hover{\n"
                                              "    color: rgb(135, 135, 135);\n"
                                              "    border: 2px solid white;\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:focus{\n"
                                              "    border: 2px solid rgb(85, 85, 255);\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "}")

            if email:
                if '.com' not in email:
                    self.ui.input.show()
                    # estilo
                    self.ui.input.setStyleSheet(
                        'color: rgb(255, 88, 88);border-radius:15px;background-color: rgb(34, 34, 34);')
                    self.ui.input_email.setStyleSheet("QLineEdit{\n"
                                                      "    color: white;\n"
                                                      "    background-color:rgb(115, 115, 115);\n"
                                                      "    border-radius:10px;\n"
                                                      "    border: 2px solid rgb(255, 88, 88);\n"
                                                      "    padding: 1px 15px\n"
                                                      "}\n"
                                                      "\n"
                                                      "QLineEdit:hover{\n"
                                                      "    color: rgb(135, 135, 135);\n"
                                                      "    border: 2px solid white;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QLineEdit:focus{\n"
                                                      "    border: 2px solid rgb(85, 85, 255);\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "}")

                    self.ui.input_texto.setText('E-mail invalído!')
                    self.ui.verifica_email.setPixmap(QPixmap('img\\erro.png'))

                else:
                    # limpando os inputs
                    self.ui.input_email.setText('')
                    self.ui.input_site.setText('')
                    self.ui.input_senha.setText('')

                    # estilos
                    self.ui.input_texto.setText('Registro adicionado!')
                    self.ui.input.setStyleSheet(
                        'color:rgb(110, 255, 94);border-radius:15px;background-color: rgb(34, 34, 34);')
                    self.ui.input.show()

                    self.ui.input_email.setStyleSheet("QLineEdit{\n"
                                                      "    color: white;\n"
                                                      "    background-color:rgb(31, 31, 31);\n"
                                                      "    border-radius:10px;\n"
                                                      "    border: 2px solid;\n"
                                                      "    padding: 1px 15px\n"
                                                      "}\n"
                                                      "\n"
                                                      "QLineEdit:hover{\n"
                                                      "    color: rgb(135, 135, 135);\n"
                                                      "    border: 2px solid white;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QLineEdit:focus{\n"
                                                      "    border: 2px solid rgb(85, 85, 255);\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "}")
                    self.ui.input_senha.setStyleSheet("QLineEdit{\n"
                                                      "    color: white;\n"
                                                      "    background-color:rgb(31, 31, 31);\n"
                                                      "    border-radius:10px;\n"
                                                      "    border: 2px solid;\n"
                                                      "    padding: 1px 15px\n"
                                                      "}\n"
                                                      "\n"
                                                      "QLineEdit:hover{\n"
                                                      "    color: rgb(135, 135, 135);\n"
                                                      "    border: 2px solid white;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QLineEdit:focus{\n"
                                                      "    border: 2px solid rgb(85, 85, 255);\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "}")
                    self.ui.input_site.setStyleSheet("QLineEdit{\n"
                                                     "    color: white;\n"
                                                     "    background-color:rgb(31, 31, 31);\n"
                                                     "    border-radius:10px;\n"
                                                     "    border: 2px solid;\n"
                                                     "    padding: 1px 15px\n"
                                                     "}\n"
                                                     "\n"
                                                     "QLineEdit:hover{\n"
                                                     "    color: rgb(135, 135, 135);\n"
                                                     "    border: 2px solid white;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QLineEdit:focus{\n"
                                                     "    border: 2px solid rgb(85, 85, 255);\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "}")

                    self.ui.verifica_email.setPixmap(
                        QPixmap('img\\valido.png'))

                    if self.cont == 1:
                        self.ui.registro_1.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_1.clicked.connect(
                            self.apagar_registro_1)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[0]['site']
                        senha_na_bd = self.db.lista_registro[0]['senha']
                        email_na_bd = self.db.lista_registro[0]['email']

                        self.ui.qual_site_1.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_1.setText(site_na_bd)
                        self.ui.text_senha_1.setText(senha_na_bd)
                        self.ui.text_email_1.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_1.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 2:
                        self.ui.registro_2.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_2.clicked.connect(
                            self.apagar_registro_2)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[1]['site']
                        senha_na_bd = self.db.lista_registro[1]['senha']
                        email_na_bd = self.db.lista_registro[1]['email']

                        self.ui.qual_site_2.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_2.setText(site_na_bd)
                        self.ui.text_senha_2.setText(senha_na_bd)
                        self.ui.text_email_2.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_2.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 3:
                        self.ui.registro_3.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_3.clicked.connect(
                            self.apagar_registro_3)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[2]['site']
                        senha_na_bd = self.db.lista_registro[2]['senha']
                        email_na_bd = self.db.lista_registro[2]['email']

                        self.ui.qual_site_3.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_3.setText(site_na_bd)
                        self.ui.text_senha_3.setText(senha_na_bd)
                        self.ui.text_email_3.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_3.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 4:
                        self.ui.registro_4.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_4.clicked.connect(
                            self.apagar_registro_4)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[3]['site']
                        senha_na_bd = self.db.lista_registro[3]['senha']
                        email_na_bd = self.db.lista_registro[3]['email']

                        self.ui.qual_site_4.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_4.setText(site_na_bd)
                        self.ui.text_senha_4.setText(senha_na_bd)
                        self.ui.text_email_4.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_4.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 5:
                        self.ui.registro_5.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_5.clicked.connect(
                            self.apagar_registro_5)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[4]['site']
                        senha_na_bd = self.db.lista_registro[4]['senha']
                        email_na_bd = self.db.lista_registro[4]['email']

                        self.ui.qual_site_5.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_5.setText(site_na_bd)
                        self.ui.text_senha_5.setText(senha_na_bd)
                        self.ui.text_email_5.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_5.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 6:
                        self.ui.registro_6.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_6.clicked.connect(
                            self.apagar_registro_6)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[5]['site']
                        senha_na_bd = self.db.lista_registro[5]['senha']
                        email_na_bd = self.db.lista_registro[5]['email']

                        self.ui.qual_site_6.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_6.setText(site_na_bd)
                        self.ui.text_senha_6.setText(senha_na_bd)
                        self.ui.text_email_6.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_6.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 7:
                        self.ui.registro_7.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_7.clicked.connect(
                            self.apagar_registro_7)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[6]['site']
                        senha_na_bd = self.db.lista_registro[6]['senha']
                        email_na_bd = self.db.lista_registro[6]['email']

                        self.ui.qual_site_7.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_7.setText(site_na_bd)
                        self.ui.text_senha_7.setText(senha_na_bd)
                        self.ui.text_email_7.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_7.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 8:
                        self.ui.registro_8.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_8.clicked.connect(
                            self.apagar_registro_8)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[7]['site']
                        senha_na_bd = self.db.lista_registro[7]['senha']
                        email_na_bd = self.db.lista_registro[7]['email']

                        self.ui.qual_site_8.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_8.setText(site_na_bd)
                        self.ui.text_senha_8.setText(senha_na_bd)
                        self.ui.text_email_8.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_8.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 9:
                        self.ui.registro_9.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_9.clicked.connect(
                            self.apagar_registro_9)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[8]['site']
                        senha_na_bd = self.db.lista_registro[8]['senha']
                        email_na_bd = self.db.lista_registro[8]['email']

                        self.ui.qual_site_9.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_9.setText(site_na_bd)
                        self.ui.text_senha_9.setText(senha_na_bd)
                        self.ui.text_email_9.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_9.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 10:
                        self.ui.registro_10.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_10.clicked.connect(
                            self.apagar_registro_10)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[9]['site']
                        senha_na_bd = self.db.lista_registro[9]['senha']
                        email_na_bd = self.db.lista_registro[9]['email']

                        self.ui.qual_site_10.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_10.setText(site_na_bd)
                        self.ui.text_senha_10.setText(senha_na_bd)
                        self.ui.text_email_10.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_10.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 11:
                        self.ui.registro_11.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_11.clicked.connect(
                            self.apagar_registro_11)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[10]['site']
                        senha_na_bd = self.db.lista_registro[10]['senha']
                        email_na_bd = self.db.lista_registro[10]['email']

                        self.ui.qual_site_11.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_11.setText(site_na_bd)
                        self.ui.text_senha_11.setText(senha_na_bd)
                        self.ui.text_email_11.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_11.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 12:
                        self.ui.registro_12.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_12.clicked.connect(
                            self.apagar_registro_12)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[11]['site']
                        senha_na_bd = self.db.lista_registro[11]['senha']
                        email_na_bd = self.db.lista_registro[11]['email']

                        self.ui.qual_site_12.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_12.setText(site_na_bd)
                        self.ui.text_senha_12.setText(senha_na_bd)
                        self.ui.text_email_12.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_12.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 13:
                        self.ui.registro_13.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_13.clicked.connect(
                            self.apagar_registro_13)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[12]['site']
                        senha_na_bd = self.db.lista_registro[12]['senha']
                        email_na_bd = self.db.lista_registro[12]['email']

                        self.ui.qual_site_13.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_13.setText(site_na_bd)
                        self.ui.text_senha_13.setText(senha_na_bd)
                        self.ui.text_email_13.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_13.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 14:
                        self.ui.registro_14.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_14.clicked.connect(
                            self.apagar_registro_14)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[13]['site']
                        senha_na_bd = self.db.lista_registro[13]['senha']
                        email_na_bd = self.db.lista_registro[13]['email']

                        self.ui.qual_site_14.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_14.setText(site_na_bd)
                        self.ui.text_senha_14.setText(senha_na_bd)
                        self.ui.text_email_14.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_14.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 15:
                        self.ui.registro_15.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_15.clicked.connect(
                            self.apagar_registro_15)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[14]['site']
                        senha_na_bd = self.db.lista_registro[14]['senha']
                        email_na_bd = self.db.lista_registro[14]['email']

                        self.ui.qual_site_15.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_15.setText(site_na_bd)
                        self.ui.text_senha_15.setText(senha_na_bd)
                        self.ui.text_email_15.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_15.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 16:
                        self.ui.registro_16.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_16.clicked.connect(
                            self.apagar_registro_16)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[15]['site']
                        senha_na_bd = self.db.lista_registro[15]['senha']
                        email_na_bd = self.db.lista_registro[15]['email']

                        self.ui.qual_site_16.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_16.setText(site_na_bd)
                        self.ui.text_senha_16.setText(senha_na_bd)
                        self.ui.text_email_16.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_16.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 17:
                        self.ui.registro_17.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_17.clicked.connect(
                            self.apagar_registro_17)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[16]['site']
                        senha_na_bd = self.db.lista_registro[16]['senha']
                        email_na_bd = self.db.lista_registro[16]['email']

                        self.ui.qual_site_17.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_17.setText(site_na_bd)
                        self.ui.text_senha_17.setText(senha_na_bd)
                        self.ui.text_email_17.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_17.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 18:
                        self.ui.registro_18.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_18.clicked.connect(
                            self.apagar_registro_18)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[17]['site']
                        senha_na_bd = self.db.lista_registro[17]['senha']
                        email_na_bd = self.db.lista_registro[17]['email']

                        self.ui.qual_site_18.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_18.setText(site_na_bd)
                        self.ui.text_senha_18.setText(senha_na_bd)
                        self.ui.text_email_18.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_18.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 19:
                        self.ui.registro_19.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_19.clicked.connect(
                            self.apagar_registro_19)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[18]['site']
                        senha_na_bd = self.db.lista_registro[18]['senha']
                        email_na_bd = self.db.lista_registro[18]['email']

                        self.ui.qual_site_19.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_19.setText(site_na_bd)
                        self.ui.text_senha_19.setText(senha_na_bd)
                        self.ui.text_email_19.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_19.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    elif self.cont == 20:
                        self.ui.registro_20.show()
                        self.db.nome_da_tabela = self.nomeDaTabela

                        # adicionando
                        self.db.inserir_registro(site, senha, email)

                        # excluindo registro
                        self.ui.button_deletar_registro_20.clicked.connect(
                            self.apagar_registro_20)

                        # mostra na tela
                        self.db.carregar_registros()
                        site_na_bd = self.db.lista_registro[19]['site']
                        senha_na_bd = self.db.lista_registro[19]['senha']
                        email_na_bd = self.db.lista_registro[19]['email']

                        self.ui.qual_site_20.setPixmap(
                            QPixmap(self.set_icon(site_na_bd)))

                        self.ui.text_site_20.setText(site_na_bd)
                        self.ui.text_senha_20.setText(senha_na_bd)
                        self.ui.text_email_20.setText(email_na_bd)

                        # botao copiar
                        self.ui.button_copiar_site_20.clicked.connect(
                            lambda: ctrlC.CtrlC(senha_na_bd))

                    else:
                        self.ui.input.show()
                        self.ui.input_texto
                    self.cont += 1

            else:
                self.ui.verifica_email.setPixmap(QPixmap(''))

                # limpando os inputs
                self.ui.input_email.setText('')
                self.ui.input_site.setText('')
                self.ui.input_senha.setText('')

                # estilos
                self.ui.input_texto.setText('Registro adicionado!')
                self.ui.input.setStyleSheet(
                    'color:rgb(110, 255, 94);border-radius:15px;background-color: rgb(34, 34, 34);')
                self.ui.input.show()
                self.ui.input_email.setStyleSheet("QLineEdit{\n"
                                                  "    color: white;\n"
                                                  "    background-color:rgb(31, 31, 31);\n"
                                                  "    border-radius:10px;\n"
                                                  "    border: 2px solid;\n"
                                                  "    padding: 1px 15px\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLineEdit:hover{\n"
                                                  "    color: rgb(135, 135, 135);\n"
                                                  "    border: 2px solid white;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLineEdit:focus{\n"
                                                  "    border: 2px solid rgb(85, 85, 255);\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "}")
                self.ui.input_senha.setStyleSheet("QLineEdit{\n"
                                                  "    color: white;\n"
                                                  "    background-color:rgb(31, 31, 31);\n"
                                                  "    border-radius:10px;\n"
                                                  "    border: 2px solid;\n"
                                                  "    padding: 1px 15px\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLineEdit:hover{\n"
                                                  "    color: rgb(135, 135, 135);\n"
                                                  "    border: 2px solid white;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QLineEdit:focus{\n"
                                                  "    border: 2px solid rgb(85, 85, 255);\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "}")
                self.ui.input_site.setStyleSheet("QLineEdit{\n"
                                                 "    color: white;\n"
                                                 "    background-color:rgb(31, 31, 31);\n"
                                                 "    border-radius:10px;\n"
                                                 "    border: 2px solid;\n"
                                                 "    padding: 1px 15px\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:hover{\n"
                                                 "    color: rgb(135, 135, 135);\n"
                                                 "    border: 2px solid white;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:focus{\n"
                                                 "    border: 2px solid rgb(85, 85, 255);\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "}")

                if self.cont == 1:
                    self.ui.registro_1.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_1.clicked.connect(
                        self.apagar_registro_1)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[0]['site']
                    senha_na_bd = self.db.lista_registro[0]['senha']
                    email_na_bd = self.db.lista_registro[0]['email']

                    self.ui.qual_site_1.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_1.setText(site_na_bd)
                    self.ui.text_senha_1.setText(senha_na_bd)
                    self.ui.text_email_1.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_1.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 2:
                    self.ui.registro_2.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_2.clicked.connect(
                        self.apagar_registro_2)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[1]['site']
                    senha_na_bd = self.db.lista_registro[1]['senha']
                    email_na_bd = self.db.lista_registro[1]['email']

                    self.ui.qual_site_2.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_2.setText(site_na_bd)
                    self.ui.text_senha_2.setText(senha_na_bd)
                    self.ui.text_email_2.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_2.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 3:
                    self.ui.registro_3.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_3.clicked.connect(
                        self.apagar_registro_3)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[2]['site']
                    senha_na_bd = self.db.lista_registro[2]['senha']
                    email_na_bd = self.db.lista_registro[2]['email']

                    self.ui.qual_site_3.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_3.setText(site_na_bd)
                    self.ui.text_senha_3.setText(senha_na_bd)
                    self.ui.text_email_3.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_3.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 4:
                    self.ui.registro_4.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_4.clicked.connect(
                        self.apagar_registro_4)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[3]['site']
                    senha_na_bd = self.db.lista_registro[3]['senha']
                    email_na_bd = self.db.lista_registro[3]['email']

                    self.ui.qual_site_4.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_4.setText(site_na_bd)
                    self.ui.text_senha_4.setText(senha_na_bd)
                    self.ui.text_email_4.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_4.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 5:
                    self.ui.registro_5.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_5.clicked.connect(
                        self.apagar_registro_5)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[4]['site']
                    senha_na_bd = self.db.lista_registro[4]['senha']
                    email_na_bd = self.db.lista_registro[4]['email']

                    self.ui.qual_site_5.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_5.setText(site_na_bd)
                    self.ui.text_senha_5.setText(senha_na_bd)
                    self.ui.text_email_5.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_5.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 6:
                    self.ui.registro_6.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_6.clicked.connect(
                        self.apagar_registro_6)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[5]['site']
                    senha_na_bd = self.db.lista_registro[5]['senha']
                    email_na_bd = self.db.lista_registro[5]['email']

                    self.ui.qual_site_6.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_6.setText(site_na_bd)
                    self.ui.text_senha_6.setText(senha_na_bd)
                    self.ui.text_email_6.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_6.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 7:
                    self.ui.registro_7.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_7.clicked.connect(
                        self.apagar_registro_7)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[6]['site']
                    senha_na_bd = self.db.lista_registro[6]['senha']
                    email_na_bd = self.db.lista_registro[6]['email']

                    self.ui.qual_site_7.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_7.setText(site_na_bd)
                    self.ui.text_senha_7.setText(senha_na_bd)
                    self.ui.text_email_7.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_7.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 8:
                    self.ui.registro_8.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_8.clicked.connect(
                        self.apagar_registro_8)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[7]['site']
                    senha_na_bd = self.db.lista_registro[7]['senha']
                    email_na_bd = self.db.lista_registro[7]['email']

                    self.ui.qual_site_8.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_8.setText(site_na_bd)
                    self.ui.text_senha_8.setText(senha_na_bd)
                    self.ui.text_email_8.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_8.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 9:
                    self.ui.registro_9.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_9.clicked.connect(
                        self.apagar_registro_9)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[8]['site']
                    senha_na_bd = self.db.lista_registro[8]['senha']
                    email_na_bd = self.db.lista_registro[8]['email']

                    self.ui.qual_site_9.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_9.setText(site_na_bd)
                    self.ui.text_senha_9.setText(senha_na_bd)
                    self.ui.text_email_9.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_9.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 10:
                    self.ui.registro_10.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_10.clicked.connect(
                        self.apagar_registro_10)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[9]['site']
                    senha_na_bd = self.db.lista_registro[9]['senha']
                    email_na_bd = self.db.lista_registro[9]['email']

                    self.ui.qual_site_10.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_10.setText(site_na_bd)
                    self.ui.text_senha_10.setText(senha_na_bd)
                    self.ui.text_email_10.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_10.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 11:
                    self.ui.registro_11.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_11.clicked.connect(
                        self.apagar_registro_11)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[10]['site']
                    senha_na_bd = self.db.lista_registro[10]['senha']
                    email_na_bd = self.db.lista_registro[10]['email']

                    self.ui.qual_site_11.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_11.setText(site_na_bd)
                    self.ui.text_senha_11.setText(senha_na_bd)
                    self.ui.text_email_11.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_11.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 12:
                    self.ui.registro_12.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_12.clicked.connect(
                        self.apagar_registro_12)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[11]['site']
                    senha_na_bd = self.db.lista_registro[11]['senha']
                    email_na_bd = self.db.lista_registro[11]['email']

                    self.ui.qual_site_12.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_12.setText(site_na_bd)
                    self.ui.text_senha_12.setText(senha_na_bd)
                    self.ui.text_email_12.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_12.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 13:
                    self.ui.registro_13.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_13.clicked.connect(
                        self.apagar_registro_13)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[12]['site']
                    senha_na_bd = self.db.lista_registro[12]['senha']
                    email_na_bd = self.db.lista_registro[12]['email']

                    self.ui.qual_site_13.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_13.setText(site_na_bd)
                    self.ui.text_senha_13.setText(senha_na_bd)
                    self.ui.text_email_13.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_13.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 14:
                    self.ui.registro_14.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_14.clicked.connect(
                        self.apagar_registro_14)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[13]['site']
                    senha_na_bd = self.db.lista_registro[13]['senha']
                    email_na_bd = self.db.lista_registro[13]['email']

                    self.ui.qual_site_14.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_14.setText(site_na_bd)
                    self.ui.text_senha_14.setText(senha_na_bd)
                    self.ui.text_email_14.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_14.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 15:
                    self.ui.registro_15.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_15.clicked.connect(
                        self.apagar_registro_15)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[14]['site']
                    senha_na_bd = self.db.lista_registro[14]['senha']
                    email_na_bd = self.db.lista_registro[14]['email']

                    self.ui.qual_site_15.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_15.setText(site_na_bd)
                    self.ui.text_senha_15.setText(senha_na_bd)
                    self.ui.text_email_15.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_15.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 16:
                    self.ui.registro_16.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_16.clicked.connect(
                        self.apagar_registro_16)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[15]['site']
                    senha_na_bd = self.db.lista_registro[15]['senha']
                    email_na_bd = self.db.lista_registro[15]['email']

                    self.ui.qual_site_16.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_16.setText(site_na_bd)
                    self.ui.text_senha_16.setText(senha_na_bd)
                    self.ui.text_email_16.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_16.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 17:
                    self.ui.registro_17.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_17.clicked.connect(
                        self.apagar_registro_17)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[16]['site']
                    senha_na_bd = self.db.lista_registro[16]['senha']
                    email_na_bd = self.db.lista_registro[16]['email']

                    self.ui.qual_site_17.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_17.setText(site_na_bd)
                    self.ui.text_senha_17.setText(senha_na_bd)
                    self.ui.text_email_17.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_17.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 18:
                    self.ui.registro_18.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_18.clicked.connect(
                        self.apagar_registro_18)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[17]['site']
                    senha_na_bd = self.db.lista_registro[17]['senha']
                    email_na_bd = self.db.lista_registro[17]['email']

                    self.ui.qual_site_18.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_18.setText(site_na_bd)
                    self.ui.text_senha_18.setText(senha_na_bd)
                    self.ui.text_email_18.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_18.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 19:
                    self.ui.registro_19.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_19.clicked.connect(
                        self.apagar_registro_19)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[18]['site']
                    senha_na_bd = self.db.lista_registro[18]['senha']
                    email_na_bd = self.db.lista_registro[18]['email']

                    self.ui.qual_site_19.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_19.setText(site_na_bd)
                    self.ui.text_senha_19.setText(senha_na_bd)
                    self.ui.text_email_19.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_19.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))

                elif self.cont == 20:
                    self.ui.registro_20.show()
                    self.db.nome_da_tabela = self.nomeDaTabela

                    # adicionando
                    self.db.inserir_registro(site, senha, email)

                    # excluindo registro
                    self.ui.button_deletar_registro_20.clicked.connect(
                        self.apagar_registro_20)

                    # mostra na tela
                    self.db.carregar_registros()
                    site_na_bd = self.db.lista_registro[19]['site']
                    senha_na_bd = self.db.lista_registro[19]['senha']
                    email_na_bd = self.db.lista_registro[19]['email']

                    self.ui.qual_site_20.setPixmap(
                        QPixmap(self.set_icon(site_na_bd)))

                    self.ui.text_site_20.setText(site_na_bd)
                    self.ui.text_senha_20.setText(senha_na_bd)
                    self.ui.text_email_20.setText(email_na_bd)

                    # botao copiar
                    self.ui.button_copiar_site_20.clicked.connect(
                        lambda: ctrlC.CtrlC(senha_na_bd))
                else:
                    self.ui.input.show()
                    self.ui.input_texto.setStyleSheet('color:red;')
                    self.ui.input_texto.setText(
                        'Limite alcançado, exclua um e reinicie o app')

                self.cont += 1

    def apagar_registro_1(self):
        self.ui.registro_1.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[0]['id']
        self.db.excluir_registro(id)

    def apagar_registro_2(self):
        self.ui.registro_2.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[1]['id']
        self.db.excluir_registro(id)

    def apagar_registro_3(self):
        self.ui.registro_3.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[2]['id']
        self.db.excluir_registro(id)

    def apagar_registro_4(self):
        self.ui.registro_4.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[3]['id']
        self.db.excluir_registro(id)

    def apagar_registro_5(self):
        self.ui.registro_5.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[4]['id']
        self.db.excluir_registro(id)

    def apagar_registro_6(self):
        self.ui.registro_6.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[5]['id']
        self.db.excluir_registro(id)

    def apagar_registro_7(self):
        self.ui.registro_7.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[6]['id']
        self.db.excluir_registro(id)

    def apagar_registro_8(self):
        self.ui.registro_8.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[7]['id']
        self.db.excluir_registro(id)

    def apagar_registro_9(self):
        self.ui.registro_9.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[8]['id']
        self.db.excluir_registro(id)

    def apagar_registro_10(self):
        self.ui.registro_10.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[9]['id']
        self.db.excluir_registro(id)

    def apagar_registro_11(self):
        self.ui.registro_11.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[10]['id']
        self.db.excluir_registro(id)

    def apagar_registro_12(self):
        self.ui.registro_12.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[11]['id']
        self.db.excluir_registro(id)

    def apagar_registro_13(self):
        self.ui.registro_13.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[12]['id']
        self.db.excluir_registro(id)

    def apagar_registro_14(self):
        self.ui.registro_14.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[13]['id']
        self.db.excluir_registro(id)

    def apagar_registro_15(self):
        self.ui.registro_15.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[14]['id']
        self.db.excluir_registro(id)

    def apagar_registro_16(self):
        self.ui.registro_16.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[15]['id']
        self.db.excluir_registro(id)

    def apagar_registro_17(self):
        self.ui.registro_17.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[16]['id']
        self.db.excluir_registro(id)

    def apagar_registro_18(self):
        self.ui.registro_18.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[17]['id']
        self.db.excluir_registro(id)

    def apagar_registro_19(self):
        self.ui.registro_19.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[18]['id']
        self.db.excluir_registro(id)

    def apagar_registro_20(self):
        self.ui.registro_20.close()

        self.ui.input.show()
        self.ui.input_texto.setText('Registro deletato!')
        self.ui.input_texto.setStyleSheet('color:red')

        self.db.carregar_registros()
        id = self.db.lista_registro[19]['id']
        self.db.excluir_registro(id)

    ''' ICONS DO SITE '''

    def set_icon(self, nome_do_site):

        nome_do_site = nome_do_site.lower()

        if 'face' in nome_do_site:
            return 'img\\facebook.png'

        elif 'whats' in nome_do_site:
            return 'img\\whatsapp.png'

        elif 'twitter' in nome_do_site:
            return 'img\\twitter.png'

        elif 'gmail' in nome_do_site:
            return 'img\\gmail.png'

        elif 'hotmail' in nome_do_site:
            return 'img\\gmail.png'

        elif 'outlook' in nome_do_site:
            return 'img\\outlook.png'

        elif 'youtube' in nome_do_site:
            return 'img\\youtube.png'

        elif 'insta' in nome_do_site:
            return 'img\\instagram.png'

        elif 'messeger' in nome_do_site:
            return 'img\\messeger.png'

        elif 'linkedin' in nome_do_site:
            return 'img\\linkedin.png'

        elif 'skype' in nome_do_site:
            return 'img\\skype.png'

        elif 'github' in nome_do_site:
            return 'img\\github.png'

        elif 'dropbox' in nome_do_site:
            return 'img\\dropbox.png'

        elif 'drive' in nome_do_site:
            return 'img\\googledrive.png'

        elif 'microsft' in nome_do_site:
            return 'img\\microsft.png'

        elif 'reddit' in nome_do_site:
            return 'img\\reddit.png'

        elif 'paypal' in nome_do_site:
            return 'img\\paypal.png'

        elif 'shoppe' in nome_do_site or 'mercadolivre' in nome_do_site:
            return 'img\\loja.png'

        elif 'nubank' in nome_do_site:
            return 'img\\nubank.png'

        elif 'banco' in nome_do_site:
            return 'img\\banco.png'

        elif 'cartão' in nome_do_site or 'cartao' in nome_do_site:
            return 'img\\cartao_de_credito.png'

        elif 'mercado pago' in nome_do_site:
            return 'img\\mercadopago.png'

        elif 'mercado livre' in nome_do_site:
            return 'img\\mercadolivre.png'

        elif 'banco do brasil' in nome_do_site:
            return 'img\\bancodobrasil.png'

        elif 'santander' in nome_do_site:
            return 'img\\santander.png'

        elif 'banco pan' in nome_do_site:
            return 'img\\bancopan.png'

        elif 'tiktok' in nome_do_site:
            return 'img\\tiktok.png'

        elif 'google' in nome_do_site:
            return 'img\\google.png'

        elif 'apple' in nome_do_site:
            return 'img\\apple.png'

        elif 'windows' in nome_do_site:
            return 'img\\windows.png'

        else:
            return 'img\\site.png'



class TelaApagar(QMainWindow):
    def __init__(self):
        super(TelaApagar, self).__init__()
        self.ui = UI_janela_apagar.Ui_Janela_apagar()
        self.ui.setupUi(self)
        self.ui.btn_nao.setIcon(QIcon('img\\não.png'))
        self.ui.btn_sim.setIcon(QIcon('img\\sim.png'))
        self.setWindowIcon(QIcon('img\\img_apagar.png'))


class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_janela_inicial.Ui_MainWindow()
        self.ui.setupUi(self)
        # janelas
        self.ui.input.close()
        self.tela_apagar = TelaApagar()
        self.conta = 0
        self.cont = 1
        self.ui.botao_saida.clicked.connect(self.ui.input.close)


        '''INFO DEV'''
        self.web = QWebEngineView()
        self.web.setWindowTitle(' ')
        self.web.setWindowIcon(QIcon('img/nav.ico'))

        self.ui.info_btn_git.clicked.connect(self.github)
        self.ui.info_btn_insta.clicked.connect(self.whatsapp)
        self.ui.info_btn_linkedin.clicked.connect(self.linkedin)
        self.ui.info_btn_twitter.clicked.connect(self.twitter)

        # avatar atual
        self.avatar_selecionado = 'img\\menino.png'
        self.ui.img_do_avatar.setPixmap(QPixmap('img\\menino.png'))

        # btn para selecionar avatar
        self.ui.avatar_1.clicked.connect(self.avatar1)
        self.ui.avatar_2.clicked.connect(self.avatar2)
        self.ui.avatar_3.clicked.connect(self.avatar3)
        self.ui.avatar_4.clicked.connect(self.avatar4)
        self.ui.avatar_5.clicked.connect(self.avatar5)
        self.ui.avatar_6.clicked.connect(self.avatar6)

        # add imagens
        self.ui.info_btn_git.setIcon(QIcon('img/info_github.png'))
        self.ui.info_btn_insta.setIcon(QIcon('img/info_instagram.png'))
        self.ui.info_btn_linkedin.setIcon(QIcon('img/info_linkedin.png'))
        self.ui.info_btn_twitter.setIcon(QIcon('img/info_twitter.png'))
        self.ui.img_contas.setPixmap(QPixmap('./img/contas.png'))
        self.ui.img_criar.setPixmap(QPixmap('img/criar_menu.png'))
        self.ui.avatar_1.setIcon(QIcon('img/menino_32x32.png'))
        self.ui.avatar_2.setIcon(QIcon('img/jason_32x32.png'))
        self.ui.avatar_3.setIcon(QIcon('img\\menina_32x32.png'))
        self.ui.avatar_4.setIcon(QIcon('img\\alerquina_32x32.png'))
        self.ui.avatar_5.setIcon(QIcon('img\\adulto_32x32.png'))
        self.ui.avatar_6.setIcon(QIcon('img\\noel.png'))
        self.ui.pushButton.setIcon(QIcon('img\\menu.png'))
        self.ui.botao_saida.setIcon(QIcon('img\\x.png'))
        self.ui.img_gera_senha.setPixmap(QPixmap('img\\img_senha.png'))
        self.ui.btn_copiar.setIcon(QIcon('img\\copiar.png'))
        self.setWindowIcon(QIcon('img\\senha.ico'))

        # chamando o banco de dados
        self.db = BD_add_conta.BD()
        self.db.carregar_contas()

        # btn cadastrar
        self.ui.btn_criar_2.clicked.connect(self.cadastro)

        # btn copiar
        self.ui.btn_copiar.clicked.connect(self.copiar)

        # btn gerar
        self.ui.btn_gerar.clicked.connect(self.gerar)

        '''listando as contas já cadatradas no GUI'''
        for v in self.db.lista_correta:
            self.db.carregar_contas()
            self.aid = v['id']
            nome_completo = f'{str(v["nome"]).capitalize()} {str(v["sobrenome"]).capitalize()}'
            if len(nome_completo) > 13:
                nome_completo = f'{str(v["nome"]).capitalize()} {str(v["sobrenome"]).capitalize()[0]}'

            # revelando o botões das contas
            if self.cont == 1:
                # revelando o botões das contas
                self.ui.botao_apagar_1.setEnabled(True)
                self.ui.botao_entrar_1.setEnabled(True)
                self.ui.nome_da_conta_1.setText(nome_completo)

                # avatar
                self.db.carregar_contas()
                avatar = str(self.db.lista_correta[0]['avatar'])
                self.ui.botao_entrar_1.setIcon(QIcon(avatar))

                # entrar
                nometabela = f"{self.db.lista_correta[0]['nome']}{self.db.lista_correta[0]['sobrenome']}"
                self.ui.botao_entrar_1.clicked.connect(
                    lambda: self.sites(nometabela))

                # Apagar conta
                self.ui.botao_apagar_1.clicked.connect(self.select_apagar1)
                self.ui.botao_apagar_1.clicked.connect(self.janela_pagar_1)

                self.ui.botao_apagar_1.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_1.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 2:
                # revelando o botões das contas
                self.ui.botao_apagar_2.setEnabled(True)
                self.ui.botao_entrar_2.setEnabled(True)
                self.ui.nome_da_conta_2.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[1]['nome']}{self.db.lista_correta[1]['sobrenome']}"
                self.ui.botao_entrar_2.clicked.connect(
                    lambda: self.sites(nometabela))

                self.db.carregar_contas()
                avatar = self.db.lista_correta[1]['avatar']
                self.ui.botao_entrar_2.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_2.clicked.connect(self.select_apagar2)
                self.ui.botao_apagar_2.clicked.connect(self.janela_pagar_2)

                self.ui.botao_apagar_2.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_2.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 3:
                # revelando o botões das contas
                self.ui.botao_apagar_3.setEnabled(True)
                self.ui.botao_entrar_3.setEnabled(True)
                self.ui.nome_da_conta_3.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[2]['nome']}{self.db.lista_correta[2]['sobrenome']}"
                self.ui.botao_entrar_3.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[2]['avatar']
                self.ui.botao_entrar_3.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_3.clicked.connect(self.janela_pagar_3)
                self.ui.botao_apagar_3.clicked.connect(self.select_apagar3)

                self.ui.botao_apagar_3.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_3.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 4:
                # revelando o botões das contas
                self.ui.botao_apagar_4.setEnabled(True)
                self.ui.botao_entrar_4.setEnabled(True)
                self.ui.nome_da_conta_4.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[3]['nome']}{self.db.lista_correta[3]['sobrenome']}"
                self.ui.botao_entrar_4.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[3]['avatar']
                self.ui.botao_entrar_4.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_4.clicked.connect(self.select_apagar4)
                self.ui.botao_apagar_4.clicked.connect(self.janela_pagar_4)

                self.ui.botao_apagar_4.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_4.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 5:
                # revelando o botões das contas
                self.ui.botao_apagar_5.setEnabled(True)
                self.ui.botao_entrar_5.setEnabled(True)
                self.ui.nome_da_conta_5.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[4]['nome']}{self.db.lista_correta[4]['sobrenome']}"
                self.ui.botao_entrar_5.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[4]['avatar']
                self.ui.botao_entrar_5.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_5.clicked.connect(self.select_apagar5)
                self.ui.botao_apagar_5.clicked.connect(self.janela_pagar_5)

                self.ui.botao_apagar_5.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_5.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 6:
                # revelando o botões das contas
                self.ui.botao_apagar_6.setEnabled(True)
                self.ui.botao_entrar_6.setEnabled(True)
                self.ui.nome_da_conta_6.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[5]['nome']}{self.db.lista_correta[5]['sobrenome']}"
                self.ui.botao_entrar_6.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[5]['avatar']
                self.ui.botao_entrar_6.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_6.clicked.connect(self.select_apagar6)
                self.ui.botao_apagar_6.clicked.connect(self.janela_pagar_6)

                self.ui.botao_apagar_6.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_6.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 7:
                # revelando o botões das contas
                self.ui.botao_apagar_7.setEnabled(True)
                self.ui.botao_entrar_7.setEnabled(True)
                self.ui.nome_da_conta_7.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[6]['nome']}{self.db.lista_correta[6]['sobrenome']}"
                self.ui.botao_entrar_7.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[6]['avatar']
                self.ui.botao_entrar_7.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_7.clicked.connect(self.select_apagar7)
                self.ui.botao_apagar_7.clicked.connect(self.janela_pagar_7)

                self.ui.botao_apagar_7.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_7.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 8:
                # revelando o botões das contas
                self.ui.botao_apagar_8.setEnabled(True)
                self.ui.botao_entrar_8.setEnabled(True)
                self.ui.nome_da_conta_8.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[7]['nome']}{self.db.lista_correta[7]['sobrenome']}"
                self.ui.botao_entrar_8.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[7]['avatar']
                self.ui.botao_entrar_8.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_8.clicked.connect(self.select_apagar8)
                self.ui.botao_apagar_8.clicked.connect(self.janela_pagar_8)

                self.ui.botao_apagar_8.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_8.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 9:
                # revelando o botões das contas
                self.ui.botao_apagar_9.setEnabled(True)
                self.ui.botao_entrar_9.setEnabled(True)
                self.ui.nome_da_conta_9.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[8]['nome']}{self.db.lista_correta[8]['sobrenome']}"
                self.ui.botao_entrar_9.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[8]['avatar']
                self.ui.botao_entrar_9.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_9.clicked.connect(self.select_apagar9)
                self.ui.botao_apagar_9.clicked.connect(self.janela_pagar_9)

                self.ui.botao_apagar_9.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_9.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 10:
                # revelando o botões das contas
                self.ui.botao_apagar_10.setEnabled(True)
                self.ui.botao_entrar_10.setEnabled(True)
                self.ui.nome_da_conta_10.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[9]['nome']}{self.db.lista_correta[9]['sobrenome']}"
                self.ui.botao_entrar_10.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[9]['avatar']
                self.ui.botao_entrar_10.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_10.clicked.connect(self.select_apagar10)
                self.ui.botao_apagar_10.clicked.connect(self.janela_pagar_10)

                self.ui.botao_apagar_10.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_10.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 11:
                # revelando o botões das contas
                self.ui.botao_apagar_11.setEnabled(True)
                self.ui.botao_entrar_11.setEnabled(True)
                self.ui.nome_da_conta_11.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[10]['nome']}{self.db.lista_correta[10]['sobrenome']}"
                self.ui.botao_entrar_11.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[10]['avatar']
                self.ui.botao_entrar_11.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_11.clicked.connect(self.select_apagar11)
                self.ui.botao_apagar_11.clicked.connect(self.janela_pagar_11)

                self.ui.botao_apagar_11.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_11.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 12:
                # revelando o botões das contas
                self.ui.botao_apagar_12.setEnabled(True)
                self.ui.botao_entrar_12.setEnabled(True)
                self.ui.nome_da_conta_12.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[11]['nome']}{self.db.lista_correta[11]['sobrenome']}"
                self.ui.botao_entrar_12.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[11]['avatar']
                self.ui.botao_entrar_12.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_12.clicked.connect(self.select_apagar12)
                self.ui.botao_apagar_12.clicked.connect(self.janela_pagar_12)

                self.ui.botao_apagar_12.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_12.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 13:
                # revelando o botões das contas
                self.ui.botao_apagar_13.setEnabled(True)
                self.ui.botao_entrar_13.setEnabled(True)
                self.ui.nome_da_conta_13.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[12]['nome']}{self.db.lista_correta[12]['sobrenome']}"
                self.ui.botao_entrar_13.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[12]['avatar']
                self.ui.botao_entrar_13.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_13.clicked.connect(self.select_apagar13)
                self.ui.botao_apagar_13.clicked.connect(self.janela_pagar_13)

                self.ui.botao_apagar_13.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_13.setStyleSheet('background-color:#6c6c6c')

            elif self.cont == 14:
                # revelando o botões das contas
                self.ui.botao_apagar_14.setEnabled(True)
                self.ui.botao_entrar_14.setEnabled(True)
                self.ui.nome_da_conta_14.setText(nome_completo)

                # entrar
                nometabela = f"{self.db.lista_correta[13]['nome']}{self.db.lista_correta[13]['sobrenome']}"
                self.ui.botao_entrar_14.clicked.connect(
                    lambda: self.sites(nometabela))

                # avatar
                self.db.carregar_contas()
                avatar = self.db.lista_correta[13]['avatar']
                self.ui.botao_entrar_14.setIcon(QIcon(avatar))

                # Apagar conta
                self.ui.botao_apagar_14.clicked.connect(self.select_apagar14)
                self.ui.botao_apagar_14.clicked.connect(self.janela_pagar_14)

                self.ui.botao_apagar_14.setIcon(QIcon('img\\img_apagar.png'))
                self.ui.user_14.setStyleSheet('background-color:#6c6c6c')

            self.cont += 1

    # Função de cadastrar conta
    def cadastro(self):
        self.ui.input_nome_2.setStyleSheet('''QLineEdit{
                            color: rgb(135, 135, 135);
                            background-color: rgb(30, 30, 30);
                            border-radius:10px;
                            border: 2px solid;
                            padding:10px
                            
                        }

                        QLineEdit:hover{
                            color: rgb(135, 135, 135);
                            border: 2px solid rgb(112, 112, 112)
                        }

                        QLineEdit:focus{
                            border: 2px solid rgb(85, 85, 255);
                            color: rgb(255, 255, 255);
                        }''')
        self.ui.input_sobrenome_2.setStyleSheet('''QLineEdit{
                        	color: rgb(135, 135, 135);
                        	background-color: rgb(30, 30, 30);
                        	border-radius:10px;
                        	border: 2px solid;
                        	padding:10px
                        }

                        QLineEdit:hover{
                        	color: rgb(135, 135, 135);
                        	border: 2px solid rgb(112, 112, 112)
                        }

                        QLineEdit:focus{
                        	border: 2px solid rgb(85, 85, 255);
                        	color: rgb(255, 255, 255);
                        }''')

        nome = self.ui.input_nome_2.text().replace(' ', '')
        sobrenome = self.ui.input_sobrenome_2.text().replace(' ', '')

        if (not nome.isalpha() or len(nome) < 2) or (not sobrenome.isalpha() or len(sobrenome) < 2):
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(255, 80, 80)};')
            self.ui.input_saida.setStyleSheet(
                'font: 87 10pt "Segoe UI Black";')
            self.ui.input_saida.setText('Nome ou Sobrenome invalídos!')
            self.ui.input_nome_2.setStyleSheet('''QLineEdit{
                            color: rgb(135, 135, 135);
                            background-color: rgb(30, 30, 30);
                            border-radius:10px;
                            border: 2px solid rgb(255, 80, 80);
                            padding:10px
                        }

                        QLineEdit:hover{
                            color: rgb(135, 135, 135);
                            border: 2px solid rgb(112, 112, 112)
                        }

                        QLineEdit:focus{
                            border: 2px solid rgb(85, 85, 255);
                            color: rgb(255, 255, 255);
                        }''')
            self.ui.input_sobrenome_2.setStyleSheet('''QLineEdit{
                                color: rgb(135, 135, 135);
                                background-color: rgb(30, 30, 30);
                                border-radius:10px;
                                border: 2px solid rgb(255, 80, 80);
                                padding:10px

                                
                            }

                            QLineEdit:hover{
                                color: rgb(135, 135, 135);
                                border: 2px solid rgb(112, 112, 112)
                            }

                            QLineEdit:focus{
                                border: 2px solid rgb(85, 85, 255);
                                color: rgb(255, 255, 255);
                            }''')

        else:
            # arrumando estilos dos inputs
            self.ui.input_nome_2.setStyleSheet("QLineEdit{\n"
                                               "    color: rgb(135, 135, 135);\n"
                                               "    background-color: rgb(30, 30, 30);\n"
                                               "    border-radius:10px;\n"
                                               "    border: 2px solid;\n"
                                               "    padding: 10px\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:hover{\n"
                                               "    color: rgb(135, 135, 135);\n"
                                               "    border: 2px solid rgb(112, 112, 112)\n"
                                               "}\n"
                                               "\n"
                                               "QLineEdit:focus{\n"
                                               "    border: 2px solid rgb(85, 85, 255);\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "}")
            self.ui.input_sobrenome_2.setStyleSheet("QLineEdit{\n"
                                                    "    color: rgb(135, 135, 135);\n"
                                                    "    background-color: rgb(30, 30, 30);\n"
                                                    "    border-radius:10px;\n"
                                                    "    border: 2px solid;\n"
                                                    "    padding: 10px\n"
                                                    "}\n"
                                                    "\n"
                                                    "QLineEdit:hover{\n"
                                                    "    color: rgb(135, 135, 135);\n"
                                                    "    border: 2px solid rgb(112, 112, 112)\n"
                                                    "}\n"
                                                    "\n"
                                                    "QLineEdit:focus{\n"
                                                    "    border: 2px solid rgb(85, 85, 255);\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "}")

            if self.cont >= 14:
                self.ui.input.setStyleSheet(
                    'QFrame{background-color: rgb(255, 80, 80)};')
                self.ui.input_saida.setStyleSheet(
                    'font: 87 7pt "Segoe UI Black";')
                self.ui.input_saida.setText(
                    'Limite atingido! exclua alguma conta e reinicie o app.')
                self.ui.input.show()
                self.ui.input_nome_2.setEnabled(False)
                self.ui.input_sobrenome_2.setEnabled(False)
            else:
                self.ui.input_nome_2.setEnabled(True)
                self.ui.input_sobrenome_2.setEnabled(True)

                try:
                    # verificando se ja tem conta existente
                    for v in self.db.lista_correta:
                        nome_completo_na_bd = f'{str(v["nome"]).capitalize()} {str(v["sobrenome"]).capitalize()}'
                        nome_completo_nos_inputs = f'{str(self.ui.input_nome_2.text()).capitalize()} ' \
                                                   f'{str(self.ui.input_sobrenome_2.text()).capitalize()}'
                        if nome_completo_na_bd == nome_completo_nos_inputs:
                            assert ()

                except:
                    self.ui.input.show()
                    self.ui.input_saida.setStyleSheet(
                        'font: 87 10pt "Segoe UI Black";')
                    self.ui.input.setStyleSheet(
                        'QFrame{background-color: rgb(255, 250, 76)};')
                    self.ui.input_saida.setText(
                        f'"{nome_completo_na_bd}" Já cadastrado!')

                else:
                    self.ui.input.show()
                    self.db.carregar_contas()
                    self.ui.input.setStyleSheet(
                        'QFrame{background-color: rgb(63, 255, 53)};')
                    self.ui.input_saida.setStyleSheet(
                        'font: 87 10pt "Segoe UI Black"')
                    self.ui.input_saida.setText(
                        'Conta cadastrada com sucesso!')

                    # adicionando conta registrada no bd / adicionando uma tabela única da conta no bd
                    nome_da_tabela = f'{str(self.ui.input_nome_2.text()).capitalize().replace(" ", "")}' \
                                     f'{str(self.ui.input_sobrenome_2.text()).capitalize().replace(" ", "")}'
                    self.db.tabela_cada_conta(nome_da_tabela)
                    self.db.inserir_contas(str(self.ui.input_nome_2.text()), str(self.ui.input_sobrenome_2.text()),
                                           self.avatar_selecionado)

                    # mostrando nome da conta
                    nome_completo = f'{str(self.ui.input_nome_2.text()).capitalize()} ' \
                                    f'{str(self.ui.input_sobrenome_2.text()).capitalize()}'
                    if len(nome_completo) > 15:
                        nome_completo = f'{str(self.ui.input_nome_2.text()).capitalize()} ' \
                                        f'{str(self.ui.input_sobrenome_2.text()).capitalize()[0]}'

                    # limpando os campos de textos
                    self.ui.input_nome_2.setText('')
                    self.ui.input_sobrenome_2.setText('')

                    if self.cont == 1:
                        # revelando o botões das contas
                        self.ui.botao_apagar_1.setEnabled(True)
                        self.ui.botao_entrar_1.setEnabled(True)
                        self.ui.nome_da_conta_1.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = str(self.db.lista_correta[0]['avatar'])
                        self.ui.botao_entrar_1.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[0]['nome']}{self.db.lista_correta[0]['sobrenome']}"
                        self.ui.botao_entrar_1.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_1.clicked.connect(
                            self.select_apagar1)
                        self.ui.botao_apagar_1.clicked.connect(
                            self.janela_pagar_1)

                        self.ui.botao_apagar_1.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_1.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 2:
                        # revelando o botões das contas
                        self.ui.botao_apagar_2.setEnabled(True)
                        self.ui.botao_entrar_2.setEnabled(True)
                        self.ui.nome_da_conta_2.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[1]['avatar']
                        self.ui.botao_entrar_2.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[1]['nome']}{self.db.lista_correta[1]['sobrenome']}"
                        self.ui.botao_entrar_2.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_2.clicked.connect(
                            self.select_apagar2)
                        self.ui.botao_apagar_2.clicked.connect(
                            self.janela_pagar_2)

                        self.ui.botao_apagar_2.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_2.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 3:
                        # revelando o botões das contas
                        self.ui.botao_apagar_3.setEnabled(True)
                        self.ui.botao_entrar_3.setEnabled(True)
                        self.ui.nome_da_conta_3.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[2]['avatar']
                        self.ui.botao_entrar_3.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[2]['nome']}{self.db.lista_correta[2]['sobrenome']}"
                        self.ui.botao_entrar_3.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_3.clicked.connect(
                            self.janela_pagar_3)
                        self.ui.botao_apagar_3.clicked.connect(
                            self.select_apagar3)

                        self.ui.botao_apagar_3.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_3.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 4:
                        # revelando o botões das contas
                        self.ui.botao_apagar_4.setEnabled(True)
                        self.ui.botao_entrar_4.setEnabled(True)
                        self.ui.nome_da_conta_4.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[3]['avatar']
                        self.ui.botao_entrar_4.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[3]['nome']}{self.db.lista_correta[3]['sobrenome']}"
                        self.ui.botao_entrar_4.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_4.clicked.connect(
                            self.select_apagar4)
                        self.ui.botao_apagar_4.clicked.connect(
                            self.janela_pagar_4)

                        self.ui.botao_apagar_4.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_4.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 5:
                        # revelando o botões das contas
                        self.ui.botao_apagar_5.setEnabled(True)
                        self.ui.botao_entrar_5.setEnabled(True)
                        self.ui.nome_da_conta_5.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[4]['avatar']
                        self.ui.botao_entrar_5.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[4]['nome']}{self.db.lista_correta[4]['sobrenome']}"
                        self.ui.botao_entrar_5.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_5.clicked.connect(
                            self.select_apagar5)
                        self.ui.botao_apagar_5.clicked.connect(
                            self.janela_pagar_5)

                        self.ui.botao_apagar_5.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_5.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 6:
                        # revelando o botões das contas
                        self.ui.botao_apagar_6.setEnabled(True)
                        self.ui.botao_entrar_6.setEnabled(True)
                        self.ui.nome_da_conta_6.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[5]['avatar']
                        self.ui.botao_entrar_6.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[5]['nome']}{self.db.lista_correta[5]['sobrenome']}"
                        self.ui.botao_entrar_6.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_6.clicked.connect(
                            self.select_apagar6)
                        self.ui.botao_apagar_6.clicked.connect(
                            self.janela_pagar_6)

                        self.ui.botao_apagar_6.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_6.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 7:
                        # revelando o botões das contas
                        self.ui.botao_apagar_7.setEnabled(True)
                        self.ui.botao_entrar_7.setEnabled(True)
                        self.ui.nome_da_conta_7.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[6]['avatar']
                        self.ui.botao_entrar_7.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[6]['nome']}{self.db.lista_correta[6]['sobrenome']}"
                        self.ui.botao_entrar_7.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_7.clicked.connect(
                            self.select_apagar7)
                        self.ui.botao_apagar_7.clicked.connect(
                            self.janela_pagar_7)

                        self.ui.botao_apagar_7.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_7.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 8:
                        # revelando o botões das contas
                        self.ui.botao_apagar_8.setEnabled(True)
                        self.ui.botao_entrar_8.setEnabled(True)
                        self.ui.nome_da_conta_8.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[7]['avatar']
                        self.ui.botao_entrar_8.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[7]['nome']}{self.db.lista_correta[7]['sobrenome']}"
                        self.ui.botao_entrar_8.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_8.clicked.connect(
                            self.select_apagar8)
                        self.ui.botao_apagar_8.clicked.connect(
                            self.janela_pagar_8)

                        self.ui.botao_apagar_8.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_8.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 9:
                        # revelando o botões das contas
                        self.ui.botao_apagar_9.setEnabled(True)
                        self.ui.botao_entrar_9.setEnabled(True)
                        self.ui.nome_da_conta_9.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[8]['avatar']
                        self.ui.botao_entrar_9.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[8]['nome']}{self.db.lista_correta[8]['sobrenome']}"
                        self.ui.botao_entrar_9.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_9.clicked.connect(
                            self.select_apagar9)
                        self.ui.botao_apagar_9.clicked.connect(
                            self.janela_pagar_9)

                        self.ui.botao_apagar_9.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_9.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 10:
                        # revelando o botões das contas
                        self.ui.botao_apagar_10.setEnabled(True)
                        self.ui.botao_entrar_10.setEnabled(True)
                        self.ui.nome_da_conta_10.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[9]['avatar']
                        self.ui.botao_entrar_10.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[9]['nome']}{self.db.lista_correta[9]['sobrenome']}"
                        self.ui.botao_entrar_10.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_10.clicked.connect(
                            self.select_apagar10)
                        self.ui.botao_apagar_10.clicked.connect(
                            self.janela_pagar_10)

                        self.ui.botao_apagar_10.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_10.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 11:
                        # revelando o botões das contas
                        self.ui.botao_apagar_11.setEnabled(True)
                        self.ui.botao_entrar_11.setEnabled(True)
                        self.ui.nome_da_conta_11.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[10]['avatar']
                        self.ui.botao_entrar_11.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[10]['nome']}{self.db.lista_correta[10]['sobrenome']}"
                        self.ui.botao_entrar_11.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_11.clicked.connect(
                            self.select_apagar11)
                        self.ui.botao_apagar_11.clicked.connect(
                            self.janela_pagar_11)

                        self.ui.botao_apagar_11.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_11.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 12:
                        # revelando o botões das contas
                        self.ui.botao_apagar_12.setEnabled(True)
                        self.ui.botao_entrar_12.setEnabled(True)
                        self.ui.nome_da_conta_12.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[11]['avatar']
                        self.ui.botao_entrar_12.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[11]['nome']}{self.db.lista_correta[11]['sobrenome']}"
                        self.ui.botao_entrar_12.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_12.clicked.connect(
                            self.select_apagar12)
                        self.ui.botao_apagar_12.clicked.connect(
                            self.janela_pagar_12)

                        self.ui.botao_apagar_12.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_12.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 13:
                        # revelando o botões das contas
                        self.ui.botao_apagar_13.setEnabled(True)
                        self.ui.botao_entrar_13.setEnabled(True)
                        self.ui.nome_da_conta_13.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[12]['avatar']
                        self.ui.botao_entrar_13.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[12]['nome']}{self.db.lista_correta[12]['sobrenome']}"
                        self.ui.botao_entrar_13.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_13.clicked.connect(
                            self.select_apagar13)
                        self.ui.botao_apagar_13.clicked.connect(
                            self.janela_pagar_13)

                        self.ui.botao_apagar_13.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_13.setStyleSheet(
                            'background-color:#6c6c6c')

                    elif self.cont == 14:
                        # revelando o botões das contas
                        self.ui.botao_apagar_14.setEnabled(True)
                        self.ui.botao_entrar_14.setEnabled(True)
                        self.ui.nome_da_conta_14.setText(nome_completo)

                        # avatar
                        self.db.carregar_contas()
                        avatar = self.db.lista_correta[13]['avatar']
                        self.ui.botao_entrar_14.setIcon(QIcon(avatar))

                        # entrar
                        nometabela = f"{self.db.lista_correta[13]['nome']}{self.db.lista_correta[13]['sobrenome']}"
                        self.ui.botao_entrar_14.clicked.connect(
                            lambda: self.sites(nometabela))

                        # Apagar conta
                        self.ui.botao_apagar_14.clicked.connect(
                            self.select_apagar14)
                        self.ui.botao_apagar_14.clicked.connect(
                            self.janela_pagar_14)

                        self.ui.botao_apagar_14.setIcon(
                            QIcon('img\\img_apagar.png'))
                        self.ui.user_14.setStyleSheet(
                            'background-color:#6c6c6c')

                    self.cont += 1

    '''FUNÇÕES PRA SELECIONAR APENAS UMA CONTA AO EXCLUIR(IGNORE)'''

    def select_apagar1(self):
        self.conta = 1

    def select_apagar2(self):
        self.conta = 2

    def select_apagar3(self):
        self.conta = 3

    def select_apagar4(self):
        self.conta = 4

    def select_apagar5(self):
        self.conta = 5

    def select_apagar6(self):
        self.conta = 6

    def select_apagar7(self):
        self.conta = 7

    def select_apagar8(self):
        self.conta = 8

    def select_apagar9(self):
        self.conta = 9

    def select_apagar10(self):
        self.conta = 10

    def select_apagar11(self):
        self.conta = 11

    def select_apagar12(self):
        self.conta = 12

    def select_apagar13(self):
        self.conta = 13

    def select_apagar14(self):
        self.conta = 14



    def apagar_conta_1(self):
        if self.conta == 1:
            self.db.carregar_contas()

            aid = self.db.lista_correta[0]['id']
            nome_tabela = f'{str(self.db.lista_correta[0]["nome"]).replace(" ", "").capitalize()}' \
                          f'{str(self.db.lista_correta[0]["sobrenome"]).replace(" ", "").capitalize()}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_1.setEnabled(False)

            nome = f'{self.db.lista_correta[0]["nome"]} {self.db.lista_correta[0]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_1(self):
        self.tela_apagar.show()

        if self.conta == 1:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_1)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_2(self):
        if self.conta == 2:
            self.db.carregar_contas()

            aid = self.db.lista_correta[1]['id']
            nome_tabela = f'{str(self.db.lista_correta[1]["nome"]).replace(" ", "").capitalize()}' \
                          f'{str(self.db.lista_correta[1]["sobrenome"]).replace(" ", "").capitalize()}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_2.setEnabled(False)

            nome = f'{self.db.lista_correta[1]["nome"]} {self.db.lista_correta[1]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_2(self):
        self.tela_apagar.show()

        if self.conta == 2:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_2)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_3(self):
        if self.conta == 3:
            self.db.carregar_contas()

            aid = self.db.lista_correta[2]['id']
            nome_tabela = f'{str(self.db.lista_correta[2]["nome"]).replace(" ", "").capitalize()}' \
                          f'{str(self.db.lista_correta[2]["sobrenome"]).replace(" ", "").capitalize()}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_3.setEnabled(False)

            nome = f'{self.db.lista_correta[2]["nome"]} {self.db.lista_correta[2]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_3(self):
        self.tela_apagar.show()

        if self.conta == 3:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_3)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_4(self):
        if self.conta == 4:
            self.db.carregar_contas()

            aid = self.db.lista_correta[3]['id']
            nome_tabela = f'{str(self.db.lista_correta[3]["nome"]).replace(" ", "").capitalize()}' \
                          f'{str(self.db.lista_correta[3]["sobrenome"]).replace(" ", "").capitalize()}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_4.setEnabled(False)

            nome = f'{self.db.lista_correta[3]["nome"]} {self.db.lista_correta[3]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_4(self):
        self.tela_apagar.show()

        if self.conta == 4:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_4)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_5(self):
        if self.conta == 5:
            self.db.carregar_contas()

            aid = self.db.lista_correta[4]['id']
            nome_tabela = f'{str(self.db.lista_correta[4]["nome"]).replace(" ", "").capitalize().capitalize()}' \
                          f'{str(self.db.lista_correta[4]["sobrenome"]).replace(" ", "").capitalize().capitalize()}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_5.setEnabled(False)

            nome = f'{self.db.lista_correta[4]["nome"]} {self.db.lista_correta[4]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_5(self):
        self.tela_apagar.show()

        if self.conta == 5:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_5)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_6(self):
        if self.conta == 6:
            self.db.carregar_contas()

            aid = self.db.lista_correta[5]['id']
            nome_tabela = f'{str(self.db.lista_correta[5]["nome"]).replace(" ", "").capitalize()}' \
                          f'{str(self.db.lista_correta[5]["sobrenome"]).replace(" ", "").capitalize()}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_6.setEnabled(False)

            nome = f'{self.db.lista_correta[5]["nome"]} {self.db.lista_correta[5]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_6(self):
        self.tela_apagar.show()

        if self.conta == 6:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_6)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_7(self):
        if self.conta == 7:
            self.db.carregar_contas()

            aid = self.db.lista_correta[6]['id']
            nome_tabela = f'{str(self.db.lista_correta[6]["nome"]).replace(" ", "").capitalize()}' \
                          f'{str(self.db.lista_correta[6]["sobrenome"]).replace(" ", "").capitalize()}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_7.setEnabled(False)

            nome = f'{self.db.lista_correta[6]["nome"]} {self.db.lista_correta[6]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_7(self):
        self.tela_apagar.show()

        if self.conta == 7:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_7)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_8(self):
        if self.conta == 8:
            self.db.carregar_contas()

            aid = self.db.lista_correta[7]['id']
            nome_tabela = f'{str(self.db.lista_correta[7]["nome"]).replace(" ", "").capitalize()}' \
                          f'{str(self.db.lista_correta[7]["sobrenome"]).replace(" ", "").capitalize()}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_8.setEnabled(False)

            nome = f'{self.db.lista_correta[7]["nome"]} {self.db.lista_correta[7]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_8(self):
        self.tela_apagar.show()

        if self.conta == 8:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_8)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_9(self):
        if self.conta == 9:
            self.db.carregar_contas()

            aid = self.db.lista_correta[8]['id']
            nome_tabela = f'{str(self.db.lista_correta[8]["nome"]).replace(" ", "")}' \
                          f'{str(self.db.lista_correta[8]["sobrenome"]).replace(" ", "")}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_9.setEnabled(False)

            nome = f'{self.db.lista_correta[8]["nome"]} {self.db.lista_correta[8]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_9(self):
        self.tela_apagar.show()

        if self.conta == 9:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_9)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_10(self):
        if self.conta == 10:
            self.db.carregar_contas()

            aid = self.db.lista_correta[9]['id']
            nome_tabela = f'{str(self.db.lista_correta[9]["nome"]).replace(" ", "")}' \
                          f'{str(self.db.lista_correta[9]["sobrenome"]).replace(" ", "")}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_10.setEnabled(False)

            nome = f'{self.db.lista_correta[9]["nome"]} {self.db.lista_correta[9]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_10(self):
        self.tela_apagar.show()

        if self.conta == 10:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_10)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_11(self):
        if self.conta == 11:
            self.db.carregar_contas()

            aid = self.db.lista_correta[10]['id']
            nome_tabela = f'{str(self.db.lista_correta[10]["nome"]).replace(" ", "")}' \
                          f'{str(self.db.lista_correta[10]["sobrenome"]).replace(" ", "")}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_11.setEnabled(False)

            nome = f'{self.db.lista_correta[10]["nome"]} {self.db.lista_correta[10]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_11(self):
        self.tela_apagar.show()

        if self.conta == 11:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_11)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_12(self):
        if self.conta == 12:
            self.db.carregar_contas()

            aid = self.db.lista_correta[11]['id']
            nome_tabela = f'{str(self.db.lista_correta[11]["nome"]).replace(" ", "")}' \
                          f'{str(self.db.lista_correta[11]["sobrenome"]).replace(" ", "")}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_12.setEnabled(False)

            nome = f'{self.db.lista_correta[11]["nome"]} {self.db.lista_correta[11]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_12(self):
        self.tela_apagar.show()

        if self.conta == 12:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_12)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_13(self):
        if self.conta == 13:
            self.db.carregar_contas()

            aid = self.db.lista_correta[12]['id']
            nome_tabela = f'{str(self.db.lista_correta[12]["nome"]).replace(" ", "")}' \
                          f'{str(self.db.lista_correta[12]["sobrenome"]).replace(" ", "")}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_13.setEnabled(False)

            nome = f'{self.db.lista_correta[12]["nome"]} {self.db.lista_correta[12]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_13(self):
        self.tela_apagar.show()

        if self.conta == 13:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_13)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    def apagar_conta_14(self):
        if self.conta == 14:
            self.db.carregar_contas()

            aid = self.db.lista_correta[13]['id']
            nome_tabela = f'{str(self.db.lista_correta[13]["nome"]).replace(" ", "")}' \
                          f'{str(self.db.lista_correta[13]["sobrenome"]).replace(" ", "")}'

            self.db.excluir_conta(aid, nome_tabela)
            self.tela_apagar.hide()
            self.ui.user_14.setEnabled(False)

            nome = f'{self.db.lista_correta[13]["nome"]} {self.db.lista_correta[13]["sobrenome"]}'
            self.ui.input.show()
            self.ui.input.setStyleSheet(
                'QFrame{background-color: rgb(18, 18, 18)};')
            self.ui.input_saida.setStyleSheet('font: 87 9pt "Segoe UI Black";'
                                              'color:rgb(255, 80, 80);')
            self.ui.input_saida.setText(f'A conta "{nome}" Foi Deletada!')

    def janela_pagar_14(self):
        self.tela_apagar.show()

        if self.conta == 14:
            self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_14)
            self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    '''FUNÇÃO DE FECHAR JANELA DE EXLUIR'''

    def fechar_excluir(self):
        self.tela_apagar.hide()

    '''FUNÇÕES PARA SELCIONAR AVATAR'''

    def avatar1(self):
        self.avatar_selecionado = 'img\\menino.png'
        self.ui.img_do_avatar.setPixmap(QPixmap('img\\menino.png'))

    def avatar2(self):
        self.avatar_selecionado = 'img\\jason.png'
        self.ui.img_do_avatar.setPixmap(QPixmap('img\\jason.png'))

    def avatar3(self):
        self.avatar_selecionado = 'img\\menina.png'
        self.ui.img_do_avatar.setPixmap(QPixmap('img\\menina.png'))

    def avatar4(self):
        self.avatar_selecionado = 'img\\alerquina.png'
        self.ui.img_do_avatar.setPixmap(QPixmap('img\\alerquina.png'))

    def avatar5(self):
        self.avatar_selecionado = 'img\\adulto.png'
        self.ui.img_do_avatar.setPixmap(QPixmap('img\\adulto.png'))

    def avatar6(self):
        self.avatar_selecionado = 'img\\noel.png'
        self.ui.img_do_avatar.setPixmap(QPixmap('img\\noel.png'))

    '''BOTÃO COPIAR'''

    def copiar(self):
        if self.ui.input_senha.text():
            self.ui.label_copiado.show()

            texto = self.ui.input_senha.text()
            ctrlC.CtrlC(texto)

            self.ui.label_copiado.setText('COPIADO!')
            self.ui.img_senha_gerada.setPixmap(QPixmap(''))
            self.ui.label_senha_gerada.setText('')

    '''BOTAO GERAR SENHA CRIPTOGRAFADA'''

    def gerar(self):
        self.ui.input_senha.setText(geraCriptografia.gerador(15))
        self.ui.img_senha_gerada.setPixmap(QPixmap('img\\check.png'))
        self.ui.label_senha_gerada.setText('SENHA GERADA')
        self.ui.label_copiado.hide()

    '''JANELAS SITES'''

    def sites(self, nome_tabela):
        self.tela_site = TelaSites(nome_tabela)
        self.tela_site.show()

    '''FUNÇÕES WEB LINKS'''
    def github(self):
        self.web.load(QUrl('https://github.com/ryanprogrammer'))
        self.web.show()

    def whatsapp(self):
        self.web.load(QUrl('https://api.whatsapp.com/send?phone=5511990132993&text=Opaa%2C%20vim%20pelo%20software'))
        self.web.show()

    def linkedin(self):
        self.web.load(QUrl('https://www.linkedin.com/in/ryanbarbosasilva/'))
        self.web.show()

    def twitter(self):
        self.web.load(QUrl('https://twitter.com/ry4nzk'))
        self.web.show()


if __name__ == '__main__':
    go = QApplication(sys.argv)
    w = TelaInicial()
    bd = BD_add_conta.BD()
    w.show()
    go.exec_()
