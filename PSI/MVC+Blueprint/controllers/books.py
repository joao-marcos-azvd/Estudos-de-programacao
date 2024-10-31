# Importando do Flask tudo que vai ser usado
from flask import Flask, render_template, url_for, request, Blueprint, redirect

# Importando modelos da pasta models,
# Esse modelos são POO, ou seja, são objetos com funções "prontas"
from models.user import User
from models.book import Book

# Instância de Blueprint
bp = Blueprint('books', __name__, url_prefix='/books')
"""
'books' -> Não sei porque, mas tem que botar um nome
__name__ -> Faz a instância da Blueprint
url_prefix -> É o prefixo da URL, ou seja toda página relacionada a book vai ser /books/...
"""



# Rotas são definidas agora com a instância bp (serve igual ao app)
@bp.route('/')
def index():
    # Retornando o templa de pasta templates/books/
    return render_template('books/index.html', books = Book.all())

# Utilizando a classe Book
@bp.route('/register', methods=['POST', 'GET'])
def register():
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        user = request.form['user']

        # Classe
        book = Book(titulo, user)
        book.save()
        return redirect(url_for('books.index'))


    return render_template('books/register.html', users=User.all())
