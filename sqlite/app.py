# Importando o flask e suas funções
from flask import Flask, render_template, url_for, request, redirect
# Importação do sqlite
import sqlite3

app = Flask(__name__)

# Função pra obter a conexão com o banco "database.db"
def obter_conexao():
    # Conectando o banco
    conn = sqlite3.connect('database.db')
    # Configuração pra pegar os dados do banco na forma de dicionário
    conn.row_factory = sqlite3.Row
    # Retornando conexão
    return conn

# Página inicial
@app.route('/')
def index():
    return render_template('pages/index.html')

# Rota para criar novos usuários
@app.route('/create', methods=['GET','POST']) 
def create_user():
    # Pegando método da requisição
    if request.method == 'POST':
        # Pegando o valor do nome do form (por meio do request) na página html
        nome = request.form['nome']
        # Obtendo conexão por meio da função "obter_conexao"
        conect = obter_conexao()
        # Função do sqlite3 que executa comando MySQL, nesse caso o Insert, tendo como valor passado o nome
        conect.execute("INSERT INTO usuarios(nome) VALUES(?)", (nome,))
        # .commit serve para alterar/adicionar os dados no banco
        conect.commit()
        # Fecanhdo conexão
        conect.close()
        # Redirecionando para rota "listar"
        return redirect(url_for('listar'))
    else:
        return render_template('pages/create-user.html')

@app.route('/listar')
def listar():
    # Obtendo conexão por meio da função "obter_conexao" 
    conect = obter_conexao()
    # Criando um dicionário com os valores do banco
    users = conect.execute('SELECT nome FROM usuarios').fetchall()
    # .fetchall serve pra pegar valores
    # Fecanhdo conexão
    conect.close()
     # Passsando dicionário como parametro para a página "listar-users.html"
    return render_template('pages/listar-users.html', users=users)
