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