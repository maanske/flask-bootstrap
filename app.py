from flask import Flask, request, redirect, url_for
from models import db, Contato
from forms import ContatoForm
from flask_migrate import Migrate
from flask import render_template_string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contatos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Início</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container mt-5">
            <h1>Bem-vindo ao projeto Flask</h1>
            <a href="/contato" class="btn btn-primary">Novo Contato</a>
            <a href="/contatos" class="btn btn-secondary">Listar Contatos</a>
        </div>
    </body>
    </html>
    '''

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
    return f'''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8" />
        <title>Novo Contato</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />
    </head>
    <body>
        <div class="container mt-5">
            <h2>Novo Contato</h2>
            <button type="button" class="btn btn-secondary mb-3" onclick="window.history.back()">Voltar</button>
            <form method="POST" action="/contato">
                <div class="mb-3">
                    <label class="form-label">Nome</label>
                    <input type="text" name="nome" class="form-control" placeholder="Digite seu nome" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Email</label>
                    <input type="email" name="email" class="form-control" placeholder="Digite seu e-mail" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Assunto</label>
                    <input type="text" name="assunto" class="form-control" placeholder="Assunto" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Mensagem</label>
                    <textarea name="mensagem" class="form-control" placeholder="Mensagem" rows="4" required></textarea>
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" name="respondido" class="form-check-input" value="on">
                    <label class="form-check-label">Respondido</label>
                </div>
                <button type="submit" class="btn btn-success">Enviar</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/contatos')
def contato_lista():
    pesquisa = request.args.get('pesquisa')
    if pesquisa:
        contatos = Contato.query.filter(Contato.nome.ilike(f'%{pesquisa}%')).all()
    else:
        contatos = Contato.query.all()
    rows = ""
    for contato in contatos:
        rows += f'''
        <tr>
            <td>{contato.nome}</td>
            <td>{contato.email}</td>
            <td>{contato.assunto}</td>
            <td>{contato.mensagem}</td>
            <td>{"Sim" if contato.respondido else "Não"}</td>
        </tr>
        '''
    if not rows:
        rows = '<tr><td colspan="5" class="text-center">Nenhum contato encontrado.</td></tr>'
    return f'''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Lista de Contatos</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h2>Lista de Contatos</h2>
            <button type="button" class="btn btn-secondary mb-3" onclick="window.history.back()">Voltar</button>
            <form method="GET" class="mb-3">
                <input type="text" name="pesquisa" placeholder="Pesquisar por nome" class="form-control" style="width: 300px; display: inline-block;">
                <button type="submit" class="btn btn-primary">Pesquisar</button>
            </form>
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th>Nome</th>
                        <th>Email</th>
                        <th>Assunto</th>
                        <th>Mensagem</th>
                        <th>Respondido</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)



