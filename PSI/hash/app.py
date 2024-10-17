from flask import Flask, request, redirect, url_for, render_template, flash
# Importando a biblioteca werkzeug.security e suas funções que vamos usar
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
# Definição de sesão no Flask
app.config['SECRET_KEY'] = 'testandocripto'
# Lista que vai dervir de Banco de dados temporário 
lista = []
# Página inícial
@app.route('/', methods=['POST','GET'])
def index():
    # Se o método usado pra acessar a página for "POST" (Pelo envio do form), vai ser pego os dados e adicionados no BD.
    if request.method == 'POST':
        # Pegando nome
        nome = request.form['nome']
        # Pegando senha
        senha= request.form['senha']
        # Guaradando dados
        dados = {
            'nome': nome,
            'senha': senha,
            # Gerando HASH
            # O generte_password_hash() é uma função da biblioteca werkzeug.security que serve para criar HASHs de senhas  
            'hash': generate_password_hash(senha)
        }
        # Adicionando dados ao BD 
        lista.append( dados )
        # Retornando a página
        return redirect(url_for('index'))
    else:
        # Se o método de requisição for "GET" retorna a página pra pegar os dados
        return render_template('index.html',users=lista)
# Rota de adivinhar a senha com base no hash gerado por ela 
@app.route('/adivinhar/<string:nome>', methods=['POST'])
def adivinhar(nome):  
    # Pega a senha que você acha que é do hash  
    senha = request.form['senha']

    # Sai analisando usuário por usuário]
    # SÓ QUE NÃO TÁ PRESTANDO
    for user in lista:
        # São passados 2 parametros para o check_password_hash(P1, P2), o user['hash'] e a senha, com isso ele nalisa se aquele hash (user['hash']) realmente foi gerado com base naquela senha (senha)
        if user['nome'] == nome and check_password_hash(user['hash'], senha):
            # Se tudo estiver certo ele retorna uma mensagem de sucesso
            flash('Você acertou a senha', 'success')
            return redirect(url_for('index'))  
    # Se não, aí a gente já sabe, né? Não vai patrao      
    flash('Você errou a senha', 'error')
    return redirect(url_for('index'))
