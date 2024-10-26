from flask import Flask
# Importando da pasta controllers (Biblioteca) os arquivo users e books (Funções)
from controllers import users, books

"""Ok, oque é o MVC?
MVC é a sigla pra Model Viwer Control, isso não é código e sim a forma de organização do código. 
"""

# Instância do Flask
app = Flask(__name__)

# Ainda não sei
# EXPICAR!!!
app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
