#from flask_project.models import de
from random import randint

#On crée une classe De qui contient la valeur et la méthode lancer le dé
class De():

    def __init__(self):
        self.valeur = 0
        self.lancer()

    def lancer(self):
        self.valeur = randint(1, 6)
        return self.valeur
#On stocke les resultats possibles dans une liste globale
Resultat = ["Yahtze","Grande Suite","Petite Suite","Full","Carré","Brelan","Rien"]
   #On crée une classe du jeu 
class Yahtzee():

    def __init__(self):
        self.nb_des = 5
        self.nb_lancers = 2
        self.valeur = [De() for i in range(self.nb_des)]
        self.lancer_actuel =0
    def __str__(self):
        repres=""
        for i in range(self.nb_des):
            repres=repres+str((self.valeur[i]).valeur)
            if i != self.nb_des-1:
                repres=repres+"\n"
        return repres
     
    def debut_jeu(self):
        for j in range(self.nb_des):
            (self.valeur[j]).lancer()
        result = [(self.valeur[j]).valeur for j in range(self.nb_des)]
        return(result)
        
    def fin_jeu(self):
        nb_valeur_consecutives = 0
        #On crée la liste d'occurences pour reperer les Yhatzee/FUll/Carre/Brelan
        occurences = [0]*6
        for i in range (self.nb_des):
            occurences[(self.valeur[i]).valeur-1] +=1
            if(i<self.nb_des-1 and (self.valeur[i]).valeur+1==(self.valeur[i+1]).valeur):    
                nb_valeur_consecutives+=1
        #On trie la liste occurences par ordre decroissant : le nombre maximal d'un même élement se trouve en position 0
        occurences.sort(reverse=True)
        if(occurences[0]==self.nb_des):
            return(0)        
        if(nb_valeur_consecutives==self.nb_des-1):
            return(1)
        if(nb_valeur_consecutives==self.nb_des-2):
            return(2) 
        if(occurences[0]==self.nb_des-1 and occurences[0]==self.nb_des-2 ):
            return(3) 
        if(occurences[0]==self.nb_des-1):
            return(4)
        if(occurences[0]==self.nb_des-2):
            return(5)
        else:
            return(6)
    
#order est le numero du dé que le joueur veut changer    
    def jouer(self,order,nb_lancer):
        if(order<0 or order>self.nb_des):
            err = "Numero de dé :" + order + " incorect."
            raise ValueError(err)
        #On change le dé numero order-1
        (self.valeur[int(order)-1]).lancer()
        #Premiere relance
        if(nb_lancer==1):
            result =[(self.valeur[j]).valeur for j in range(self.nb_des)]
        #Deuxieme relance
        else:
            if(self.fin_jeu()>6 or self.fin_jeu()<0 ):
                err = "Résultat :" + self.fin_jeu() + " incorect."
                raise ValueError(err)
            result =[(self.valeur[j]).valeur for j in range(self.nb_des)]
            result.append( Resultat[self.fin_jeu()])         
        return(result)
      
    
    
