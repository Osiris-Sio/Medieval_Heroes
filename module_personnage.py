# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Personnage.

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################
from graphe import parcourir_graphe
from graphe import module_graphe_dic
import random
######################################################
### Classe Personnage
######################################################

##Dictionnaire des pv d'attaques
DIC_PV = {'archere' : 10,
                'paladin' : 10,
                'cavalier' :10,
                'geant' : 10,
                'sorciere' : 10,
                'poulet' : 10,
                'ivrogne' : 10,
                'barbare' : 10,
                'cracheur de feu' : 10,
                'valkyrie' : 10,
                'mage' : 10,
                'monstre' : 10
                }

DIC_ATTAQUES = {'archere' : 7,
                'paladin' : 5,
                'cavalier' : 7,
                'geant' : 15,
                'sorciere' : 0,
                'poulet' : 2,
                'ivrogne' : 5,
                'barbare' : 10,
                'cracheur de feu' : 10,
                'valkyrie' : 12,
                'mage' : 8,
                'monstre' : 3
                }
               
def mut_dic_attaques(personnage, val):
    '''
    modifie le DIC_ATTAQUES
    : params
        personnage (str), le personnage du dic pour lequel il y a un changement
        val (int), la nouvelle valeur
    '''
    #assertions
    assert personnage in ['monstre', 'mage', 'paladin', 'geant', 'sorciere', 'valkyrie', 'archere', 'poulet', 'cavalier', 'cracheur de feu', 'ivrogne', 'barbare'], 'le personnage doit exister !' 
    assert isinstance(val, int), 'la nouvelle valeur à entrer dans le dictionnaire doit être un entier !'
    #code
    DIC_ATTAQUES[personnage] = val

class Personnage():
    '''
    une classe pour les personnages du jeu
    '''
    def __init__(self, personnage, equipe, x, y, pv):
        '''
        initialise le personnage
        : params
            personnage (str)
            equipe (str), une des deux équipes, 'bleu' ou 'rouge'
            x (int), 0 <= x <= 20
            y (int), 0 <= y <= 20
            pv (int), pv <= 60
        '''
        #assertions
        assert personnage in ['monstre', 'mage', 'paladin', 'geant', 'sorciere', 'valkyrie', 'archere', 'poulet', 'cavalier', 'cracheur de feu', 'ivrogne', 'barbare'], 'le personnage doit exister !' 
        assert equipe in ['bleu','rouge', 'neutre'], "l'équipe est soit bleu, soit rouge ou neutre (monstre)"
        assert 0 <= x <= 20, "x ne doit pas être hors de la grille !"
        assert 0 <= y <= 20, "y ne doit pas être hors de la grille !"
        assert pv <= 60, "les pv ne doivent pas dépasser 60"
        #code
        self.personnage = personnage
        self.equipe = equipe
        self.x = x
        self.y = y
        self.pv = pv
        self.endommage = False
        self.direction_droite = False
        
    def __repr__(self):
        '''
        renvoie une chaîne de caractères pour décrire le paladin
        : return (str)
        >>> s = Personnage('sorciere', 'bleu', 12, 10, 6)
        >>> s
        sorciere de coordonnées (12,10), possédant 6pv et appartenant à l'équipe bleu
        >>> a = Personnage('archere', 'rouge', 13, 4, 12)
        >>> a
        archere de coordonnées (13,4), possédant 12pv et appartenant à l'équipe rouge
        '''
        return self.personnage + ' de coordonnées (' + str(self.x)+ ',' + str(self.y) + '), possédant ' + str(self.pv) + "pv et appartenant à l'équipe " + self.equipe
        
    def __str__(self):
        '''
        renvoie une chaîne de caractères représentant le personnage
        : return (str)
        >>> p = Personnage('paladin', 'rouge', 4, 8, 5)
        >>> print(p)
        P
        >>> c = Personnage('cracheur de feu', 'rouge', 15, 15, 12)
        >>> print(c)
        C
        '''
        lettre = self.personnage[0]
        return lettre.upper() #la première lettre du personnage en majuscule
    
    ######################################################
    ### Accesseurs
    ######################################################

    def acc_personnage(self):
        '''
        renvoie l'attribut personnage
        : return (str)
        '''
        return self.personnage
    
    def acc_equipe(self):
        '''
        renvoie l'attribut equipe
        : return (str)
        '''
        return self.equipe
        
    def acc_x(self):
        '''
        renvoie l'attribut x
        : return (int), 0 <= x <= 20
        >>> p = Personnage('paladin', 'bleu', 12, 5, 12)
        >>> p.acc_x()
        12
        >>> s = Personnage('sorciere', 'bleu', 20, 1, 13)
        >>> s.acc_x()
        20
        >>> c = Personnage('cracheur de feu', 'rouge', 3, 10, 2)
        >>> c.acc_x()
        3
        '''
        return self.x
        
    def acc_y(self):
        '''
        renvoie l'attribut y
        : return (int), 0 <= y <= 20
        >>> c = Personnage('cavalier', 'rouge', 19, 15, 10)
        >>> c.acc_y()
        15
        >>> v = Personnage('valkyrie', 'bleu', 16, 9, 5)
        >>> v.acc_y()
        9
        >>> p = Personnage('poulet', 'rouge', 13, 4, 4)
        >>> p.acc_y()
        4
        '''
        return self.y
    
    def acc_endommage(self):
        '''
        renvoie l'attribut endommage
        : return (bool)
        '''
        return self.endommage
    
    def acc_pv(self):
        '''
        renvoie l'attribut pv
        : return (int)
        '''
        return self.pv
    
    ######################################################
    ### Mutateurs
    ######################################################
    
    def mut_endommage(self):
        '''
        modifie l'attribut endommage du personnage
        : pas de return
        '''
        self.endommage = not self.endommage
        
    def mut_pv(self, valeur):
        '''
        modifie l'attribut pv
        : pas de return
        '''
        #assertion
        assert isinstance(valeur, int), 'la nouvelle valeur doit être un entier !'
        #code
        self.pv = valeur
        
    def mut_personnage(self, nouveau_perso):
        '''
        modifie l'attribut personnage
        : param nouveau_perso (str)
        : pas de return
        '''
        #assertion
        assert isinstance(nouveau_perso, str), 'le nouveau personnage doit être de type str !'
        #code
        self.personnage = nouveau_perso
        
    def deplacer(self, nouveau_x, nouveau_y):
        '''
        déplace le personnage aux nouvelles coordonnées (nouveau_x, nouveau_y)
        : params
            nouveau_x (int), 0 <= nouveau_x <= 20
            nouveau_y (int), 0 <= nouveau_y <= 20
        : pas de return, modifie les attributs x et y
        >>> p = Personnage('poulet', 'rouge', 12, 15, 2)
        >>> p.acc_x()
        12
        >>> p.acc_y()
        15
        >>> p.deplacer(10, 10)
        >>> p.acc_x()
        10
        >>> p.acc_y()
        10
        '''
        self.x = nouveau_x
        self.y = nouveau_y

    def est_mort(self):
        '''
        renvoie True si le personnage est mort (0 pv) et False sinon
        : return (bool)
        >>> c = Personnage('cracheur de feu', 'rouge', 12, 15, -1)
        >>> c.est_mort()
        True
        >>> p = Personnage('poulet', 'rouge', 8, 8, 0)
        >>> p.est_mort()
        True
        >>> a = Personnage('archere', 'bleu', 11, 20, 9)
        >>> a.est_mort()
        False
        '''
        return self.pv <= 0
    
    def est_attaque(self, ennemi):
        '''
        retire le nombre de pv au personnage correspondant à l'ennemi
        : ennemi (str)
        : pas de return, modifie l'attribut pv
        '''
        self.pv -= DIC_ATTAQUES[ennemi]
    #################################################
    ####### Déplacements + Attaques
    #################################################
    def cases_valides_attaques(self, terrain):
        '''
        améliore les cases d'attaques
        Les cases valides sont :
        - Les cases avec un personnage dont les monstres
        : param terrain (Terrain)
        : pas de return
        '''
        cases = self.cases_attaques() #les cases d'attaques par défaut
        attaques_valides = [] #les cases valides finales
        for attaque in cases: #on regarde chaque case
            perso = terrain.acc_terrain(attaque[0], attaque[1])
            if isinstance(perso, Personnage) and not perso.acc_equipe() == self.equipe : #on vérifie que c'est un personnage de l'équipe adverse
                attaques_valides.append(attaque) # si elle est bonne, on l'ajoute
        terrain.attributs_jeu.mut_attaques(attaques_valides)

    def cases_valides_deplacement(self, terrain):
        '''
        améliore les cases de déplacements
        Les cases valides sont :
        - Les cases vides, sans personnages ni obstacles
        - Des cases accessibles depuis le personnage sans sauts
        : param terrain (Terrain)
        : pas de return
        '''
        #Cases atteignables sans obstacles ni personnages
        dep_base = self.cases_deplacements()
        dep_sans_obstacles = self.cases_sans_obstacles(terrain, dep_base)
        dep_valides = self.cases_finales(dep_sans_obstacles)
        
        #Changement dans deplacements
        terrain.attributs_jeu.mut_deplacements(dep_valides)  #change les cases déplacements
    
    #################################################
    ####### Sous_fonctions
    #################################################
    
    def cases_deplacements(self):
        '''
        renvoie un tableau contenant les coordonnées des cases sur lesquelles le personnage pourrait éventuellement aller
        : return (list of tuple)
        >>> p = Personnage('paladin', 'bleu', 12, 8, 5)
        >>> p.cases_deplacements()
        [(11, 7), (13, 7), (11, 9), (13, 9), (11, 8), (13, 8), (12, 7), (12, 9), (10, 8), (14, 8), (12, 6), (12, 10)]
        '''
        ###Dictionnaire des déplacements
        dic_deplacements = { 'archere' : [(-1, -1), (1, -1), (-1, 1), (1, 1), (-2, -2), (2, -2), (-2, 2), (2, 2)],
                             'barbare' : [(-1, 0), (1, 0), (0, -1), (0, 1), (-2, 0), (2, 0), (0, -2), (0, 2)],
                             'valkyrie' : [(-3, 0), (0, -3), (3, 0), (0, 3), (2, -1), (-1, 2), (1, 2), (2, 1), (-2, 1), (1, -2), (-2, -1), (-1, -2)],
                            }
        ###Définition des cases
        if self.personnage == 'ivrogne':
            cases = dic_deplacements['archere'][:4] #une partie des déplacements de l'archère
        elif self.personnage == 'paladin' or self.personnage == 'cracheur de feu' or self.personnage == 'mage':
            cases = dic_deplacements['archere'][:4] + dic_deplacements['barbare'] #déplacements de l'ivrogne + ceux du barbare
        elif self.personnage == 'sorciere':
            cases = dic_deplacements['archere'][:4] + dic_deplacements['barbare'][4:] #déplacements de l'ivrogne + une partie de ceux du barbare 
        elif self.personnage == 'valkyrie':
            cases = dic_deplacements['barbare'] + dic_deplacements['valkyrie'] #contient les déplacements du barbare
        elif self.personnage == 'poulet':
            #contour
            tab = []
            for x in range(-4, 5):
                tuple1 = (x, 4 - abs(x))
                tab.append(tuple1)
                tuple2 = (x, -(4 - abs(x)))
                if not tuple2 in tab:
                    tab.append(tuple2)
            #cases
            cases = dic_deplacements['barbare'] + dic_deplacements['valkyrie'] + dic_deplacements['archere'][:4] + tab #valkyrie + ivrogne + reste           
        else:
            cases = dic_deplacements[self.personnage]
        
        ###Les coordonnées
        return self.tuples_en_coordonnees(cases)
    
    def cases_attaques(self):
        '''
        renvoie un tableau contenant les coordonnées des cases sur lesquelles le personnage peut attaquer
        : return (list of tuples)
        >>> v = Personnage('valkyrie', 'bleu', 15, 6, 3)
        >>> v.cases_attaques()
        [(14, 5), (16, 5), (14, 7), (16, 7), (16, 6), (15, 7), (14, 6), (15, 5)]
        '''
        ###Dictionnaire des attaques
        dic_attaques = { 'ivrogne' : [(-1, -1), (1, -1), (-1, 1), (1, 1)],
                         'barbare' : [(1, 0), (0, 1), (-1, 0), (0, -1)],
                         'cracheur de feu' : [(-1, 0), (1, 0), (0, -1), (0, 1), (-2, 0), (2, 0), (0, -2), (0, 2)],
                         'archere' : [(-1, -4), (0, -4), (1, -4), (-1, 4), (0, 4), (1, 4), (-4, -1), (-4, 0), (-4, 1), (4, -1), (4, 0), (4, 1), (-3, -3), (-3, 3), (3, -3), (3, 3)],
                         'sorciere' : [(-2, -2), (-1, -2), (-2, -1), (1, -2), (2, -2), (2, -1), (-2, 1), (2, 2), (1, 2), (-1, 2), (-2, 2), (-2, 1)],
                         'mage' : [(-1, -3), (0, -3), (1, -3), (-1, -2), (1, -2), (-1, 3), (0, 3), (1, 3), (-1, 2), (1, 2), (-3, -1), (-3, 0), (-3, 1), (-2, -1), (-2, 1), (3, -1), (3, 0), (3, 1), (2, -1), (2, 1)]
                          }
        
        ###Définition des cases
        if self.personnage == 'poulet' or self.personnage == 'paladin' or self.personnage == 'valkyrie':
            cases = dic_attaques['ivrogne'] + dic_attaques['barbare'] #ceux de l'ivrogne + ceux du barbare
        elif self.personnage == 'cavalier':
            cases = dic_attaques['cracheur de feu'][:4] + dic_attaques['ivrogne'] + dic_attaques['barbare'] #une partie de ceux du cracheur de feu + ceux de l'ivrogne + ceux du barbare 
        elif self.personnage == 'mage' :
            cases = dic_attaques['mage'] + dic_attaques['cracheur de feu'] 
        else:
            cases = dic_attaques[self.personnage]
            
        ###Les coordonnées
        return self.tuples_en_coordonnees(cases)
    
    def cases_sans_obstacles(self, terrain, cases):
        '''
        améliore les cases de déplacements en enlevant celle où il y a un obstacle ou un autre personnage
        : params
            terrain (Terrain)
            cases (list of tuples)
        : return (list of tuples)
        '''
        deplacements_valides = []
        for elt in cases:
            if terrain.est_possible(elt[0], elt[1]): #on teste si la case est vide
                deplacements_valides.append(elt) #si elle est bonne, on l'ajoute
        return deplacements_valides
    
    def cases_finales(self, cases):
        '''
        finalise les cases déplacements en ne gardant que les cases atteignables par un chemin
        : params
        : return (list of tuples)
        '''
        dep_ok = []  
        graphe = self.construire_graphe_perso((self.x, self.y), cases)
        for elt in cases :
            try:
                parcourir_graphe.depiler_chemin(graphe, (self.x, self.y), elt) #on regarde si la case est atteignable par un chemin
                dep_ok.append(elt)
            except:
                None
        return dep_ok

    def tuples_en_coordonnees(self, cases):
        '''
        change les tuples composés de -1, 1 et de 0 avec des coordonnées de case
        : return (list of tuples), le tableau avec les coordonnées des cases
        '''
        tab_cases = []
        for tuples in cases:
            x = self.x + tuples[0]
            y =  self.y + tuples[1]
            if 0 <= x <= 20 and  0 <= y <= 20 : #dans la grille
                nouveau_tuple = (x, y)
                tab_cases.append(nouveau_tuple)
        return tab_cases
    
    def construire_graphe_perso(self, coordo, deplacements):
        '''
        renvoie le graphe construit à partir des déplacements possibles et des coordonnées du personnage
        : params
            coordo (tuple)
            deplacements (list), tableau des déplacements possibles
        : return (dict)
        '''
        graphe = module_graphe_dic.Graphe_non_oriente_dic()
        for coordo_centre in [coordo] + deplacements :
            for coordo_voisin in self.coordonnees_autour(coordo_centre): #on regarde les voisins de la case
                if coordo_voisin in [coordo] + deplacements : #si le voisin est atteignable par le personnage
                    graphe.ajouter_arete(coordo_centre, coordo_voisin) #on ajoute une arête entre les deux cases
        return graphe
    
    def coordonnees_autour(self, coordo):
        '''
        renvoie les 8 coordonnées se situant juste à côté de la case de coordonnées (x, y)
        met en premier les cases en haut, en bas, à droite et à gauche
        : params
            cordo (tuple of int), coordonnées de la case centrale
        : return (list)
        '''
        tab = []
        for tuples in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]: #haut, bas, gauche, droite en premier
            tuple_case = (coordo[0] + tuples[0],coordo[1] + tuples[1])
            if 0 <= tuple_case[0] <= 20 and 0 <= tuple_case[1] <= 20: #si la case ne sort pas du terrain
                tab.append(tuple_case) 
        return tab
    
########################################
#### Cavalier
########################################
                
class Cavalier(Personnage):
    '''
    une classe pour un cavalier
    '''
    def __init__(self, equipe, x, y, pv):
        '''
        initialise une classe pour un cavalier, hérite de la classe Personnage
        : params
            personnage (str)
            equipe (str), une des deux équipes, 'bleu' ou 'rouge'
            x (int), 0 <= x <= 20
            y (int), 0 <= y <= 20
            pv (int), pv <= 60
            numero_geant (int), 0 <= numero_geant <= 3
        '''
        super().__init__('cavalier', equipe, x, y, pv)
        
    def cases_deplacements(self):
        '''
        renvoie un tableau contenant les coordonnées des cases sur lesquelles le personnage pourrait éventuellement aller
        : return (list of tuple)
        >>> p = Cavalier('rouge', 15, 10, 10)
        >>> p.cases_deplacements()
        [(13, 9), (14, 8), (16, 8), (13, 11), (14, 12), (17, 9), (16, 12), (17, 11)]
        '''
        tab_cavalier = [(-2, -1), (-1, -2), (1, -2), (-2, 1), (-1, 2), (2, -1), (1, 2), (2, 1)]
        
        #Les coordonnées
        return self.tuples_en_coordonnees(tab_cavalier)
    
    def cases_valides_deplacement(self, terrain):
        '''
        améliore les cases de déplacements
        Les cases valides sont :
        - Les cases vides, sans personnages ni obstacles
        - Des cases accessibles depuis le personnage sans sauts
        : param terrain (Terrain)
        : pas de return
        '''
        #Déplacements pour bouger
        perso = Personnage('paladin', 'bleu', self.x, self.y, 10) #déplacements des paladins
        deplacements_cavalier = self.cases_deplacements()
        dep_bouger =  deplacements_cavalier + perso.cases_deplacements() #déplacements invisibles
        #Déplacements sans obstacles
        dep_valides = self.cases_sans_obstacles(terrain, dep_bouger)
        #Cases accessibles par un chemin
        dep_finales = self.cases_finales(dep_valides)
        #Pour l'affichage
        dep_affichage = []
        for dep in dep_valides:
            if dep in deplacements_cavalier :
                dep_affichage.append(dep)
        terrain.attributs_jeu.mut_deplacements(dep_affichage) #change les cases déplacements
        terrain.attributs_jeu.mut_deplacements_cavalier(dep_finales) #change les cases déplacements affichées

########################################
#### Geant
########################################
class Geant(Personnage):
    '''
    une classe pour un géant
    '''
    def __init__(self, equipe, x, y, pv, numero_geant):
        '''
        initialise une classe pour un géant, hérite de la classe Personnage
        : params
            personnage (str)
            equipe (str), une des deux équipes, 'bleu' ou 'rouge'
            x (int), 0 <= x <= 20
            y (int), 0 <= y <= 20
            pv (int), pv <= 60
            numero_geant (int), 0 <= numero_geant <= 3
        '''
        #assertion
        assert isinstance(numero_geant, int) and -1 <= numero_geant <= 3 , 'le numéro du géant doit être 0, 1, 2 ou 3 !'
        #code
        super().__init__('geant', equipe, x, y, pv)
        self.numero_geant = numero_geant
        self.dic = {0 : (0, 0),
                     1 : (-1, 0),
                     2 : (0, -1),
                     3 : (-1, -1)
                     }
        
    def cases_deplacements(self):
        '''
        renvoie un tableau contenant les coordonnées des cases sur lesquelles le personnage pourrait éventuellement aller
        : return (list of tuple)
        >>> g = Geant('rouge', 0, 12, 15, 2)
        >>> g.cases_deplacements()
        [(0, 10), (1, 10), (0, 13), (2, 11), (2, 12), (1, 13)]
        '''
        ###Dictionnaire des déplacements
        tab_geant = [(0, -1), (-1, 0), (-1, 1), (1, -1), (0, 2), (2, 0), (2, 1), (1, 2)]
        
        ##dépend de la case sélectionnée du géant
        return self.tuples_en_coordonnees(tab_geant)
    
    def cases_attaques(self):
        '''
        renvoie un tableau contenant les coordonnées des cases sur lesquelles le personnage peut attaquer
        : return (list of tuples)
        >>> g = Geant('rouge', 20, 15, 5, 3)
        >>> g.cases_attaques()
        [(19, 13), (18, 14), (18, 15), (20, 13), (19, 16), (20, 16), (18, 13), (18, 16)]
        '''
        tab_geant = [(0, -1), (-1, 0), (-1, 1), (1, -1), (0, 2), (2, 0), (2, 1), (1, 2), (-1, -1), (-1, 2), (2, -1), (2, 2)]
        
        ##dépend de la case sélectionnée du géant
        return self.tuples_en_coordonnees(tab_geant)
    
    def cases_valides_deplacement(self, terrain):
        '''
        améliore les cases de déplacements
        Les cases valides sont :
        - Les cases vides, sans personnages ni obstacles
        - Des cases accessibles depuis le personnage sans sauts*
        : param terrain (Terrain)
        : pas de return
        '''
        deplacements = self.cases_deplacements() #les déplacements accessibles par défaut
        dep_valides = self.cases_sans_obstacles(terrain, deplacements) #cases sans obstacles
        
        ###Les deux cases doivent être libres
        dep_ok = [] #déplacements finaux
        dep_couples = self.deplacements_couples(dep_valides) #range les cases par couple car le géant fait 2 cases sur 2
        for couple in dep_couples: #on regarde chaque couple de cases
            if couple[0] in dep_valides and couple[1] in dep_valides: #si les deux cases dans une direction sont bien libres
                dep_ok.append(couple[0])
                dep_ok.append(couple[1])
        terrain.attributs_jeu.mut_deplacements(dep_ok)  #change les cases déplacements
        terrain.attributs_jeu.mut_deplacements_cavalier([])  #on enlève les déplacements du cavalier
                
    def deplacements_couples(self, deplacements):
        '''
        renvoie un tableau de tableau où les coordonnées atteignables par défaut par le géant sont par paires
        : param deplacements (list of tuples)
        : return (list of list)
        '''
        dep_deja_fait = [] #copie
        tableau_couple = []
        for case in deplacements:
            if not case in dep_deja_fait: #si ce couple n'a pas déjà été fait
                couple = []
                for case_autour in self.coordonnees_autour(case)[:4] :#seulement à droite, à gauche, en haut ou en bas
                    if case_autour in deplacements:
                        #création du nouveau couple
                        couple.append(case)
                        couple.append(case_autour)
                        #on l'ajoute au tableau des couples
                        tableau_couple.append(couple)
                        #ils sont à présents fait
                        dep_deja_fait.append(case)
                        dep_deja_fait.append(case_autour)
        return tableau_couple
    
    def tuples_en_coordonnees(self, cases):
        '''
        change les tuples composés de -1, 1 et de 0 avec des coordonnées de case
        : return (list of tuples), le tableau avec les coordonnées des cases
        '''
        tab_cases = []
        for tuples in cases:
            nouveau_tuple = (self.dic[self.numero_geant][0] + tuples[0], self.dic[self.numero_geant][1] + tuples[1])
            x = self.x + nouveau_tuple[0]
            y =  self.y + nouveau_tuple[1]
            if 0 <= x <= 20 and  0 <= y <= 20 : #dans la grille
                tab_cases.append((x, y))
        return tab_cases
    
    
########################################
#### Monstre
########################################
    
class Monstre(Personnage):
    '''
    une classe pour un monstre
    '''
    def __init__(self, x, y, pv, etat):
        '''
        initialise une classe pour un monstre
        : params
            x, y (int) avec 0 <= x, y <= 20
            pv (int)
            etat (int), 1 = dans la terre / ??? = hors de la terre
        '''
        #assertions
        assert isinstance(etat, int), "l'état doit être un entier !"
        #code
        super().__init__('monstre', 'neutre', x, y, pv)
        self.etat = etat
        self.tab_victime = []
        self.coord_x = x * 38 + 250
        self.coord_y = y * 38
        self.futur_coord_x = None
        self.futur_coord_y = None
        self.futur_x = None
        self.futur_y = None
        
    ####################################
    ####### Accesseurs
    ####################################
    def acc_etat(self):
        '''
        renvoie l'attribut etat
        : return (int)
        '''
        return self.etat
    
    ####################################
    ####### Mutateurs
    ####################################
    def mut_etat(self, nouvel_etat):
        '''
        modifie l'attribut etat du monstre
        : param nouvel_etat (int) 1 ou 2
        : pas de return
        '''
        #assertion
        assert isinstance(nouvel_etat, int) and nouvel_etat in [1, 2], "le nouvel état doit être un entier ! (1 ou 2)"
        #code
        self.etat = nouvel_etat
        
    ####################################
    ####### Méthodes
    ####################################
    
    def trouver_joueurs_proches(self, terrain):
        '''
        renvoie les coordonnées des joueurs les plus proches de lui
        : return (list of tuples)
        '''
        cases = []
        l = -1
        h = 2
        while cases == []: #on cherche jusqu'à ce qu'on trouve un joueur
            for longueur in range(l, h):
                for hauteur in range(l, h):
                    #coordonnées des cases
                    x = self.x + longueur
                    y = self.y + hauteur
                    if 0 <= x <= 20 and 0 <= y <= 20 : #si la case est dans le terrain
                        perso = terrain.acc_terrain(x, y) #on regarde le personnage
                    #regarde le contenu de la case
                    if isinstance(perso, Personnage) and not perso.acc_personnage() == 'monstre' : #c'est un perso et pas un monstre
                        cases.append((x, y))
            #agrandissement de la recherche
            l -= 1
            h += 1
        return cases
    
    def prochaine_victime(self, terrain):
        '''
        renvoie les coordonnées de la prochaine victime (choisis au hasard parmi la liste possible
        : return tuple
        '''
        victimes = self.trouver_joueurs_proches(terrain)
        if len(victimes) == 1: #une seule victime
            pro_victime = victimes[0]
        else: #sinon, à choisir au hasard
            pro_victime = random.choice(victimes)
        return pro_victime #les coordonnées de la prochaine victime
       
    def construire_graphe_perso(self, victime, terrain):
        '''
        renvoie le graphe construit à partir de toutes les cases du terrain
        : params
            victime (tuple)
            terrain (Terrain)
        : return (Graphe)
        '''
        graphe = module_graphe_dic.Graphe_non_oriente_dic() #un graphe vide
        for x in range(21): #les x
            for y in range(21): #les y
                case = (x, y) #la case
                if terrain.est_possible(x, y) or case == victime or (self.x, self.y) == case: #si la case est vide ou si c'est la victime ou si c'est le monstre
                    cases_autour = self.coordonnees_autour(case)
                    for case_voisine in cases_autour :
                        if terrain.est_possible(case_voisine[0], case_voisine[1]): #si la cases est vide
                            graphe.ajouter_arete(case, case_voisine) #on ajoute une arête entre les deux cases
        return graphe
    
    def prochaines_coordonnees(self, terrain):
        '''
        renvoie les coordonnées du déplacement le plus optimable, le chemin le plus court
        : param terrain (Terrain)
        : return (tuple)
        '''
        victime = self.prochaine_victime(terrain)
        ##graphe
        graphe = self.construire_graphe_perso(victime, terrain)
        chemin = parcourir_graphe.depiler_chemin(graphe, (self.x, self.y), victime)
        #renvoie la prochaine case
        return chemin[1] #la prochaine case autre que la case du monstre elle-même

    def attaquer(self, terrain):
        '''
        modifie l'attribut attaque_possible si il y a un ou des ennemis à côté du monstre et renvoie
        le tableau contenant toutes les victimes autour du monstre
        : terrain (Terrain)
        : return (list), la liste des victimes
        '''
        #tableau cases
        tab = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        tab_coordo = self.tuples_en_coordonnees(tab)

        #victimes
        tab_v = []
        for cases in tab_coordo: #on regarde toutes les cases autour du monstre
            perso = terrain.acc_terrain(cases[0], cases[1])
            if isinstance(perso, Personnage) and not perso.acc_personnage() == 'monstre': #si c'est un personnage sans être un monstre
                tab_v.append(perso)

        ##mutateur
        self.tab_victime = tab_v
            
    def attaquer_ennemi_proche(self):
        '''
        attaque l'ennemi le plus proche et renvoie le personnage attaqué
        : terrain (Terrain)
        : return (Personnage)
        '''
        if not self.tab_victime == [] : #si une attaque est possible
            victime = random.choice(self.tab_victime) #on choisit au hasard la victime à attaquer
        else:
            victime = None #pas de victime à proximité
        return victime
    
        

############### DOCTEST #####################  
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)