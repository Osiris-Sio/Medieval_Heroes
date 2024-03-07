# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Robot.

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################

import module_jeu, module_attributs_jeu, module_terrain, module_personnage, random, time
from graphe import module_graphe_dic, parcourir_graphe

######################################################
### Classe Robot :
######################################################

class Robot():
    '''
    Une classe pour le robot.
    '''
    def __init__(self, jeu, attributs_jeu):
        '''
        initialise le robot.
        : params
            jeu (module_jeu.Jeu)
            attributs_jeu (module_attributs_jeu.Attributs_Jeu)
            terrain (module_terrain.Terrain)
        '''
        #assertions :
        assert isinstance(jeu, module_jeu.Jeu), "jeu doit venir de la classe Jeu (module_jeu) !"
        assert isinstance(attributs_jeu, module_attributs_jeu.Attributs_Jeu), "attributs_jeu doit venir de la classe Attributs_Jeu (module_attributs_jeu) !"
        #Attributs Paramètres:
        self.jeu = jeu
        self.attributs_jeu = attributs_jeu
        
        #Attributs :
        self.personnage_deplace = []
        self.en_attente = False
        self.temps_attente = None
        
    ######################################################
    ### Méthodes Déplacer Personnages :
    ######################################################
    
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
    
    def construire_graphe(self, allie, ennemi, terrain):
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
                if terrain.est_possible(x, y) or case == ennemi or (allie.x, allie.y) == case:
                    cases_autour = self.coordonnees_autour(case)
                    for case_voisine in cases_autour :
                        if terrain.est_possible(case_voisine[0], case_voisine[1]): #si la cases est vide
                            graphe.ajouter_arete(case, case_voisine) #on ajoute une arête entre les deux cases
        return graphe
        
    def trouver_ennemi_proche(self, allie, terrain):
        '''
        renvoie les coordonnées de l'ennemi le plus proches du personnage allie passé en paramètre
        : param allie (module_personnage.Personnage), personnage de l'équipe du robot ("rouge")
        : return (module_personnage.Personnage)
        '''
        assert allie.acc_equipe() == "rouge", 'Le paramètre doit être un personnage de l\'équipe du robot (rouge) !'
        ennemi = None
        l = -1
        h = 2
        while ennemi == None :
            longueur = l
            while l <= longueur <= h and ennemi == None :
                hauteur = l
                while l <= hauteur <= h and ennemi == None :
                    #coordonnées des cases
                    x = allie.acc_x() + longueur
                    y = allie.acc_y() + hauteur
                    if 0 <= x <= 20 and 0 <= y <= 20 : #si la case est dans le terrain
                        perso = terrain.acc_terrain(x, y) #on regarde le personnage
                        #regarde le contenu de la case
                        if isinstance(perso, module_personnage.Personnage) and perso.acc_equipe() != "rouge" :
                            ennemi = perso
                    hauteur += 1
                longueur += 1
            #agrandissement de la recherche
            l -= 1
            h += 1
        return ennemi
    
    def choisir_personnage_deplacement(self, terrain) :
        '''
        Regarde pour chacun de ses personnages s'il y un ennemi pas loin.
        '''
        tab_perso_chemin = []
        for personnage in self.attributs_jeu.acc_tab_personnages() :
            if personnage.acc_equipe() == 'rouge' and not (personnage in self.personnage_deplace) :
                try :
                    ennemi = self.trouver_ennemi_proche(personnage, terrain)
                    graphe = self.construire_graphe(personnage, (ennemi.acc_x(), ennemi.acc_y()), terrain)
                    chemin = parcourir_graphe.depiler_chemin(graphe, (personnage.x, personnage.y), (ennemi.acc_x(), ennemi.acc_y()))
                    if tab_perso_chemin == [] or len(chemin) < len(tab_perso_chemin[1]):
                        tab_perso_chemin = [personnage, chemin]
                        case = self.prochaine_coordonnees(tab_perso_chemin)
                        if case == None :
                            tab_perso_chemin = []
                except :
                    pass
                    
        return [tab_perso_chemin[0], case]
    
    def prochaine_coordonnees(self, tab_perso_chemin) :
        '''
        En fonction du personnage allie passer en paramètre,
        le robot va prendre la meilleur case pour aller jusqu'à sa cible
        : param tab_perso_chemin (list), [personnage, chemin]
            personnage (module_personnage.Personnage)
            chemin (list), le chemin jusqu'à l'ennemi
        : return (tuple)
        '''
        assert isinstance(tab_perso_chemin[0], module_personnage.Personnage) and isinstance(tab_perso_chemin[1], list), 'Le paramètre doit être un tableau (list) avec comme premier element un personnage (module_personnage.Personnage) et en second, un chemin (list) !'
        self.jeu.changer_personnage(tab_perso_chemin[0])
        prochaine_case = None
        i_chemin = len(tab_perso_chemin[1]) - 1
        while i_chemin >= 0 and prochaine_case == None :
            if not isinstance(tab_perso_chemin[0], module_personnage.Cavalier) and tab_perso_chemin[1][i_chemin] in self.attributs_jeu.acc_deplacements() :
                prochaine_case = tab_perso_chemin[1][i_chemin]
            elif tab_perso_chemin[1][i_chemin] in self.attributs_jeu.acc_deplacements_cavalier() :
                prochaine_case = tab_perso_chemin[1][i_chemin]
            i_chemin -= 1
        return prochaine_case
    
    def deplacer_personnage(self, terrain) :
        '''
        Le robot choisit le meilleur personnage à deplacer et le déplace
        '''
        tab_perso_case = self.choisir_personnage_deplacement(terrain)
        self.jeu.deplacer(tab_perso_case[1][0], tab_perso_case[1][1])
        self.jeu.deplacement_console(self.attributs_jeu.acc_selection(), tab_perso_case[1]) #Ajoute une phrase de déplacement dans la console du jeu
        self.jeu.effacer_actions()
        self.attributs_jeu.mut_nombre_action(self.attributs_jeu.acc_nombre_action() + 1) #Augmente le nombre d'action de 1
        self.personnage_deplace.append(tab_perso_case[0])
        print(self.personnage_deplace)
        
    ######################################################
    ### Méthodes Attaquer Personnages :
    ######################################################
    
    def tuples_en_coordonnees(self, allie, cases):
        '''
        change les tuples composés de -1, 1 et de 0 avec des coordonnées de case
        : return (list of tuples), le tableau avec les coordonnées des cases
        '''
        tab_cases = []
        for tuples in cases:
            x = allie.x + tuples[0]
            y =  allie.y + tuples[1]
            if 0 <= x <= 20 and  0 <= y <= 20 : #dans la grille
                nouveau_tuple = (x, y)
                tab_cases.append(nouveau_tuple)
        return tab_cases
        
    def attaquer_ennemi_proche(self, allie, terrain) :
        '''
        Le robot regarde s'il y a un ennemi proche de son personnage allie.
        '''
        #tableau cases
        tab = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        tab_coordo = self.tuples_en_coordonnees(allie, tab)
        
        ennemi = None
        i = 0
        while i < len(tab_coordo) and ennemi == None : 
            perso = terrain.acc_terrain(tab_coordo[i][0], tab_coordo[i][1])
            if isinstance(perso, module_personnage.Personnage) and perso.acc_equipe() != 'rouge' :
                if isinstance(perso, module_personnage.Monstre) and perso.acc_etat() != 1 :
                    ennemi = perso
                else :
                    ennemi = perso
            i += 1
        return ennemi
    
    def choisir_personnage_attaquer(self, terrain) :
        '''
        Le robot choisit le personnage allie avec lequel il va attaquer.
        '''
        tab_personnage_rouge = []
        tab_allie_ennemi = []
        i = 0
        for perso in self.attributs_jeu.acc_tab_personnages() :
            if perso.acc_equipe() == 'rouge' :
                tab_personnage_rouge.append(perso)
        while i < len(tab_personnage_rouge) and tab_allie_ennemi == [] :
            ennemi = self.attaquer_ennemi_proche(tab_personnage_rouge[i], terrain)
            if ennemi != None :
                tab_allie_ennemi = [tab_personnage_rouge[i], ennemi]
            i += 1
        return tab_allie_ennemi
    
    def attaquer_ennemi(self, terrain) :
        '''
        Le robot attaque un ennemi proche d'un de ses personnages.
        '''
        tab_allie_ennemi = self.choisir_personnage_attaquer(terrain)
        
        if tab_allie_ennemi != [] :
            allie = tab_allie_ennemi[0]
            ennemi = tab_allie_ennemi[1]
            
            if ennemi.acc_personnage() == 'geant':
                famille = self.jeu.famille_geant((ennemi.acc_x(), ennemi.acc_y()))[0]
                for geant in famille :
                    geant.est_attaque(allie.acc_personnage())
                    geant.mut_endommage()
            else :
                ennemi.est_attaque(allie.acc_personnage()) 
                ennemi.mut_endommage()
                
            self.attributs_jeu.mut_attaque_en_cours(True)
            self.attributs_jeu.mut_attaque_temps(0)
            self.jeu.changer_personnage(' ') #Enlève le personnage sélectionner par le joueur (rien sélectionné)
            self.attributs_jeu.mut_nombre_action(self.attributs_jeu.acc_nombre_action() + 1) #Augmente le nombre d'action de 1
            self.jeu.effacer_actions()
            self.jeu.jouer_monstres()
            return True
        
        return False
                
    ######################################################
    ### Méthodes Ouvrir Coffres :
    ######################################################
    
    
    
    
    
    
    
    
    ######################################################
    ### Méthode Jouer :
    ######################################################
    
    def jouer_robot(self, terrain) :
        '''
        Fait jouer le robot quand c'est à son tour avec de pause de 5 secondes entres les actions
        '''
        if self.attributs_jeu.acc_equipe_en_cours() == 'rouge' :
            if self.temps_attente == None and not self.attributs_jeu.acc_deplacement_en_cours() and not self.attributs_jeu.acc_attaque_en_cours() :
                self.temps_attente = time.time()
            elif self.temps_attente != None and time.time() - self.temps_attente > 0.5 :
                if not self.attaquer_ennemi(terrain) :
                    print('ok')
                    self.deplacer_personnage(terrain)
                self.temps_attente = None
                
        else :
            self.personnage_deplace = []