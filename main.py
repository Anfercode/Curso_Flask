from flask import Flask, request, redirect, make_response, render_template, session
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'SUPER SECRETO'


todos = ['Comprar Cafe','Enviar Solicitud de compra','Entregar video al productor']


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos':todos
        }

    return render_template('hello.html',**context)
