from flask import Flask, render_template, url_for, request, redirect
import sqlite3

app = Flask(__name__)

def obter_conexao_bd():
    conn = sqlite3.connect('banco_funcionarios.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/cadastrar', methods = ['GET', 'POST'])
def cadastrar():
    if  request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        with obter_conexao_bd() as conexao:
            conexao.execute("INSERT INTO funcionarios(nome, email, cpf) VALUES(?, ?, ?)", (nome, email, cpf))
            conexao.commit()
        return redirect(url_for('mostrar'))
    else: 
        return render_template('pages/cadastrar.html')

@app.route('/mostrar')
def mostrar():
    with obter_conexao_bd() as conexao:
        funcionarios = conexao.execute('SELECT nome FROM funcionarios').fetchall()
    return render_template('pages/mostrar.html', users = funcionarios)
