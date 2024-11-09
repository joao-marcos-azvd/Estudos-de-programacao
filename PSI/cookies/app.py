from flask import Flask, render_template, make_response, request
# Funções necesárias para a criação dos cookies: make_response, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Aqui é onde eu vou criar o cookie:
@app.route('/setcookie', methods=['GET', 'POST'])
def criar_cookie():
    # Só posso criar um cookie se o método usado na requisição for post
    if request.method == 'POST':

        # Pegando o valor do cookie do form da página ínicial
        valor = request.form['nome']

        # Criando uma resposta
        respota = make_response(render_template('readcookie.html'))

        # Criando o cookie ('primeiro_cookie') e atribuindo um valor (valor) a ele
        respota.set_cookie('primeiro_cookie', valor)

        return respota
    
# Retornamdo o valor do cookie
@app.route('/getcookie')
def getcookie():
    
    # Pegando valor do cookie e guardando em uma variável
    conteudo = request.cookies.get('primeiro_cookie')

    return f"O valor do cookie é: {conteudo}"

# Deletando o cookie
@app.route('/deletecookie')
def deletecookie():
    
    # Criando uma resposta (Não é obrigatório)
    resp = make_response("Cookie removido do sistema!")

    # Atribui uma string vazia ao valor do cookie ('primeiro_cookie', '') e define a data de expiração do cookie como uma data no passado (expires=0).
    resp.set_cookie('primeiro_cookie', '', expires=0)
    
    return resp
