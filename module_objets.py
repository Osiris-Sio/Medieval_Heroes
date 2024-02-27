# -*- coding: utf-8 -*-

'''
-> Medieval Fight: Module pour les objets du jeu

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''
######################################################
### Importation
######################################################
import random

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
                    2 : 'envoie une météorite sur un endroit choisi par le joueur',
                    3 : 'changement de personnage',
                    4 : 'nuage de fumée à un endroit donné',
                    5 : "augmente les dégâts d'attaque du personnage",
                    6 : "fait spawn un géant dans l'équipe du personnage",
                    7 : "fait spawn un géant dans l'équipe adverse",
                    8 : "ressuscite le dernier personnage mort de l'équipe du personnage",
                    }
    def __repr__(self):
        '''
        renvoie une chaîne de caractères pour décrire le coffre
        : return (str)
        '''
        
        return "Un coffre de coordonnées (" + str(self.x) + ', ' + str(self.y) + ") et de contenu : " + self.dic_contenu[self.contenu]
    
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
    
    def mut_avancement_ouverture(self, valeur) :
        '''
        Modifie l'attribut avancement_ouverture
        :param valeur (int)
        :pas de return
        '''
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int) !'
        self.avancement_ouverture = valeur
    
    ######################################################
    ### Méthodes :
    ######################################################
    
    def definir_contenu(self):
        '''
        renvoie un nombre entre 1 et 5 suivant le contenu du coffre:
            1 : +bonus de vie pour le personnage (30%)
            2 : +envoie une météorite sur un endroit choisi par le joueur (11%)
            3 : +changement de personnage (5%)
            4 : -nuage de fumée à un endroit donné (15%)
            5 : +augmente les dégâts d'attaque du personnage (25%)
            6 : +fait spawn un géant dans l'équipe du personnage (3%)
            7 : -fait spawn un géant dans l'équipe adverse (4%)
            8 : +ressuscite le dernier personnage mort de l'équipe du personnage (7%)
        '''
        '''
        nombre = random.randint(0, 100)
        if 0 <= nombre <= 29:
            reponse = 1
        elif 30 <= nombre <= 41 :
            reponse = 2
        elif 42 <= nombre <= 46:
            reponse = 3
        elif 47 <= nombre <= 61:
            reponse = 4
        elif 62 <= nombre <= 86:
            reponse = 5
        elif 87 <= nombre <= 89:
            reponse = 6
        elif 90 <= nombre <= 93:
            reponse = 7
        else:
            reponse = 8
        '''
        return random.choice([1, 3, 5, 8])
    
    def alentour(self):
        '''
        renvoie les coordonnées des cases autour du coffre
        : return (list)
        '''
        tab = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                n_x = self.x + i
                n_y = self.y + j
                if 0 <= n_x <= 20 and 0 <= n_y <= 20: #la case est dans le terrain
                    tab.append((n_x, n_y))
        return tab
    
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
    def __init__(self, x, y):
        '''
        initialise une potion mystère
        : params
            x, y (int), coordonnées de la case où a atteri la potion
        '''
        self.x = x
        self.y = y
        self.contenu = self.definir_contenu()
        self.etendu = self.etendue_potion()
        self.cases_atteintes = self.definir_cases_atteintes
        
    def __repr__(self):
        '''
        renvoie une chaîne de caractères pour décrire la potion
        : return (str)
        '''
        dic_contenu = {1 : 'réduit les pv du personnage visé',
                       }
        return "Une potion qui" + dic_contenu[self.contenu] + " et qui a une portée de " + str(len(self.etendue_potion()))
    
    def acc_contenu(self):
        '''
        renvoie le contenu de la potion avec un entier naturel compris entre 1 et 1
        : return (int)
        '''
        return self.contenu
    
    def acc_cases(self):
        '''
        renvoie le tableau contenant toutes les cases atteintes par la potion
        : return (list)
        '''
        return self.cases_atteintes
        
    def definir_contenu(self):
        '''
        renvoie le contenu de la potion avec un entier naturel compris entre 0 et 5
            1 : réduit les pv du personnage visé (100%)
        : return (int)
        '''
        nombre = random.randint(0, 100)
        return 1
        
    def etendue_potion(self):
        '''
        renvoie les cases que la potion va atteindre
            1 : une case (70%)
            2 : deux cases (au hasard entre haut, bas, droite et gauche)  (24%)
            3 : cinq cases (haut, bas, droite, gauche, centre) (5%)
            4 : neuf cases (le carré autour du centre) (1%)
        : return (int)
        '''
        nombre = random.randint(0, 100)
        if 0 <= nombre <= 69:
            reponse = 1
        elif 70 <= nombre <= 94:
            reponse = 2
        elif 95 <= nombre <= 99:
            reponse = 3
        else:
            reponse = 4
        return reponse
    
    def definir_cases_atteintes(self):
        '''
        renvoie un tableau avec les coordonnées des cases touchées par la potion
        : return (list)
        '''
        ##Tableau des coordonnées finales
        tab_cases = []
        ##Intermédiaire
        tuples_cases_2 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        tuples_cases = [(0, 0)]
        if not self.etendu == 1: #2, 3 et 4
            if self.etendu == 2: #2
                tuples_cases.append(random.choice(tuples_cases_2))
            else: #3 et 4
                for tuples in tuples_cases_2 :
                    tuples_cases.append(tuples)
                if self.etendu == 4: #4
                    for tuples in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
                        tuples_cases.append(tuples)
        #Finalité                            
        for tuples in tuples_cases:
            tab_cases.append((self.x + tuples[0], self.y + tuples[1]))
        return tab_cases
        
        
        
            
            
            
            
            
            
            
            
            
        