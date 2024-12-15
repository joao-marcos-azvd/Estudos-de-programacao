# Importando coisas do Flask
from flask import Flask, render_template
# Importando sqlite3
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')