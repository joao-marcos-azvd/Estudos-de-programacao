# O arquivo __init__.py serve pra poder permitir que tudo seja importado
import sqlite3
import os

DATABASE = 'database.db'
dirname = os.path.dirname(os.path.realpath(__file__))

# função pra conectar o banco
def get_connection():    
    conn = sqlite3.connect(os.path.join(dirname, DATABASE))
    conn.row_factory = sqlite3.Row
    return conn
