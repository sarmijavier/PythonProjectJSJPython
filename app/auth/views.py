from flask import  render_template, url_for, request, flash, redirect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from . import auth
from app.models import UserModel, UserData
from app.firestore_service import get_user, create_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import Register, Login




@auth.route('/login', methods=['POST', 'GET'])
def login():

    form = Login()


    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():

        email = form.email.data 
        password = form.password.data    

        user_doc = get_user(email)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']
            if check_password_hash(password_from_db, password):

                user_data = UserData(user_doc.to_dict()['name'], email, password)
                
                user = UserModel(user_data)

                login_user(user)

                flash(u'Bienvenido de nuevo!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Información no validad', 'error')
        else:
            flash('El usuario no existe!', 'error')
        
        return redirect(url_for('auth.login'))

    return render_template('login.html', form=form)


@auth.route('/register', methods=['POST', 'GET'])
def register():

    form = Register()

    if form.validate_on_submit():
        user ={
            'name': form.name.data,
            'email': form.email.data,
            'password': form.password.data,  
            'confirm_password': form.confirm_password.data,    
        }

        if len(user['password']) < 8:
            print('1')
            flash('La contraseña debe contener por lo menos 8 caracteres', 'error')

        elif user['password'] == None:
            print('2')
            flash('Contraseña no valida', 'error')

        elif user['password'] != user['confirm_password']:
            print('3')
            flash('Las contraseñas no coinciden', 'error')
            return redirect(url_for('auth.register'))
        else:
            user_doc = get_user(user['email'])
            if user_doc.to_dict() is None:
                password_hash = generate_password_hash(user['password'])
                user_data = UserData(user['name'], user['email'], password_hash)
                create_user(user_data)

                user = UserModel(user_data)
                login_user(user)
                flash('Que bueno verte de nuevo!', 'success')

                return redirect(url_for('auth.login'))
            else:
                flash('El usuario ya existe', 'error')
            

    return render_template('register.html', form=form)



#@auth.route('/logout')
#@login_required
#def logout():
#    logout_user()
#    flash('Regresa pronto', 'success')

#    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():

    return '<h1>Lo siento :( </h1>'