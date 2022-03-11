from flask import Flask
from flask import render_template, redirect, url_for

app = Flask(__name__)


@app.route('/para/<user>')
def index(user):
    if user == '123':
        return redirect(url_for('login'))
    return render_template('abc.html', user_template=user)


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
