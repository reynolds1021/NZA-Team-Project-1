from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash
from app.models import User, CaseNotes
from flask_login import login_user, logout_user, login_required
from app.forms import UserInfoForm, LoginForm, CaseNotesForm


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/whoweare')
def whoweare():

    return render_template('whoweare.html')

@app.route('/whatwedo')
def whatwedo():

    return render_template('whatwedo.html')    

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

@app.route('/login', methods =['GET','POST'])
def login():
    form = LoginForm()

    context = {
        'form': form
    }
    if request.method == 'POST' and form.validate():

        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            flash('Incorrect Email/Password. Please try again.', 'danger')
            return redirect(url_for('login'))
        # Log user in
        login_user(user, remember=form.remember_me.data)

        flash("You have successfully logged in!", 'success')
        return redirect(url_for('index'))
    return render_template ('login.html', **context)

#@app.route('/lawyers', methods = ['GET','POST'])
#def lawyers():
 #   form = CaseNotesForm()
  #  context = {
   #     'form': form
    #}    
    #if request.method == 'POST' and form.validate():

     #   create = form.create.data
    


      # db.session.add(new_casenotes)
       # db.session.commit()

        #flash("You have successfully created a new case note!", 'success')
        #return redirect(url_for('casenotes'))
    #return render_template ('lawyers.html', **context)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary') #Specifying Colors for flash message 
    return redirect(url_for('index'))    


@app.route('/lawyers', methods = ['GET','POST'])
@login_required
def lawyers():
    context = {
        'users':User.query.all() 
        
    }
    return render_template('lawyers.html', **context)

@app.route('/casenotes', methods = ['GET','POST'])
def casenotes():
    form = CaseNotesForm()
    context = {
        'form': form
    
    }  
    if request.method == 'POST' and form.validate():

        create = form.create.data
        
        

        new_casenotes = CaseNotes(create)
        db.session.add(new_casenotes)
        db.session.commit()

        flash("You have successfully created a case note!", 'success')

        

        return redirect(url_for('index'))
    return render_template('casenotes.html', **context)

    #if request.method == 'POST' and form.validate():

     #   create = form.create.data
     #   username = form.username.data
     #   password = form.password.data


      #  new_casenotes = CaseNotes(create, username, password)
       # db.session.add(new_casenotes)
       # db.session.commit()

       # flash("You have successfully created a new case note!", 'success')
        
       # casenote = CaseNotes.query.get(int(casenote_id))

       # if casenote is None or not check_password_hash(casenotes.password, password):
        #    flash('Case note(s) does/do not exist.', 'danger')
            #return redirect(url_for('login'))
        # Log user in
       # login_user(user, remember=form.remember_me.data)
      
    