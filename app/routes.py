from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from app.models import User

from app.forms import UserInfoForm


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/whoweare')
def whoweare():

    return render_template('whoweare.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserInfoForm()

    context = {
        'form': form
    }
    if request.method == 'POST' and form.validate():

        username = form.username.data
        email = form.email.data
        password = form.password.data

        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()

        flash("You have successfully registered", 'success')

        

        return redirect(url_for('index'))
    return render_template('register.html', **context)

@app.route('/attorneys')
def attorneys():

    return render_template ('attorneys.html')
