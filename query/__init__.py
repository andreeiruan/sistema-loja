"""Aqui estão as querys que serão executados no banco de dados MySQL"""
import pymysql


def conexao(h, u, s):
    connect = pymysql.connect(host=h, user=u, passwd=s)
    return connect

def create_table_users(h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute("USE loja;")
    cursor.execute("CREATE TABLE IF NOT EXISTS users("
                   "user VARCHAR(10),"
                   "senha VARCHAR(20))")
    con.commit()
    cursor.close()


def create_database(h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()

    cursor.execute("""CREATE DATABASE IF NOT EXISTS loja;""")
    con.commit()
    cursor.close()


def create_table_clientes(h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()

    cursor.execute("""USE loja;""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (id INT NOT NULL AUTO_INCREMENT, nome VARCHAR(20), 
            sobrenome VARCHAR(20), cpf CHAR(11) UNIQUE, email VARCHAR(35), telefone CHAR(11) , 
            data_nasc DATE, PRIMARY KEY (id));""")
    con.commit()
    cursor.close()


def create_table_funcionarios(h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute('USE loja;')
    cursor.execute("""CREATE TABLE IF NOT EXISTS funcionarios (id INT NOT NULL AUTO_INCREMENT, nome VARCHAR(20),
          sobrenome VARCHAR(30), cpf CHAR(11) UNIQUE, cargo VARCHAR(25), telefone CHAR(11), 
          email VARCHAR(35), admissao DATE, 
          nasc DATE, PRIMARY KEY(id));""")
    con.commit()
    cursor.close()


def create_table_produtos(h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute('USE loja;')
    cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (id INT NOT NULL auto_increment, 
                      nome VARCHAR(30), marca VARCHAR(30), preco FLOAT, descricao TEXT, 
                      estoque INT,
                      PRIMARY KEY (id));""")
    con.commit()
    cursor.close()


def insert_produto(nome, marca, preco, descricao, estoque, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute('USE loja;')
    cursor.execute(f'INSERT INTO produtos VALUES (DEFAULT, "{nome.title()}", "{marca}", '
                   f'"{preco}", "{descricao}", "{estoque}")')
    con.commit()
    cursor.close()


def insert_funcionario(nome, sobrenome, cpf, cargo, telefone, email, admissao, nasc, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute('USE loja;')
    cursor.execute(f'INSERT INTO funcionarios VALUES '
                   f'(DEFAULT, "{nome}", "{sobrenome}", "{cpf}", "{cargo}", "{telefone}", "{email}",'
                   f'"{admissao}", "{nasc}")')
    con.commit()
    cursor.close()


def insert_cliente(nome, sobrenome, cpf, telefone, nasc, email, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute("USE loja;")
    cursor.execute(f'INSERT INTO clientes VALUES (DEFAULT, "{nome}", "{sobrenome}" , "{cpf}",'
                   f' "{email}", "{telefone}", "{nasc}");')
    con.commit()
    cursor.close()


def insert_user(nome, senha, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute("USE loja;")
    cursor.execute(f'INSERT INTO users VALUES ("{nome}", "{senha}")')


def getter(tabela, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()

    cursor.execute('USE loja;')
    cursor.execute(f'SELECT * FROM {tabela}')
    dados = cursor.fetchall()
    cursor.close()
    return dados


def get_produto(codigo, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute("use loja;")
    cursor.execute(f'''SELECT id, nome, marca, CAST(preco AS CHAR(15)), descricao, estoque
                        FROM produtos WHERE id = {codigo};''')
    dados = cursor.fetchall()
    cursor.close()
    return dados


def get_funcionario(cpf, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute("use loja;")
    cursor.execute(f'''SELECT id, nome, sobrenome, cpf, cargo, telefone, email, CAST(admissao AS CHAR(10)), 
                   CAST(nasc AS CHAR(10)) 
                   FROM funcionarios 
                   WHERE cpf = "{cpf}";''')
    dados = cursor.fetchall()
    cursor.close()
    return dados


def get_cliente(cpf, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute("USE loja;")
    cursor.execute(f'''SELECT id, nome, sobrenome, 
    cpf, email, telefone , CAST(data_nasc AS CHAR(10))  FROM clientes WHERE cpf = "{cpf}";''')
    dados = cursor.fetchall()
    cursor.close()
    return dados


def get_users(h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute("USE loja;")
    cursor.execute("SELECT * FROM users;")
    dados = cursor.fetchall()
    cursor.close()
    return dados


def update_funcionario(codigo, nome, sobrenome, cpf, cargo, telefone, email, admissao, nasc, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute('USE loja;')
    cursor.execute(f'''UPDATE funcionarios 
                        SET nome = "{nome}", 
                            sobrenome = "{sobrenome}",
                            cpf = "{cpf}", 
                            cargo = "{cargo}",
                            telefone = "{telefone}", 
                            email = "{email}", 
                            admissao = "{admissao}", 
                            nasc = "{nasc}" 
                       WHERE id = {codigo};''')
    con.commit()
    cursor.close()


def update_cliente(codigo, nome, sobrenome, cpf, telefone, email, nasc, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute('USE loja;')
    cursor.execute(f'''UPDATE clientes
                        SET nome = "{nome}", 
                            sobrenome = "{sobrenome}",
                            cpf = "{cpf}", 
                            telefone = "{telefone}", 
                            email = "{email}",
                            data_nasc = "{nasc}"
                    WHERE id = {codigo};''')
    con.commit()
    cursor.close()


def update_produto(codigo, nome, marca, preco, descricao, estoque, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute('USE loja;')
    cursor.execute(f'''UPDATE produtos
                            SET nome = "{nome}",
                                marca = "{marca}",
                                preco = "{preco}",
                                descricao = "{descricao}",
                                estoque = {estoque}
                        WHERE codigo = {codigo}''')
    con.commit()
    cursor.close()


def delete_funcionario(cpf, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute('USE loja;')
    cursor.execute(f'''DELETE FROM funcionarios
                       WHERE cpf = "{cpf}"''')
    con.commit()
    cursor.close()


def delete_cliente(cpf, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute('USE loja;')
    cursor.execute(f'''DELETE FROM clientes
                           WHERE cpf = "{cpf}"''')
    con.commit()
    cursor.close()


def delete_produto(cod, h, u, s):
    con = conexao(h, u, s)
    cursor = con.cursor()
    cursor.execute('USE loja;')
    cursor.execute(f'''DELETE FROM produtos
                       WHERE codigo = {cod} ''')
    con.commit()
    cursor.close()
