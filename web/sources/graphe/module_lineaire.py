# -*- coding: utf-8 -*-

'''
-> Medieval Heroes : Module pour les classes Pile et File

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''

#####################################
class Maillon:
    '''
    une classe pour un maillon
    '''
    def __init__(self, valeur = None, suivant = None):
        '''
        initialise un maillon
        : params
            valeur (type inconnu)
            suivant (Maillon)
        '''
        self.valeur = valeur
        self.suivant = suivant
    
    def est_vide(self):
        '''
        renvoie True si le maillon est vide et False sinon
        : return (bool)
        '''
        return self.valeur == None
    
    def acc_valeur(self):
        '''
        accesseur de l'attribut valeur qui renvoie la valeur
        : return (?) valeur
        '''
        return self.valeur
    
    def acc_suivant(self):
        '''
        accesseur de l'attribut suivant qui renvoie le suivant
        : return (?) suivant
        '''
        return self.suivant
        
    def mut_valeur(self, nouvelle_valeur):
        '''
        mutateur de l'attribut valeur qui change sa valeur
        : param nouvelle_valeur (?)
        : pas de return
        : effet de bord sur l'attribut valeur
        '''
        self.valeur = nouvelle_valeur
    
    def mut_suivant(self, nouveau_suivant):
        '''
        mutateur de l'attribut suivant qui change la valeur du suivant
        : param nouveau_suivant (Maillon) ou (None)
        : pas de return
        : effet de bord sur l'attribut suivant
        '''
        self.suivant = nouveau_suivant

#####################################        
class Pile():
    '''
    implémentation d'une pile avec des maillons
    '''
    def __init__(self):
        '''
        initialise une classe pour une pile
        '''
        self.sommet = None
        
    def est_vide(self):
        '''
        renvoie True si la pile est vide et False sinon
        : return (bool)
        '''
        return self.sommet == None
    
    def empiler(self, valeur):
        '''
        ajoute la valeur en tête de pile
        : param valeur (?)
        : pas de return
        '''
        maillon = Maillon(valeur, self.sommet)
        self.sommet = maillon        
    
    def depiler(self):
        '''
        enlève si possible la valeur en tête de pile et la renvoie ou déclenche un message d'erreur si la pile est vide.
        : return (?)
        '''
        #assertion
        assert not self.est_vide(), 'la pile ne doit pas être vide !'
        #code
        valeur = self.sommet.acc_valeur()
        self.sommet = self.sommet.acc_suivant() #on change juste la tête  
        return valeur #la valeur de ce qu'on dépile 
 
#####################################
class File():
    '''
    une classe pour les Files
    '''
    def __init__(self):
        '''
        contruit une file vide de longueur 0 possédant une tête et une queue
        '''
        self.tete = None # premier maillon de la queue
        self.queue = None # dernier maillon de la queue
        self.longueur = 0 # la longueur de la file
    
    def acc_longueur(self):
        '''
        renvoie l'attribut longueur
        : return (int)
        '''
        return self.longueur
    
    def est_vide(self):
        '''
        renvoie True si la file est vide et False sinon
        : return (bool)
        '''
        return self.tete == None
     
    def enfiler(self, valeur):
        '''
        ajoute un élement à la file. On distinguera 2 cas:
        - le cas où la file est vide : la tête et la queue sont le maillon portant la valeur
        - le cas où la file n'est pas vide mais la queue est None
        : param valeur (?) la valeur à ajouter
        : pas de return
        '''
        #1er cas
        nouveau_maillon = Maillon(valeur, None)
        if self.est_vide():
            self.tete = nouveau_maillon
            self.queue = nouveau_maillon
        #2e cas
        else:
            self.queue.mut_suivant(nouveau_maillon)
            self.queue = nouveau_maillon
        self.longueur += 1 #la longueur augmente de 1
   
    def defiler(self):
        '''
        renvoie la valeur en tête de file et la retire de la file si la file n'est pas vide, déclenche un message d'erreur sinon.
        : return (?), la valeur du maillon retiré
        '''
        #assertion
        assert not self.est_vide(), '/!\ la file ne doit pas être vide !'
        #code
        valeur = self.tete.acc_valeur()
        self.tete = self.tete.acc_suivant() #on change la tête par son suivant
        self.longueur -= 1 #la longueur diminue de 1
        return valeur