from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Isso aqui define a chave da sessão
app.config['SECRET_KEY'] = 'testandocripto'

# Lista pra armazenar os dados coletados
lista = []

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        # Pegando valor de nome do formulário
        nome = request.form['nome']

        # Pegando valor da senha do formulário
        senha= request.form['senha']

        dados = {
            'nome': nome,
            'senha': senha,

            # Gerando HASH da senha com uma função
            'hash': generate_password_hash(senha)
        }
        lista.append( dados )
        return redirect(url_for('index'))
    
    return render_template('index.html',users=lista)

@app.route('/adivinhar/<string:nome>', methods=['POST'])
def adivinhar(nome):    
    senha = request.form['senha']
    for user in lista:
        # Verificando dados
        if user['nome'] == nome and check_password_hash(user['hash'], senha):
            flash('Você acertou a senha', 'success')
            return redirect(url_for('index'))        
    flash('Você errou a senha', 'error')
    return redirect(url_for('index'))