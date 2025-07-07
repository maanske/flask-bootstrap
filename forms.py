from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = TextAreaField('Mensagem', validators=[DataRequired()])
    respondido = BooleanField('Respondido')
    submit = SubmitField('Enviar')
