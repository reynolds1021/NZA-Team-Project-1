# Import for Forms
from app import app
from app.forms import LoginForm
from flask_login import login_user
from flask import render_template

@app.route('/login')
def login():
    form = LoginForm()
    print(form)
    context = {
        'form': form
    }
    return render_template('login.html', **context)