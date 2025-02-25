from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Regexp
from wtforms import StringField, EmailField, PasswordField, SubmitField, IntegerField, SelectField, DecimalField
from wtforms import validators

class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message='Este campo es requerido'),        
    ])
    edad = IntegerField('Edad', [
        validators.DataRequired(message='Este campo es requerido')
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message='Este campo es requerido')
    ])
    apellidos = StringField('Apellidos', [
        validators.DataRequired(message='Este campo es requerido')
    ])
    email = EmailField('Email', [
        validators.Email(message='Este campo debe ser un correo electrónico válido')
    ])