import mysql.connector

def criar_conexao():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='estoque_flet'
    )

def validar_login(email, senha):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM usuarios WHERE email=%s AND senha=%s", (email, senha))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def listar_produtos(filtro=""):
    conn = criar_conexao()
    cursor = conn.cursor()

    sql = "SELECT id, nome_produto, quantidade, estoque_minimo, categoria, lote, validade FROM produtos"

    if filtro:
        sql += " WHERE nome_produto LIKE %s"
        cursor.execute(sql, (f"%{filtro}%",))
    else:
        cursor.execute(sql)

    produtos = cursor.fetchall()
    conn.close()
    return produtos

def salvar_produto(nome, cat, lote, val, qtd, min_estoque):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = """INSERT INTO produtos
        (nome_produto, categoria, lote, validade, quantidade, estoque_minimo) 
        VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql,(nome, cat, lote, val, qtd, min_estoque))
    conn.commit()
    conn.close()

def deletar_produto(id_prod):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id=%s", (id_prod))
    conn.commit()
    conn.close()

def registrar_movimentacoes(id_prod, qtd, tipo, id_user):
    conn = criar_conexao()
    cursor = conn.cursor()

    sql_hist = "INSERT INTO movimentacoes (tipo, quantidade, id_usuario, id_produto) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_hist, (tipo, qtd, id_user, id_prod))

    if tipo == "Entrada":
        sql_update = "UPDATE produtos SET quantidade = quantidade + %s WHERE id=%s"
    else:
        sql_update = "UPDATE produtos SET quantidade = quantidade - %s WHERE id=%s"

    cursor.execute(sql_update, (qtd, id_prod))
    conn.commit()

    cursor.execute("SELECT quantidade, estoque_minimo, nome_produto, FROM produtos WHERE id=%s", (id_prod))
    dados = cursor.fetchone()
    conn.close()

    if dados and dados[0] < dados[1]:
        return True, dados[2]
    return False