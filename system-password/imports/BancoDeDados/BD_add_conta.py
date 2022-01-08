import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class BD:
    def __init__(self):
        self.conexao = sqlite3.connect(rf'{BASE_DIR}\users.db')
        self.cursor = self.conexao.cursor()
        self.lista = []
        self.lista_correta = []
        self.dict = {}
        self.criar_tabela_admin()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS contas ('
                            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'nome TEXT ,'
                            'sobrenome TEXT)')
        self.conexao.commit()

    def tabela_cada_conta(self, nome):
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {nome} ('
                            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'site TEXT,'
                            'senha TEXT)')
        self.conexao.commit()

    def inserir_contas(self, nome, sobrenome):
        consulta = f'INSERT INTO contas (nome, sobrenome) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, sobrenome))
        self.conexao.commit()

    def carregar_contas(self):
        try:
            self.cursor.execute('SELECT * FROM contas')
            for v in self.cursor.fetchall():
                aid, nome, sobrenome = v
                self.dict['id'] = aid
                self.dict['nome'] = nome
                self.dict['sobrenome'] = sobrenome
                self.lista.append(self.dict.copy())
        except:
            pass
        else:
            for v in self.lista:
                if v in self.lista_correta:
                    pass
                else:
                    self.lista_correta.append(v)

    def verificar_admin(self):
        self.cursor.execute('SELECT * FROM admin')
        cont = 0
        if self.cursor.fetchall():
            cont = 1

        return cont

    def criar_tabela_admin(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS admin ('
                            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'senha TEXT UNIQUE)')
        self.conexao.commit()

    def inserir_admin(self, senha):
        consulta = f'INSERT OR IGNORE INTO admin (senha) VALUES (?)'
        self.cursor.execute(consulta, (senha,))
        self.conexao.commit()

    def excluir_conta(self, aid, nome_tabela, index):
        try:
            self.cursor.execute(f"DELETE FROM contas WHERE id={aid}")
        except:
            print('ERRO AO EXCLUIR CONTA')
        try:
            self.cursor.execute(f'DROP TABLE {nome_tabela}')
            self.conexao.commit()
        except:
            print('\033[1;31mERRO AO EXCLUIR TABELA\033[m')


