from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Classe 
class Base(DeclarativeBase):
    pass

# Instancia do SQLAlchemy
db = SQLAlchemy(model_class=Base)
class User(db.Model):
    __tablename__= 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] 