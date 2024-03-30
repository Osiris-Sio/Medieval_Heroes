# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Terrain

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''

######################################################
### Importation Module :
######################################################

import random

######################################################
### Fonctions hors-classe :
######################################################

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
    
def tuples_en_coordonnees(coordo_perso, cases, numero_geant = None):
    '''
    change les tuples composés de -1, 1 et de 0 avec des coordonnées de cases
    : params
        coordo_perso (tuple)
        cases (list)
        numero_geant (int ou None) si int alors c'est un géant sinon personnage "normal"
    : return (list of tuples), le tableau avec les coordonnées des cases
    '''
    #Assertions
    assert isinstance(coordo_perso, tuple), "les coordonnées doivent être dans un tuple"
    assert isinstance(cases, list), "les cases sont un tableau"
    assert numero_geant == None or numero_geant in [0, 1, 2, 3], "le numéro du géant doit être soit None soit 0, 1, 2, 3"
    #Code
    dic_geant = {0 : (0, 0),
                 1 : (-1, 0),
                 2 : (0, -1),
                 3 : (-1, -1)
                }
    
    tab_cases = []
    for tuples in cases:
        if not numero_geant == None :
            tuples = (dic_geant[numero_geant][0] + tuples[0], dic_geant[numero_geant][1] + tuples[1])
        x = coordo_perso[0] + tuples[0]
        y =  coordo_perso[1] + tuples[1]
        if 0 <= x <= 20 and  0 <= y <= 20 : #dans la grille
            nouveau_tuple = (x, y)
            tab_cases.append(nouveau_tuple)
    return tab_cases
    
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
            niveau (int) valant par défaut 1
        '''
        #Assertion
        #assert isinstance(attributs_jeu, module_attributs_jeu.Attributs_Jeu), 'attributs_jeu doit être de la classe Attributs_Jeu (module_attributs_jeu) !'
        assert isinstance(niveau, int) and niveau > 0, "le niveau doit être un entier strictement positif"
        #Code
        self.attributs_jeu = attributs_jeu
        self.niveau = niveau
        self.grille = Terrain.attribuer_grille(self)
        
    def attribuer_grille(self):
        '''
        attribue une grille en fonction du niveau demandé
        : return (list of list)
        '''
        grille = []
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
    
    def est_possible(self, x, y):
        '''
        renvoie True si la case de coordonnées (x,y) est vide et False sinon
        : params
            x, y (int)
        : return (bool)
        '''
        #assertions
        assert isinstance(x, int) and 0 <= x <= 20, 'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20, 'y doit être un entier compris entre 0 et 20 inclus'
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
        assert isinstance(x, int) and 0 <= x <= 20, 'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20, 'y doit être un entier compris entre 0 et 20 inclus'
        #code
        self.grille[y][x] = personnage
    
    ######################################
    ########### Méthodes
    ######################################
    
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
            trouve = self.condition_case_geant(x, y)
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
        #Assertions
        assert isinstance(x, int) and 0 <= x <= 20,'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20,'y doit être un entier compris entre 0 et 20 inclus'
        #Code
        return (self.est_possible(x + 1, y) and
                self.est_possible(x , y + 1) and
                self.est_possible(x + 1, y + 1))
    
    def trouver_case_libre(self, chaine = None):
        '''
        renvoie un tuple de coordonnées pris au hasard et avec la case à ces coordonnées libre
        : param chaine (str ou None), si str, vaut soit 'bas' soit 'haut' → utilisé pour l'apparition des coffres dans une 
        zone spécifique
        : return (tuple)
        '''
        tab_pont = [(3, 2), (17, 2), (3, 18), (17, 18), #petit pont
                    (2, 9), (3, 9), (2, 10), (3, 10), (2, 11), (3, 11), #pont gauche
                    (17, 9), (18, 9), (17, 10), (18, 10), (17, 11), (18, 11), #pont droit
                    (9, 9), (10, 9), (11, 9), (9, 10), (10, 10), (11, 10), (9, 11), (10, 11), (11, 11)] #pont central
        
        ##Données
        trouve = False #par défaut, on n'a pas trouvé de case
        
        #Tant que la future case n'est pas libre, on choisit une nouvelle fois une case au hasard
        while not trouve :
            #Coordonnées au hasard
            x = random.randint(0, 20)
            if chaine == 'haut':
                y = random.randint(0, 10)
            elif chaine == 'bas' :
                y = random.randint(10, 20)
            else :
                y = random.randint(0, 20)
            trouve = self.est_possible(x, y)
            if trouve and chaine == 'monstre' :
                trouve = not (x, y) in tab_pont #les monstres ne doivent pas apparaître sur les ponts
        return x, y
