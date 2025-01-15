from flask import Flask, render_template, request
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.db'

# Registra a aplicação no SQLAlchemy
db.init_app(app)

# Só é usado uma vez
# Tá funcionando no contexto da aplicação
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    
    user = User(nome='Mundim')
    db.session.add(user)
    db.session.commit()

    return render_template("listar.html")