import sqlite3


# 1 - Conectando o DB
def conecta_db():
    conexao = sqlite3.connect('titulo.db') # altere o nome do DB para o que vc desejar
    return conexao

# 2 - Criar Tabela (somente uma vez)
def cria_tabela():
    conexao = conecta_db()
    cursor = conexao.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        nota REAL NOT NULL
        )
        """
    )
    conexao.commit()
    conexao.close()

# 3 - Inserir dados
def insere_dados(nome, ano, nota):
    conexao = conecta_db()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO filmes (nome, ano, nota)
        VALUES (?,?,?)
        """,
        (nome, ano, nota)
    )

    conexao.commit()
    conexao.close()

# 4 - Listagem de Dados
def obter_dados():
    conexao = conecta_db()
    cursor = conexao.cursor()
    cursor.execute(
        """
        SELECT * FROM filmes
        """
    )
    dados = cursor.fetchall()
    conexao.close()
    return dados