import sqlite3

conn = sqlite3.connect('banco_funcionarios.db')

with open('banco/flaskdb.sql') as arquivo:
    conn.executescript(arquivo.read())
    conn.close()
