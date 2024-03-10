# -*- coding: utf-8 -*-

'''
-> Medieval Fight: Module pour les objets du jeu

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''
######################################################
### Importations
######################################################
import random, module_personnage, module_terrain

######################################################
### Coffres
######################################################
class Coffre():
    '''
    une classe pour les coffres
    '''
    def __init__(self, x, y):
        '''
        initialise la classe
        : params
            x, y (int)
        '''
        self.x = x
        self.y = y
        self.contenu = self.definir_contenu()
        self.est_ouvert = False
        self.avancement_ouverture = 1 
        self.dic_contenu = {1 : 'bonus de vie pour le personnage',
                            2 : 'changement de personnage',
                            3 : "augmente de 5 les dégâts d'attaque du personnage",
                            4 : "ressuscite le dernier personnage mort de l'équipe du personnage",
                            5 : "ressuscite le dernier personnage mort de l'équipe adverse",
                            6 : 'ajoute une potion de vie à la réserve de la sorcière',
                            7 : 'ajoute une potion de mort à la réserve de la sorcière',
                            8 : "ajoute une potion de changement d'équipe à la réserve de la sorcière",
                            9 : 'ajoute une potion de mort à la réserve de la sorcière ennemie',
                            10 : "augmente de 1 les dégâts d'attaque de tous les personnages de l'équipe adverse"
                            }
        
    ######################################################
    ### Accesseurs :
    ######################################################
    def acc_x(self):
        '''
        renvoie l'attribut x
        : return (int)
        '''
        return self.x
    
    def acc_y(self):
        '''
        renvoie l'attribut y
        : return (int)
        '''
        return self.y
    
    def acc_contenu(self):
        '''
        renvoie l'attribut contenu
        : return (int)
        '''
        return self.contenu
    
    def acc_est_ouvert(self):
        '''
        renvoie l'attribut est_ouvert
        : return (bool)
        '''
        return self.est_ouvert
    
    def acc_avancement_ouverture(self) :
        '''
        renvoie l'attribut avancement_ouverture
        : return (bool)
        '''
        return self.avancement_ouverture
    
    ######################################################
    ### Mutateurs :
    ######################################################
    
    def mut_contenu(self):
        '''
        modifie le contenu du coffre en modifiant l'attribut contenu
        : pas de return
        '''
        self.contenu = self.definir_contenu()
        
    def mut_avancement_ouverture(self, valeur) :
        '''
        Modifie l'attribut avancement_ouverture
        : param valeur (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int) !'
        #Code
        self.avancement_ouverture = valeur
    
    ######################################################
    ### Méthodes :
    ######################################################
    
    def definir_contenu(self):
        '''
        renvoie un nombre entre 1 et 5 suivant le contenu du coffre:
            1 : bonus de vie pour le personnage (9%)
            2 : changement de personnage (8%)
            3 : augmente de 5 les dégâts d'attaque du personnage (7%)
            4 : ressuscite le dernier personnage mort de l'équipe du personnage (8%)
            5 : ressuscite le dernier personnage mort de l'équipe adverse (18%)
            6 : ajoute trois potions de soin à la réserve de la sorcière (14%)
            7 : ajoute une potion de mort à la réserve de la sorcière (8%)
            8 : ajoute deux potions de changement d'équipe à la réserve de la sorcière (6%)
            9 : ajoute deux potions de mort à la réserve de la sorcière ennemie (9%)
            10 : augmente de 1 les dégâts d'attaque de tous les personnages de l'équipe adverse (13%)
        '''
        nombre = random.randint(0, 99)
        if 0 <= nombre <= 8 : #bonus de vie pour le personnage
            reponse = 1
        elif 9 <= nombre <= 16 : #changement de personnage
            reponse = 2
        elif 17 <= nombre <= 23 : #augmente de 5 les dégâts d'attaque du personnage
            reponse = 3
        elif 24 <= nombre <= 31 : #ressuscite le dernier personnage mort de l'équipe du personnage
            reponse = 4
        elif 32 <= nombre <= 49 : #ressuscite le dernier personnage mort de l'équipe adverse
            reponse = 5
        elif 50 <= nombre <= 63 : #ajoute trois potions de vie à la réserve de la sorcière
            reponse = 6
        elif 64 <= nombre <= 71 : #ajoute une potion de mort à la réserve de la sorcière 
            reponse = 7
        elif 72 <= nombre <= 77 : #ajoute deux potions de changement d'équipe à la réserve de la sorcière
            reponse = 8
        elif 78 <= nombre <= 86 : #ajoute une potion de mort à la réserve de la sorcière ennemie
            reponse = 9
        else : #augmente de 2 les dégâts d'attaque de tous les personnages de l'équipe adverse
            reponse = 10
        return reponse
    
    def est_present_autour(self, terrain, personnage):
        '''
        renvoie True si il y a un personnage de l'équipe qui joue autour du coffre et False sinon
        : params
            terrain (module_terrain.Terrain)
            personnage (module_personnage.Personnage)
        : return (bool)
        '''
        #Assertions
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        assert isinstance(personnage, module_personnage.Personnage), "le personnage doit être de la classe Personnage"
        #Code
        alentour = module_terrain.cases_autour((self.x, self.y)) #on regarde les cases autour du coffre
        present = False
        i = 0
        while not present and i < len(alentour): #tant qu'on n'a pas trouvé ou qu'on n'a pas tout regardé
            perso = terrain.acc_terrain(alentour[i][0], alentour[i][1])
            present = perso == personnage
            i += 1
        return present
    
    def ouverture(self):
        '''
        change l'attribut ouvert en True
        : pas de return
        '''
        self.est_ouvert = True
        self.avancement_ouverture = 2
           
######################################################
### Potions
######################################################      
class Potion():
    '''
    une classe pour une potion
    '''
    def __init__(self, contenu):
        '''
        initialise une potion mystère
        : param contenu (int)
            • 1 : réduit les pv du personnage visé
            • 2 : augmente les pv du personnage visé
            • 3 : tue le personnage visé
            • 4 : change l'équipe du personnage visé
        '''
        #assertions
        assert isinstance(contenu, int) and contenu in [1, 2, 3, 4], "le contenu doit être une entier entre 1 et 4 inclus !"
        #code
        self.contenu = contenu
        self.etendue = self.etendue_potion()
        
    ####################################
    ############# Accesseurs :
    ####################################
    
    def acc_contenu(self):
        '''
        renvoie le contenu de la potion avec un entier naturel compris entre 1 et 1
        : return (int)
        '''
        return self.contenu
    
    def acc_etendue(self):
        '''
        renvoie l'attribut etendue
        : return (int)
        '''
        return self.etendue
        
    def etendue_potion(self):
        '''
        renvoie les cases que la potion va atteindre
            1 : une case (60%)
            2 : deux cases (au hasard entre haut, bas, droite et gauche)  (25%)
            3 : cinq cases (haut, bas, droite, gauche, centre) (10%)
            4 : neuf cases (le carré autour du centre) (5%)
        : return (int)
        '''
        if self.contenu == 1 or self.contenu == 2: #potion d'attaque ou de guérison
            nombre = random.randint(0, 99)
            if 0 <= nombre <= 59:
                reponse = 1
            elif 60 <= nombre <= 84:
                reponse = 2
            elif 85 <= nombre <= 94:
                reponse = 3
            else:
                reponse = 4
        else : #potion de mort ou changement d'équipe
            reponse = 1 #juste la case elle-même
        return reponse

    def definir_cases_atteintes(self, x, y, terrain):
        '''
        renvoie un tableau avec les coordonnées des cases touchées par la potion
        : params
            x, y (int)
            terrain (module_terrain.Terrain)
        : return (list)
        '''
        #Assertions
        assert isinstance(x, int) and 0 <= x <= 20, 'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20, 'y doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        #Code
        ##Tableau des coordonnées finales
        tab_cases = []
        ##Intermédiaire
        tuples_cases_2 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        tuples_cases = [(0, 0)]
        if not self.etendue == 1: #2, 3 et 4 
            if self.etendue == 2: #2 cases
                tuples_cases.append(random.choice(tuples_cases_2))
            else: #3 et 4 (5 ou 9 cases)
                for tuples in tuples_cases_2 :
                    tuples_cases.append(tuples)
                if self.etendue == 4: #9 cases
                    for tuples in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
                        tuples_cases.append(tuples)
        #Finalité                            
        for tuples in tuples_cases:
            n_x = x + tuples[0]
            n_y = y + tuples[1]
            tab_cases.append((n_x, n_y))
            #Si c'est un géant, tout le géant doit être touché
            perso = terrain.acc_terrain(n_x, n_y)
            if isinstance(perso, module_personnage.Personnage) and perso.acc_personnage() == 'geant': #si c'est un géant
                famille = module_personnage.trouve_famille_geant(perso)
                for elt in famille : #pour chaque partie du géant
                    if not elt in tab_cases : #si il n'y est pas déjà dans le tableau
                        tab_cases.append(elt) #on l'ajoute
        return tab_cases