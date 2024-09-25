# Código usado pra criar/iniciar o banco 
# Tem que rodar no terminal python ( python <nome_do_arquivo> )
import sqlite3

conn = sqlite3.connect('database.db')

with open('db/flask-sqlite.sql') as arquivo:
    conn.executescript(arquivo.read())

