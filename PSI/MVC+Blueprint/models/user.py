# Modelo de User

# Impotando a função de conexão do banco
from database import get_connection

class User:
    # Metodo construtor
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    # Função para salvar os dados
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO users(email, nome) values(?,?)", (self.email, self.nome))
        conn.commit()
        conn.close()
        return True
    
    # Função para pegar os valores do banco
    @classmethod #Decorador que serve para não usar o .self
    def all(cls):
        conn = get_connection()
        users = conn.execute("SELECT * FROM users").fetchall()
        return users