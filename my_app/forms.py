# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:44:48 2020

@author: Robin_user
"""
#J'utilise Flask Form pour pouvoir obtenir les inputs du joueur
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,IntegerField, SubmitField, validators


class LoginForm(FlaskForm):
    #Nom du Joueur
    username = StringField('Username', validators=[validators.DataRequired(),])
    #Numero du dé qu'on veut changer
    num_de = IntegerField('Relancer le dé numéro: ', validators=[validators.DataRequired(),validators.NumberRange(min=1, max=6)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Jouer')