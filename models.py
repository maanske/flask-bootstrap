from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    assunto = db.Column(db.String(100), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)
    respondido = db.Column(db.Boolean, default=False)
