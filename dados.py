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

# 5 - Editar Dados
def editar_dados(id, nome=None, ano=None, nota=None):
    """
    Atualiza campos de um filme. Só altera o que for != None.
    Retorna quantas linhas foram afetadas.
    """
    conexao = conecta_db()
    cursor = conexao.cursor()

    sets = []
    params = []

    if nome is not None:
        nome = str(nome).strip()
        if nome != "":
            sets.append("nome = ?")
            params.append(nome)

    if ano is not None:
        sets.append("ano = ?")
        params.append(int(ano))

    if nota is not None:
        sets.append("nota = ?")
        params.append(float(nota))

    if not sets:
        conexao.close()
        return 0  # nada para atualizar

    sql = f"UPDATE filmes SET {', '.join(sets)} WHERE id = ?"
    params.append(int(id))

    cursor.execute(sql, params)
    conexao.commit()
    afetadas = cursor.rowcount 
    conexao.close()
    return afetadas

    
    sql = f"UPDATE filmes SET {', '.join(sets)} WHERE id = ?"
    params.append(int(id))

    cursor.execute(sql, params)
    conexao.commit()
    afetadas = cursor.rowcount()
    conexao.close()
    return afetadas


# 6 - Deletar Dados
def deletar_dados(ids):
    con = conecta_db()
    cur = con.cursor()

    # aceita 1 id (int/str/np.int64) ou coleção (list/tuple/set)
    if isinstance(ids, (list, tuple, set)):
        ids = [int(x) for x in ids]
        if not ids:
            con.close()
            return 0
        placeholders = ",".join("?" * len(ids))
        sql = f"DELETE FROM filmes WHERE id IN ({placeholders})"
        cur.execute(sql, ids)
    else:
        cur.execute("DELETE FROM filmes WHERE id = ?", (int(ids),))  # tupla de 1 elemento

    con.commit()
    afetadas = cur.rowcount
    con.close()
    return afetadas
