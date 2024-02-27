# -*- coding: utf-8 -*-
'''
    Module graphe avec un dictionnaire
    : Auteur
        LAPÔTRE Marylou
'''

class Graphe_oriente_dic() :
    '''
    une classe pour les graphes orientés construits avec un dictionnaire d'adjacence
    '''
    def __init__(self):
        '''
        construit le graphe avec pour seul attribut un dictionnaire vide
        '''
        self.adj = {}
        
    def __repr__(self):
        '''
        renvoie une chaîne de caractères pour décrire le graphe
        : return (str)
        >>> g = Graphe_oriente_dic()
        >>> g.ajouter_sommet('ella')
        >>> g.ajouter_arete('mick', 'etta')
        >>> g
        Graphe orienté de 3 sommets
        '''
        return "Graphe orienté de " + str(len(self.adj)) + " sommets"
    
    def __str__(self):
        '''
        renvoie une chaîne de caractères pour afficher le graphe
        : return (str)
        >>> g = Graphe_oriente_dic()
        >>> g.ajouter_arete('Ray', 'Mick')
        >>> g.ajouter_arete('Mick', 'Jim')
        >>> g.ajouter_arete('Mick', 'Ray')
        >>> g.ajouter_arete('Jim', 'Joe')
        >>> g.ajouter_arete('Joe', 'Etta')
        >>> g.ajouter_arete('Joe', 'Mick')
        >>> g.ajouter_arete('Ella', 'Ray')
        >>> g.ajouter_arete('Ella', 'Etta')
        >>> print(g)
        Ray : Mick 
        Mick : Jim Ray 
        Jim : Joe 
        Joe : Etta Mick 
        Etta : 
        Ella : Ray Etta 
        '''
        chaine = ''
        i = 0
        for sommet in self.adj :
            chaine += str(sommet) + ' : '
            for voisin in self.voisins(sommet):
                chaine += str(voisin) + ' '
            i += 1
            if not i == len(self.adj): #si on n'est pas à la fin
                chaine += '\n'
        return chaine
        
    def ajouter_sommet(self, sommet):
        '''
        ajoute le sommet au dictionnaire, si ce sommet n'y est pas et ne fait rien sinon
        : param sommet (??)
        >>> g = Graphe_oriente_dic()
        >>> g.ajouter_sommet('ella')
        >>> g.adj == {'ella' : []}
        True
        '''
        if not sommet in self.adj: #si le sommet n'y est pas déjà
            self.adj[sommet] = [] #un tableau vide
            
    def ajouter_arete(self, sommet1, sommet2):
        '''
        crée les deux sommets différents via la méthode précédente puis ajoute sommet2 à la liste des suivants de sommet1
        : params
            sommet1 (??)
            sommet2 (??)
        >>> g = Graphe_oriente_dic()
        >>> g.ajouter_arete('ella', 'etta')
        >>> g.adj == {'ella' : ['etta'], 'etta' : []}
        True
        '''
        #ajout des deux sommets
        self.ajouter_sommet(sommet1)
        self.ajouter_sommet(sommet2)
        #arête
        self.adj[sommet1].append(sommet2)

    def a_arete(self, sommet1, sommet2) :
        '''
        renvoie True si il y a un arête de sommet1 vers sommet2 et False sinon
        : param sommet1, sommet2 (??) deux sommets différents
        : return (boolean)
        >>> g = Graphe_oriente_dic()
        >>> g.ajouter_sommet('A')
        >>> g.ajouter_arete('B', 'C')
        >>> g.a_arete('B', 'C')
        True
        >>> g.a_arete('A', 'B')
        False
        '''
        return sommet2 in self.adj[sommet1]

    def voisins(self, sommet):
        '''
        renvoie la liste des successeurs du sommet passé en paramètre
        : param sommet (??)
        : return (list)
        >>> g = Graphe_oriente_dic()
        >>> g.ajouter_sommet('A')
        >>> g.ajouter_arete('B', 'C')
        >>> g.ajouter_arete('B', 'A')
        >>> g.voisins('B')
        ['C', 'A']
        '''
        return self.adj[sommet]


class Graphe_non_oriente_dic(Graphe_oriente_dic) :
    '''
    une classe pour un graphe non-orienté avec une matrice adjacente
    '''
    def __init__(self):
        '''
        initialise une classe pour un graphe non-orienté
        '''
        super().__init__()
        
    def __repr__(self):
        '''
        renvoie une chaîne de caractères pour décrire le graphe
        : return (str)
        >>> g = Graphe_non_oriente_dic()
        >>> g.ajouter_sommet('ella')
        >>> g.ajouter_arete('mick', 'etta')
        >>> g
        Graphe non-orienté de 3 sommets
        '''
        return "Graphe non-orienté de " + str(len(self.adj)) + " sommets"

    def ajouter_arete(self, sommet1, sommet2):
        '''
        crée les deux sommets différents via la méthode précédente puis ajoute sommet2 à la liste des suivants de sommet1
        : params
            sommet1 (??)
            sommet2 (??)
        >>> g = Graphe_oriente_dic()
        >>> g.ajouter_arete('ella', 'etta')
        >>> g.adj == {'ella' : ['etta'], 'etta' : []}
        True
        '''
        #ajout des deux sommets
        self.ajouter_sommet(sommet1)
        self.ajouter_sommet(sommet2)
        #arête
        if not sommet2 in self.adj[sommet1]: #si il n'y est pas déjà
            self.adj[sommet1].append(sommet2)
        if not sommet1 in self.adj[sommet2]: #si il n'y est pas déjà
            self.adj[sommet2].append(sommet1) #dans les deux sens
    







#######DOCTEST################
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)