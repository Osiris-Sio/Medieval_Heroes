# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Personnage

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################

from graphe import parcourir_graphe
from graphe import module_graphe_dic
import random, module_terrain

######################################################
### Fonction hors-classe :
######################################################

def trouve_famille_geant(perso):
    '''
    renvoie la bonne famille des géants
    : params
        perso (Personnage)
    : return (list)
    '''
    ##Assertions
    assert isinstance(perso, Personnage) and perso.acc_personnage() == 'geant', "le personnage doit être de la classe Geant"
    #Code
    tab = []
    dic_coordo = {0 : [(1, 0), (0, 1), (1, 1)],
                  1 : [(-1, 0), (0, 1), (-1, 1)],
                  2 : [(0, -1), (1, 0), (1, -1)],
                  3 : [(0, -1), (-1, 0), (-1, -1)]}
    
    for case in dic_coordo[perso.acc_numero_geant()]:
        tab.append((perso.acc_x() + case[0], perso.acc_y() + case[1]))
    return tab
    
######################################################
### Classe Personnage
######################################################

##Dictionnaire des pv 
DIC_PV = {'archere' : 10,
         'paladin' : 8,
         'cavalier' :8,
         'geant' : 30,
         'sorciere' : 15,
         'poulet' : 5,
         'ivrogne' : 7,
         'barbare' : 12,
         'cracheur de feu' : 13,
         'valkyrie' : 9,
         'mage' : 12,
         'monstre' : 5
                }

#Dictionnaire des dégâts infligés
DIC_ATTAQUES_BLEU = {'archere' : 7,
                'paladin' : 5,
                'cavalier' : 7,
                'geant' : 10,
                'sorciere' : 0,
                'poulet' : 2,
                'ivrogne' : 5,
                'barbare' : 10,
                'cracheur de feu' : 10,
                'valkyrie' : 12,
                'mage' : 8,
                'monstre' : 3
                }
               
DIC_ATTAQUES_ROUGE = {'archere' : 7,
                'paladin' : 5,
                'cavalier' : 7,
                'geant' : 10,
                'sorciere' : 0,
                'poulet' : 2,
                'ivrogne' : 5,
                'barbare' : 10,
                'cracheur de feu' : 10,
                'valkyrie' : 12,
                'mage' : 8,
                'monstre' : 3
                }

def mut_dic_attaques(personnage, equipe, val):
    '''
    modifie le DIC_ATTAQUES de la couleur passée en paramètre (equipe)
    : params
        personnage (str), le personnage du dic pour lequel il y a un changement
        equipe (str), 'bleu' ou 'rouge'
        val (int), la nouvelle valeur
    : pas de return
    '''
    #assertions
    assert personnage in ['monstre', 'mage', 'paladin', 'geant', 'sorciere', 'valkyrie', 'archere', 'poulet', 'cavalier', 'cracheur de feu', 'ivrogne', 'barbare'], 'le personnage doit exister !' 
    assert equipe in ['bleu', 'rouge'], "l'équipe doit être rouge ou bleu !"
    assert isinstance(val, int), 'la nouvelle valeur à entrer dans le dictionnaire doit être un entier !'
    #code
    if equipe == 'bleu':
        DIC_ATTAQUES_BLEU[personnage] = val
    else :
        DIC_ATTAQUES_ROUGE[personnage] = val
    

class Personnage():
    '''
    une classe pour les personnages du jeu
    '''
    def __init__(self, personnage, equipe, x, y):
        '''
        initialise le personnage
        : params
            personnage (str)
            equipe (str), une des deux équipes, 'bleu' ou 'rouge'
            x (int), 0 <= x <= 20
            y (int), 0 <= y <= 20
        '''
        #assertions
        assert personnage in ['monstre', 'mage', 'paladin', 'geant', 'sorciere', 'valkyrie', 'archere', 'poulet', 'cavalier', 'cracheur de feu', 'ivrogne', 'barbare'], 'le personnage doit exister !' 
        assert equipe in ['bleu','rouge', 'neutre'], "l'équipe est soit bleu, soit rouge ou neutre (monstre)"
        assert 0 <= x <= 20, "x ne doit pas être hors de la grille !"
        assert 0 <= y <= 20, "y ne doit pas être hors de la grille !"
        #code
        self.personnage = personnage
        self.equipe = equipe
        self.x = x
        self.y = y
        self.pv = DIC_PV[personnage]
        self.endommage = False
        self.attaque = False #par défaut, le personnage n'attaque personne
        self.soigne = False
  
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
    
    def acc_attaque(self):
        '''
        renvoie l'attribut attaque
        : return (bool)
        '''
        return self.attaque
        
    def acc_x(self):
        '''
        renvoie l'attribut x
        : return (int), 0 <= x <= 20
        '''
        return self.x
        
    def acc_y(self):
        '''
        renvoie l'attribut y
        : return (int), 0 <= y <= 20
        '''
        return self.y
    
    def acc_endommage(self):
        '''
        renvoie l'attribut endommage
        : return (bool)
        '''
        return self.endommage
    
    def acc_soigne(self):
        '''
        renvoie l'attribut soigne
        : return (bool)
        '''
        return self.soigne
    
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
        
    def mut_attaque(self):
        '''
        modifie l'attribut attaque du personnage
        : pas de return
        '''
        self.attaque = not self.attaque
        
    def mut_soigne(self):
        '''
        modifie l'attribut soigne du personnage
        : pas de return
        '''
        self.soigne = not self.soigne
        
    def mut_pv(self, valeur):
        '''
        modifie l'attribut pv
        : param valeur (int)
        : pas de return
        '''
        #assertion
        assert isinstance(valeur, int), 'la nouvelle valeur doit être un entier'
        #code
        self.pv = valeur
        
    def mut_personnage(self, nouveau_perso):
        '''
        modifie l'attribut personnage
        : param nouveau_perso (str)
        : pas de return
        '''
        #assertion
        assert nouveau_perso in ['monstre', 'mage', 'paladin', 'geant', 'sorciere', 'valkyrie', 'archere', 'poulet', 'cavalier', 'cracheur de feu', 'ivrogne', 'barbare'], 'le personnage doit exister !' 
        #code
        self.personnage = nouveau_perso
        
    def mut_equipe(self):
        '''
        modifie l'attribut equipe
        : pas de return
        '''
        if self.equipe == 'bleu':
            self.equipe = 'rouge' #devient rouge
        else:
            self.equipe = 'bleu' #devient bleu
        
    def deplacer(self, nouveau_x, nouveau_y):
        '''
        déplace le personnage aux nouvelles coordonnées (nouveau_x, nouveau_y)
        : params
            nouveau_x (int), 0 <= nouveau_x <= 20
            nouveau_y (int), 0 <= nouveau_y <= 20
        : pas de return, modifie les attributs x et y
        '''
        self.x = nouveau_x
        self.y = nouveau_y

    def est_mort(self):
        '''
        renvoie True si le personnage est mort (<= 0 pv) et False sinon
        : return (bool)
        '''
        return self.pv <= 0
    
    def est_attaque(self, ennemi, nombre = None):
        '''
        retire le nombre de pv au personnage correspondant à l'ennemi
        : params
            ennemi (str)
            nombre (int), par défaut vaut None
        : pas de return, modifie l'attribut pv
        '''
        #Assertion
        assert ennemi in ['monstre', 'mage', 'paladin', 'geant', 'sorciere', 'valkyrie', 'archere', 'poulet', 'cavalier', 'cracheur de feu', 'ivrogne', 'barbare'], 'le personnage doit exister !' 
        #Code
        if nombre is None: #autre qu'une sorcière
            if self.acc_equipe() == 'bleu' : #Si le personnage est bleu
                self.mut_pv(self.acc_pv() - DIC_ATTAQUES_ROUGE[ennemi]) 
            else :
                self.mut_pv(self.acc_pv() - DIC_ATTAQUES_BLEU[ennemi]) 
        
        else : #une sorcière, donc dépend de la potion 
            self.pv -= nombre
        
    #################################################
    ####### Déplacements + Attaques
    #################################################
    
    def cases_valides_attaques(self, terrain):
        '''
        améliore les cases d'attaques
        Les cases valides sont les cases avec un personnage dont les monstres
        : param terrain (Terrain)
        : return (list)
        '''
        #Assertion
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        #Code
        cases = self.cases_attaques() #les cases d'attaques par défaut
        attaques_valides = [] #les cases valides finales
        for attaque in cases: #on regarde chaque case
            perso = terrain.acc_terrain(attaque[0], attaque[1])
            if isinstance(perso, Personnage) and (not perso.acc_equipe() == self.equipe or self.personnage == 'sorciere') : #on vérifie que c'est un personnage de l'équipe adverse
                #si c'est un monstre
                if isinstance(perso, Monstre) and not perso.acc_etat() == 1 :#si le monstre n'est pas sous-terre
                    attaques_valides.append(attaque) # si elle est bonne, on l'ajoute
                #géant
                elif perso.acc_personnage() == 'geant':
                    famille = trouve_famille_geant(perso) #tous les membres du géant
                    for elt in famille :
                        if not elt in attaques_valides :
                            attaques_valides.append(elt)
                #"classique"
                else:
                    attaques_valides.append(attaque)
            
        terrain.attributs_jeu.mut_attaques(attaques_valides)
        return attaques_valides

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
        return module_terrain.tuples_en_coordonnees((self.x, self.y), cases)
    
    def cases_attaques(self):
        '''
        renvoie un tableau contenant les coordonnées des cases sur lesquelles le personnage peut attaquer
        : return (list of tuples)
        '''
        ###Dictionnaire des attaques
        dic_attaques = { 'ivrogne' : [(-1, -1), (1, -1), (-1, 1), (1, 1)],
                         'barbare' : [(1, 0), (0, 1), (-1, 0), (0, -1)],
                         'cracheur de feu' : [(-1, 0), (1, 0), (0, -1), (0, 1), (-2, 0), (2, 0), (0, -2), (0, 2)],
                         'archere' : [(-1, -4), (0, -4), (1, -4), (-1, 4), (0, 4), (1, 4), (-4, -1), (-4, 0), (-4, 1), (4, -1), (4, 0), (4, 1), (-3, -3), (-3, 3), (3, -3), (3, 3)],
                         'sorciere' : [(-2, -2), (-1, -2), (-2, -1), (1, -2), (2, -2), (2, -1), (-2, 1), (2, 2), (1, 2), (-1, 2), (-2, 2), (2, 1)],
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
        return module_terrain.tuples_en_coordonnees((self.x, self.y), cases)
    
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
        : param cases (list)
        : return (list of tuples)
        '''
        dep_ok = []  
        graphe = self.construire_graphe((self.x, self.y), cases)
        for elt in cases :
            try: #on essaie de trouver un chemin
                parcourir_graphe.depiler_chemin(graphe, (self.x, self.y), elt) 
                dep_ok.append(elt)
            except:
                None
        return dep_ok
    
    def construire_graphe(self, coordo, terrain):
        '''
        renvoie le graphe construit à partir des déplacements possibles et des coordonnées du personnage
        : params
            coordo (tuple)
            terrain (list), tableau des déplacements possibles
        : return (dict)
        '''
        graphe = module_graphe_dic.Graphe_non_oriente_dic()
        for coordo_centre in [coordo] + terrain :
            for coordo_voisin in module_terrain.cases_autour(coordo_centre): #on regarde les voisins de la case
                if coordo_voisin in [coordo] + terrain : #si le voisin est atteignable par le personnage
                    graphe.ajouter_arete(coordo_centre, coordo_voisin) #on ajoute une arête entre les deux cases
        return graphe
    
########################################
#### Cavalier
########################################
                
class Cavalier(Personnage):
    '''
    une classe pour un cavalier
    '''
    def __init__(self, equipe, x, y):
        '''
        initialise une classe pour un cavalier, hérite de la classe Personnage
        : params
            equipe (str), une des deux équipes, 'bleu' ou 'rouge'
            x (int), 0 <= x <= 20
            y (int), 0 <= y <= 20
        '''
        super().__init__('cavalier', equipe, x, y)
        
    def cases_deplacements(self):
        '''
        renvoie un tableau contenant les coordonnées des cases sur lesquelles le personnage pourrait éventuellement aller
        : return (list of tuple)
        '''
        tab_cavalier = [(-2, -1), (-1, -2), (1, -2), (-2, 1), (-1, 2), (2, -1), (1, 2), (2, 1)]
        #Les coordonnées
        return module_terrain.tuples_en_coordonnees((self.x, self.y), tab_cavalier)
    
    def cases_valides_deplacement(self, terrain):
        '''
        améliore les cases de déplacements
        Les cases valides sont :
        - Les cases vides, sans personnages ni obstacles
        - Des cases accessibles depuis le personnage sans sauts
        : param terrain (Terrain)
        : pas de return
        '''
        #Assertion
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        #Déplacements pour bouger
        perso = Personnage('paladin', 'bleu', self.x, self.y) #déplacements des paladins
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
    def __init__(self, equipe, x, y, numero_geant):
        '''
        initialise une classe pour un géant, hérite de la classe Personnage
        : params
            equipe (str), une des deux équipes, 'bleu' ou 'rouge'
            x (int), 0 <= x <= 20
            y (int), 0 <= y <= 20
            numero_geant (int), 0 <= numero_geant <= 3
        '''
        #assertion
        assert isinstance(numero_geant, int) and -1 <= numero_geant <= 3 , 'le numéro du géant doit être 0, 1, 2 ou 3 !'
        #code
        super().__init__('geant', equipe, x, y)
        self.numero_geant = numero_geant
        
    #####################################
    ##### Accesseur :
    #####################################
    
    def acc_numero_geant(self):
        '''
        renvoie l'attribut numero_geant
        : return (int), 0, 1, 2, ou 3
        '''
        return self.numero_geant

    #####################################
    ##### Méthodes :
    #####################################
        
    def cases_deplacements(self):
        '''
        renvoie un tableau contenant les coordonnées des cases sur lesquelles le personnage pourrait éventuellement aller
        : return (list of tuple)
        '''
        ###Dictionnaire des déplacements
        tab_geant = [(0, -1), (-1, 0), (-1, 1), (1, -1), (0, 2), (2, 0), (2, 1), (1, 2)]
        ##dépend de la case sélectionnée du géant
        return module_terrain.tuples_en_coordonnees((self.x, self.y), tab_geant, self.numero_geant)
    
    def cases_attaques(self):
        '''
        renvoie un tableau contenant les coordonnées des cases sur lesquelles le personnage peut attaquer
        : return (list of tuples)
        '''
        tab_geant = [(0, -1), (-1, 0), (-1, 1), (1, -1), (0, 2), (2, 0), (2, 1), (1, 2), (-1, -1), (-1, 2), (2, -1), (2, 2)]
        ##dépend de la case sélectionnée du géant
        return module_terrain.tuples_en_coordonnees((self.x, self.y), tab_geant, self.numero_geant)
    
    def cases_valides_deplacement(self, terrain):
        '''
        améliore les cases de déplacements
        Les cases valides sont :
        - Les cases vides, sans personnages ni obstacles
        - Des cases accessibles depuis le personnage sans sauts*
        : param terrain (Terrain)
        : pas de return
        '''
        #Assertion
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        #Code
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
                for case_autour in module_terrain.cases_autour(case)[:4] :#seulement à droite, à gauche, en haut ou en bas
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
            0 <= pv 
            etat (int), 1 = dans la terre / 2 = hors de la terre
        '''
        #assertions
        assert etat in [1, 2], "l'état doit être soit 1 soit 2 !"
        assert 0 <= pv, "le monstre doit avoir des pv positifs !"
        #code
        super().__init__('monstre', 'neutre', x, y)
        self.pv = pv
        self.etat = etat
        self.tab_victime = []
        #pour l'affichage
        self.coordo_x = x * 38 + 250
        self.coordo_y = y * 38
        self.futur_coordo_x = None
        self.futur_coordo_y = None
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
    
    def acc_futur_x(self):
        '''
        renvoie l'attribut futur_x
        : return (int)
        '''
        return self.futur_x
    
    def acc_futur_y(self):
        '''
        renvoie l'attribut futur_y
        : return (int)
        '''
        return self.futur_y
    
    def acc_coordo_x(self):
        '''
        renvoie l'attribut coordo_x
        : return (int)
        '''
        return self.coordo_x
    
    def acc_coordo_y(self):
        '''
        renvoie l'attribut coordo_y
        : return (int)
        '''
        return self.coordo_y
    
    def acc_futur_coordo_x(self):
        '''
        renvoie l'attribut futur_coordo_x
        : return (int)
        '''
        return self.futur_coordo_x
    
    def acc_futur_coordo_y(self):
        '''
        renvoie l'attribut futur_coordo_y
        : return (int)
        '''
        return self.futur_coordo_y
    
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
        
    def mut_coordo_x(self, val):
        '''
        modifie l'attribut coordo_x
        : param val (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(val, int), "la valeur doit être un entier"
        #Code
        self.coordo_x = val
        
    def mut_coordo_y(self, val):
        '''
        modifie l'attribut coordo_y
        : param val (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(val, int), "la valeur doit être un entier"
        #Code
        self.coordo_y = val
        
    def mut_futur_x(self, val):
        '''
        modifie l'attribut futur_x
        : param val (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(val, int), "la valeur doit être un entier"
        #Code
        self.futur_x = val
        
    def mut_futur_y(self, val):
        '''
        modifie l'attribut futur_y
        : param val (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(val, int), "la valeur doit être un entier"
        #Code
        self.futur_y = val
        
    def mut_futur_coordo_x(self, val):
        '''
        modifie l'attribut futur_coordo_x
        : param val (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(val, int), "la valeur doit être un entier"
        #Code
        self.futur_coordo_x = val
        
    def mut_futur_coordo_y(self, val):
        '''
        modifie l'attribut futur_coordo_y
        : param val (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(val, int), "la valeur doit être un entier"
        #Code
        self.futur_coordo_y = val
        
    ####################################
    ####### Méthodes
    ####################################
    
    def trouver_joueurs_proches(self, terrain):
        '''
        renvoie les coordonnées des joueurs les plus proches de lui
        : param terrain (module_terrain.Terrain)
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
                            cases.append(perso) #on ajoute le personnage au tableau
            #agrandissement de la recherche
            l -= 1
            h += 1
        return cases
    
    def prochaine_victime(self, terrain, equipe_en_cours):
        '''
        renvoie les coordonnées de la prochaine victime (choisis au hasard parmi la liste possible)
        : params
            terrain (module_terrain.Terrain)
            equipe_en_cours (str), 'bleu' ou 'rouge'
        : return tuple
        '''
        victimes = self.trouver_joueurs_proches(terrain)
        #on essaie de prendre une victime appartenant à l'équipe en cours ou alors on choisit au pif
        pro_victime = self.choisir_victime(victimes, equipe_en_cours)
        
        return pro_victime #les coordonnées de la prochaine victime
       
    def choisir_victime(self, victimes, equipe_en_cours):
        '''
        renvoie la victime choisie parmi les victimes possibles en priorisant une victime appartenant à l'équipe en cours
        : params
            victimes (list)
            equipe_en_cours (str)
        : return (Personnage)
        '''
        pro_victime = None
        i = 0
        #on essaie de trouver une victime de l'équipe qui est en train de jouer
        while i < len(victimes) and pro_victime == None:
            vic = victimes[i]
            #on regarde si la victime est de l'équipe qui est en train de jouer
            if vic.acc_equipe() == equipe_en_cours :
                pro_victime = vic
            i += 1
            
        #si il n'y a aucune victime de l'équipe en cours
        if pro_victime == None :
            pro_victime = random.choice(victimes) #on choisit au hasard
        
        return pro_victime
         
    def construire_graphe(self, coordo, terrain):
        '''
        renvoie le graphe construit à partir de toutes les cases du terrain
        : params
            coordo (tuple), coordonnées de la victime
            terrain (Terrain)
        : return (Graphe)
        '''
        graphe = module_graphe_dic.Graphe_non_oriente_dic() #un graphe vide
        for x in range(21): #les x
            for y in range(21): #les y
                case = (x, y) #la case
                if terrain.est_possible(x, y) or case == coordo or (self.x, self.y) == case: #si la case est vide ou si c'est la victime ou si c'est le monstre
                    cases_autour = module_terrain.cases_autour(case)
                    for case_voisine in cases_autour :
                        if terrain.est_possible(case_voisine[0], case_voisine[1]): #si la cases est vide
                            graphe.ajouter_arete(case, case_voisine) #on ajoute une arête entre les deux cases
        return graphe
    
    def prochaines_coordonnees(self, terrain, equipe_en_cours):
        '''
        renvoie les coordonnées du déplacement le plus optimal, du chemin le plus court
        : params
            terrain (Terrain)
            equipe_en_cours(str)
        : return (tuple)
        '''
        #assertion
        assert isinstance(equipe_en_cours, str) and equipe_en_cours in ['bleu', 'rouge'], "l'équipe en cours doit être une chaîne de caractères entre bleu et rouge !"
        #code
        victime = self.prochaine_victime(terrain, equipe_en_cours)
        ##graphe
        graphe = self.construire_graphe((victime.acc_x(), victime.acc_y()), terrain)
        chemin = parcourir_graphe.depiler_chemin(graphe, (self.x, self.y), (victime.acc_x(), victime.acc_y()))
        #renvoie la prochaine case
        return chemin[1] #la prochaine case autre que la case du monstre elle-même

    def attaquer(self, terrain):
        '''
        modifie l'attribut attaque_possible si il y a un ou des ennemis à côté du monstre et renvoie
        le tableau contenant toutes les victimes autour du monstre
        : terrain (module_terrain.Terrain)
        : return (list), la liste des victimes
        '''
        #tableau cases
        tab = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        tab_coordo = module_terrain.tuples_en_coordonnees((self.x, self.y), tab)

        #victimes
        tab_v = []
        for cases in tab_coordo: #on regarde toutes les cases autour du monstre
            perso = terrain.acc_terrain(cases[0], cases[1])
            if isinstance(perso, Personnage) and not perso.acc_personnage() == 'monstre': #si c'est un personnage sans être un monstre
                tab_v.append(perso)

        ##mutateur
        self.tab_victime = tab_v
            
    def attaquer_ennemi_proche(self, equipe_en_cours):
        '''
        attaque l'ennemi le plus proche et renvoie le personnage attaqué
        : param equipe_en_cours (str), 'bleu' ou 'rouge'
        : return (Personnage)
        '''
        #assertion
        assert isinstance(equipe_en_cours, str) and equipe_en_cours in ['bleu', 'rouge'], "l'équipe en cours doit être une chaîne de caractères entre bleu et rouge !"
        #code
        if not self.tab_victime == [] : #si une attaque est possible
            victime = self.choisir_victime(self.tab_victime, equipe_en_cours) #on choisit au hasard la victime à attaquer, de préférance appartenant à l"équipe qui joue
        else:
            victime = None #pas de victime à proximité
        return victime