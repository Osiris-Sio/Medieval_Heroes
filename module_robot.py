# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Robot

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################

import module_jeu, module_attributs_jeu, module_terrain, module_personnage, random, time, module_objets
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
    ### Méthodes Personnages Rouges :
    ######################################################
    
    def acc_tab_personnages_rouges(self) :
        '''
        
        '''
        tab_personnages_rouges = []
        for perso in self.attributs_jeu.acc_tab_personnages() :
            if perso.acc_equipe() == 'rouge' :
                tab_personnages_rouges.append(perso)
        random.shuffle(tab_personnages_rouges)
        return tab_personnages_rouges
                
    ######################################################
    ### Méthodes Déplacer Personnages :
    ######################################################
    
    def choisir_personnage_deplacement(self, tab_personnages_rouges, terrain) :
        '''
        Regarde pour chacun de ses personnages s'il y un ennemi pas loin.
        '''
        tab_perso_case = []
        
        i = 0
        for personnage in tab_personnages_rouges :
        
            self.jeu.changer_personnage(personnage)
            ennemi_proche = self.attaquer_ennemi_proche(personnage, terrain, True)
            
            if ennemi_proche != None :
                case = random.choice(self.attributs_jeu.acc_deplacements())
                tab_perso_case = [personnage, case]
                    
        if tab_perso_case == [] :
            
            i_personnage = 0
            while i_personnage < len(tab_personnages_rouges) and tab_perso_case == [] :
                personnage = tab_personnages_rouges[i_personnage]
                self.jeu.changer_personnage(personnage)
                
                i_case = 0
                while i_case < len(terrain.attributs_jeu.acc_deplacements()) and tab_perso_case == [] :
                    
                    if personnage.personnage == 'cavalier' :   
                        perso_annexe = module_personnage.Cavalier(personnage.acc_equipe(), self.attributs_jeu.acc_deplacements_cavalier()[i_case][0], self.attributs_jeu.acc_deplacements_cavalier()[i_case][1], personnage.acc_pv())
                        
                        
                        
                        
                    perso_annexe = module_personnage.Personnage(personnage.acc_personnage(), personnage.acc_equipe(), self.attributs_jeu.acc_deplacements()[i_case][0], self.attributs_jeu.acc_deplacements()[i_case][1], personnage.acc_pv())
                    
                    
                    ennemi_a_attaquer = self.attaquer_ennemi_proche(perso_annexe, terrain)
            
                    if ennemi_a_attaquer != None : 
                        if personnage.personnage == 'cavalier' :
                            tab_perso_case = [personnage, self.attributs_jeu.acc_deplacements_cavalier()[i_case]]
                        else :
                            tab_perso_case = [personnage, self.attributs_jeu.acc_deplacements()[i_case]]

                    i_case += 1
                i_personnage += 1
            
        if tab_perso_case == [] :
            personnage = random.choice(tab_personnages_rouges)
            self.jeu.changer_personnage(personnage)
            
            if personnage.personnage == 'cavalier' :
                case = random.choice(self.attributs_jeu.acc_deplacements_cavalier())
            else :
                case = random.choice(self.attributs_jeu.acc_deplacements())
            
            while case[1] <= 0 :
                personnage = random.choice(tab_personnages_rouges)
                self.jeu.changer_personnage(personnage)
                if personnage.personnage == 'cavalier' :
                    case = random.choice(self.attributs_jeu.acc_deplacements_cavalier())
                else :
                    case = random.choice(self.attributs_jeu.acc_deplacements())
            
            tab_perso_case = [personnage, case]
                                
        #case = self.attributs_jeu.acc_deplacements()[random.randint(0, len(self.attributs_jeu.acc_deplacements()) - 1)]
        return tab_perso_case
    
    def deplacer_personnage(self, tab_personnages_rouges, terrain) :
        '''
        Le robot choisit le meilleur personnage à deplacer et le déplace
        '''
        tab_perso_case = self.choisir_personnage_deplacement(tab_personnages_rouges, terrain)
        
        if self.attributs_jeu.acc_selection().acc_personnage() == 'geant':
            self.jeu.deplacer_geant(tab_perso_case[1][0], tab_perso_case[1][1])  
        else :
            self.jeu.deplacer(tab_perso_case[1][0], tab_perso_case[1][1])
        
        self.jeu.deplacement_console(self.attributs_jeu.acc_selection(), tab_perso_case[1]) #Ajoute une phrase de déplacement dans la console du jeu
        self.jeu.effacer_actions()
        self.attributs_jeu.mut_nombre_action(self.attributs_jeu.acc_nombre_action() + 1) #Augmente le nombre d'action de 1
        self.personnage_deplace.append(tab_perso_case[0])
        
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
        
    def attaquer_ennemi_proche(self, allie, terrain, une_case_proche = False) :
        '''
        Le robot regarde s'il y a un ennemi proche de son personnage allie (dans les cases d'attaques possibles).
        '''
        #tableau cases
        if not une_case_proche :
            if allie.personnage == 'geant' :
                tab = [(0, -1), (-1, 0), (-1, 1), (1, -1), (0, 2), (2, 0), (2, 1), (1, 2), (-1, -1), (-1, 2), (2, -1), (2, 2)]
                tab = self.tuples_en_coordonnees(allie, tab)
            else :
                tab = allie.cases_valides_attaques(terrain)
        else :
            tab = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            tab = self.tuples_en_coordonnees(allie, tab)
        
        ennemi = None
        i = 0
        while i < len(tab) and ennemi == None : 
            perso = terrain.acc_terrain(tab[i][0], tab[i][1])
            
            if allie.acc_personnage() == 'sorciere' and isinstance(perso, module_personnage.Personnage) and perso.acc_equipe() == 'rouge' and 0 < perso.acc_pv() <= 4 :
                ennemi = perso #Pour le soigner (même équipe)
            
            elif isinstance(perso, module_personnage.Personnage) and perso.acc_equipe() != 'rouge' :
                if isinstance(perso, module_personnage.Monstre) and perso.acc_etat() != 1 :
                    ennemi = perso
                else :
                    ennemi = perso
            
            i += 1
        return ennemi
    
    def choisir_personnage_attaquer(self, tab_personnages_rouges, terrain) :
        '''
        Le robot choisit le personnage allie avec lequel il va attaquer.
        '''
        tab_allie_ennemi = []
        
        i_personnage = 0
        while i_personnage < len(tab_personnages_rouges) and tab_allie_ennemi == [] :
            personnage = tab_personnages_rouges[i_personnage]
            self.jeu.changer_personnage(personnage)
            
            ennemi = self.attaquer_ennemi_proche(personnage, terrain)
            
            if ennemi != None and personnage.acc_personnage() == 'sorciere' :
                if ennemi.acc_equipe() == 'rouge' and not self.attributs_jeu.acc_potions_rouges()[2].est_vide():
                    self.attributs_jeu.mut_potion_rouge_selectionnee(2)
                elif ennemi.acc_personnage() == 'sorciere' and not self.attributs_jeu.acc_potions_rouges()[4].est_vide() :
                    self.attributs_jeu.mut_potion_rouge_selectionnee(4)
                elif ennemi.acc_personnage() == 'monstre' :
                    self.attributs_jeu.mut_potion_rouge_selectionnee(1)
                else :
                    tab = [1, 3, 4]
                    numero_potion = random.choice(tab)
                    while self.attributs_jeu.acc_potions_rouges()[numero_potion].est_vide() :   
                        tab.remove[numero_potion]
                        numero_potion = random.choice(tab)
                    self.jeu.attaque_sorciere_console(personnage.acc_equipe())
                    self.attributs_jeu.mut_potion_rouge_selectionnee(numero_potion)
                    
                self.jeu.ouverture_potion(ennemi.acc_x(), ennemi.acc_y())
                tab_allie_ennemi = [personnage, None]
            
            elif ennemi != None :
                tab_allie_ennemi = [personnage, ennemi]
            
            i_personnage += 1
        
        return tab_allie_ennemi
    
    def attaquer_ennemi(self, tab_personnages_rouges, terrain) :
        '''
        Le robot attaque un ennemi proche d'un de ses personnages.
        '''
        tab_allie_ennemi = self.choisir_personnage_attaquer(tab_personnages_rouges, terrain)
        
        if tab_allie_ennemi != [] :
            allie = tab_allie_ennemi[0]
            ennemi = tab_allie_ennemi[1]
            
            
            if ennemi.acc_personnage() == 'geant':
                famille = self.jeu.famille_geant((ennemi.acc_x(), ennemi.acc_y()))[0]
                for geant in famille :
                    geant.est_attaque(allie.acc_personnage())
                    geant.mut_endommage()
            
            elif ennemi.acc_personnage() != 'sorciere' :
                ennemi.est_attaque(allie.acc_personnage()) 
                ennemi.mut_endommage()
                
            self.attributs_jeu.mut_attaque_en_cours(True)
            self.attributs_jeu.mut_attaque_temps(0)
            if allie.acc_personnage() != "sorciere" :
                self.jeu.attaque_console(allie, ennemi)
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
            
            
            
            elif self.temps_attente != None and time.time() - self.temps_attente > 2 :
                tab_personnages_rouges = self.acc_tab_personnages_rouges()
                
                if not self.attaquer_ennemi(tab_personnages_rouges, terrain) :
                    self.deplacer_personnage(tab_personnages_rouges, terrain)
                
                self.temps_attente = None
                
        else :
            self.personnage_deplace = []