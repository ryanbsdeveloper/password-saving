import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon
from windows.UI import UI_janela_inicial, UI_janela_admin, UI_janela_apagar
from imports.BancoDeDados import BD_add_conta

class TelaApagar(QMainWindow):
    def __init__(self):
        super(TelaApagar, self).__init__()
        self.ui = UI_janela_apagar.Ui_Janela_apagar()
        self.ui.setupUi(self)
        self.ui.btn_nao.setIcon(QIcon('img\\btn_não.png'))
        self.ui.btn_sim.setIcon(QIcon('img\\btn_sim.png'))
        self.setWindowIcon(QIcon('img\\img_apagar.png'))
        self.sim = 1
        self.ui.btn_sim.clicked.connect(self.valida_sim)
        # self.tela_ini = TelaInicial()
        # self.ui.btn_sim.clicked.connect(self)

    def valida_sim(self):
        self.sim = 2


class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_janela_inicial.Ui_Janela_login()
        self.ui.setupUi(self)
        #janelas
        self.tela_apagar = TelaApagar()
        # add imagens
        self.ui.btn_criar_2.setIcon(QIcon('img\\login.png'))
        self.ui.img_contas.setPixmap(QPixmap('img\\contas.png'))
        self.ui.img_criar.setPixmap(QPixmap('img\\add_contas.png'))
        self.setWindowIcon(QIcon('img\\icon_login.ico'))
        self.db = BD_add_conta.BD()
        # btn cadastrar
        self.ui.btn_criar_2.clicked.connect(self.cadastro)
        self.cont = 0
        self.db.carregar_contas()
        # for v in self.db.lista_contas:
        #     if v in self.lista_correta:
        #         pass
        #     else:
        #         self.lista_correta.append(v)

        '''listando as contas já cadatradas no GUI'''
        for v in self.db.lista_correta:
            try:
                self.aid = v['id']
                self.cont += 1
                nome_completo = f'{str(v["nome"]).capitalize()} {str(v["sobrenome"]).capitalize()}'
                if len(nome_completo) > 13:
                    nome_completo = f'{str(v["nome"]).capitalize()} {str(v["sobrenome"]).capitalize()[0]}'

                if self.cont == 1:

                    # revelando o botões das contas
                    self.ui.btn_editar_1.setEnabled(True)
                    self.ui.btn_apagar_1.setEnabled(True)
                    self.ui.btn_entrar_1.setEnabled(True)
                    self.ui.btn_entrar_1.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_1.clicked.connect(self.janela_pagar_1)

                    ######
                    self.ui.btn_editar_1.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_1.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_1.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 2:

                    # revelando o botões das contas
                    self.ui.btn_editar_2.setEnabled(True)
                    self.ui.btn_apagar_2.setEnabled(True)
                    self.ui.btn_entrar_2.setEnabled(True)
                    self.ui.btn_entrar_2.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_2.clicked.connect(self.janela_pagar_2)

                    ######
                    self.ui.btn_editar_2.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_2.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_2.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 3:

                    # revelando o botões das contas
                    self.ui.btn_editar_3.setEnabled(True)
                    self.ui.btn_apagar_3.setEnabled(True)
                    self.ui.btn_entrar_3.setEnabled(True)
                    self.ui.btn_entrar_3.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_3.clicked.connect(self.janela_pagar_3)

                    ######
                    self.ui.btn_editar_3.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_3.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_3.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 4:

                    # revelando o botões das contas
                    self.ui.btn_editar_4.setEnabled(True)
                    self.ui.btn_apagar_4.setEnabled(True)
                    self.ui.btn_entrar_4.setEnabled(True)
                    self.ui.btn_entrar_4.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_4.clicked.connect(self.janela_pagar_4)

                    ######
                    self.ui.btn_editar_4.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_4.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_4.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 5:

                    # revelando o botões das contas
                    self.ui.btn_editar_5.setEnabled(True)
                    self.ui.btn_apagar_5.setEnabled(True)
                    self.ui.btn_entrar_5.setEnabled(True)
                    self.ui.btn_entrar_5.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_5.clicked.connect(self.janela_pagar_5)

                    ######
                    self.ui.btn_editar_5.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_5.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_5.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 6:

                    # revelando o botões das contas
                    self.ui.btn_editar_6.setEnabled(True)
                    self.ui.btn_apagar_6.setEnabled(True)
                    self.ui.btn_entrar_6.setEnabled(True)
                    self.ui.btn_entrar_6.setText(nome_completo)

                    # Apagar conta
                    # att conta criada
                    self.ui.btn_apagar_6.clicked.connect(self.janela_pagar_6)

                    ######
                    self.ui.btn_editar_6.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_6.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_6.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 7:

                    # revelando o botões das contas
                    self.ui.btn_editar_7.setEnabled(True)
                    self.ui.btn_apagar_7.setEnabled(True)
                    self.ui.btn_entrar_7.setEnabled(True)
                    self.ui.btn_entrar_7.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_7.clicked.connect(self.janela_pagar_7)

                    ######
                    self.ui.btn_editar_7.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_7.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_7.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 8:

                    # revelando o botões das contas
                    self.ui.btn_editar_8.setEnabled(True)
                    self.ui.btn_apagar_8.setEnabled(True)
                    self.ui.btn_entrar_8.setEnabled(True)
                    self.ui.btn_entrar_8.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_8.clicked.connect(self.janela_pagar_8)

                    ######
                    self.ui.btn_editar_8.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_8.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_8.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 9:

                    # revelando o botões das contas
                    self.ui.btn_editar_9.setEnabled(True)
                    self.ui.btn_apagar_9.setEnabled(True)
                    self.ui.btn_entrar_9.setEnabled(True)
                    self.ui.btn_entrar_9.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_9.clicked.connect(self.janela_pagar_9)

                    ######
                    self.ui.btn_editar_9.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_9.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_9.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 10:

                    # revelando o botões das contas
                    self.ui.btn_editar_10.setEnabled(True)
                    self.ui.btn_apagar_10.setEnabled(True)
                    self.ui.btn_entrar_10.setEnabled(True)
                    self.ui.btn_entrar_10.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_10.clicked.connect(self.janela_pagar_10)

                    ######
                    self.ui.btn_editar_10.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_10.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_10.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 11:

                    # revelando o botões das contas
                    self.ui.btn_editar_11.setEnabled(True)
                    self.ui.btn_apagar_11.setEnabled(True)
                    self.ui.btn_entrar_11.setEnabled(True)
                    self.ui.btn_entrar_11.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_11.clicked.connect(self.janela_pagar_11)

                    ######
                    self.ui.btn_editar_11.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_11.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_11.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 12:

                    # revelando o botões das contas
                    self.ui.btn_editar_12.setEnabled(True)
                    self.ui.btn_apagar_12.setEnabled(True)
                    self.ui.btn_entrar_12.setEnabled(True)
                    self.ui.btn_entrar_12.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_12.clicked.connect(self.janela_pagar_12)

                    ######
                    self.ui.btn_editar_12.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_12.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_12.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 13:

                    # revelando o botões das contas
                    self.ui.btn_editar_13.setEnabled(True)
                    self.ui.btn_apagar_13.setEnabled(True)
                    self.ui.btn_entrar_13.setEnabled(True)
                    self.ui.btn_entrar_13.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_13.clicked.connect(self.janela_pagar_13)

                    ######
                    self.ui.btn_editar_13.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_13.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_13.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 14:

                    # revelando o botões das contas
                    self.ui.btn_editar_14.setEnabled(True)
                    self.ui.btn_apagar_14.setEnabled(True)
                    self.ui.btn_entrar_14.setEnabled(True)
                    self.ui.btn_entrar_14.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_14.clicked.connect(self.janela_pagar_14)

                    ######
                    self.ui.btn_editar_14.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_14.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_14.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 15:

                    # revelando o botões das contas
                    self.ui.btn_editar_15.setEnabled(True)
                    self.ui.btn_apagar_15.setEnabled(True)
                    self.ui.btn_entrar_15.setEnabled(True)
                    self.ui.btn_entrar_15.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_15.clicked.connect(self.janela_pagar_15)

                    ######
                    self.ui.btn_editar_15.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_15.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_15.setStyleSheet('background-color:#6c6c6c')

                elif self.cont == 16:

                    # revelando o botões das contas
                    self.ui.btn_editar_16.setEnabled(True)
                    self.ui.btn_apagar_16.setEnabled(True)
                    self.ui.btn_entrar_16.setEnabled(True)
                    self.ui.btn_entrar_16.setText(nome_completo)

                    # Apagar conta
                    self.ui.btn_apagar_16.clicked.connect(self.janela_pagar_16)

                    ######
                    self.ui.btn_editar_16.setIcon(QIcon('img\\img_navegar.png'))
                    self.ui.btn_apagar_16.setIcon(QIcon('img\\img_apagar.png'))
                    self.ui.user_16.setStyleSheet('background-color:#6c6c6c')
            except:
                self.ui.input_saida.setStyleSheet('color:red;font: 87 italic 10pt "Segoe UI Black";')
                self.ui.input_saida.setText('Erro inesperado, reinicie o aplicativo.')

    # Função de cadastrar conta
    def cadastro(self):
        self.db.carregar_contas()

        if self.ui.input_nome_2.text().isnumeric() or self.ui.input_sobrenome_2.text().isnumeric() or len(
                self.ui.input_nome_2.text()) < 2 or len(self.ui.input_sobrenome_2.text()) < 2:
            self.ui.input_saida.setStyleSheet('color:red;font: 87 italic 10pt "Segoe UI Black";')
            self.ui.input_saida.setText('Nome ou sobrenome invalído!')
        else:
            try:
                # verificando se ja tem conta existente
                for v in self.db.lista_correta:
                    nome_completo_na_bd = f'{str(v["nome"]).capitalize()} {str(v["sobrenome"]).capitalize()}'
                    nome_completo_nos_inputs = f'{str(self.ui.input_nome_2.text()).capitalize()} ' \
                                               f'{str(self.ui.input_sobrenome_2.text()).capitalize()}'
                    if nome_completo_na_bd == nome_completo_nos_inputs:
                        assert ()

            except:
                self.ui.input_saida.setStyleSheet('color:yellow;font: 87 italic 10pt "Segoe UI Black";')
                self.ui.input_saida.setText(f'"{nome_completo_na_bd}" Já cadastrado!')

            else:
                self.cont += 1
                self.db.carregar_contas()
                self.ui.input_saida.setStyleSheet('color:green;font: 87 italic 10pt "Segoe UI Black";')
                self.ui.input_saida.setText('Conta cadastrada com sucesso!')

                # adicionando conta registrada no bd / adicionando uma tabela única da conta no bd
                nome_da_tabela = f'{str(self.ui.input_nome_2.text()).capitalize().replace(" ", "")}' \
                                 f'{str(self.ui.input_sobrenome_2.text()).capitalize().replace(" ", "")}'
                self.db.tabela_cada_conta(nome_da_tabela)
                self.db.inserir_contas(str(self.ui.input_nome_2.text()), str(self.ui.input_sobrenome_2.text()))

                # mostrando nome da conta
                nome_completo = f'{str(self.ui.input_nome_2.text()).capitalize()} ' \
                                f'{str(self.ui.input_sobrenome_2.text()).capitalize()}'
                if len(nome_completo) > 13:
                    nome_completo = f'{str(self.ui.input_nome_2.text()).capitalize()} ' \
                                    f'{str(self.ui.input_sobrenome_2.text()).capitalize()[0]}'

                # limpando os campos de textos
                self.ui.input_nome_2.setText('')
                self.ui.input_sobrenome_2.setText('')

                try:
                    if self.cont == 1:

                        # revelando o botões das contas
                        self.ui.btn_editar_1.setEnabled(True)
                        self.ui.btn_apagar_1.setEnabled(True)
                        self.ui.btn_entrar_1.setEnabled(True)
                        self.ui.btn_entrar_1.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_1.clicked.connect(self.janela_pagar_1)

                        ######
                        self.ui.btn_editar_1.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_1.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_1.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 2:

                        # revelando o botões das contas
                        self.ui.btn_editar_2.setEnabled(True)
                        self.ui.btn_apagar_2.setEnabled(True)
                        self.ui.btn_entrar_2.setEnabled(True)
                        self.ui.btn_entrar_2.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_2.clicked.connect(self.janela_pagar_2)

                        ######
                        self.ui.btn_editar_2.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_2.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_2.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 3:

                        # revelando o botões das contas
                        self.ui.btn_editar_3.setEnabled(True)
                        self.ui.btn_apagar_3.setEnabled(True)
                        self.ui.btn_entrar_3.setEnabled(True)
                        self.ui.btn_entrar_3.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_3.clicked.connect(self.janela_pagar_3)

                        ######
                        self.ui.btn_editar_3.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_3.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_3.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 4:

                        # revelando o botões das contas
                        self.ui.btn_editar_4.setEnabled(True)
                        self.ui.btn_apagar_4.setEnabled(True)
                        self.ui.btn_entrar_4.setEnabled(True)
                        self.ui.btn_entrar_4.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_4.clicked.connect(self.janela_pagar_4)

                        ######
                        self.ui.btn_editar_4.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_4.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_4.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 5:

                        # revelando o botões das contas
                        self.ui.btn_editar_5.setEnabled(True)
                        self.ui.btn_apagar_5.setEnabled(True)
                        self.ui.btn_entrar_5.setEnabled(True)
                        self.ui.btn_entrar_5.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_5.clicked.connect(self.janela_pagar_5)

                        ######
                        self.ui.btn_editar_5.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_5.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_5.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 6:

                        # revelando o botões das contas
                        self.ui.btn_editar_6.setEnabled(True)
                        self.ui.btn_apagar_6.setEnabled(True)
                        self.ui.btn_entrar_6.setEnabled(True)
                        self.ui.btn_entrar_6.setText(nome_completo)

                        # Apagar conta
                        # att conta criada
                        self.ui.btn_apagar_6.clicked.connect(self.janela_pagar_6)

                        ######
                        self.ui.btn_editar_6.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_6.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_6.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 7:

                        # revelando o botões das contas
                        self.ui.btn_editar_7.setEnabled(True)
                        self.ui.btn_apagar_7.setEnabled(True)
                        self.ui.btn_entrar_7.setEnabled(True)
                        self.ui.btn_entrar_7.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_7.clicked.connect(self.janela_pagar_7)

                        ######
                        self.ui.btn_editar_7.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_7.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_7.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 8:

                        # revelando o botões das contas
                        self.ui.btn_editar_8.setEnabled(True)
                        self.ui.btn_apagar_8.setEnabled(True)
                        self.ui.btn_entrar_8.setEnabled(True)
                        self.ui.btn_entrar_8.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_8.clicked.connect(self.janela_pagar_8)

                        ######
                        self.ui.btn_editar_8.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_8.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_8.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 9:

                        # revelando o botões das contas
                        self.ui.btn_editar_9.setEnabled(True)
                        self.ui.btn_apagar_9.setEnabled(True)
                        self.ui.btn_entrar_9.setEnabled(True)
                        self.ui.btn_entrar_9.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_9.clicked.connect(self.janela_pagar_9)

                        ######
                        self.ui.btn_editar_9.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_9.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_9.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 10:

                        # revelando o botões das contas
                        self.ui.btn_editar_10.setEnabled(True)
                        self.ui.btn_apagar_10.setEnabled(True)
                        self.ui.btn_entrar_10.setEnabled(True)
                        self.ui.btn_entrar_10.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_10.clicked.connect(self.janela_pagar_10)

                        ######
                        self.ui.btn_editar_10.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_10.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_10.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 11:

                        # revelando o botões das contas
                        self.ui.btn_editar_11.setEnabled(True)
                        self.ui.btn_apagar_11.setEnabled(True)
                        self.ui.btn_entrar_11.setEnabled(True)
                        self.ui.btn_entrar_11.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_11.clicked.connect(self.janela_pagar_11)

                        ######
                        self.ui.btn_editar_11.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_11.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_11.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 12:

                        # revelando o botões das contas
                        self.ui.btn_editar_12.setEnabled(True)
                        self.ui.btn_apagar_12.setEnabled(True)
                        self.ui.btn_entrar_12.setEnabled(True)
                        self.ui.btn_entrar_12.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_12.clicked.connect(self.janela_pagar_12)

                        ######
                        self.ui.btn_editar_12.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_12.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_12.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 13:

                        # revelando o botões das contas
                        self.ui.btn_editar_13.setEnabled(True)
                        self.ui.btn_apagar_13.setEnabled(True)
                        self.ui.btn_entrar_13.setEnabled(True)
                        self.ui.btn_entrar_13.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_13.clicked.connect(self.janela_pagar_13)

                        ######
                        self.ui.btn_editar_13.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_13.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_13.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 14:

                        # revelando o botões das contas
                        self.ui.btn_editar_14.setEnabled(True)
                        self.ui.btn_apagar_14.setEnabled(True)
                        self.ui.btn_entrar_14.setEnabled(True)
                        self.ui.btn_entrar_14.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_14.clicked.connect(self.janela_pagar_14)

                        ######
                        self.ui.btn_editar_14.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_14.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_14.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 15:

                        # revelando o botões das contas
                        self.ui.btn_editar_15.setEnabled(True)
                        self.ui.btn_apagar_15.setEnabled(True)
                        self.ui.btn_entrar_15.setEnabled(True)
                        self.ui.btn_entrar_15.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_15.clicked.connect(self.janela_pagar_15)

                        ######
                        self.ui.btn_editar_15.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_15.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_15.setStyleSheet('background-color:#6c6c6c')

                    elif self.cont == 16:

                        # revelando o botões das contas
                        self.ui.btn_editar_16.setEnabled(True)
                        self.ui.btn_apagar_16.setEnabled(True)
                        self.ui.btn_entrar_16.setEnabled(True)
                        self.ui.btn_entrar_16.setText(nome_completo)

                        # Apagar conta
                        self.ui.btn_apagar_16.clicked.connect(self.janela_pagar_16)

                        ######
                        self.ui.btn_editar_16.setIcon(QIcon('img\\img_navegar.png'))
                        self.ui.btn_apagar_16.setIcon(QIcon('img\\img_apagar.png'))
                        self.ui.user_16.setStyleSheet('background-color:#6c6c6c')
                except:
                    self.ui.input_saida.setStyleSheet('color:red;font: 87 italic 10pt "Segoe UI Black";')
                    self.ui.input_saida.setText('Erro inesperado, reinicie o aplicativo.')

    '''FUNÇÕES PARA APAGAR AS CONTAS'''
    def apagar_conta_1(self):
        self.ui.user_1.deleteLater()
        self.db.carregar_contas()

        aid = self.db.lista_correta[0]['id']
        nome_tabela = f'{str(self.db.lista_correta[0]["nome"]).replace(" ", "").capitalize()}' \
                      f'{str(self.db.lista_correta[0]["sobrenome"]).replace(" ", "").capitalize()}'

        self.db.excluir_conta(aid, nome_tabela, 0)
        self.tela_apagar.hide()

    def janela_pagar_1(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_1)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_2(self):
        self.db.carregar_contas()

        self.ui.user_2.deleteLater()
        aid = self.db.lista_correta[1]['id']
        nome_tabela = f'{str(self.db.lista_correta[1]["nome"]).replace(" ", "").capitalize()}' \
                      f'{str(self.db.lista_correta[1]["sobrenome"]).replace(" ", "").capitalize()}'

        self.db.excluir_conta(aid, nome_tabela, 1)
        self.tela_apagar.hide()


    def janela_pagar_2(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_2)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_3(self):
        self.db.carregar_contas()

        self.ui.user_3.deleteLater()
        aid = self.db.lista_correta[2]['id']
        nome_tabela = f'{str(self.db.lista_correta[2]["nome"]).replace(" ", "").capitalize()}' \
                      f'{str(self.db.lista_correta[2]["sobrenome"]).replace(" ", "").capitalize()}'

        self.db.excluir_conta(aid, nome_tabela, 2)
        self.tela_apagar.hide()


    def janela_pagar_3(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_3)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_4(self):
        self.ui.user_4.deleteLater()
        self.db.carregar_contas()

        aid = self.db.lista_correta[3]['id']
        nome_tabela = f'{str(self.db.lista_correta[3]["nome"]).replace(" ", "").capitalize()}' \
                      f'{str(self.db.lista_correta[3]["sobrenome"]).replace(" ", "").capitalize()}'

        self.db.excluir_conta(aid, nome_tabela, 3)
        self.tela_apagar.hide()


    def janela_pagar_4(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_4)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_5(self):
        self.db.carregar_contas()

        self.ui.user_5.deleteLater()
        aid = self.db.lista_correta[4]['id']
        nome_tabela = f'{str(self.db.lista_correta[4]["nome"]).replace(" ", "").capitalize().capitalize()}' \
                      f'{str(self.db.lista_correta[4]["sobrenome"]).replace(" ", "").capitalize().capitalize()}'
        print(f'TABELA {aid} EXCLUIDA')

        self.db.excluir_conta(aid, nome_tabela, 4)
        self.tela_apagar.hide()


    def janela_pagar_5(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_5)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_6(self):
        self.db.carregar_contas()
        self.ui.user_6.deleteLater()
        aid = self.db.lista_correta[5]['id']
        nome_tabela = f'{str(self.db.lista_correta[5]["nome"]).replace(" ", "").capitalize()}' \
                      f'{str(self.db.lista_correta[5]["sobrenome"]).replace(" ", "").capitalize()}'
        self.db.excluir_conta(aid, nome_tabela, 5)
        self.tela_apagar.hide()


    def janela_pagar_6(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_6)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_7(self):
        self.db.carregar_contas()
        self.ui.user_7.deleteLater()
        aid = self.db.lista_correta[6]['id']
        nome_tabela = f'{str(self.db.lista_correta[6]["nome"]).replace(" ", "").capitalize()}' \
                      f'{str(self.db.lista_correta[6]["sobrenome"]).replace(" ", "").capitalize()}'
        self.db.excluir_conta(aid, nome_tabela, 6)
        self.tela_apagar.hide()


    def janela_pagar_7(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_7)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_8(self):
        self.ui.user_8.deleteLater()
        self.db.carregar_contas()
        aid = self.db.lista_correta[7]['id']
        nome_tabela = f'{str(self.db.lista_correta[7]["nome"]).replace(" ", "").capitalize()}' \
                      f'{str(self.db.lista_correta[7]["sobrenome"]).replace(" ", "").capitalize()}'
        self.db.excluir_conta(aid, nome_tabela, 7)
        self.tela_apagar.hide()


    def janela_pagar_8(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_8)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_9(self):
        self.ui.user_9.deleteLater()
        self.db.carregar_contas()

        aid = self.db.lista_correta[8]['id']
        nome_tabela = f'{str(self.db.lista_correta[8]["nome"]).replace(" ", "")}' \
                      f'{str(self.db.lista_correta[8]["sobrenome"]).replace(" ", "")}'
        self.db.excluir_conta(aid, nome_tabela, 8)
        self.tela_apagar.hide()


    def janela_pagar_9(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_9)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_10(self):
        self.db.carregar_contas()
        self.ui.user_10.deleteLater()
        aid = self.db.lista_correta[9]['id']
        nome_tabela = f'{str(self.db.lista_correta[9]["nome"]).replace(" ", "")}' \
                      f'{str(self.db.lista_correta[9]["sobrenome"]).replace(" ", "")}'
        self.db.excluir_conta(aid, nome_tabela, 9)
        self.tela_apagar.hide()


    def janela_pagar_10(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_10)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_11(self):
        self.db.carregar_contas()
        self.ui.user_11.deleteLater()
        aid = self.db.lista_correta[10]['id']
        nome_tabela = f'{str(self.db.lista_correta[10]["nome"]).replace(" ", "")}' \
                      f'{str(self.db.lista_correta[10]["sobrenome"]).replace(" ", "")}'
        self.db.excluir_conta(aid, nome_tabela, 10)
        self.tela_apagar.hide()


    def janela_pagar_11(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_11)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_12(self):
        self.db.carregar_contas()
        self.ui.user_12.deleteLater()
        aid = self.db.lista_correta[11]['id']
        nome_tabela = f'{str(self.db.lista_correta[11]["nome"]).replace(" ", "")}' \
                      f'{str(self.db.lista_correta[11]["sobrenome"]).replace(" ", "")}'
        self.db.excluir_conta(aid, nome_tabela, 11)
        self.tela_apagar.hide()


    def janela_pagar_12(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_12)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_13(self):
        self.db.carregar_contas()
        self.ui.user_13.deleteLater()
        aid = self.db.lista_correta[12]['id']
        nome_tabela = f'{str(self.db.lista_correta[12]["nome"]).replace(" ", "")}' \
                      f'{str(self.db.lista_correta[12]["sobrenome"]).replace(" ", "")}'
        self.db.excluir_conta(aid, nome_tabela, 12)
        self.tela_apagar.hide()


    def janela_pagar_13(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_13)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_14(self):
        self.db.carregar_contas()
        self.ui.user_14.deleteLater()
        aid = self.db.lista_correta[13]['id']
        nome_tabela = f'{str(self.db.lista_correta[13]["nome"]).replace(" ", "")}' \
                      f'{str(self.db.lista_correta[13]["sobrenome"]).replace(" ", "")}'
        self.db.excluir_conta(aid, nome_tabela, 13)
        self.tela_apagar.hide()


    def janela_pagar_14(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_14)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_15(self):
        self.db.carregar_contas()

        self.ui.user_15.deleteLater()
        aid = self.db.lista_correta[14]['id']
        nome_tabela = f'{str(self.db.lista_correta[14]["nome"]).replace(" ", "")}' \
                      f'{str(self.db.lista_correta[14]["sobrenome"]).replace(" ", "")}'
        self.db.excluir_conta(aid, nome_tabela, 14)
        self.tela_apagar.hide()


    def janela_pagar_15(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_15)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)


    def apagar_conta_16(self):
        self.db.carregar_contas()
        self.ui.user_16.deleteLater()
        aid = self.db.lista_correta[15]['id']
        nome_tabela = f'{str(self.db.lista_correta[15]["nome"]).replace(" ", "")}' \
                      f'{str(self.db.lista_correta[15]["sobrenome"]).replace(" ", "")}'
        self.db.excluir_conta(aid, nome_tabela, 15)
        self.tela_apagar.hide()


    def janela_pagar_16(self):
        self.tela_apagar.show()
        self.tela_apagar.ui.btn_sim.clicked.connect(self.apagar_conta_16)
        self.tela_apagar.ui.btn_nao.clicked.connect(self.fechar_excluir)

    '''FUNÇÃO DE FECHAR JANELA DE EXLUIR'''
    def fechar_excluir(self):
        self.tela_apagar.close()

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
    bd = BD_add_conta.BD()

    if bd.verificar_admin():
        w.tela_inicial.show()
        go.exec_()
    else:
        w.tela_admin.show()
        go.exec_()
