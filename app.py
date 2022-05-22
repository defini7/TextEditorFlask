import os

from flask import Flask, render_template, session, redirect
from functools import wraps

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.app_context().push()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect('/sign_in')
        return f(*args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='192.168.1.10', port=5000)
