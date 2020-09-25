from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.fields.html5 import EmailField


class Register(FlaskForm):
    name = StringField('Nombre', [validators.DataRequired()])
    email = EmailField('Correo Electrónico', [ validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    confirm_password = PasswordField('Confirmar Contraseña', [validators.DataRequired()])
    submit = SubmitField('Registrarse')

class Login(FlaskForm):
    email = EmailField('Correo Electrónico', [ validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Iniciar Sesión')

