# Importando as "ferramentas" flask
from flask import render_template, Blueprint, url_for, request, flash, redirect
# Importando modelo user da pasta models.user
from models.user import User

# Instância do Blueprint
bp = Blueprint(name='users', import_name=__name__, url_prefix='/users')
# Nome, instância, préfixo da url


# Rotas com a instância bp (serve igual o app)
# Os templates estão sendo pegos da pasta templates/users/
# As funções estão sendo puxadas da pasta models/
# Os outros procedimemtos eu entendo
@bp.route('/')
def index():
    return render_template('users/index.html', users = User.all())

@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        nome= request.form['nome']

        if not email:
            flash('Email é obrigatório')
        else:
            user = User(email, nome)
            user.save()
            return redirect(url_for('users.index'))
    
    return render_template('users/register.html')
