# -*- coding: utf-8 -*-

'''
-> Medieval Heroes : Module pour la classe Jeu

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################

import pygame, module_attributs_jeu, module_terrain, module_afficher, module_souris, module_objets, module_personnage, random, module_sauvegarde, module_robot, module_musique_et_sons 
from graphe import parcourir_graphe

######################################################
### Classe Jeu :
######################################################

class Jeu() :
    '''
    Une classe Jeu qui gère le calcule et l'affichage pour un bon déroulement du jeu grâce aux modules importés.
    '''
    def __init__(self) :
        '''
        Initialise le jeu
        '''
        #Attributs Fenêtre :
        self.ecran = pygame.display.set_mode((1300, 800)) #Affiche l'écran du jeu de dimension 1300 x 800
        self.horloge = pygame.time.Clock() #Permet de fixer les fps du de la fenêtre (rafraîchissement et calculs par seconde)
        
        #Attributs des Importations :
        self.attributs_jeu = module_attributs_jeu.Attributs_Jeu()
        self.sauvegarde = module_sauvegarde.Sauvegarde(self, self.attributs_jeu)
        self.gestionnaire_son = module_musique_et_sons.Gestionnaire_Son()
        self.terrain = module_terrain.Terrain(self.attributs_jeu)
        self.souris = module_souris.Souris(self, self.attributs_jeu, self.sauvegarde, self.terrain, self.gestionnaire_son)
        self.affichage = module_afficher.Affichage(self, self.attributs_jeu, self.terrain, self.ecran, self.souris)
        self.robot = module_robot.Robot(self, self.attributs_jeu, self.terrain)
        
        #Options :
        self.sols_de_couleur = True
        self.deplacements_attaques = True
        self.option_console = True
        self.x_pointeur = 550 #Volume
                                           
    ######################################################
    ### Accesseurs :
    ######################################################
    
    def acc_horloge(self):
        '''
        Renvoie l'attribut horloge
        '''
        return self.horloge
    
    def acc_sols_de_couleur(self):
        '''
        Renvoie l'attribut sols_de_couleur
        : return (bool)
        '''
        return self.sols_de_couleur
    
    def acc_deplacements_attaques(self):
        '''
        Renvoie l'attribut deplacements_attaques
        : return (bool)
        '''
        return self.deplacements_attaques
    
    def acc_option_console(self):
        '''
        Renvoie l'attribut option_console
        : return (bool)
        '''
        return self.option_console
    
    def acc_x_pointeur(self):
        '''
        renvoie l'attribut x_pointeur
        : return (int)
        '''
        return self.x_pointeur
    
    ######################################################
    ### Mutateurs :
    ######################################################   
    
    def mut_sols_de_couleur(self, valeur) :
        '''
        Modifie l'attribut sols_de_couleur
        : param valeur (boolean)
        : pas de return, modifie l'attribut sols_de_couleur
        '''
        #Assertion :
        assert isinstance(valeur, bool), 'Le paramètre doit être soit True, soit False !'
        #Code :
        self.sols_de_couleur = valeur
        
    def mut_deplacements_attaques(self, valeur) :
        '''
        Modifie l'attribut deplacements_attaques
        : param valeur (boolean)
        : pas de return, modifie l'attribut deplacements_attaques
        '''
        #Assertion :
        assert isinstance(valeur, bool), 'Le paramètre doit être soit True, soit False !'
        #Code :
        self.deplacements_attaques = valeur
        
    def mut_option_console(self, valeur) :
        '''
        Modifie l'attribut option_console
        : param valeur (boolean)
        : pas de return, modifie l'attribut option_console
        '''
        #Assertion :
        assert isinstance(valeur, bool), 'Le paramètre doit être soit True, soit False !'
        #Code :
        self.option_console = valeur
    
    def mut_x_pointeur(self, x):
        '''
        modifie le x de l'attribut x_pointeur
        : param x (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(x, int), "x doit être un entier"
        #Code
        self.x_pointeur = x
    
    ######################################################
    ### Placement de personnages :
    ######################################################
    
    def placer(self) :
        '''
        Place les personnages, monstres et coffres sur le terrain
        : pas de return
        '''
        for elt in self.attributs_jeu.acc_tab_personnages() + self.attributs_jeu.acc_tab_monstres() + self.attributs_jeu.acc_tab_coffres() :
            self.terrain.mut_terrain(elt.acc_x(), elt.acc_y(), elt)
    
    def placer_par_defaut(self) :
        '''
        Place les personnages, monstres et coffres sur le terrain (modèle par défaut)
        : pas de return
        '''
        ###Pose des personnages (par défaut)
        
        #Géant rouge:
        ##n°1
        geant1r = module_personnage.Geant('rouge', 8, 0, 0)
        geant2r = module_personnage.Geant('rouge', 9, 0, 1)
        geant3r = module_personnage.Geant('rouge', 8, 1, 2)
        geant4r = module_personnage.Geant('rouge', 9, 1, 3)
        ##n°2
        geant5r = module_personnage.Geant('rouge', 11, 0, 0)
        geant6r = module_personnage.Geant('rouge', 12, 0, 1)
        geant7r = module_personnage.Geant('rouge', 11, 1, 2)
        geant8r = module_personnage.Geant('rouge', 12, 1, 3)
        self.attributs_jeu.mut_famille_geant_rouge([[geant1r, geant2r, geant3r, geant4r], [geant5r, geant6r, geant7r, geant8r]]) ##La famille des géants
        
        #Geant bleu:
        ##n°1
        geant1b = module_personnage.Geant('bleu', 8, 19, 0)
        geant2b = module_personnage.Geant('bleu', 9, 19, 1)
        geant3b = module_personnage.Geant('bleu', 8, 20, 2)
        geant4b = module_personnage.Geant('bleu', 9, 20, 3)
        ##n°2
        geant5b = module_personnage.Geant('bleu', 11, 19, 0) 
        geant6b = module_personnage.Geant('bleu', 12, 19, 1) 
        geant7b = module_personnage.Geant('bleu', 11, 20, 2) 
        geant8b = module_personnage.Geant('bleu', 12, 20, 3) 
        self.attributs_jeu.mut_famille_geant_bleu([[geant1b, geant2b, geant3b, geant4b], [geant5b, geant6b, geant7b, geant8b]]) ##La famille des géants    
        
        self.attributs_jeu.mut_tab_personnages([
    
        #rouge :
        
        module_personnage.Personnage('paladin', 'rouge', 6, 2),#personnage, equipe, x, y
        module_personnage.Personnage('cavalier', 'rouge', 8, 2),
        module_personnage.Personnage('ivrogne', 'rouge', 7, 2),
        module_personnage.Personnage('poulet', 'rouge', 8, 3),
        module_personnage.Personnage('poulet', 'rouge', 12, 3),
        module_personnage.Personnage('valkyrie', 'rouge', 9, 2),
        module_personnage.Personnage('sorciere', 'rouge', 10, 2),
        module_personnage.Personnage('archere', 'rouge', 11, 2),
        module_personnage.Personnage('barbare', 'rouge', 12, 2),
        module_personnage.Personnage('mage', 'rouge', 13, 2),
        module_personnage.Personnage('cracheur de feu', 'rouge', 14, 2),
        geant1r, geant2r, geant3r, geant4r,
        geant5r, geant6r, geant7r, geant8r,
        
        #bleu :
        module_personnage.Personnage('paladin', 'bleu', 6, 18),#personnage, equipe, x, y
        module_personnage.Personnage('cavalier', 'bleu', 8, 18),
        module_personnage.Personnage('ivrogne', 'bleu', 7, 18),
        module_personnage.Personnage('poulet', 'bleu', 8, 17),
        module_personnage.Personnage('poulet', 'bleu', 12, 17),
        module_personnage.Personnage('valkyrie', 'bleu', 9, 18),
        module_personnage.Personnage('sorciere', 'bleu', 10, 18),
        module_personnage.Personnage('archere', 'bleu', 11, 18),
        module_personnage.Personnage('barbare', 'bleu', 12, 18),
        module_personnage.Personnage('mage', 'bleu', 13, 18),
        module_personnage.Personnage('cracheur de feu', 'bleu', 14, 18),
        geant1b, geant2b, geant3b, geant4b,
        geant5b, geant6b, geant7b, geant8b,
        ])
        
        ###Pose des coffres (par défaut)
        self.attributs_jeu.mut_tab_coffres([
        module_objets.Coffre(1, 6),
        module_objets.Coffre(19, 14),
        module_objets.Coffre(1, 14),
        module_objets.Coffre(19, 6)
        ])
        
        self.placer()
            
    ######################################################
    ### Méthodes Console :
    ######################################################
    
    def partie_commence_console(self) :
        '''
        Ajoute dans la console que l'équipe a changé
        : pas de return
        '''
        self.attributs_jeu.ajouter_console(['·La partie commence !', 'noir'])
    
    def equipe_console(self, equipe) :
        '''
        Ajoute dans la console que l'équipe a changé
        : param equipe (str)
        : pas de return
        '''
        #Assertion :
        assert equipe in ['bleu', 'rouge'], "le paramètre doit être soit 'rouge' soit 'bleu'"
        #Code :
        self.attributs_jeu.ajouter_console(['·À l\'équipe ' + equipe + ' de jouer !', 'noir'])
    
    def deplacement_console(self, personnage, position_deplacement) :
        '''
        Ajoute dans la console que le personnage (passé en paramètre) s'est déplacé
        : params 
            personnage (module_personnage.Personnage)
            position_deplacement (tuple)
        : pas de return
        '''
        #Assertions :
        assert isinstance(personnage, module_personnage.Personnage), 'personnage_qui_attaque doit être un personnage de la classe Personnage (module_personnage) !'
        assert isinstance(position_deplacement, tuple) and 0 <= position_deplacement[0] <= 20 and 0 <= position_deplacement[1] <= 20, 'position_deplacement doit être un tuple de coordonnées (x, y) du terrain (compris entre 0 et 20) !'
        #Code :
        self.attributs_jeu.ajouter_console(['·' + personnage.acc_personnage() + ' s\'est déplacé (' + self.attributs_jeu.acc_dic_alphabet()[position_deplacement[0]] + "," + str(position_deplacement[1]) + ")" , personnage.acc_equipe()])
        
    def attaque_console(self, personnage_qui_attaque, personnage_qui_subit) :
        '''
        Ajoute dans la console que le personnage attaque un personnage de l'équipe adverse
        : params
            personnage_qui_attaque (module_personnage.Personnage)
            personnage_qui_subit (module_personnage.Personnage)
        : pas de return
        '''
        #Assertions :
        assert isinstance(personnage_qui_attaque, module_personnage.Personnage), 'personnage_qui_attaque doit être un personnage de la classe Personnage (module_personnage) !'
        assert isinstance(personnage_qui_subit, module_personnage.Personnage), 'personnage_qui_subit doit être un personnage de la classe Personnage (module_personnage) !'
        #Code :
        self.attributs_jeu.ajouter_console(['·' + personnage_qui_attaque.acc_personnage() + ' a attaqué ' + personnage_qui_subit.acc_personnage() + '.', personnage_qui_attaque.acc_equipe()])
    
    def attaque_sorciere_console(self, equipe) :
        '''
        Ajoute dans la console qu'une sorciere a lancé une potion d'attaque.
        : param equipe (str), 'bleu' or 'rouge'
        : pas de return
        '''
        #Assertions :
        assert equipe in ['bleu', 'rouge'], "Le paramètre doit être soit 'bleu' soit 'rouge' !"
        #Code :
        self.attributs_jeu.ajouter_console(["·sorciere a lancé une potion d'attaque", equipe])

    def coffre_console(self, numero_contenu) :
        '''
        Ajoute dans la console le contenu du coffre ouvert.
        : param numero_contenu (int)
        : pas de return
        '''
        #Assertion :
        assert isinstance(numero_contenu, int), 'Le paramètre doit être un entier (int) !'
        #Code :
        dictionnaire_contenu = {1 : 'Bonus de vie',
                                2 : 'Changement de personnage',
                                3 : 'Bonus de dégâts',
                                4 : 'Nécromancie claire',
                                5 : 'Nécromancie obscure',
                                6 : "Potions de soin",
                                7 : "Potion de mort",
                                8 : "Potions changement d'équipe",
                                9 : "Potions de mort adverse",
                                10 : "Bonus de dégâts adverse"
                                    }
        
        self.attributs_jeu.ajouter_console(['·Coffre : ' + dictionnaire_contenu[numero_contenu], 'noir'])
        
    def guerison_console(self, personnage) :
        '''
        Ajoute dans la console que le personnage a été soigné
        : params
            personnage (module_personnage.Personnage)
        : pas de return
        '''
        #Assertions :
        assert isinstance(personnage, module_personnage.Personnage), 'Le paramètre doit être un personnage de la classe Personnage (module_personnage) !'
        #Code :
        if personnage.acc_personnage() != 'geant' or (personnage.acc_personnage() == 'geant' and personnage.acc_numero_geant() == 0) :
            self.attributs_jeu.ajouter_console(["·" + personnage.acc_personnage() + ' a été soigné', personnage.acc_equipe()])
        
    def changement_equipe_personnage_console(self, personnage) :
        '''
        Ajoute dans la console que le personnage a changé d'équipe.
        : params
            personnage (module_personnage.Personnage)
        : pas de return
        '''
        #Assertions :
        assert isinstance(personnage, module_personnage.Personnage), 'Le paramètre doit être un personnage de la classe Personnage (module_personnage) !'
        #Code :
        if personnage.acc_personnage() != 'geant' or (personnage.acc_personnage() == 'geant' and personnage.acc_numero_geant() == 0) :
            self.attributs_jeu.ajouter_console(["·" + personnage.acc_personnage() + " a changé d'équipe", personnage.acc_equipe()])
        
    def mort_personnage_console(self, personnage) :
        '''
        Ajoute dans la console qu'un personnage est mort.
        : param personnage (module_personnage.Personnage)
        : pas de return
        '''
        #Assertions :
        assert isinstance(personnage, module_personnage.Personnage), 'Le paramètre doit être un personnage de la classe Personnage (module_personnage) !'
        #Code :
        if personnage.acc_personnage() == 'monstre' :
            self.attributs_jeu.ajouter_console(["·" + personnage.acc_personnage() + " est mort", 'noir'])
        
        elif personnage.acc_personnage() != 'geant' or (personnage.acc_personnage() == 'geant' and personnage.acc_numero_geant() == 0) :
            self.attributs_jeu.ajouter_console(["·" + personnage.acc_personnage() + " (" + personnage.acc_equipe() + ") est mort", 'noir'])
            
    def equipe_gagnante_console(self):
        '''
        Ajoute dans la console l'équipe qui a gagné.
        : pas de return
        '''
        self.attributs_jeu.ajouter_console(["· L'équipe " + self.attributs_jeu.acc_equipe_gagnante() + " a gagné !", 'noir'])
            
    ######################################################
    ### Déplacements :
    ######################################################
    
    def deplacer(self, x, y):
        '''
        déplace un personnage sur la grille
        : params
            x, y (int), les nouvelles coordonnées
        : pas de return
        '''
        self.terrain.mut_terrain(self.attributs_jeu.acc_selection().acc_x(), self.attributs_jeu.acc_selection().acc_y(), ' ')# remplace l'ancienne place du personnage par une case vide
        self.attributs_jeu.mut_nouvelles_coord((x, y))
        ######PARTIE AFFICHAGE DU DEPLACEMENT
        
        #Récupération du bon chemin : 
        perso = self.attributs_jeu.acc_selection()
        coordonnees = (perso.acc_x(), perso.acc_y())
        if perso.acc_personnage() == 'cavalier' : #si c'est un cavalier
            dep = self.attributs_jeu.acc_deplacements_cavalier()
        else:
            dep = self.attributs_jeu.acc_deplacements()
        ##Graphe et chemin
        graphe = perso.construire_graphe(coordonnees, dep)
        chemin = parcourir_graphe.depiler_chemin(graphe, coordonnees, (x, y))
        chemin2 = []
        for elt in chemin:
            chemin2.append((elt[0] * 38 + 250, elt[1] * 38))
        self.attributs_jeu.mut_chemin(chemin2) # on obtient un chemin avec toutes les coordonnées dans lesquelles le personnage doit passer
        self.attributs_jeu.mut_coordonnees_personnage((chemin2[0])) # le personnage se situe au premier point du chemin
        self.attributs_jeu.mut_personnage_en_deplacement(perso) # on désigne le personnage qui se déplace
        self.attributs_jeu.mut_deplacement_en_cours(True) # on déclare qu'un déplacement est en cours
        self.attributs_jeu.mut_nb_actions(self.attributs_jeu.acc_nb_actions() + 1) # on augmente le nombre d'action effectuée du joueur de 1
    
    def arreter_animation_deplacement(self):
        '''
        Arrête l'animation une fois que l'image du personnage en déplacement est arrivée à destination
        : pas de return
        '''
        if self.attributs_jeu.acc_indice_courant() >= len(self.attributs_jeu.acc_chemin()) - 1 and self.attributs_jeu.acc_nb_actions() != 0:           
            self.attributs_jeu.mut_indice_courant(0)
            self.replacer()
          
    def replacer(self):
        '''
        replace le personnage après l'avoir déplacé
        : pas de return
        '''
        x, y = self.attributs_jeu.acc_nouvelles_coord()
        perso = self.attributs_jeu.acc_selection()
        
        if perso != None :
            perso.deplacer(x, y) # change les attributs des personnages dans la grille
            self.terrain.mut_terrain(x, y, perso) # déplace la selection aux nouvelles coordonnées
            self.attributs_jeu.mut_selection(None)
            self.attributs_jeu.mut_personnage_en_deplacement(None)
            self.attributs_jeu.mut_deplacement_en_cours(False)
        self.jouer_monstres()

    def deplacer_geant(self, x, y):
        '''
        Déplace les bouts du géant aux nouvelles coordonnées
        : params
            x, y (int)
        : pas de return
        '''
        position = (self.attributs_jeu.acc_selection().acc_x(), self.attributs_jeu.acc_selection().acc_y())
        perso = self.terrain.acc_terrain(position[0], position[1])
        famille = self.famille_geant(perso)
        deplacement = self.coordonnees_geant(famille[0].acc_x(), famille[0].acc_y(), x, y)
        ##vide l'ancien emplacement
        for geant in famille:
            self.terrain.mut_terrain(geant.acc_x(), geant.acc_y(), ' ') # vide à l'ancienne place

        for geant in famille:
            n_x = geant.acc_x() + deplacement[0]
            n_y = geant.acc_y() + deplacement[1]
            geant.deplacer(n_x, n_y) # pour le personnage
            self.terrain.mut_terrain(n_x, n_y, geant)
        self.jouer_monstres() #Fait jouer les monstres
  
    def coordonnees_geant(self, tete_x, tete_y, nouveau_x, nouveau_y):
        '''
        : params
            tete_x, tete_y (int)
            nouveau_x, nouveau_y (int)        
        : return (tuple)
        '''
        #Assertions
        assert isinstance(tete_x, int) and  isinstance(tete_y, int), "tete_x et tete_y doivent être des entiers"
        assert isinstance(nouveau_x, int) and  isinstance(nouveau_y, int), "nouveau_x et nouveau_y doivent être des entiers"
        #Code
        dic_directions = {'h' : (0, -1),
                          'b' : (0, 1),
                          'g' : (-1, 0),
                          'd' : (1, 0)}
        if tete_x - nouveau_x == 1:
            ou = 'g'
        elif tete_x - nouveau_x == -2:
            ou = 'd'
        elif tete_y - nouveau_y == 1:
            ou = 'h'
        else:
            ou = 'b'    
        return dic_directions[ou]
    
    def famille_geant(self, geant):
        '''
        renvoie la bonne famille de géant selon l'équipe et les coordonnées du géant voulu
        : param geant (Geant)
        : return (list), la famille géant
        '''
        #assertions
        assert isinstance(geant, module_personnage.Geant), "le personnage doit être de la classe Geant"
        #code
        coordo_geant = module_personnage.trouve_famille_geant(geant)
        trouve = False
        i = 0
        ####les familles des géants
        if geant.acc_equipe() == 'bleu':
            geants = self.attributs_jeu.acc_famille_geant_bleu()
        else :
            geants = self.attributs_jeu.acc_famille_geant_rouge()
        ##recherche de la famille
        while not trouve and i < len(geants):
            trouve = (geants[i][0].acc_x(), geants[i][0].acc_y()) in coordo_geant
            i += 1
        ##la famille du géant      
        fam = geants[i-1]
        return fam
    
    ######################################################
    ### Attaques :
    ######################################################
    
    def gerer_animations_attaques(self):
        '''
        Gère le fonctionnement de l'affichage des attaques dans le jeu
        : pas de return
        '''
        ##Temps de l'animation
        if self.attributs_jeu.acc_cases_potions() == []:
            nb = 20
        else :
            nb = 44 #animations plus longues quand il a des bulles
        #Si le temps de l'attaque est strictement inférieur, pas de return à 20 et qu'il y a une attaque en cours :
        if self.attributs_jeu.acc_attaque_temps() < nb and self.attributs_jeu.acc_attaque_en_cours() :
            self.attributs_jeu.mut_attaque_temps(self.attributs_jeu.acc_attaque_temps() + 1) #Ajoute 1 au temps de l'attaque
        
        #Sinon si le temps de l'attaque est à 20 :
        elif self.attributs_jeu.acc_attaque_temps() == nb :
            self.attributs_jeu.mut_attaque_en_cours(False) #Il n'y a plus d'attaque en cours
            self.attributs_jeu.mut_attaque_temps(0) #Le temps de l'attaque est mis à 0
            
            #Pour chaque personnage dans le tableau de personnages :
            for personnage in self.attributs_jeu.acc_tab_personnages() + self.attributs_jeu.acc_tab_monstres() :
                #Si le personnage est endommagé :
                if personnage.acc_endommage():
                    personnage.mut_endommage() #Change son attribut en son inverse (dans ce cas True devient False)
                #Si le personnage est soigné :
                elif personnage.acc_soigne():
                    personnage.mut_soigne()  #Change son attribut en son inverse (dans ce cas True devient False)
                #Si le personnage a attaqué :
                elif personnage.acc_attaque():
                    personnage.mut_attaque() #Change son attribut en son inverse (dans ce cas True devient False)
                    
            self.attributs_jeu.mut_cases_potions([]) #la potion n'agit plus
            
            if self.attributs_jeu.acc_personnage_qui_attaque() :
                self.personnages_sont_mort()
                self.attributs_jeu.mut_personnage_qui_attaque(False)
                self.jouer_monstres()
    
    ######################################################
    ### Monstres :
    ######################################################
    
    def changer_etat_monstres(self) :
        '''
        Change l'état des monstres qui sont dans la terre quand le soleil se couche.
        : pas de return
        '''
        #Si le nombre de tour est un multiple de 4 (hors 0), le monstre sort de terre :
        if self.attributs_jeu.acc_nombre_tour() % 4 == 0 and self.attributs_jeu.acc_nombre_tour() != 0 :
            for monstre in self.attributs_jeu.acc_tab_monstres() :
                #Si le monstre est dans la terre :
                if monstre.acc_etat() == 1 :
                    monstre.mut_etat(2)
    
    def ajouter_tab_monstres(self) :
        '''
        Ajoute des monstres avec des coordonnées aléatoires dans le tableau en fonction de combien de Nuit sont passées.
        : pas de return
        '''
        #Si l'ajout de monstres est "activé" et qu'ils n'ont pas encore été ajouté alors on ajoute des monstres
        if self.attributs_jeu.acc_nombre_tour() % 8 == 2 and self.attributs_jeu.acc_monstres_active() :
            for _ in range(self.attributs_jeu.acc_nombre_monstre_a_ajoute()) :
                #Coordonnées au hasard
                x, y = self.terrain.trouver_case_libre('monstre')
                self.attributs_jeu.ajouter_monstre(module_personnage.Monstre(x, y, self.attributs_jeu.acc_pv_monstre(), 1)) #Ajoute le monstre dans le tableau des monstres
            #Augmente le nombre de monstre de 1 pour la prochaine fois s'il ne dépasse pas le nombre de 4 monstres :
            if self.attributs_jeu.acc_nombre_monstre_a_ajoute() < 4 :
                self.attributs_jeu.mut_nombre_monstre_a_ajoute(1)
                
            #Augmente le nombre de pv des monstre de 1 pour la prochaine fois s'il ne dépasse pas le nombre de 10 pv (seulement pour les nouveaux monstres):
            if self.attributs_jeu.acc_pv_monstre() < 5 :
                self.attributs_jeu.mut_pv_monstre(1)
                
            #Ajout de chaque monstre du tableau des monstres sur le terrain :
            for monstre in self.attributs_jeu.acc_tab_monstres() :
                self.terrain.mut_terrain(monstre.acc_x(), monstre.acc_y(), monstre)
                
            #Monstres déjà déplacés
            self.attributs_jeu.mut_monstres_active(False) #Active la possibilité d’interactions
            
        elif self.attributs_jeu.acc_nombre_tour() % 8 != 2 and not self.attributs_jeu.acc_monstres_active() :
            self.attributs_jeu.mut_monstres_active(True)
        
    def attaquer_monstre(self, monstre) :
        '''
        Le monstre passé en paramètre attaque un personnage si c'est possible.
        : param monstre (module_personnage.Monstre)
        : return (bool), True si le monstre a attaqué, False sinon.
        '''
        #Assertion :
        assert isinstance(monstre, module_personnage.Monstre), 'Le paramètre doit être un monstre de la classe Monstre du module_personnage !'
        #Code :
        monstre.attaquer(self.terrain) #Le monstre cherche une victime à attaquer à proximité
        
        #Si le monstre a trouvé une victime :
        if monstre.attaquer_ennemi_proche(self.attributs_jeu.acc_equipe_en_cours()) != None:
            victime = monstre.attaquer_ennemi_proche(self.attributs_jeu.acc_equipe_en_cours()) #La victime qui est attaquée/sélectionné par le monstre
        #Si la victime est le Géant :
            if victime.acc_personnage() == 'geant':
                famille = self.famille_geant(victime) #détermine la famille du géant
                #Pour chaque partie du geant :
                for geant in famille :
                    geant.est_attaque('monstre')
                    if not geant.acc_endommage() : #si elle n'est pas déjà attaquée par un autre monstre/personnage
                        geant.mut_endommage()
            else: #autre personnage
                victime.est_attaque('monstre') #La victime perd des pv
                if not victime.acc_endommage() : #si elle n'est pas déjà attaquée par un autre monstre/personnage
                    victime.mut_endommage() #blesse la victime
                
            self.attributs_jeu.mut_attaque_en_cours(True)
            self.attributs_jeu.mut_attaque_temps(0)
            return True #Le monstre a attaqué
        
        return False #Le monstre n'a pas attaqué
    
    def jouer_monstres(self):
        '''
        Déplace chaque monstre sur le plateau et gère leurs attaques
        : pas de return
        '''
        #Pour chaque monstre dans le tableau des monstres :
        for monstre in self.attributs_jeu.acc_tab_monstres() :
            #Si le monstre était déjà sortis de terre
            if monstre.acc_etat() != 1 :
                if not self.attaquer_monstre(monstre) :
                    self.attributs_jeu.ajouter_monstres_a_deplacer(monstre)
                    self.attributs_jeu.mut_deplacement_en_cours(True)
                    
    ########################################################
    #### Méthodes Coffre :
    ########################################################
    
    def apparition_coffres(self):
        '''
        ajoute des coffres à tab_coffres en respectant cette condition :
            • respect la position : autant de coffres dans la partie haute que dans la partie basse du terrain
        : pas de return
        '''
        if self.attributs_jeu.acc_nombre_tour() % 8 == 0 and not self.attributs_jeu.acc_nombre_tour() == 0 and self.attributs_jeu.acc_coffres_apparition_active() : #tous les matins, les coffres apparaissent
            ##tab anciennes coordonnées des coffres
            tab = []
            for coffre in self.attributs_jeu.acc_tab_coffres() :
                x = coffre.acc_x()
                y = coffre.acc_y()
                tab.append((x, y))
                self.terrain.mut_terrain(x, y, ' ') #on enlève les anciens coffres du terrain
            #on supprime tous les coffres
            self.attributs_jeu.mut_tab_coffres([])
            #on ajoute deux coffres en 'bas' et deux coffres en 'haut'
            self.ajouter_coffre('haut', tab)
            self.ajouter_coffre('bas', tab)
            self.attributs_jeu.mut_coffres_apparition_active(False)
                
        elif self.attributs_jeu.acc_nombre_tour()% 8 != 0 and not self.attributs_jeu.acc_coffres_apparition_active() :
            self.attributs_jeu.mut_coffres_apparition_active(True)
        
    def ajouter_coffre(self, chaine, deja_present):
        '''
        ajoute au tab_coffres le nombre de coffre qu'il faut dans la bonne partie du terrain
        : params
            chaine (str) 'bas' ou 'haut'
            deja_present (list of tuples), les coordonnées des emplacements des anciens coffres
        : pas de return, modifie l'attribut tab_coffre
        '''
        #assertion
        assert isinstance(chaine, str) and chaine in ['haut', 'bas'], "la chaîne doit être de type str et doit être soit 'haut' soit 'bas'"
        #code
        ##dic des cases prédéfinies pour les coffres
        dic_coffre = {'haut' : [(1, 6), (19, 6), (0, 4), (20, 4), (4, 0), (16, 0), (0, 0), (20, 0), (10, 10), (2, 10)],
                      'bas' : [(1, 14), (19, 14), (20, 16), (0, 16), (4, 20), (16, 20), (0, 20), (20, 20), (10, 10), (18, 10)]
                      }
        ##coordonnées possibles pour les coffres
        tab_coordonnees = dic_coffre[chaine]
        random.shuffle(tab_coordonnees) #on mélange le tableau pour que l'apparition soit aléatoire
        ##on ajoute 2 coffres
        for _ in range(2):
            trouve = False #par défaut, on n'a pas encore trouvé de case pour le futur coffre
            i = 0
            while not trouve and i < len(tab_coordonnees): #tant qu'on n'a pas trouvé de case libre ou qu'on n'a pas tout regardé
                trouve = self.terrain.est_possible(tab_coordonnees[i][0], tab_coordonnees[i][1]) and not tab_coordonnees[i] in deja_present
                i += 1
            if trouve : #si une case est vide
                coffre = module_objets.Coffre(tab_coordonnees[i-1][0], tab_coordonnees[i-1][1])
                self.attributs_jeu.ajouter_tab_coffres(coffre) #ajout d'un nouveau coffre
                self.terrain.mut_terrain(tab_coordonnees[i-1][0], tab_coordonnees[i-1][1], coffre) #ajout dans le terrain
            else :
                ###Coordonnées au hasard
                x, y = self.terrain.trouver_case_libre(chaine)
                coffre = module_objets.Coffre(x, y)
                self.attributs_jeu.ajouter_tab_coffres(coffre)
                self.terrain.mut_terrain(x, y, coffre) #ajout dans le terrain        
      
    def ouverture_coffre(self, coffre, case):
        '''
        réalise la bonne action en fonction du contenu du coffre
        : params
            coffre (module_objets.Coffre)
            case (list), la case qui a permis d'ouvrir le coffre
        : pas de return
        '''
        #Assertion
        assert isinstance(coffre, module_objets.Coffre), "le coffre doit être de la classe Coffre"
        #Code
        self.attributs_jeu.mut_annonce_coffre(True)
        self.attributs_jeu.event_coffre = coffre.acc_contenu()
        
        ########################################################
        #### BONUS DE VIE POUR LE PERSONNAGE
        ########################################################
        
        if coffre.acc_contenu() == 1 :
            perso = self.terrain.acc_terrain(case[0], case[1]) #le personnage sélectionné
            if perso.acc_personnage() == 'geant' : #un géant
                famille = self.famille_geant(perso)
                for elt in famille:
                    elt.mut_pv(perso.acc_pv() + 10)
            else : #personnage "normal"
                perso.mut_pv(perso.acc_pv() + 10) #on augmente de 10 les pv du personnage
            
        ########################################################
        #### CHANGEMENT DE PERSONNAGE (aléatoire)
        ########################################################
        
        elif coffre.acc_contenu() == 2 :
            perso = self.terrain.acc_terrain(case[0], case[1])
            personnages_plateau = ['monstre', 'mage', 'paladin', 'sorciere', 'valkyrie', 'archere', 'poulet', 'cavalier', 'cracheur de feu', 'ivrogne', 'barbare']
            if not perso.acc_personnage() == 'geant': #le personnage ne peut pas se transformer en géant
                personnages_plateau.remove(perso.acc_personnage()) #il ne faut pas que le nouveau personnage soit l'ancien
            else : #un géant
                famille = self.famille_geant(perso) #la bonne famille de géant
                for i in range(0, 4):
                    if not famille[i] == perso: #on garde la case la plus proche du coffre
                        famille[i].mut_pv(0) #on les tue
                    else:
                        survivant = i
                perso = famille[survivant] #la case la plus proche du coffre
            perso.mut_personnage(random.choice(personnages_plateau)) #on remplace au hasard le personnage
        
        ########################################################
        #### AUGMENTATION DES DÉGÂTS DU PERSONNAGE
        ########################################################
            
        elif coffre.acc_contenu() == 3 :
            perso = self.terrain.acc_terrain(case[0], case[1]) #le personnage sélectionné
            if perso.acc_equipe() == 'bleu' :
                ##géant
                if perso.acc_personnage() == 'geant':
                    famille = self.famille_geant(perso)
                    nouvelle_attaque = module_personnage.DIC_ATTAQUES_BLEU['geant'] + 5 #les nouveaux pv de dommage du personnage
                    for elt in famille:
                        module_personnage.mut_dic_attaques('geant', 'bleu', nouvelle_attaque) #on change dans le dictionnaire
                ##personnage "normal"
                else:
                    nouvelle_attaque = module_personnage.DIC_ATTAQUES_BLEU[perso.acc_personnage()] + 5 #les nouveaux pv de dommage du personnage
                    module_personnage.mut_dic_attaques(perso.acc_personnage(), 'bleu', nouvelle_attaque) #on change dans le dictionnaire
                
            else:
                ##géant
                if perso.acc_personnage() == 'geant':
                    famille = self.famille_geant(perso)
                    for elt in famille:
                        nouvelle_attaque = module_personnage.DIC_ATTAQUES_ROUGE['geant'] + 5 #les nouveaux pv de dommage du personnage
                        module_personnage.mut_dic_attaques('geant', 'rouge', nouvelle_attaque) #on change dans le dictionnaire
                ##personnage "normal"
                nouvelle_attaque = module_personnage.DIC_ATTAQUES_ROUGE[perso.acc_personnage()] + 5 #les nouveaux pv de dommage du personnage
                module_personnage.mut_dic_attaques(perso.acc_personnage(), 'rouge', nouvelle_attaque) #on change dans le dictionnaire
            
        #############################################################################
        #### RESUSCITATION DU DERNIER PERSONNAGE MORT DE L'EQUIPE QUI JOUE / ADVERSE
        #############################################################################
        
        elif coffre.acc_contenu() == 4 or coffre.acc_contenu() == 5:        
            if self.attributs_jeu.acc_equipe_en_cours() == 'bleu':
                if coffre.acc_contenu() == 4 : #bonne équipe
                    perso = self.attributs_jeu.acc_dernier_personnage_mort_bleu()
                else : #équipe adverse
                    perso = self.attributs_jeu.acc_dernier_personnage_mort_rouge()
            else :
                if coffre.acc_contenu() == 4 : #bonne équipe
                    perso = self.attributs_jeu.acc_dernier_personnage_mort_rouge()
                else : #équipe adverse
                    perso = self.attributs_jeu.acc_dernier_personnage_mort_bleu()
            
            #resuscitation du personnage
            if not perso == None : #si il y a quelqu'un à ressusciter
                ##si géant
                if isinstance(perso, list) :
                    dic = { 0 : (0, 0),
                              1 : (1, 0),
                              2 : (0, 1),
                              3 : (1, 1)
                              }
                    case = self.terrain.trouver_case_libre_proche(perso[0].acc_x(), perso[0].acc_y(), 'oui') #on trouve une nouvelle case libre proche
                    for geant in perso :
                        geant.mut_pv(module_personnage.DIC_PV[geant.acc_personnage()]) #on réinitialise ses pv
                        self.attributs_jeu.supprimer_positions_tombes(geant) #on enlève son ancienne tombe
                        geant.deplacer(case[0] + dic[geant.acc_numero_geant()][0], case[1] + dic[geant.acc_numero_geant()][1]) #on change les coordonnées du personnage
                        self.attributs_jeu.ajouter_personnage(geant)
                        #on ajoute le personnage ressuscité au terrain
                        self.terrain.mut_terrain(geant.acc_x(), geant.acc_y(), geant)
                ##si autre
                else:
                    case = self.terrain.trouver_case_libre_proche(perso.acc_x(), perso.acc_y(), 'non') #on trouve une nouvelle case libre proche
                    perso.mut_pv(module_personnage.DIC_PV[perso.acc_personnage()]) #on réinitialise ses pv
                    self.attributs_jeu.supprimer_positions_tombes(perso) #on enlève son ancienne tombe
                    perso.deplacer(case[0], case[1]) #on change les coordonnées du personnage
                    self.attributs_jeu.ajouter_personnage(perso)
                    #on ajoute le personnage ressuscité au terrain
                    self.terrain.mut_terrain(perso.acc_x(), perso.acc_y(), perso)
                
            else: #aucun personnage à ressusciter
                coffre.mut_contenu() #on change le contenu du coffre
                self.ouverture_coffre(coffre, case) #on le rouvre
                
        ###################################################################################
        #### AJOUT DE POTION(S) DE VIE/MORT/CHANGEMENT D'EQUIPE A L'EQUIPE QUI JOUE/ADVERSE
        ###################################################################################
        
        elif coffre.acc_contenu() == 6 or coffre.acc_contenu() == 7 or coffre.acc_contenu() == 8 or coffre.acc_contenu() == 9 :
            #dic_potion[contenu] = (nb de potion, type potion)
            dic_potion = {6 : (2, 2),
                          7 : (1, 3),
                          8 : (1, 4)
                          }
            if not coffre.acc_contenu() == 9 : #ajout à la bonne équipe
                if self.attributs_jeu.acc_equipe_en_cours() == 'bleu' :
                    for _ in range(dic_potion[coffre.acc_contenu()][0]):
                        self.attributs_jeu.ajouter_potions_bleues(module_objets.Potion(dic_potion[coffre.acc_contenu()][1]))
                else:
                    for _ in range(dic_potion[coffre.acc_contenu()][0]):
                        self.attributs_jeu.ajouter_potions_rouges(module_objets.Potion(dic_potion[coffre.acc_contenu()][1]))
            else : #ajout à l'équipe adverse
                if self.attributs_jeu.acc_equipe_en_cours() == 'bleu' :
                    #deux potions de mort
                    self.attributs_jeu.ajouter_potions_rouges(module_objets.Potion(3))
                    self.attributs_jeu.ajouter_potions_rouges(module_objets.Potion(3))
                else:
                    #deux potions de mort
                    self.attributs_jeu.ajouter_potions_bleues(module_objets.Potion(3))
                    self.attributs_jeu.ajouter_potions_bleues(module_objets.Potion(3))
        
        #######################################################################
        #### AUGMENTATION DES DÉGÂTS DE TOUS LES PERSONNAGES ADVERSES
        #######################################################################
        
        else : #10
            equipe = self.attributs_jeu.acc_equipe_en_cours()
            for perso in ['monstre', 'mage', 'paladin', 'geant', 'sorciere', 'valkyrie', 'archere', 'poulet', 'cavalier', 'cracheur de feu', 'ivrogne', 'barbare'] :
                if equipe == 'bleu' :
                    nouvelle_attaque = module_personnage.DIC_ATTAQUES_ROUGE[perso] + 2 #les nouveaux pv de dommage du personnage
                    module_personnage.mut_dic_attaques(perso, 'rouge', nouvelle_attaque) #on change dans le dictionnaire
                else :
                    nouvelle_attaque = module_personnage.DIC_ATTAQUES_BLEU[perso] + 2 #les nouveaux pv de dommage du personnage
                    module_personnage.mut_dic_attaques(perso, 'bleu', nouvelle_attaque) #on change dans le dictionnaire
        
    ########################################################
    #### Méthode Potion :
    ########################################################   
    
    def ouverture_potion(self, x, y):
        '''
        réalise la bonne action en fonction du contenu de la potion
        : params
            x, y (int) coordonnées où est jetée la potion
        : return (bool), True si la potion a atterrit sur un perso et False sinon
        '''
        #Assertions
        assert isinstance(x, int) and 0 <= x <= 20, 'x doit être un entier compris entre 0 et 20 inclus'
        assert isinstance(y, int) and 0 <= y <= 20, 'y doit être un entier compris entre 0 et 20 inclus'
        #Code
        
        ##récupération de la potion
        equipe = self.attributs_jeu.acc_equipe_en_cours()
        
        if not self.attributs_jeu.est_vide_file_potion() :
            if equipe == 'bleu':
                potion = self.attributs_jeu.enleve_potions_bleues()
            else :
                potion = self.attributs_jeu.enleve_potions_rouges()
            potion_valide = True
        else:
            potion_valide = False
            a_attaque = False

        ##les cases atteintes par la potion
        if potion_valide :
            cases = potion.definir_cases_atteintes(x, y, self.terrain, equipe)
            a_attaque = len(cases) != 0 #un personnage au moins a été touché et il reste encore des potions du type choisi
            perso_soigne = [] #les différents personnages soignés
        
            ########################################################
            #### ATTAQUE PERSONNAGE
            ########################################################
            if potion.acc_contenu() == 1:
                pv = random.randint(3, 10) #on retire des pv au hasard
                for case in cases: #chaque case de l'étendu
                    perso = self.terrain.acc_terrain(case[0], case[1])
                    perso.est_attaque('sorciere', pv) #on retire le bon nombre de pv
                    perso.mut_endommage()
                    
                if a_attaque :
                    ##la file ne doit pas être vide
                    if equipe == 'bleu':
                        self.attributs_jeu.ajouter_potions_bleues(module_objets.Potion(1))
                    else:
                        self.attributs_jeu.ajouter_potions_rouges(module_objets.Potion(1))
                    ##console
                    self.attaque_sorciere_console(equipe)
                    
            ########################################################
            #### GUERISON PERSONNAGE
            ########################################################
            elif potion.acc_contenu() == 2:
                for case in cases : #chaque case de l'étendu
                    perso = self.terrain.acc_terrain(case[0], case[1])
                    ecart_pv = module_personnage.DIC_PV[perso.acc_personnage()] - perso.acc_pv()
                    ##le nombre de pv ne doit pas dépassé le nombre de pv par défaut
                    if ecart_pv >= 10 : 
                        perso.est_attaque('sorciere', -10) #on ajoute 10 pv
                    else :
                        perso.est_attaque('sorciere', ecart_pv) #on ajoute 10 pv
                    perso.mut_soigne()
                    #pour la console, tous les personnages soignés
                    if not perso in perso_soigne :
                        perso_soigne.append(perso)
                ###affiche dans la console
                if a_attaque :
                    for perso in perso_soigne : #plusieurs personnages peuvent avoir été guéris
                        self.guerison_console(perso)
                
            ########################################################
            #### MORT DU PERSONNAGE
            ########################################################
            elif potion.acc_contenu() == 3:
                if a_attaque :
                    for case in cases :
                        perso = self.terrain.acc_terrain(case[0], case[1])
                        perso.est_attaque('sorciere', perso.acc_pv()) #on retire tous les pv
                        perso.mut_endommage()
                    self.attaque_sorciere_console(equipe)
                
            ########################################################
            #### CHANGEMENT D'EQUIPE
            ########################################################
            else :
                if a_attaque :
                    tab_ancien_g = []
                    tab_nouveau_g = []
                    for case in cases :
                        perso = self.terrain.acc_terrain(case[0], case[1])
                        if not perso.acc_personnage() == 'monstre' :
                            if perso.acc_personnage() == 'geant':
                                tab_ancien_g.append(perso)
                            perso.mut_equipe() #le personnage change d'équipe
                            self.changement_equipe_personnage_console(perso)
                            if perso.acc_personnage() == 'geant':
                                tab_nouveau_g.append(perso)
                        else :
                            a_attaque = False

                    if perso.acc_personnage() == 'geant' and perso.acc_equipe() == 'bleu':
                        self.attributs_jeu.supprimer_famille_geant_rouge(tab_ancien_g)
                        self.attributs_jeu.ajouter_famille_geant_bleu(tab_nouveau_g)
                    elif perso.acc_personnage() == 'geant' :
                        self.attributs_jeu.supprimer_famille_geant_bleu(tab_ancien_g)
                        self.attributs_jeu.ajouter_famille_geant_rouge(tab_nouveau_g)
            if a_attaque :
                ###Attributs attaques
                self.attributs_jeu.mut_attaque_en_cours(True)
                self.attributs_jeu.mut_attaque_temps(0)
                self.attributs_jeu.mut_cases_potions(cases)
        
            else :
                #si pas d'attaque, on renfile la potion
                if equipe == 'bleu':
                    self.attributs_jeu.ajouter_potions_bleues(potion)
                else:
                    self.attributs_jeu.ajouter_potions_rouges(potion)  
        return a_attaque
    
    ######################################################
    ### Méthodes de Clique :
    ###################################################### 
        
    def deplacement_est_clique(self) :
        '''
        Déplace le personnage en question sur le cercle selon s'il est un personnage "classique" ou s'il est un Géant.
        : return (bool) True si un deplacement a été effectué, False sinon
        '''
        position_case = self.souris.acc_position_case()
        
        #Si le joueur a cliqué sur un personnage de l'équipe en cours et s'il a cliqué sur un cercle de déplacement :
        if self.attributs_jeu.est_meme_equipe() and position_case in self.attributs_jeu.acc_deplacements():
            
            #Si le personnage est un Géant, alors déplace le Géant :
            if self.attributs_jeu.acc_selection().acc_personnage() == 'geant':
                self.deplacer_geant(position_case[0], position_case[1])
            
            #Sinon, le personnage est "classique" :
            else :
                self.deplacer(position_case[0], position_case[1])
            
            self.deplacement_console(self.attributs_jeu.acc_selection(), position_case) #Ajoute une phrase de déplacement dans la console du jeu
            self.effacer_actions()
            self.attributs_jeu.mut_nombre_action(self.attributs_jeu.acc_nombre_action() + 1) #Augmente le nombre d'action de 1
            return True
            
        return False
    
    def jouer_son_attaque(self):
        '''
        joue le son d'attaque en fonction du personnage
        '''
        if self.attributs_jeu.acc_selection().acc_personnage() == 'sorciere' :
            self.gestionnaire_son.jouer_effet_sonore("potion")
        elif self.attributs_jeu.acc_selection().acc_personnage() == 'poulet' or self.attributs_jeu.acc_selection().acc_personnage() == 'ivrogne':
            self.gestionnaire_son.jouer_effet_sonore("poing")
        elif self.attributs_jeu.acc_selection().acc_personnage() == 'cracheur de feu' or self.attributs_jeu.acc_selection().acc_personnage() == 'mage' :
            self.gestionnaire_son.jouer_effet_sonore("feu")
        elif self.attributs_jeu.acc_selection().acc_personnage() == 'archere':
            self.gestionnaire_son.jouer_effet_sonore("tir")
        else :
            self.gestionnaire_son.jouer_effet_sonore("lame")
            
    def attaque_est_clique(self):
        '''
        attaque le personnage en question selon si il est "normal" ou si il est un geant.
        : return (bool) True si une attaque a été effectuée, False sinon
        '''
        position_case = self.souris.acc_position_case()
        #Si la souris est dans une case d'attaque :
        if self.attributs_jeu.est_meme_equipe() and position_case in self.attributs_jeu.acc_attaques() :
            
            personnage_qui_subit = self.terrain.acc_terrain(position_case[0], position_case[1]) #Sélectionne le personnage qui va subir les attaques
            a_attaque = True #par défaut, on a attaqué
            self.jouer_son_attaque() #on appelle la Méthode pour jouer un son d'attaque
            perso_qui_attaque = self.attributs_jeu.acc_selection()
            #Si la sorcière attaque
            if perso_qui_attaque.acc_personnage() == 'sorciere' :
                a_attaque = self.ouverture_potion(position_case[0], position_case[1])
                
            #Si le géant attaque (attaque tous les personnages autour de lui)
            elif perso_qui_attaque.acc_personnage() == 'geant' :
                for case in self.attributs_jeu.acc_attaques():
                    perso = self.terrain.acc_terrain(case[0], case[1])
                    perso.est_attaque('geant')
                    perso.mut_endommage()
                self.attaque_console(self.attributs_jeu.acc_selection(), personnage_qui_subit) #Ajoute une phrase d'attaque dans la console du jeu
            
            #Sinon, le personnage est "classique" :
            else :
                personnage_qui_subit.est_attaque(self.attributs_jeu.acc_selection().acc_personnage())
                personnage_qui_subit.mut_endommage()
                    
                self.attaque_console(self.attributs_jeu.acc_selection(), personnage_qui_subit) #Ajoute une phrase d'attaque dans la console du jeu
            
            #Si le personnage_qui_subit est le Géant  :
            if personnage_qui_subit.acc_personnage() == 'geant' :
                famille = self.famille_geant(personnage_qui_subit)
                #Pour chaque partie du geant :
                for geant in famille :
                    geant.est_attaque(self.attributs_jeu.acc_selection().acc_personnage())
                    geant.mut_endommage()
            
            if a_attaque : 
                #Attributs jeu
                self.attributs_jeu.mut_nombre_action(self.attributs_jeu.acc_nombre_action() + 1) #Augmente le nombre d'action de 1
                self.attributs_jeu.acc_selection().mut_attaque() #le personnage a attaqué
                self.attributs_jeu.mut_attaque_en_cours(True)
                self.attributs_jeu.mut_attaque_temps(0)
                
            self.changer_personnage(' ') #Enlève le personnage sélectionné par le joueur (rien sélectionné)
            self.effacer_actions()
            self.attributs_jeu.mut_personnage_qui_attaque(True)
            return True
            
        return False

    def coffre_est_clique(self, coffre = None):
        '''
        si un coffre est cliqué et qu'il y a un joueur de l'équipe en cours autour du coffre, celui-ci s'ouvre
        : pas de return
        '''
        #vérification d'un joueur autour
        if coffre == None :
            coffre = self.attributs_jeu.acc_coffre_selection()
        perso_selectionne = self.attributs_jeu.acc_selection()
        #si le coffre n'a pas déjà été ouvert et personnage sélectionné de la bonne équipe
        if not coffre.acc_est_ouvert() and isinstance(perso_selectionne, module_personnage.Personnage) and perso_selectionne.acc_personnage() != 'monstre' and perso_selectionne.acc_equipe() == self.attributs_jeu.acc_equipe_en_cours() : 
            present, case = coffre.est_present_autour(self.terrain, perso_selectionne)
            #si oui, ouverture du coffre
            if present :
                coffre.ouverture()
                self.ouverture_coffre(coffre, case)
                self.coffre_console(coffre.acc_contenu())
                
                if not self.attributs_jeu.acc_annonce_coffre() :
                    self.attributs_jeu.mut_annonce_coffre(True)
                 
                self.attributs_jeu.mut_nombre_action(self.attributs_jeu.acc_nombre_action() + 1)
                self.jouer_monstres() #on fait jouer les monstres
    
    ######################################################
    ### Événements pendant une partie :
    ######################################################
    
    def effacer_actions(self) :
        '''
        Efface les indications de déplacement et d'attaques du personnage sélectionné
        : pas de return
        '''
        self.attributs_jeu.mut_deplacements([]) #Enlève les déplacements
        self.attributs_jeu.mut_deplacements_coord([])
        self.attributs_jeu.mut_deplacements_cavalier([]) #Enlève les déplacements (du cavalier)
        self.attributs_jeu.mut_attaques([]) #Enlève les attaques
    
    def changer_personnage(self, selection) :
        '''
        Enlève le personnage sélectionné et donc le change
        : param selection (?)
        : pas de return
        '''
        if isinstance(selection, module_objets.Coffre):# si c'est un coffre
            self.attributs_jeu.mut_coffre_selection(selection)
        else: #sinon
            self.attributs_jeu.mut_selection(selection)
        
        #Si clique un personnage ou déplacement/attaque de l'équipe qui joue :
        if selection != ' ' and isinstance(selection, module_personnage.Personnage) and selection.acc_personnage() != 'monstre' :
            selection.cases_valides_deplacement(self.terrain) #déplacements
            selection.cases_valides_attaques(self.terrain) #attaques
        
        #Sinon (si clique sur autre chose) :
        else :
            self.effacer_actions()
    
    def changer_equipe(self):
        '''
        Change l'équipe en cours et enlève le personnage sélectionné
        : pas de return
        '''
        dic_equipes = {'bleu' : 'rouge', 'rouge' : 'bleu'}
        self.attributs_jeu.mut_equipe_en_cours(dic_equipes[self.attributs_jeu.acc_equipe_en_cours()]) #Change l'équipe en cours.
        self.effacer_actions()
        self.changer_personnage(' ') #Enlève le personnage sélectionné
        self.attributs_jeu.mut_nombre_action(0) #Met le nombre d'action à 0
        self.attributs_jeu.augmente_nombre_tour() #Augmente le nombre de tour de 1
        self.equipe_console(self.attributs_jeu.acc_equipe_en_cours()) #Indique dans la console (du jeu) qu'il y a eu un changement d'équipe
        
    def personnages_sont_mort(self):
        '''
        Vérifie si des personnages ou monstres sont mort (pv <= 0). 
        Si c'est le cas, on les supprime du tableau correspondant et on les enlève du terrain
        : pas de return
        '''
        #Pour chaque personnage et monstre dans leur tableau respectif :
        for personnage in self.attributs_jeu.acc_tab_personnages() + self.attributs_jeu.acc_tab_monstres() :
            #S'il est mort :
            if personnage.est_mort() :
                #Si le personnage n'est pas un monstre :
                if not isinstance(personnage, module_personnage.Monstre) :
                    #Si le personnage est un geant :
                    if isinstance(personnage, module_personnage.Geant) :
                        #Si son numero est 0, place une tombe à sa position :
                        if personnage.acc_numero_geant() == 0:
                            self.attributs_jeu.ajouter_positions_tombes((personnage.acc_x() * 38 + 269, personnage.acc_y() * 38 + 19))
                            print('position : ', (personnage.acc_x() * 38 + 269, personnage.acc_y() * 38 + 19))
                        famille_geant = self.famille_geant(personnage)
                        if personnage.acc_equipe() == 'bleu':
                            self.attributs_jeu.mut_dernier_personnage_mort_bleu(famille_geant)
                        else:
                            self.attributs_jeu.mut_dernier_personnage_mort_rouge(famille_geant)
                            
                    #Sinon, le personnage est un personnage "classique", place une tombe à sa position :
                    else :
                        self.attributs_jeu.ajouter_positions_tombes((personnage.acc_x() * 38 + 250, personnage.acc_y() * 38))
                        #Si le personnage est de l'équipe bleu, alors on change le dernier personnage mort de l'équipe bleu par ce personnage :
                        if personnage.acc_equipe() == 'bleu':
                            self.attributs_jeu.mut_dernier_personnage_mort_bleu(personnage)
                        #Sinon, le personnage est de l'équipe rouge, alors on change le dernier personnage mort de l'équipe rouge par ce personnage :
                        else:
                            self.attributs_jeu.mut_dernier_personnage_mort_rouge(personnage)
                    self.attributs_jeu.supprimer_personnage(personnage) #Supprime le personnage du tableau des personnages
                #Sinon, le personnage est un monstre, alors on le supprime du tableau des monstres
                else :
                    self.attributs_jeu.supprimer_monstre(personnage)
                
                self.terrain.mut_terrain(personnage.acc_x(), personnage.acc_y(), ' ') #Place une case vide sur la case où le personnage est mort.
                self.mort_personnage_console(personnage)
                    
    def qui_gagne(self, bleu_present, rouge_present) :
        '''
        Renvoie l'équipe qui a gagné 
        : params
            bleu_present (bool)
            rouge_present (bool)
        : return (str)
        '''
        #Assertions
        assert isinstance(bleu_present, bool) and isinstance(rouge_present, bool), "les deux paramètres doivent être des booléens"
        #Code
        if bleu_present and not rouge_present : #bleu gagne
            return 'bleu'
        elif not bleu_present and rouge_present : #rouge gagne
            return 'rouge'
        elif not bleu_present and not rouge_present : #monstres gagnent
            return 'monstres'           
    
    def est_fini(self):
        '''
        Renvoie True s'il reste que des personnages d'une même équipe, False sinon
        : return (bool)
        '''
        tab = self.attributs_jeu.acc_tab_personnages()
        indice = 0
        bleu_present = False
        rouge_present = False
        
        #Tant qu'un personnage de chaque équipe est vivant dans le tableau des personnages :
        while not (bleu_present and rouge_present) and indice < len(tab):
            personnage = tab[indice]
            #Si le personnage est de l'équipe bleu, alors il y a au moins un personnage de l'équipe bleu qui est présent :
            if personnage.acc_equipe() == 'bleu' :
                bleu_present = True
            #Sinon, le personnage est de l'équipe rouge, alors il y a au moins un personnage de l'équipe rouge qui est présent :
            else :
                rouge_present = True
                
            indice += 1       
        #Si il reste une seule équipe en jeu (ou les monstres), alors change la partie terminée en True et change l'équipe qui a gagné (neutre pour les monstres):
        if not (bleu_present and rouge_present) :
            self.attributs_jeu.mut_partie_terminee(not (bleu_present and rouge_present)) 
            equipe_qui_gagne = self.qui_gagne(bleu_present, rouge_present)
            self.attributs_jeu.mut_equipe_gagnante(equipe_qui_gagne)
            self.equipe_gagnante_console()
        
        return self.attributs_jeu.acc_partie_terminee()
        
    ######################################################
    ### Méthode Réinitialiser :
    ######################################################
        
    def reinitialiser_attributs(self, par_defaut = False, mode_robot = False) :
        '''
        Réinitialise quelques attributs du jeu quand le joueur charge une partie
        '''
        #Conserver les attributs en cas d'erreur de fichier :
        if not par_defaut :   
            attributs_importation = [self.attributs_jeu, self.terrain, self.souris, self.affichage, self.robot]
        
        #Attributs Jeu :
        self.attributs_jeu = module_attributs_jeu.Attributs_Jeu()
        
        #Attributs des Importations :
        self.terrain = module_terrain.Terrain(self.attributs_jeu)
        self.souris = module_souris.Souris(self, self.attributs_jeu, self.sauvegarde, self.terrain, self.gestionnaire_son)
        self.affichage = module_afficher.Affichage(self, self.attributs_jeu, self.terrain, self.ecran, self.souris)
        self.robot = module_robot.Robot(self, self.attributs_jeu, self.terrain)
        
        if par_defaut :
            self.attributs_jeu.mut_menu(False)
            self.partie_commence_console()
            self.placer_par_defaut()
            
        if mode_robot :
            self.attributs_jeu.mut_mode_robot(True)

        if not par_defaut :    
            return attributs_importation, self.attributs_jeu
    
    def restaurer_attributs_importation(self, tab) :
        '''
        Restaure les anciens attributs en cas de chargement de fichier texte incorrecte
        :param tab (list of attributs)
        :return (Attributs_Jeu), pour la classe Sauvegarder
        '''
        #Assertion :
        assert isinstance(tab, list) and len(tab) == 5, 'Le tableau doit contenir 5 éléments !'
        assert isinstance(tab[0], module_attributs_jeu.Attributs_Jeu), 'Le premier élément du tableau des attributs doit être de la classe Attributs_Jeu (module_attributs_jeu) !'
        assert isinstance(tab[1], module_terrain.Terrain), 'Le deuxième élément du tableau des attributs doit être de la classe Terrain (module_terrain) !'
        assert isinstance(tab[2], module_souris.Souris), 'Le troisième élément du tableau des attributs doit être de la classe Souris (module_souris) !'
        assert isinstance(tab[3], module_afficher.Affichage), 'Le quatrième élément du tableau des attributs doit être de la classe Affichage (module_afficher) !'
        assert isinstance(tab[4], module_robot.Robot), 'Le cinquième élément du tableau des attributs doit être de la classe Robot (module_robot) !'
        #Code :
        self.attributs_jeu = tab[0]
        self.terrain = tab[1]
        self.souris = tab[2]
        self.affichage = tab[3]
        self.robot = tab[4]
        
        return self.attributs_jeu
        
        
    ######################################################
    ### Méthode Boucle / Déroulement du Jeu :
    ######################################################

    def boucle(self) :
        '''
        Ici on effectue tous les calculs et affichages nécessaires au jeu
        : pas de return
        '''
        music = self.gestionnaire_son.lancer_musique_fond()
        
        #Tant que l'attribut continuer est True, alors la boucle continue et le jeu aussi :
        while self.attributs_jeu.acc_continuer() :
            
            #Si la musique s'arrête, on la relance.
            self.gestionnaire_son.boucle_musique(music)
            
            #Quand le compteur arrive à 70, il repart à 0. Règle à la vitesse d'animation des personnages.
            self.attributs_jeu.mut_compteur((self.attributs_jeu.acc_compteur() + 1) % 70)  
            
            #Arrête toutes les animations de déplacement.
            self.arreter_animation_deplacement() 
            
            ######################################################
            ### Menu :
            ######################################################
            
            #Si l'attribut menu est True, alors le joueur se trouve dans le menu :
            if self.attributs_jeu.acc_menu() :
                
                ######################################################
                ### Clavier / Souris :
                ######################################################
                
                #Pour chaque entrées :
                for evenement in pygame.event.get() :
                    self.souris.entrees_menu(evenement) #Vérifie s'il y a eu une interaction dans le menu
                    
                ######################################################
                ### Affichage :
                ######################################################

                self.affichage.afficher_menu() #Affiche le menu
            
            ######################################################
            ### Jeu :
            ######################################################
            
            #Si l'attribut menu est False, alors le joueur se trouve dans le jeu (dans une partie) :
            else:
                
                self.gerer_animations_attaques() #Gère le temps d'animation des attaques
                
                #Si il n'y a pas de déplacement et/ou d'attaque de personnage en cours et que la partie n'est pas finie :
                if not self.attributs_jeu.acc_deplacement_en_cours() and not self.attributs_jeu.acc_attaque_en_cours() and not self.attributs_jeu.acc_partie_terminee() :
                    self.personnages_sont_mort() #Vérifie s'il y a des morts (personnages et monstres) 
                    self.est_fini() #Vérifie si la partie est fini
                    
                    #Change d'équipe au bout de 3 actions :
                    if self.attributs_jeu.acc_nombre_action() == 3 :
                        self.changer_equipe()
                
                ######################################################
                ### Clavier / Souris :
                ######################################################
                
                #Pour chaque entrées :
                for evenement in pygame.event.get() :
                    self.souris.entrees_jeu(evenement) #Vérifie s'il y a eu une interaction dans le jeu
                
                ######################################################
                ### Coffres :
                ######################################################
                    
                self.apparition_coffres()
                
                ######################################################
                ### Monstres :
                ######################################################
                
                self.changer_etat_monstres()
                self.ajouter_tab_monstres()
                
                ######################################################
                ### Console :
                ######################################################
                            
                self.attributs_jeu.enlever_console()
                
                ######################################################
                ### Temps :
                ######################################################
                
                self.attributs_jeu.changer_temps_jeu() #Modifie l'atmosphère quand le temps est venu
                
                ######################################################
                ### Affichage :
                ######################################################
                
                self.affichage.afficher_jeu()
                
                ######################################################
                ### Robot :
                ######################################################
                
                if self.attributs_jeu.acc_mode_robot() :
                    self.robot.jouer_robot()
            
            ######################################################
            ### Animations :
            ######################################################

            self.souris.deselectionner_bouton() #Désélectionne le bouton après 0.3 secondes
            
            ######################################################
            ### Fréquence de 60 images par seconde :
            ###################################################### 
            
            pygame.display.flip()
            self.acc_horloge().tick(30)
        
        pygame.quit() #Ferme la fenêtre Pygame si la boucle s'arrête
        
    ######################################################
    ### Initialisation du Jeu et de la fenêtre :
    ######################################################
        
    def jouer(self):
        '''
        Initialise la fenêtre et lance le jeu avec un taux de 60 rafraîchissements/calculs par seconde
        : pas de return
        '''
        pygame.init() #Initialise Pygame 
        pygame.display.set_caption('Medieval Heroes') #Le nom de la fenêtre sera "Medieval Heroes"
        pygame.mouse.set_visible(False) #La souris n'est pas visible quand elle est sur la fenêtre Pygame
        pygame.display.set_icon(pygame.image.load('medias/medieval_heroes.png')) #Ajoute l'icone à la fenêtre :
        self.boucle() #Lance la boucle du jeu