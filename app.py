from flask import Flask, render_template, redirect, url_for, request
from models import db, Contato
from forms import ContatoForm
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contatos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        contato = Contato(
            nome=form.nome.data,
            email=form.email.data,
            assunto=form.assunto.data,
            mensagem=form.mensagem.data,
            respondido=form.respondido.data
        )
        db.session.add(contato)
        db.session.commit()
        return redirect(url_for('contato_lista'))  
    return render_template('contato.html', form=form)

@app.route('/contatos')
def contato_lista():
    pesquisa = request.args.get('pesquisa')
    if pesquisa:
        contatos = Contato.query.filter(Contato.nome.ilike(f'%{pesquisa}%')).all()
    else:
        contatos = Contato.query.all()
    return render_template('contato_lista.html', contatos=contatos)

if __name__ == '__main__':
    app.run(debug=True)
