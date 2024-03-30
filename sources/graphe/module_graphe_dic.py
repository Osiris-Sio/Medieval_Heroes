# -*- coding: utf-8 -*-

'''
-> Medieval Heroes : Module pour la classe Graphe

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
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