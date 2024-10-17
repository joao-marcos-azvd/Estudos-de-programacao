from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)
BANCO = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/dados', methods = ['GET', 'POST']) #Digo pra rota que ela vai ter 2 methodos (GET e POST)
def dados():
    # Se o methodo for GET, a requisição foi feita pela url 
    # Logo o sistema não vai permitir isso e vai retorna o usuário novamente pra pagina de cadastro.
    if request.method == 'GET':
        # Retorna o usuário para cadastro
        return redirect(url_for('cadastro'))

  # Se a requisição for POST o sistema continua com seu fluxo
    else:
        # Pegando o valor do email do form, usando o nome que foi dado no input ('f_email")
        email = request.form['f_email']
        # Pega o valor da senha do form, usando o nome que foi dado no input ('f_senha')
        senha = request.form['f_senha']
        
        # Aqui deu pau
        dados = {}
        dados['email'] = email
        dados['senha'] = senha
        BANCO.append(dados.copy)
        return BANCO
        
