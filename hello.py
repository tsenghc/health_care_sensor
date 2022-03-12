from flask import Flask
from flask import render_template, redirect, url_for
from fdk300 import FDK300
from fdk400 import FDK400
from m170 import M170
from mtk_a1 import MTKA1
app = Flask(__name__)
fdk300 = FDK300("C6:05:04:07:4D:54")
scale = MTKA1()

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
