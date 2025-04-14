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
    def __init__(self, jeu, attributs_jeu, terrain):
        '''
        Initialise le robot
        : params
            jeu (module_jeu.Jeu)
            attributs_jeu (module_attributs_jeu.Attributs_Jeu)
        '''
        #assertions :
        assert isinstance(jeu, module_jeu.Jeu), "jeu doit venir de la classe Jeu (module_jeu) !"
        assert isinstance(attributs_jeu, module_attributs_jeu.Attributs_Jeu), "attributs_jeu doit venir de la classe Attributs_Jeu (module_attributs_jeu) !"
        assert isinstance(terrain, module_terrain.Terrain), 'terrain doit être de la classe Terrain (module_terrain) !'
        
        #Attributs Paramètres:
        self.jeu = jeu
        self.attributs_jeu = attributs_jeu
        self.terrain = terrain
        
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
            if perso.acc_equipe() == 'rouge' and perso.acc_pv() > 0 :
                if perso.acc_personnage() != 'geant' or (perso.acc_personnage() == 'geant' and perso.acc_numero_geant() == 0) :
                    tab_personnages_rouges.append(perso)
        random.shuffle(tab_personnages_rouges)
        return tab_personnages_rouges
    
    ######################################################
    ### Méthode d'Attaque d'un Ennemie Proche :
    ######################################################
                
    def attaquer_ennemi_proche(self, allie, une_case_proche = False) :
        '''
        Le robot regarde s'il y a un ennemi proche de son personnage allie (dans les cases d'attaques possibles)
        : params
            allie (module_personnage.Personnage)
            une_case_proche (bool), par défaut vaut False
        : return (module_personnage.Personnage)
        '''
        #Assertions
        assert isinstance(allie, module_personnage.Personnage), "l'allié doit être de la classe Personnage"
        assert isinstance(une_case_proche, bool), "la case proche doit être soit True soit False"
        #Code
        
        #tableau cases
        if not une_case_proche :
            if allie.acc_personnage() == 'geant' :
                tab = [(0, -1), (-1, 0), (-1, 1), (1, -1), (0, 2), (2, 0), (2, 1), (1, 2), (-1, -1), (-1, 2), (2, -1), (2, 2)]
                tab = module_terrain.tuples_en_coordonnees((allie.acc_x(), allie.acc_y()), tab, allie.acc_numero_geant())
            else :
                tab = allie.cases_valides_attaques(self.terrain)
        else :
            tab = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            tab = module_terrain.tuples_en_coordonnees((allie.acc_x(), allie.acc_y()), tab)
        
        ennemi = None
        i = 0
        
        ### Regarde autour du personnage sélectionné (allie) :
        while i < len(tab) and ennemi == None : 
            perso = self.terrain.acc_terrain(tab[i][0], tab[i][1])
            
            if allie.acc_personnage() == 'sorciere' and isinstance(perso, module_personnage.Personnage) and perso.acc_equipe() == 'rouge' and 0 < perso.acc_pv() <= 4 :
                ennemi = perso #Pour le soigner (même équipe)
            
            elif isinstance(perso, module_personnage.Personnage) and perso.acc_equipe() != 'rouge' :
                if isinstance(perso, module_personnage.Monstre) and perso.acc_etat() != 1 :
                    ennemi = perso
                else :
                    ennemi = perso
            
            i += 1
        return ennemi
    
    ######################################################
    ### Méthodes Déplacer Personnages :
    ######################################################
    
    def choisir_personnage_deplacement(self, tab_personnages_rouges) :
        '''
        Regarde pour chacun de ses personnages s'il y un ennemi pas loin ou un coffre.
        Sinon, déplace un personnage aléatoirement
        : param tab_personnages_rouges (list)
        : return (list)
        '''
        #Assertions
        assert isinstance(tab_personnages_rouges, list), "le tableau des personnages rouges doit être un tableau"
        #Code
        tab_perso_case = []
        
        ### MONSTRE PROCHE :
        i_personnage = 0
        while i_personnage < len(tab_personnages_rouges) and tab_perso_case == [] :
            personnage = tab_personnages_rouges[i_personnage]
            self.jeu.changer_personnage(personnage)
            ennemi_proche = self.attaquer_ennemi_proche(personnage, True) #on regarde si il y a un ennemi à proximité
            
            if ennemi_proche != None : #si il y a un ennemi à attaquer
                case = random.choice(self.attributs_jeu.acc_deplacements()) #on se déplace au hasard
                tab_perso_case = [personnage, case]
                
            i_personnage += 1
           
        ### ATTAQUER ENNEMI :         
        if tab_perso_case == [] : #si aucun ennemi proche
            
            i_personnage = 0
            while i_personnage < len(tab_personnages_rouges) and tab_perso_case == [] :
                personnage = tab_personnages_rouges[i_personnage]
                self.jeu.changer_personnage(personnage)
                
                i_case = 0
                while i_case < len(self.attributs_jeu.acc_deplacements()) and tab_perso_case == [] :
                    
                    if personnage.acc_personnage() == 'geant':
                        perso_annexe = module_personnage.Geant(personnage.acc_equipe(), self.attributs_jeu.acc_deplacements()[i_case][0], self.attributs_jeu.acc_deplacements()[i_case][1], personnage.acc_numero_geant())
                    else:
                        perso_annexe = module_personnage.Personnage(personnage.acc_personnage(), personnage.acc_equipe(), self.attributs_jeu.acc_deplacements()[i_case][0], self.attributs_jeu.acc_deplacements()[i_case][1])
                    
                    
                    ennemi_a_attaquer = self.attaquer_ennemi_proche(perso_annexe)
            
                    if ennemi_a_attaquer != None :
                        tab_perso_case = [personnage, self.attributs_jeu.acc_deplacements()[i_case]]

                    i_case += 1
                i_personnage += 1
                
        ### CHERCHER COFFRE :        
        if tab_perso_case == [] : #si aucun ennemi à attaquer
            
            i_personnage = 0
            while i_personnage < len(tab_personnages_rouges) and tab_perso_case == [] :
                personnage = tab_personnages_rouges[i_personnage]
                self.jeu.changer_personnage(personnage)
                i_coffre = 0
                while i_coffre < len(self.attributs_jeu.acc_tab_coffres()) and tab_perso_case == [] :
                    coffre = self.attributs_jeu.acc_tab_coffres()[i_coffre]
                    if not coffre.acc_est_ouvert() :
                        alentour_coffre = module_terrain.cases_autour((coffre.acc_x(), coffre.acc_y()))
                        i_case = 0
                        while i_case < len(self.attributs_jeu.acc_deplacements()) and tab_perso_case == [] :
                            if self.attributs_jeu.acc_deplacements()[i_case] in alentour_coffre :
                                tab_perso_case = [personnage, self.attributs_jeu.acc_deplacements()[i_case]]
                            i_case += 1
                    i_coffre += 1
                i_personnage += 1
          
        ### DEPLACEMENT ALÉATOIRE AVEC PERSO ALÉATOIRE :  
        if tab_perso_case == [] :
            
            case_correcte = False
            case = None
            while not case_correcte :
                
                personnage = random.choice(tab_personnages_rouges)
                self.jeu.changer_personnage(personnage)
                ##le personnage doit pouvoir se déplacer
                while self.attributs_jeu.acc_deplacements() == [] :
                    personnage = random.choice(tab_personnages_rouges)
                    self.jeu.changer_personnage(personnage)
                
                #Choisit une case aléatoire :
                case = random.choice(self.attributs_jeu.acc_deplacements())
                    
                if personnage.acc_y() <= 4 and case[1] - personnage.acc_y() > 0 : #En haut du terrain
                    case_correcte = True
                elif personnage.acc_y() >= 16 and personnage.acc_y() - case[1] < 0 : #En bas du terrain
                    case_correcte = True
                elif 4 < personnage.acc_y() < 16 : #Au milieu du terrain
                    case_correcte = True
                        
            tab_perso_case = [personnage, case]
        
        return tab_perso_case
    
    def deplacer_personnage(self, tab_personnages_rouges) :
        '''
        Le robot choisit le meilleur personnage à deplacer et le déplace
        : param tab_personnages_rouges (list)
        : pas de return
        '''
        #Assertions
        assert isinstance(tab_personnages_rouges, list), "le tableau des personnages rouges doit être un tableau"
        #Code
        tab_perso_case = self.choisir_personnage_deplacement(tab_personnages_rouges)
        
        try :
            
            if self.attributs_jeu.acc_selection().acc_personnage() == 'geant' :
                self.jeu.deplacer_geant(tab_perso_case[1][0], tab_perso_case[1][1])
            
            else :
                self.jeu.deplacer(tab_perso_case[1][0], tab_perso_case[1][1])
            
            self.jeu.effacer_actions()
            self.jeu.deplacement_console(tab_perso_case[0], tab_perso_case[1]) #Ajoute une phrase de déplacement dans la console du jeu
        
        except :
            self.deplacer_personnage(tab_personnages_rouges)
        
    ######################################################
    ### Méthodes Attaquer Personnages :
    ######################################################
    
    def choisir_personnage_attaquer(self, tab_personnages_rouges) :
        '''
        Le robot choisit le personnage allie avec lequel il va attaquer
        : param tab_personnages_rouges (list)
        : return (list)
        '''
        #Assertions
        assert isinstance(tab_personnages_rouges, list), "le tableau des personnages rouges doit être un tableau"
        #Code
        tab_allie_ennemi = []
        
        i_personnage = 0
        
        ### Pour chaque personnage de son équipe tant qu'il n'a pas de personnage avec lequel attaquer/soigner/changer d'équipe :
        while i_personnage < len(tab_personnages_rouges) and tab_allie_ennemi == [] :
            personnage = tab_personnages_rouges[i_personnage]
            self.jeu.changer_personnage(personnage)
            
            ennemi = self.attaquer_ennemi_proche(personnage)
            
            ### Pour une sorcière (différente potion) :
            if ennemi != None and personnage.acc_personnage() == 'sorciere' :
                ### Joue intelligemment :
                if ennemi.acc_equipe() == 'rouge' and not self.attributs_jeu.acc_potions_rouges()[2].est_vide():
                    self.attributs_jeu.mut_potion_rouge_selectionnee(2)
                elif ennemi.acc_personnage() == 'sorciere' and not self.attributs_jeu.acc_potions_rouges()[4].est_vide() :
                    self.attributs_jeu.mut_potion_rouge_selectionnee(4)
                elif ennemi.acc_personnage() == 'monstre' :
                    self.attributs_jeu.mut_potion_rouge_selectionnee(1)
                
                ### Sinon, utilise un potion aléatoire (sauf guérison) :
                else :
                    tab = [1, 3, 4]
                    numero_potion = random.choice(tab)
                    while self.attributs_jeu.acc_potions_rouges()[numero_potion].est_vide() :   
                        tab.remove[numero_potion]
                        numero_potion = random.choice(tab)
                    self.jeu.attaque_sorciere_console(personnage.acc_equipe())
                    self.attributs_jeu.mut_potion_rouge_selectionnee(numero_potion)
                    
                self.jeu.ouverture_potion(ennemi.acc_x(), ennemi.acc_y()) #Jette sa potion
                tab_allie_ennemi = [personnage, None]
            
            elif ennemi != None :
                tab_allie_ennemi = [personnage, ennemi]
            
            i_personnage += 1
        
        return tab_allie_ennemi
    
    def attaquer_ennemi(self, tab_personnages_rouges) :
        '''
        Le robot attaque un ennemi proche d'un de ses personnages
        : param tab_personnages_rouges (list)
        : return (bool)
        '''
        #Assertions
        assert isinstance(tab_personnages_rouges, list), "le tableau des personnages rouges doit être un tableau"
        #Code
        tab_allie_ennemi = self.choisir_personnage_attaquer(tab_personnages_rouges)
        
        if tab_allie_ennemi != [] :
            allie = tab_allie_ennemi[0]
            ennemi = tab_allie_ennemi[1]
            
            if allie.acc_personnage() == 'geant' :
                for case in self.attributs_jeu.acc_attaques():
                    perso = self.terrain.acc_terrain(case[0], case[1])
                    perso.est_attaque('geant')
                    perso.mut_endommage()
                
            if ennemi != None and ennemi.acc_personnage() == 'geant':
                famille = self.jeu.famille_geant(ennemi)
                for geant in famille :
                    geant.est_attaque(allie.acc_personnage())
                    geant.mut_endommage()
            
            elif allie.acc_personnage() != 'sorciere' :
                ennemi.est_attaque(allie.acc_personnage()) 
                ennemi.mut_endommage()
                
            self.attributs_jeu.mut_attaque_en_cours(True)
            self.attributs_jeu.mut_attaque_temps(0)
            #Si ce n'est pas une sorcière, affiche dans la console que le personnage (allie) a attaqué son ennemi :
            if allie.acc_personnage() != "sorciere" :
                self.jeu.attaque_console(allie, ennemi)
            self.attributs_jeu.mut_personnage_qui_attaque(True)
            return True
        
        return False
                
    ######################################################
    ### Méthodes Ouvrir Coffres :
    ######################################################
    
    def chercher_coffre_proche(self) :
        '''
        Cherche un coffre proche d'un de ses personnages
        : return (None or module_objets.Coffre)
        '''
        tab_perso_coffre = []
        i_coffre = 0
        while i_coffre < len(self.attributs_jeu.acc_tab_coffres()) and tab_perso_coffre == [] : #Tant qu'on à pas trouvé de coffre avec un personnage rouge à côté :
            coffre_possible = self.attributs_jeu.acc_tab_coffres()[i_coffre]
            if not coffre_possible.acc_est_ouvert() :
                alentour = module_terrain.cases_autour((coffre_possible.acc_x(), coffre_possible.acc_y()))
            
                i_case = 0
                while tab_perso_coffre == [] and i_case < len(alentour) : #tant qu'on n'a pas tout regardé
                    perso = self.terrain.acc_terrain(alentour[i_case][0], alentour[i_case][1])
                    if isinstance(perso, module_personnage.Personnage) and perso.acc_equipe() == 'rouge' :
                        tab_perso_coffre = [perso, coffre_possible]
                    i_case += 1
                
            i_coffre += 1
        return tab_perso_coffre
    
    def ouvrir_coffre(self) :
        '''
        Le robot ouvre un coffre s'il y en a un à côté d'un de ses personnages
        : return (bool)
        '''
        tab_perso_coffre = self.chercher_coffre_proche()
        
        if tab_perso_coffre != [] :
            perso = tab_perso_coffre[0]
            coffre = tab_perso_coffre[1]
            
            coffre.ouverture()
            self.jeu.ouverture_coffre(coffre, (perso.acc_x(), perso.acc_y()))
            self.jeu.coffre_console(coffre.acc_contenu())
                
            if not self.attributs_jeu.acc_annonce_coffre() :
                self.attributs_jeu.mut_annonce_coffre(True)
            return True
        return False
    
    ######################################################
    ### Méthode Jouer :
    ######################################################
    
    def jouer_robot(self) :
        '''
        Fait jouer le robot quand c'est à son tour avec de pause de 5 secondes entres les actions        
        : pas de return
        '''
        #Si c'est à son tour :
        if self.attributs_jeu.acc_equipe_en_cours() == 'rouge' :
            #S'il n'y a pas eu une pause et qu'il n'y a pas de déplacement, d'attaque ou d'ouverture de coffre en cours :
            if self.temps_attente == None and not self.attributs_jeu.acc_deplacement_en_cours() and not self.attributs_jeu.acc_attaque_en_cours() and not self.attributs_jeu.acc_annonce_coffre():
                self.temps_attente = time.time()
            #Dés qu'une pause de plus de 3 secondes a été faite :
            elif self.temps_attente != None and time.time() - self.temps_attente > 1 :
                tab_personnages_rouges = self.acc_tab_personnages_rouges()
                #Si le robot n'a pas attaqué ou ouvert un coffre, il déplace un personnage de son équipe :
                if not (self.attaquer_ennemi(tab_personnages_rouges) or self.ouvrir_coffre()) :
                    self.deplacer_personnage(tab_personnages_rouges)
                
                self.attributs_jeu.mut_nombre_action(self.attributs_jeu.acc_nombre_action() + 1)
                self.jeu.effacer_actions()
                
                self.temps_attente = None