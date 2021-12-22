from flask import Flask
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('http://127.0.0.1:5000/users')


users_list = [{'username': 'jpretov', 'name': 'John', 'surname': 'Petrov', 'age': 19},
         {'username': 'aivanov', 'name': 'Alex', 'surname': 'Ivanov', 'age': 21}]


@app.route('/users')
def user():
    tt = ''
    for i in users_list:
        t = '<a href="http://127.0.0.1:5000/users/%s"> %s %s</a><br>' % (i['username'], i['name'], i['surname'])
        tt += t
    return tt


@app.route('/users/<username>')
def check(username):
    users = ''
    for i in users_list:
        if username == i['username']:
            users = i
    return f'<h2>UserName:{users["username"]} </h2> <br>'\
           f'<h2>Name:{users["name"]} </h2> <br>'\
           f'<h2>Surname:{users["surname"]} </h2> <br>'


if __name__ == '__main__':
    app.run(debug=True)
