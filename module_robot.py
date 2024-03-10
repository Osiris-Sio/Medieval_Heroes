# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Robot

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################

import module_jeu, module_attributs_jeu, module_terrain, module_personnage, random, time

######################################################
### Classe Robot :
######################################################

class Robot():
    '''
    Une classe pour le robot
    '''
    def __init__(self, jeu, attributs_jeu):
        '''
        Initialise le robot
        : params
            jeu (module_jeu.Jeu)
            attributs_jeu (module_attributs_jeu.Attributs_Jeu)
        '''
        #assertions :
        assert isinstance(jeu, module_jeu.Jeu), "jeu doit venir de la classe Jeu (module_jeu) !"
        assert isinstance(attributs_jeu, module_attributs_jeu.Attributs_Jeu), "attributs_jeu doit venir de la classe Attributs_Jeu (module_attributs_jeu) !"
        #Attributs Paramètres:
        self.jeu = jeu
        self.attributs_jeu = attributs_jeu
        
        #Attributs :
        self.en_attente = False
        self.temps_attente = None
        
    ######################################################
    ### Méthodes Personnages Rouges :
    ######################################################
    
    def acc_tab_personnages_rouges(self) :
        '''
        renvoie le tableau avec tous les personnages rouges dans le désordre
        : return (list)
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
        Regarde pour chacun de ses personnages s'il y un ennemi pas loin
        : params
            tab_personnages_rouges (list)
            terrain (module_terrain.Terrain)
        : return (list)
        '''
        #Assertions
        assert isinstance(tab_personnages_rouges, list), "le tableau des personnages rouges doit être un tableau"
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        #Code
        tab_perso_case = []
        
        for personnage in tab_personnages_rouges :
        
            self.jeu.changer_personnage(personnage) #on essaie le personnage
            ennemi_proche = self.attaquer_ennemi_proche(personnage, terrain, True) #on regarde si il y a un ennemi à proximité
            
            if ennemi_proche != None : #si il y a un ennemi à attaquer
                case = random.choice(self.attributs_jeu.acc_deplacements()) #on se déplace au hasard
                tab_perso_case = [personnage, case]
                    
        if tab_perso_case == [] : #si aucun ennemi proche
            
            i_personnage = 0
            while i_personnage < len(tab_personnages_rouges) and tab_perso_case == [] :
                personnage = tab_personnages_rouges[i_personnage]
                self.jeu.changer_personnage(personnage)
                
                i_case = 0
                while i_case < len(terrain.attributs_jeu.acc_deplacements()) and tab_perso_case == [] :
                    
                    if personnage.acc_personnage() == 'cavalier' :   
                        perso_annexe = module_personnage.Cavalier(personnage.acc_equipe(), self.attributs_jeu.acc_deplacements()[i_case][0], self.attributs_jeu.acc_deplacements()[i_case][1])
                    elif personnage.acc_personnage() == 'geant':
                        perso_annexe = module_personnage.Geant(personnage.acc_equipe(), self.attributs_jeu.acc_deplacements()[i_case][0], self.attributs_jeu.acc_deplacements()[i_case][1], personnage.acc_numero_geant())
                    else:
                        perso_annexe = module_personnage.Personnage(personnage.acc_personnage(), personnage.acc_equipe(), self.attributs_jeu.acc_deplacements()[i_case][0], self.attributs_jeu.acc_deplacements()[i_case][1])
                    
                    
                    ennemi_a_attaquer = self.attaquer_ennemi_proche(perso_annexe, terrain)
            
                    if ennemi_a_attaquer != None :
                        tab_perso_case = [personnage, self.attributs_jeu.acc_deplacements()[i_case]]

                    i_case += 1
                i_personnage += 1
            
        if tab_perso_case == [] :
            personnage = random.choice(tab_personnages_rouges)
            self.jeu.changer_personnage(personnage)
            ##le personnage doit pouvoir se déplacer
            while self.attributs_jeu.acc_deplacements() == [] : 
                personnage = random.choice(tab_personnages_rouges)
                self.jeu.changer_personnage(personnage)
            
            case_correcte = False
            case = None
            while not case_correcte :
                
                personnage = random.choice(tab_personnages_rouges)
                self.jeu.changer_personnage(personnage)
                
                if self.attributs_jeu.acc_deplacements() != [] :
                    case = random.choice(self.attributs_jeu.acc_deplacements())
                else :
                    case = None
                    
                if case != None :
                    
                    if personnage.acc_y() <= 4 and case[1] - personnage.acc_y() > 0 :
                        case_correcte = True
                    elif personnage.acc_y() >= 16 and personnage.acc_y() - case[1] < 0 :
                        case_correcte = True
            
            tab_perso_case = [personnage, case]
        
        return tab_perso_case
    
    def deplacer_personnage(self, tab_personnages_rouges, terrain) :
        '''
        Le robot choisit le meilleur personnage à deplacer et le déplace
        : params
            tab_personnages_rouges (list)
            terrain (module_terrain.Terrain)
        : pas de return
        '''
        #Assertions
        assert isinstance(tab_personnages_rouges, list), "le tableau des personnages rouges doit être un tableau"
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        #Code
        tab_perso_case = self.choisir_personnage_deplacement(tab_personnages_rouges, terrain)
        
        if self.attributs_jeu.acc_selection().acc_personnage() == 'geant' :
            self.jeu.deplacer_geant(tab_perso_case[1][0], tab_perso_case[1][1])  
        else :
            self.jeu.deplacer(tab_perso_case[1][0], tab_perso_case[1][1])
        
        print(tab_perso_case[0].personnage, tab_perso_case[1])
        self.jeu.deplacement_console(self.attributs_jeu.acc_selection(), tab_perso_case[1]) #Ajoute une phrase de déplacement dans la console du jeu
        self.jeu.effacer_actions()
        self.attributs_jeu.mut_nombre_action(self.attributs_jeu.acc_nombre_action() + 1) #Augmente le nombre d'action de 1
        
    ######################################################
    ### Méthodes Attaquer Personnages :
    ######################################################
        
    def attaquer_ennemi_proche(self, allie, terrain, une_case_proche = False) :
        '''
        Le robot regarde s'il y a un ennemi proche de son personnage allie (dans les cases d'attaques possibles)
        : params
            allie (module_personnage.Personnage)
            terrain (module_terrain.Terrain)
            une_case_proche (bool), par défaut vaut False
        : return (module_personnage.Personnage)
        '''
        #Assertions
        assert isinstance(allie, module_personnage.Personnage), "l'allié doit être de la classe Personnage"
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        assert isinstance(une_case_proche, bool), "la case proche doit être soit True soit False"
        #Code
        #tableau cases
        if not une_case_proche :
            if allie.acc_personnage() == 'geant' :
                tab = [(0, -1), (-1, 0), (-1, 1), (1, -1), (0, 2), (2, 0), (2, 1), (1, 2), (-1, -1), (-1, 2), (2, -1), (2, 2)]
                tab = module_terrain.tuples_en_coordonnees((allie.acc_x(), allie.acc_y()), tab, allie.acc_numero_geant())
            else :
                tab = allie.cases_valides_attaques(terrain)
        else :
            tab = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            tab = module_terrain.tuples_en_coordonnees((allie.acc_x(), allie.acc_y()), tab)
        
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
        Le robot choisit le personnage allie avec lequel il va attaquer
        : params
            tab_personnages_rouges (list)
            terrain (module_terrain.Terrain)
        : return (list)
        '''
        #Assertions
        assert isinstance(tab_personnages_rouges, list), "le tableau des personnages rouges doit être un tableau"
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        #Code
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
        Le robot attaque un ennemi proche d'un de ses personnages
        : params
            tab_personnages_rouges (list)
            terrain (module_terrain.Terrain)
        : return (bool)
        '''
        #Assertions
        assert isinstance(tab_personnages_rouges, list), "le tableau des personnages rouges doit être un tableau"
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        #Code
        tab_allie_ennemi = self.choisir_personnage_attaquer(tab_personnages_rouges, terrain)
        
        if tab_allie_ennemi != [] :
            allie = tab_allie_ennemi[0]
            ennemi = tab_allie_ennemi[1]
            
            if allie.acc_personnage() == 'geant' :
                for case in self.attributs_jeu.acc_attaques():
                        perso = terrain.acc_terrain(case[0], case[1])
                        perso.est_attaque('geant')
                        perso.mut_endommage()
                
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
            self.attributs_jeu.mut_personnage_qui_attaque(True)
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
        : param terrain (module_terrain.Terrain)
        : pas de return
        '''
        #Assertions
        assert isinstance(terrain, module_terrain.Terrain), "le terrain doit être de la classe Terrain"
        #Code :
        if self.attributs_jeu.acc_equipe_en_cours() == 'rouge' :
           
            if self.temps_attente == None and not self.attributs_jeu.acc_deplacement_en_cours() and not self.attributs_jeu.acc_attaque_en_cours() :
                self.temps_attente = time.time()
            
            elif self.temps_attente != None and time.time() - self.temps_attente > 1 :
                tab_personnages_rouges = self.acc_tab_personnages_rouges()
                
                if not self.attaquer_ennemi(tab_personnages_rouges, terrain) :
                    self.deplacer_personnage(tab_personnages_rouges, terrain)
                
                self.temps_attente = None