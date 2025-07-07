# Sistema de Contatos com Flask

Projeto simples de CRUD para gerenciamento de contatos, desenvolvido com Flask, SQLAlchemy e Flask-WTF.

---

## Funcionalidades

- Cadastro de contatos com nome, email, assunto, mensagem e status de respondido.
- Listagem de contatos.
- Pesquisa por nome.
- Formulário seguro com validação.
- Interface simples com Bootstrap.

---

## Como usar

1. Clone o repositório:

git clone https://github.com/maanske/flask-bootstrap.git

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Inicialize o banco de dados:

flask db init
flask db migrate -m "Criando tabela de contatos"
flask db upgrade

5. Execute a aplicação:

flask run

6. Acesse no navegador:

http://127.0.0.1:5000/

---

## Exemplo de interface

![Interface do Sistema de Contatos](C:\Users\christian_manske\Downloads\img.png)

---

## Tecnologias usadas

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-WTF
- Bootstrap 5

---

## Autor

Christian Manske - [christian_manske@estudante.sesisenai.org.br](mailto:christian_manske@estudante.sesisenai.org.br)