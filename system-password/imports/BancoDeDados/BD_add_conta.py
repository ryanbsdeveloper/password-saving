import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class BD:
    def __init__(self):
        self.conexao = sqlite3.connect(rf'{BASE_DIR}\users.db')
        self.cursor = self.conexao.cursor()

    def criar_tabela(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS contas ('
                            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'nome TEXT,'
                            'sobrenome TEXT)')
        self.conexao.commit()

    def inserir_conta(self, nome, sobrenome):
        consulta = f'INSERT INTO contas (nome, sobrenome) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, sobrenome))
        self.conexao.commit()

    def mostrar_conta(self):
        self

    def verificar_admin(self):
        self.cursor.execute('SELECT * FROM admin')
        cont = 0
        if self.cursor.fetchall():
            cont = 1

        return cont

    def inserir_admin(self, senha):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS admin ('
                            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'senha TEXT UNIQUE)')
        self.conexao.commit()

        consulta = f'INSERT OR IGNORE INTO admin (senha) VALUES (?)'
        self.cursor.execute(consulta, (senha,))
        self.conexao.commit()

