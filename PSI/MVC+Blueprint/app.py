from flask import Flask
# Importando da pasta controllers (Biblioteca) os arquivo users e books (Funções)
# Lá todas as rotas e ações de usesr e books já estão prontas, aqui é só rodar.
from controllers import users, books

"""Ok, oque é o MVC?
MVC é a sigla pra Model Viwer Control, isso não é código e sim a forma de organização do código. 
"""

# Instância do Flask
app = Flask(__name__)

# Registra as Blueprits de cada controller
app.register_blueprint(users.bp) #nome_do_arquivo.nome_da_instancia_blueprint
app.register_blueprint(books.bp) #nome_do_arquivo.nome_da_instancia_blueprint
