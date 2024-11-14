# ESSE CÓDIGO NÃO É MEU! É DE ARIANE!
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha_chave_secreta'  # Para exibir mensagens flash

# Configuração do banco de dados SQLAlchemy
DATABASE_URI = 'sqlite:///meu_banco.db'

# Criação do motor do banco de dados
engine = create_engine(DATABASE_URI, connect_args={"check_same_thread": False})

# Base para criar as classes
Base = declarative_base()

# Definição do modelo de Usuário
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    senha = Column(String(120), nullable=False)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criação de uma fábrica de sessões
Session = sessionmaker(bind=engine)
session = Session()

# Rota de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        # Verifica se o usuário já está cadastrado
        usuario_existente = session.query(Usuario).filter_by(email=email).first()
        if usuario_existente:
            flash("Esse email já está cadastrado. Tente outro.")
            return redirect(url_for('cadastro'))

        # Adiciona o novo usuário ao banco de dados
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        session.add(novo_usuario)
        session.commit()
        flash("Cadastro realizado com sucesso!")
        return redirect(url_for('login'))

    return render_template('cadastro.html')

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Busca o usuário pelo email e senha
        usuario = session.query(Usuario).filter_by(email=email, senha=senha).first()
        if usuario:
            flash(f"Bem-vindo, {usuario.nome} !")
            return redirect(url_for('lista_usuarios'))
        else:
            flash("Email ou senha incorretos.")
            return redirect(url_for('login'))

    return render_template('login.html')

# Rota para listar usuários
@app.route('/lista_usuarios')
def lista_usuarios():
    usuarios = session.query(Usuario).all()  # Recupera todos os usuários cadastrados
    return render_template('home.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
