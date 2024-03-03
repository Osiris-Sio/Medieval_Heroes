# -*- coding: utf-8 -*-
'''
    la classe Maillon
    : Auteur
        Lapôtre Marylou 
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
        
    def __repr__(self):
        '''
        renvoie une chaîne qui décrit le maillon 
        '''
        return 'Maillon de valeur : ' + str(self.valeur)
    
    def est_vide(self):
        '''
        renvoie True si le maillon est vide et False sinon
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
class ListeChainee() :
    '''
    une classe pour implémenter une liste chaînée
    '''
    def __init__(self):                   
        '''
        construit une liste chaînée vide de longueur 0
        '''
        self.tete = None
        self.longueur = 0
    
    def __repr__(self):
        '''
        donne la classe de l'objet et sa taille
        : return (str)
        '''
        return 'Class ListeChainee de taille ' + str(self.longueur)
    
    def __str__(self):
        '''
        renvoie une chaine pour visualiser la liste
        : return (str)
        >>> l = ListeChainee()
        >>> print(l)
        ()
        >>> l.ajouter_tete(1)
        >>> print(l)
        (1,())
        >>> l.ajouter_tete(2)
        >>> print(l)
        (2,(1,()))
        >>> l.supprimer(0)
        >>> print(l)
        (1,())
        '''
        chaine = '('
        maillon = self.tete # on se place sur le maillon de tete
        nb_maillon = 1
        while maillon != None :
            chaine = chaine + str(maillon.acc_valeur()) + ',('
            maillon = maillon.acc_suivant()
            nb_maillon += 1
        chaine = chaine +  ')' * nb_maillon # on ajoute la valeur du maillon à la chaine puis ',('
        return chaine
            
    def __len__(self):
        '''
        renvoie la longueur de la liste
        : return (int)
        >>> l = ListeChainee()
        >>> len(l)
        0
        >>> l.ajouter_tete(12)
        >>> len(l)
        1
        '''
        return self.longueur #la longueur de la liste chaînée

    def est_vide(self):
        '''
        renvoie True si la liste est vide et False sinon
        : return (boolean)
        >>> l = ListeChainee()
        >>> l.est_vide()
        True
        >>> l.ajouter_tete(1)
        >>> l.est_vide()
        False
        '''
        return self.tete == None #ou self.longueur == 0
    
    def ajouter_tete(self, valeur):
        '''
        ajoute un maillon de valeur précisé en tête de liste
        : param valeur (?)
        : pas de return
        >>> l = ListeChainee()
        >>> l.ajouter_tete(2)
        >>> l.tete.acc_valeur()
        2
        >>> l.ajouter_tete(3)
        >>> l.tete.acc_valeur()
        3
        >>> l.tete.acc_suivant().acc_valeur()
        2
        >>> l.longueur
        2
        '''
        nouveau_maillon = Maillon(valeur, self.tete)
        self.tete = nouveau_maillon #la tête devient le nouveau maillon
        self.longueur += 1 #la longueur de la chaîne augmente de 1
        
    def retirer_tete(self):
        '''
        enlève la tête de la liste chaînée
        : pas de return
        : effet de bord sur la liste chaînée
        >>> l = ListeChainee()
        >>> l.ajouter_tete(1)
        >>> l.ajouter_tete(2)
        >>> l.ajouter_tete(3)
        >>> print(l)
        (3,(2,(1,())))
        >>> l.retirer_tete()
        >>> print(l)
        (2,(1,()))
        '''
        if not self.est_vide(): #si la liste n'est pas vide
            self.tete = self.tete.acc_suivant() #la tête change/on supprime la tête
            self.longueur -= 1
        
    def acceder(self, n):
        '''
        renvoie le maillon d'indice n s'il existe
        : param n (int) n < longueur de la liste
        : return (Maillon)
        >>> l = ListeChainee()
        >>> l.ajouter_tete(4)
        >>> l.ajouter_tete(3)
        >>> l.ajouter_tete(2)
        >>> l.ajouter_tete(1)
        >>> l.acceder(0).acc_valeur()
        1
        >>> l.acceder(2).acc_valeur()
        3
        '''
        #assertion
        assert n < self.longueur, 'donnez un n strictement inférieur à la longueur de la liste chaînée'
        #code
        maillon = self.tete
        for _ in range(n):
            maillon = maillon.acc_suivant() #on change de maillon tant qu'on n'a pas atteint celui qu'on veut
        return maillon
    
    def inserer(self, valeur, n):
        '''
        insère le maillon dans la liste chaînée à l'indice n
        : params
            valeur (??)
            n (int) 0 <= n <= self.longueur
        : pas de return
        : effet de bord de la liste chaînée
        >>> l = ListeChainee()
        >>> l.ajouter_tete(4)
        >>> l.ajouter_tete(3)
        >>> l.ajouter_tete(2)
        >>> l.ajouter_tete(1)
        >>> print(l)
        (1,(2,(3,(4,()))))
        >>> l.inserer(5, 1)
        >>> print(l)
        (1,(5,(2,(3,(4,())))))
        >>> l.inserer(0, 0)
        >>> print(l)
        (0,(1,(5,(2,(3,(4,()))))))
        '''
        #assertions
        assert isinstance(n, int) and n >= 0, 'n doit être positif'
        assert n <= self.longueur, 'out of range :)'
        #code
        if n == 0:
            self.ajouter_tete(valeur)
        else:
            maillon_precedent = self.acceder(n-1) #on accède au maillon précédent
            nouveau_maillon = Maillon(valeur, maillon_precedent.acc_suivant()) #on crée le nouveau maillon
            maillon_precedent.mut_suivant(nouveau_maillon) #on change le suivant du maillon précédent
            self.longueur += 1
        
    def supprimer(self, n):
        '''
        supprime le maillon d'indice n
        : param n (int) 0 <= n < self.longueur
        : pas de return
        >>> l = ListeChainee()
        >>> l.ajouter_tete(4)
        >>> l.ajouter_tete(3)
        >>> l.ajouter_tete(2)
        >>> l.ajouter_tete(1)
        >>> print(l)
        (1,(2,(3,(4,()))))
        >>> l.supprimer(1)
        >>> print(l)
        (1,(3,(4,())))
        >>> l.supprimer(2)
        >>> print(l)
        (1,(3,()))
        '''
        #assertions
        assert isinstance(n, int) and n >= 0, 'n doit être positif'
        assert n < self.longueur, 'out of range :)'
        #code
        if n == 0:
            self.retirer_tete() #on retire en tête
        else:
            maillon_precedent = self.acceder(n-1) #on accède au maillon précédent
            maillon_precedent.mut_suivant(maillon_precedent.acc_suivant().acc_suivant()) #on change le suivant du maillon précédent
            self.longueur -= 1
    
    def __getitem__(self, n):
        '''
        renvoie la valeur du maillon d'indice n
        : param n (int) 0 <= n < self.longueur
        : return (??)
        >>> l = ListeChainee()
        >>> l.ajouter_tete(4)
        >>> l.ajouter_tete(3)
        >>> l.ajouter_tete(2)
        >>> l.ajouter_tete(1)
        >>> print(l)
        (1,(2,(3,(4,()))))
        >>> l[0]
        1
        >>> l[3]
        4
        >>> l.inserer('B', 4)
        >>> l[4]
        'B'
        '''
        #assertions
        assert isinstance(n, int) and n >= 0, 'n doit être positif'
        assert n < self.longueur, 'out of range :)'
        #code
        maillon = self.acceder(n) #on accède au maillon d'indice n
        return maillon.acc_valeur() #on renvoie la valeur du maillon
    
    def __setitem__(self, n, valeur):
        '''
        remplace la valeur du maillon d'indice n par valeur
        : params
            n (int) 0 <= n < self.longueur
            valeur (?)
        : pas de return
        >>> l = ListeChainee()
        >>> l.ajouter_tete(4)
        >>> l.ajouter_tete(3)
        >>> l.ajouter_tete(2)
        >>> l.ajouter_tete(1)
        >>> print(l)
        (1,(2,(3,(4,()))))
        >>> l[0] = 'bonjour'
        >>> print(l)
        (bonjour,(2,(3,(4,()))))
        >>> l[3] = 'bye'
        >>> print(l)
        (bonjour,(2,(3,(bye,()))))
        '''
        #assertions
        assert isinstance(n, int) and n >= 0, 'n doit être positif'
        assert n < self.longueur, 'out of range :)'
        #code
        maillon = self.acceder(n) #on accède au maillon
        maillon.mut_valeur(valeur) #on change la valeur du maillon

#####################################        
class Pile:
    '''
    implémentation d'une pile avec des maillons
    '''
    def __init__(self):
        '''
        initialise une classe pour une pile
        '''
        self.sommet = None
        
    def __repr__(self):
        '''
        renvoie une chaîne de caractères pour décrire la classe pile
        '''
        return 'Classe Pile'
    
    def __str__(self):
        '''
        renvoie une chaine pour visualiser la pile
        : return (str)
        >>> l = Pile()
        >>> l.empiler(1)
        >>> print(l)
        1
        _
        >>> l.empiler(2)
        >>> print(l)
        2
        1
        _
        '''
        chaine = ''
        maillon = self.sommet
        while not maillon == None:
            chaine += str(maillon.acc_valeur()) + '\n' #on ajoute à la chaîne la valeur du maillon
            maillon = maillon.acc_suivant() #on change le maillon
        chaine += '_' #pour représenter le fond de la pile
        return chaine
        
    def est_vide(self):
        '''
        renvoie True si la pile est vide et False sinon
        : return (bool)
        >>> p = Pile()
        >>> p.est_vide()
        True
        >>> p.empiler(1)
        >>> p.est_vide()
        False
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
        >>> p = Pile()
        >>> p.empiler(2)
        >>> p.empiler('a')
        >>> p.depiler()
        'a'
        >>> p.depiler()
        2
        '''
        #assertion
        assert not self.est_vide(), 'la pile ne doit pas être vide !'
        #code
        valeur = self.sommet.acc_valeur()
        self.sommet = self.sommet.acc_suivant() #on change juste la tête  
        return valeur #la valeur de ce qu'on dépile 
 
#####################################
class File:
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
    
    def __str__(self):
        '''
        renvoie la chaine permettant d'afficher la file
        : return (str)
        >>> f = File()
        >>> f.enfiler(3)
        >>> f.enfiler(2)
        >>> f.enfiler('a')
        >>> print(f)
        (3, (2, (a, ())))
        '''
        maillon = self.tete
        nb_maillon = 1
        chaine = '('
        while not maillon == None:
            chaine += str(maillon.acc_valeur()) + ', ('
            maillon = maillon.acc_suivant() #on passe au maillon suivant
            nb_maillon += 1
        chaine = chaine +  ')' * nb_maillon # on ajoute la valeur du maillon à la chaine puis ',('
        return chaine
        
    def __repr__(self):
        '''
        renvoie une représentation de la file
        : return (str)
        '''
        return 'Classe File'
    
    def acc_longueur(self):
        '''
        renvoie l'attribut longueur
        : return (int)
        >>> f = File()
        >>> f.enfiler(2)
        >>> f.enfiler(1)
        >>> f.enfiler(9)
        >>> f.enfiler(5)
        >>> f.acc_longueur()
        4
        >>> f.defiler()
        2
        >>> f.acc_longueur()
        3
        '''
        return self.longueur
    
    def est_vide(self):
        '''
        renvoie True si la file est vide et False sinon
        >>> f = File()
        >>> f.est_vide()
        True
        '''
        return self.tete == None
     
    def enfiler(self, valeur):
        '''
        ajoute un élement à la file. On distinguera 2 cas:
        - le cas où la file est vide : la tête et la queue sont le maillon portant la valeur
        - le cas où la file n'est pas vide mais la queue est None
        : param valeur (?) la valeur à ajouter
        >>> f = File()
        >>> f.enfiler(1)
        >>> f.enfiler(2)
        >>> f.est_vide()
        False
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
        >>> f = File()
        >>> f.enfiler(1)
        >>> f.enfiler(2)
        >>> f.defiler()
        1
        >>> f.defiler()
        2
        >>> f.est_vide()
        True
        '''
        #assertion
        assert not self.est_vide(), '/!\ la file ne doit pas être vide !'
        #code
        valeur = self.tete.acc_valeur()
        self.tete = self.tete.acc_suivant() #on change la tête par son suivant
        self.longueur -= 1 #la longueur diminue de 1
        return valeur
            
    
################# DOCTEST #################
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)