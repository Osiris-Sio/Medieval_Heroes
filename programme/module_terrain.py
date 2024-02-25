# -*- coding: utf-8 -*-

'''
-> Medieval Heroes : Module pour la classe Terrain.

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''

######################################################
### Importation Modules :
######################################################
import module_personnage
######################################################
### Classe Terrain :
######################################################

class Terrain():
    '''
    Une Classe pour le terrain.
    '''
    def __init__(self, attributs_jeu, clavier_souris, niveau = 1):
        '''
        initialise le terrain
        : params 
            attributs_jeu (Attributs_Jeu) module
            clavier_souris (Clavier_Souris) module
            niveau (int) valant par défaut 1
        '''
        self.attributs_jeu = attributs_jeu
        self.clavier_souris = clavier_souris
        self.niveau = niveau
        self.grille = Terrain.attribuer_grille(self)
        
    def attribuer_grille(self):
        '''
        attribue une grille en fonction du niveau demandé
        '''
        grille = None
        if self.niveau == 1:
            grille = [[' ', ' ', ' ', 'X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', ' ', ' ', ' '],
                      [' ', 'X', ' ', 'X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', 'X', 'X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', 'X', ' ', ' '],
                      [' ', 'X', 'X', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', 'X', 'X', ' '],
                      ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X'],
                      ['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X'],
                      ['X', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', 'X'],
                      ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
                      ['X', 'X', ' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', 'X', 'X'],
                      ['X', 'X', ' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', 'X', 'X'],
                      ['X', 'X', ' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', 'X', 'X'],
                      ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
                      ['X', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ', 'X'],
                      ['X', ' ', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X'],
                      ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X'],
                      [' ', 'X', 'X', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', ' ', 'X', 'X', ' '],
                      [' ', ' ', 'X', 'X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', 'X', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', 'X', ' ', 'X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' '],
                      [' ', ' ', ' ', 'X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', ' ', ' ', ' ']
                      ]
        return grille
    
    def __str__(self):
        '''
        renvoie le terrain
        : return (str)
        '''
        grille = ''
        separation = '+' + '-+'*21 + '\n'
        grille += separation
        for ligne in self.grille:
            chaine = '|'
            for elt in ligne:
                chaine += str(elt) + '|'
            grille += chaine + '\n'
            grille += separation
        return grille
    
    def taille_terrain(self):
        '''
        renvoie la taille du terrain dans un tuple (longueur, hauteur)
        : return (tuple)
        '''
        longueur = len(self.grille[0])
        hauteur = len(self.grille)
        return (longueur, hauteur)
        
    def acc_terrain(self, x, y) :
        '''
        renvoie le contenu du terrain aux coordonnées précisées
        : params x, y (int)
        : return (str)
        '''
        #assertions
        assert isinstance(x, int) and 0 <= x <= 20,'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20,'y doit être un entier compris entre 0 et 20 inclus'
        #code
        return self.grille[y][x]
    
    def acc_grille(self):
        '''
        renvoie l'attribut grille
        '''
        return self.grille

    def mut_terrain(self, x, y, personnage) :
        '''
        modifie le labyrinthe en écrivant le personnage aux coordonnées x, y
        : params
            x, y (int)
            personnage (str)
        : pas de return, modifie l'attribut lab
        '''
        #assertions
        assert isinstance(x, int) and 0 <= x <= 20,'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20,'y doit être un entier compris entre 0 et 20 inclus'
        #code
        self.grille[y][x] = personnage
        
    def est_possible(self, x, y):
        '''
        renvoie True si la case de coordonnées (x,y) est vide et False sinon
        : params
            x, y (int)
        : return (bool)
        '''
        #assertions
        assert isinstance(x, int) and 0 <= x <= 20,'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20,'y doit être un entier compris entre 0 et 20 inclus'
        #code
        return self.acc_terrain(x, y) == ' '
    
    def est_personnage(self, x, y):
        '''
        renvoie True si il y a un personnage (autre qu'un monstre) sur la case (x, y) et False sinon
        : params
            x, y (int)
        : return (bool)
        '''
        return isinstance(self.acc_terrain(x, y), module_personnage.Personnage) and not self.acc_terrain(x, y).acc_personnage() == 'monstre' 
                
    def trouver_case_libre_proche(self, x, y):
        '''
        renvoie les coordonnées de la case libre la plus proche de la case dont les coordonnées sont ceux passés en paramètres
        : params x, y (int)
        : return (tuple)
        '''
        trouve = False
        i = 1
        while not trouve : #on cherche tant qu'on n'a pas trouvé
            tab = self.trouver_case(i)
            t = 0
            while t < len(tab) and not trouve:
                n_x = x + tab[t][0]
                n_y = y + tab[t][1]
                if 0 <= n_x <= 20 and 0 <= n_y <= 20: #si la case est dans la grille
                    trouve = self.est_possible(n_x, n_y)
                    case = (n_x, n_y)
                t += 1
            i += 1
        return case

    def trouver_case(self, rang):
        '''
        renvoie le tableau avec des semis-coordonnées des cases éloignés de rang de la case centrale
        : return (list)
        '''
        tab = []
        for i in range(-rang, rang+1):
            for j in range(-rang, rang+1):
                if abs(i) == rang or abs(j) == rang:
                    tab.append((i, j))
        return tab
    

            
    
            
    
    
    
    
############### DOCTEST #####################     
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)       