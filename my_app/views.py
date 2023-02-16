from flask import Flask,render_template, url_for, request,session,flash,redirect


from my_app import app
#On importe les inputs
from my_app.forms import LoginForm
#On importe le jeu
from my_app.yahtzee import Yahtzee
#On instancie le jeu
Jeu_test = Yahtzee()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #J'utilise un session object pour conserver le nombre de relance du joueur 
    x = session.get('x', None)
    if not x:
        session['x'] = 1
    #Au bout de 2 relances on revient à 0
    elif x>=3:
        session.clear()
    else:
        session['x']+=1
    #Input du joueur
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        #numero du de relance
        numero_de = int(form.num_de.data)
        #Premier relance
        if(x==1):
            resultat_premier_lancer = Jeu_test.jouer(numero_de,1)
            return render_template('login.html',title='Premier lancer', form =form,liste_des = resultat_premier_lancer )
        #Deuxieme relance
        if(x==2):
            resultat_deuxieme_lancer = (Jeu_test.jouer(numero_de,2))
            return render_template('resultat.html',title='Resultat Final',liste_des = resultat_deuxieme_lancer)  
    return render_template('login.html', title='Sign In', form=form, liste_des = Jeu_test.debut_jeu())

