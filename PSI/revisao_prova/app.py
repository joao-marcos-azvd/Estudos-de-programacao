# Só quero lembrar que esses contextos forma definidos porque eu não tô trabalhando ccom rotas, então só é necessário o de criar o banco, quando se trabalha com rotas

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Instância do Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'  # Aqui eu estou indicando que vou usar SQLite
# Acho que essa parte de baico não precisa
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Evita warnings 

db = SQLAlchemy(app) #Instância do banco, como eu posso chamar

# Criando uma classe de usuários apartir do SQLAlchemy
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True) #Definição do ID
    nome = db.Column(db.String(80), nullable=False) #Definição do nome
    email = db.Column(db.String(120), unique=True, nullable=False) #Definição do E-mail

    # Aqui eu defino uma mensagem padrão para mostrar os usuários
    def __repr__(self):
        return f'<Usuario {self.nome}>'

# Definimdo um contexto para a aplicação criar um banco.
with app.app_context():
    db.create_all()

# Aqui eu defino um contexto na aplicação para adicionar um novo usuário no banco
with app.app_context():
    novo_usuario = Usuario(nome="João", email="joao@email.com") #Crio um novo usuário
    # Os dois passos a seguir são para adiciona-los no banco
    db.session.add(novo_usuario) 
    db.session.commit()

# Aqui eu defino um contexto para a aplicação pegar os usuários do banco e listar
with app.app_context():
    usuarios = Usuario.query.all()  # Retorna todos os usuários
    usuario = Usuario.query.filter_by(nome="João").first()  # Retorna um usuário específico

    print(usuarios)  # Lista de usuários
    print(usuario)   # Primeiro usuário com nome "João"

# Defino um contexto para adicionar um novo email para o primiero usuário com o nome "João"
with app.app_context():
    usuario = Usuario.query.filter_by(nome="João").first() #Pego o primeiro user com o parametro passado, no caso o nome joão
    usuario.email = "novoemail@email.com" # Mudo o email do usuário para "novoemail@email.com"
    db.session.commit() # Confirmo a mudança

# Defino um contexto para a aplicação deletar um user
with app.app_context():
    usuario = Usuario.query.filter_by(nome="João").first() # Seleciono o primeiro usuário com o nome "João"
    db.session.delete(usuario) # Deleto ele do banco
    db.session.commit() # Confirmo a mudança