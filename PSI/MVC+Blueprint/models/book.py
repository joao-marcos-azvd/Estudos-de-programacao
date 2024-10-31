# Modelo de book

# Impotando de database a função get_connection para fazer conexão com o banco
from database import get_connection

# Classe Book. Responsável por todas as ações de Book.
# Vai ser utilizada na pasta controlles, para facilitar o trabalho e não ter que tá toda hora criando funções
class Book:
    # Metodo construtor
    def __init__(self, titulo, user_id):
        self.titulo = titulo
        self.user_id = user_id

    # Função pra salavar os dados
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO books(titulo, user_id) values(?,?)", (self.titulo, self.user_id))
        conn.commit()
        conn.close()
        return True

    # Responsável por pegar os valores do banco
    @classmethod  #Decorador que serve para não usar o .self
    def all(cls):
        conn = get_connection()
        books = conn.execute("SELECT * FROM books").fetchall()
        return books