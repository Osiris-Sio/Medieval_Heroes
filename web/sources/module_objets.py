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
            equipe_en_cours (str), 'bleu' ou 'rouge'
        : return (tuple)
        '''
        #Assertions
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        assert isinstance(personnage, module_personnage.Personnage), "le personnage doit être de la classe Personnage"
        #Code
        alentour = module_terrain.cases_autour((self.x, self.y)) #on regarde les cases autour du coffre
        present = False
        case = None #la case qui a ouvert le coffre
        i = 0
        if personnage.acc_personnage() == 'geant' :
            famille = module_personnage.trouve_famille_geant(personnage)
            while not present and i < len(famille) :
                present = famille[i] in alentour
                i += 1
                if present :
                    case = famille[i-1] 
        else :
            while not present and i < len(alentour): #tant qu'on n'a pas trouvé ou qu'on n'a pas tout regardé
                perso = terrain.acc_terrain(alentour[i][0], alentour[i][1])
                present = perso == personnage
                i += 1
                if present :
                    case = (alentour[i-1])
        return present, case
    
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
    
    def definir_cases_etendue(self):
        '''
        renvoie les cases sous forme de tuples composés de 1, -1 et de 0 suivant l'étendue de la potion
        : return (list)
        '''
        tuples = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        cases_etendue = [(0, 0)]
        if self.etendue == 2: #2 cases
            cases_etendue.append(random.choice(tuples[:4]))
        elif self.etendue == 3: #5 cases
            for case in tuples[:4] :
                cases_etendue.append(case)
        elif self.etendue == 4: #9 cases
            for case in tuples:
                cases_etendue.append(case)
        return cases_etendue
    
    def definir_cases_potion(self, tab, x, y, terrain, equipe_en_cours):
        '''
        renvoie le tableau contenant des tuples (coordonnées de case) respectant ces conditions :
        • la case doit être dans le terrain
        • le contenu de la case doit être un personnage
        • si c'est un géant, tout le géant doit être touché
        • vérifie l'équipe du personnage en fonction du contenu de la potion (seule la potion 2 permet "d'attaquer" des personnages de son équipe
        : params
            tab (list)
            x, y (int)
            terrain (module_terrain.Terrain)
            equipe_en_cours (str), 'bleu' ou 'rouge'
        : return (list)
        '''
        #Assertions
        assert isinstance(tab, list), "le paramètre doit être un tableau !"
        assert isinstance(x, int) and 0 <= x <= 20, 'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20, 'y doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        assert equipe_en_cours in ['bleu', 'rouge'], "l'équipe en cours doit être soit bleu soit rouge"
        #Code
        tab_cases = []
        for case in tab:
            n_x = x + case[0]
            n_y = y + case[1]
            if 0 <= n_x <= 20 and 0 <= n_y <= 20 and isinstance(terrain.acc_terrain(n_x, n_y), module_personnage.Personnage) : #dans le terrain et c'est un personnage
                perso = terrain.acc_terrain(n_x, n_y)
                if (perso.acc_equipe() == equipe_en_cours and self.contenu == 2) or (not perso.acc_equipe() == equipe_en_cours and not self.contenu == 2) : #equipe du perso en fonction de la potion
                    #Si c'est un géant, tout le géant doit être touché
                    if perso.acc_personnage() == 'geant': #si c'est un géant
                        famille = module_personnage.trouve_famille_geant(perso)
                        for elt in famille : #pour chaque partie du géant
                            if not elt in tab_cases : #si il n'y est pas déjà dans le tableau
                                tab_cases.append(elt) #on l'ajoute
                    else :
                        if not (n_x, n_y) in tab_cases :
                            tab_cases.append((n_x, n_y))
        return tab_cases
    
    def definir_cases_atteintes(self, x, y, terrain, equipe_en_cours):
        '''
        renvoie un tableau avec les coordonnées des cases touchées par la potion
        : params
            x, y (int)
            terrain (module_terrain.Terrain)
            equipe_en_cours (str), 'bleu' ou 'rouge'
        : return (list)
        '''
        #Assertions
        assert isinstance(x, int) and 0 <= x <= 20, 'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20, 'y doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        assert equipe_en_cours in ['bleu', 'rouge'], "l'équipe en cours doit être soit bleu soit rouge"
        #Code
        ##Tuples
        cases_etendue = self.definir_cases_etendue()
        #Coordonnées de case
        tab_coordonnees = self.definir_cases_potion(cases_etendue, x, y, terrain, equipe_en_cours)
        return tab_coordonnees
