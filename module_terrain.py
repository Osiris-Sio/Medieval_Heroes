# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Terrain

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''

######################################################
### Importation Modules :
######################################################
import module_personnage, module_objets
######################################################
### Classe Terrain :
######################################################

class Terrain():
    '''
    Une Classe pour le terrain
    '''
    def __init__(self, attributs_jeu, niveau = 1):
        '''
        initialise le terrain
        : params 
            attributs_jeu (Attributs_Jeu) module
            clavier_souris (Clavier_Souris) module
            niveau (int) valant par défaut 1
        '''
        self.attributs_jeu = attributs_jeu
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
        separation = '+' + '-+' * 21 + '\n'
        grille += separation
        for ligne in self.grille:
            chaine = '|'
            for elt in ligne:
                chaine += str(elt) + '|'
            grille += chaine + '\n'
            grille += separation
        return grille
        
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
    
    #################################
    ### Accesseur :
    #################################
    
    def acc_terrain(self, x, y) :
        '''
        renvoie le contenu du terrain aux coordonnées précisées
        : params x, y (int)
        : return (str)
        '''
        #assertions
        assert isinstance(x, int) and 0 <= x <= 20, 'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20, 'y doit être un entier compris entre 0 et 20 inclus'
        #code
        return self.grille[y][x]
    
    #################################
    ### Mutateur :
    #################################
    
    def mut_terrain(self, x, y, personnage) :
        '''
        modifie le terrain en écrivant le personnage aux coordonnées x, y
        : params
            x, y (int)
            personnage (??)
        : pas de return, modifie l'attribut lab
        '''
        #assertions
        assert isinstance(x, int) and 0 <= x <= 20,'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20,'y doit être un entier compris entre 0 et 20 inclus'
        #code
        self.grille[y][x] = personnage
    
    ######################################
    ########### Méthodes
    ######################################
    def cases_autour(coordo):
        '''
        renvoie les 8 cases se situant autour de la case de coordonnées (coordo):
        : param coordo (tuple):
        : return (list of tuples)
        '''
        #Assertion
        assert isinstance(coordo, tuple), "les coordonnées doivent être dans un tuple"
        assert 0 <= coordo[0] <= 20 and 0 <= coordo[1] <= 20, "les coordonnées doivent être dans le terrain"
        #Code
        tab = []
        for tuples in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]: #haut, bas, gauche, droite en premier
            tuple_case = (coordo[0] + tuples[0],coordo[1] + tuples[1])
            if 0 <= tuple_case[0] <= 20 and 0 <= tuple_case[1] <= 20: #si la case ne sort pas du terrain
                tab.append(tuple_case) 
        return tab
        
        
        
    def trouver_case_libre_proche(self, x, y, chaine):
        '''
        renvoie les coordonnées de la case libre la plus proche de la case dont les coordonnées sont ceux passés en paramètres
        : params
            x, y (int)
            chaine (str), 'non' si le personnage à ressusciter est un géant et 'non' sinon
        : return (tuple)
        '''
        #Assertions
        assert isinstance(x, int) and 0 <= x <= 20,'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20,'y doit être un entier compris entre 0 et 20 inclus'
        assert chaine in ['oui', 'non'], "la chaîne doit être soit 'oui' soit 'non'"
        #Code
        ##on vérifie la case de départ
        case = (x, y)
        trouve = self.est_possible(x, y) #regarde si la case passée en paramètre est libre
        i = 1
        if trouve and chaine == 'oui' : #si on a trouvé une case libre mais que le personnage est un géant
            #4 cases doivent être libre
            self.condition_case_geant(x, y)
        ##on cherche
        while not trouve : #on cherche tant qu'on n'a pas trouvé
            tab = self.trouver_case(i)
            t = 0
            while t < len(tab) and not trouve:
                n_x = x + tab[t][0]
                n_y = y + tab[t][1]
                if 0 <= n_x <= 20 and 0 <= n_y <= 20: #si la case est dans la grille
                    trouve = self.est_possible(n_x, n_y)
                    case = (n_x, n_y)
                    if trouve and chaine == 'oui' : #si on a trouvé une case libre mais que le personnage est un géant
                        #4 cases doivent être libre
                        self.condition_case_geant(n_x, n_y) 
                t += 1
            i += 1
        return case

    def trouver_case(self, rang):
        '''
        renvoie le tableau avec des semis-coordonnées des cases éloignéds de rang de la case centrale
        : param rang (int)
        : return (list)
        '''
        #Assertion
        assert isinstance(rang, int) and rang > 0 , "rang doit être un entier strictement positif"
        #Code
        tab = []
        for i in range(-rang, rang+1):
            for j in range(-rang, rang+1):
                if abs(i) == rang or abs(j) == rang:
                    tab.append((i, j))
        return tab
    
    def condition_case_geant(self, x, y):
        '''
        renvoie Vrai si la case de coordonnées x, y peut être la case en haut à gauche d'un géant
        (les 3 autres cases doivent être libres)
        : params
            x, y (int)
        : return (bool)
        '''
        return (self.est_possible(x + 1, y) and
                self.est_possible(x , y + 1) and
                self.est_possible(x + 1, y + 1))
    

      
    
            
    
    
    
    
############### DOCTEST #####################     
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)       