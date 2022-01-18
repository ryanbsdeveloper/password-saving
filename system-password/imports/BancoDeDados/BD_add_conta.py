import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class BD:
    def __init__(self):
        self.conexao = sqlite3.connect(rf'{BASE_DIR}\users.db')
        self.cursor = self.conexao.cursor()
        self.nome_da_tabela = ''
        self.lista = []
        self.lista2 = []
        self.lista_correta = []
        self.lista_registro = []
        self.dict = {}
        self.dict2 = {}
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS contas ('
                            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'nome TEXT ,'
                            'sobrenome TEXT,'
                            'avatar TEXT)')
        self.conexao.commit()

    def tabela_cada_conta(self, nome):
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {nome} ('
                            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'site TEXT,'
                            'senha TEXT,'
                            'email TEXT)')
        self.conexao.commit()

    def inserir_contas(self, nome, sobrenome, avatar):
        consulta = f'INSERT INTO contas (nome, sobrenome, avatar) VALUES (?, ?, ?)'
        self.cursor.execute(consulta, (nome, sobrenome, avatar))
        self.conexao.commit()

    def carregar_contas(self):
        try:
            self.cursor.execute('SELECT * FROM contas')
            for v in self.cursor.fetchall():
                aid, nome, sobrenome, avatar = v
                self.dict['id'] = aid
                self.dict['nome'] = nome
                self.dict['sobrenome'] = sobrenome
                self.dict['avatar'] = avatar
                self.lista.append(self.dict.copy())
        except:
            pass
        else:
            for v in self.lista:
                if v in self.lista_correta:
                    pass
                else:
                    self.lista_correta.append(v)

    def excluir_conta(self, aid, nome_tabela):
        try:
            self.cursor.execute(f"DELETE FROM contas WHERE id={aid}")
        except:
            print('ERRO AO EXCLUIR CONTA')
        try:
            self.cursor.execute(f'DROP TABLE {nome_tabela}')
            self.conexao.commit()
        except:
            pass
        
    def excluir_registro(self, aid):
            try:
                self.cursor.execute(f"DELETE FROM {self.nome_da_tabela} WHERE id={aid}")
            except:
                print('ERRO AO EXCLUIR CONTA')
            else:
                self.conexao.commit()

    def carregar_registros(self):
            try:
                self.cursor.execute(f'SELECT * FROM {self.nome_da_tabela}')
                for v in self.cursor.fetchall():
                    aid, site, senha, email = v
                    self.dict2['id'] = aid
                    self.dict2['site'] = site
                    self.dict2['senha'] = senha
                    self.dict2['email'] = email
                    self.lista2.append(self.dict2.copy())
            except:
                pass
            else:
                for v in self.lista2:
                    if v in self.lista_registro:
                        pass
                    else:
                        self.lista_registro.append(v)

    def inserir_registro(self, site, senha, email):
            consulta = f'INSERT INTO {self.nome_da_tabela} (site, senha, email) VALUES (?, ?, ?)'
            self.cursor.execute(consulta, (site, senha, email))
            self.conexao.commit()

if __name__ == '__main__':
    bd = BD()
    bd.nome_da_tabela = 'RyanSilva'
    bd.carregar_registros()
    print(bd.lista_registro)