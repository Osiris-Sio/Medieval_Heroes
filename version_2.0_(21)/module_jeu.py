# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Jeu.

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################

import pygame, module_attributs_jeu, module_terrain, module_afficher, module_clavier_souris, module_objets, module_personnage, time, random, module_sauvegarde
from graphe import parcourir_graphe
from graphe import module_lineaire #provisoire

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
        self.ecran = pygame.display.set_mode((1300, 800))
        self.horloge = pygame.time.Clock()
        
        #Attributs des Importations :
        self.attributs_jeu = module_attributs_jeu.Attributs_Jeu()
        self.partie_commence_console() #Console de départ
        self.sauvegarde = module_sauvegarde.Sauvegarde(self.attributs_jeu)
        self.clavier_souris = module_clavier_souris.Clavier_Souris(self.attributs_jeu)
        self.terrain = module_terrain.Terrain(self.attributs_jeu, self.clavier_souris)
        self.affichage = module_afficher.Affichage(self.attributs_jeu, self.terrain, self.ecran, self.clavier_souris)
        
        ###Pose des personnages (par défaut)
        
        #Geant rouge:
        geant1r = module_personnage.Geant('rouge', 10, 0, 8, 0)
        geant2r = module_personnage.Geant('rouge', 11, 0, 8, 1)
        geant3r = module_personnage.Geant('rouge', 10, 1, 8, 2)
        geant4r = module_personnage.Geant('rouge', 11, 1, 8, 3)
        self.famille_geant_rouge = [geant1r, geant2r, geant3r, geant4r] ##La famille des géants
        self.coordonnees_rouge = [(geant1r.acc_x(), geant1r.acc_y()), (geant2r.acc_x(), geant2r.acc_y()),
                                   (geant3r.acc_x(), geant3r.acc_y()), (geant4r.acc_x(), geant4r.acc_y())]
        
        #Geant bleu:
        geant1b = module_personnage.Geant('bleu', 10, 19, 8, 0)
        geant2b = module_personnage.Geant('bleu', 11, 19, 8, 1)
        geant3b = module_personnage.Geant('bleu', 10, 20, 8, 2)
        geant4b = module_personnage.Geant('bleu', 11, 20, 8, 3)
        self.famille_geant_bleu = [geant1b, geant2b, geant3b, geant4b] ##La famille des géants    
        self.coordonnees_bleu = [(geant1b.acc_x(), geant1b.acc_y()), (geant2b.acc_x(), geant2b.acc_y()),
                                   (geant3b.acc_x(), geant3b.acc_y()), (geant4b.acc_x(), geant4b.acc_y())]
        
        
        self.attributs_jeu.mut_tab_personnages([
            
        #rouge :
        module_personnage.Personnage('paladin', 'rouge', 6, 2, 8),#personnage, equipe, x, y, pv
        module_personnage.Cavalier('rouge', 8, 2, 8),
        module_personnage.Personnage('ivrogne', 'rouge', 7, 2, 8),
        module_personnage.Personnage('poulet', 'rouge', 10, 3, 8),
        module_personnage.Personnage('valkyrie', 'rouge', 9, 2, 8),
        module_personnage.Personnage('sorciere', 'rouge', 10, 2, 8),
        module_personnage.Personnage('archere', 'rouge', 11, 2, 8),
        module_personnage.Personnage('barbare', 'rouge', 12, 2, 8),
        module_personnage.Personnage('mage', 'rouge', 13, 2, 8),
        module_personnage.Personnage('cracheur de feu', 'rouge', 14, 2, 8),
        geant1r,
        geant2r,
        geant3r,
        geant4r,
        
        #bleu :
        module_personnage.Personnage('paladin', 'bleu', 6, 18, 8),#personnage, equipe, x, y, pv
        module_personnage.Cavalier('bleu', 8, 18, 8),
        module_personnage.Personnage('ivrogne', 'bleu', 7, 18, 8),
        module_personnage.Personnage('poulet', 'bleu', 10, 17, 8),
        module_personnage.Personnage('valkyrie', 'bleu', 9, 18, 8),
        module_personnage.Personnage('sorciere', 'bleu', 10, 18, 8),
        module_personnage.Personnage('archere', 'bleu', 11, 18, 8),
        module_personnage.Personnage('barbare', 'bleu', 12, 18, 8),
        module_personnage.Personnage('mage', 'bleu', 13, 18, 8),
        module_personnage.Personnage('cracheur de feu', 'bleu', 14, 18, 8),
        geant1b,
        geant2b,
        geant3b,
        geant4b,
        ])
        
        
        
        
    def placer(self) :
        '''
        Place les personnages, monstres et coffres sur le terrain
        '''
        for elt in self.attributs_jeu.acc_tab_personnages() + self.attributs_jeu.acc_tab_monstres() + self.attributs_jeu.acc_tab_coffres() :
            self.terrain.mut_terrain(elt.acc_x(), elt.acc_y(), elt)
                
    ######################################################
    ### Accesseurs :
    ######################################################
        
    def acc_ecran(self):
        '''
        Renvoie la propriété de l'ecran
        '''
        return self.ecran
    
    def acc_horloge(self):
        '''
        Renvoie l'attribut horloge
        '''
        return self.horloge
    
    ######################################################
    ### Mutateurs :
    ######################################################
    
    def mut_famille_coordo(self, equipe):
        '''
        réactualise les coordonnées du géant appartenant à l'équipe passée en paramètre
        : param equipe (str), 'bleu' ou 'rouge':
        : pas de return
        '''
        #assertion
        assert equipe in ['bleu', 'rouge'], "l'équipe doit être soit bleu soit rouge"
        #code
        if equipe == 'bleu':
            famille = self.famille_geant_bleu
            self.coordonnees_bleu = [(famille[0].acc_x(), famille[0].acc_y()), (famille[1].acc_x(), famille[1].acc_y()),
                                   (famille[2].acc_x(), famille[2].acc_y()), (famille[3].acc_x(), famille[3].acc_y())]
        else : #rouge
            famille = self.famille_geant_rouge
            self.coordonnees_rouge = [(famille[0].acc_x(), famille[0].acc_y()), (famille[1].acc_x(), famille[1].acc_y()),
                                   (famille[2].acc_x(), famille[2].acc_y()), (famille[3].acc_x(), famille[3].acc_y())]
    
    ######################################################
    ### Déplacements :
    ######################################################
    
    def deplacer(self, x, y):
        '''
        déplace un personnage sur la grille
        : params
            x, y (int), les nouvelles coordonnées
        '''
        print('boucle' , self.attributs_jeu.compteur)
        ##
        self.terrain.mut_terrain(self.attributs_jeu.acc_selection().acc_x(), self.attributs_jeu.acc_selection().acc_y(), ' ')# remplace l'ancienne place du personnage par une case vide
        self.attributs_jeu.mut_nouvelles_coord((x, y))
        print('attributs_jeu.nouvelles_coord')
        ######PARTIE AFFICHAGE DU DEPLACEMENT
        
        #Récupération du bon chemin :
        perso = self.attributs_jeu.acc_selection()
        coordo = (self.attributs_jeu.acc_selection().acc_x(), self.attributs_jeu.acc_selection().acc_y())
        if perso.acc_personnage() == 'cavalier' : #si c'est un cavalier
            dep = self.attributs_jeu.acc_deplacements_cavalier()
        else:
            dep = self.attributs_jeu.acc_deplacements()
        graphe = perso.construire_graphe_perso(coordo, dep)
        chemin = parcourir_graphe.depiler_chemin(graphe, coordo, (x, y))
        chemin2 = []
        for elt in chemin:
            chemin2.append((elt[0] * 38 + 250, elt[1] * 38))
        self.attributs_jeu.mut_chemin(chemin2) # on obtient un chemin avec toutes les coordonnées dans lesquelles le personnage doit passer
        self.attributs_jeu.mut_coordonnees_personnage((chemin2[0])) # le personnage se situe au premier point du chemin
        self.attributs_jeu.mut_personnage_en_deplacement([self.attributs_jeu.acc_selection().acc_personnage(), self.attributs_jeu.acc_selection().acc_equipe()]) # on désigne le personnage qui se déplace
        self.attributs_jeu.mut_deplacement_en_cours(True) # on déclare qu'un déplacement est en cours
        self.attributs_jeu.nb_actions += 1 # on augmente le nombre d'action effectuée du joueur de 1
        
    def arreter_animation(self):
        '''
        arrête l'animation une fois que l'image du personnage en déplacement est arrivée à destination
        '''
        if self.attributs_jeu.acc_indice_courant() >= len(self.attributs_jeu.acc_chemin()) - 1 and self.attributs_jeu.acc_nb_actions() != 0:           
            self.attributs_jeu.mut_indice_courant(0)
            self.replacer()
          
    def replacer(self):
        '''
        replace le personnage après l'avoir déplacé
        '''
        print('yes')
        print(self.attributs_jeu.acc_nouvelles_coord())
        print(self.attributs_jeu.acc_selection())
        
        x, y = self.attributs_jeu.acc_nouvelles_coord()
        perso = self.attributs_jeu.acc_selection()
        
        if perso != None :
            perso.deplacer(x, y) # change les attributs des personnages dans la grille
            #
            self.terrain.mut_terrain(x, y, perso) # déplace la selection aux nouvelles coordonnées
            self.attributs_jeu.mut_selection(None)
            self.attributs_jeu.mut_personnage_en_deplacement(None)
            self.attributs_jeu.mut_deplacement_en_cours(False)

    def deplacer_geant(self, x, y):
        '''
        Déplace les bouts du géant aux nouvelles coordonnées
        : params
            x, y (int)
        '''
        position = (self.attributs_jeu.acc_selection().acc_x(), self.attributs_jeu.acc_selection().acc_y())
        if position in self.coordonnees_bleu : #le géant bleu
            famille = self.famille_geant_bleu
            equipe = 'bleu'
        else: #le géant rouge
            famille = self.famille_geant_rouge
            equipe = 'rouge'
        deplacement = self.coordo_geant(famille[0].acc_x(), famille[0].acc_y(), x, y)
        ##vide l'ancien emplacement
        for geant in famille:
            self.terrain.mut_terrain(geant.acc_x(), geant.acc_y(), ' ') # vide à l'ancienne place
            
        for geant in famille:
            n_x = geant.acc_x() + deplacement[0]
            n_y = geant.acc_y() + deplacement[1]
            geant.deplacer(n_x, n_y) # pour le personnage  
            self.terrain.mut_terrain(n_x, n_y, geant)
        self.mut_famille_coordo(equipe)
        
    def coordo_geant(self, tete_x, tete_y, nouveau_x, nouveau_y):
        '''
        : params
            tete_x (int)
            tete_y (int)
            nouveau_x (int)
            nouveau_y (int)        
        : return (tuple)
        '''
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

    ######################################################
    ### Attaques :
    ######################################################
    
    def gerer_animations_attaques(self):
        '''
        gere le fonctionnement de l'affichage des attaques dans le jeu
        '''
        if self.attributs_jeu.acc_attaque_temps() < 20 and self.attributs_jeu.acc_attaque_en_cours() :
            self.attributs_jeu.mut_attaque_temps(self.attributs_jeu.acc_attaque_temps() + 1)
        elif self.attributs_jeu.acc_attaque_temps() == 20:
            self.attributs_jeu.mut_attaque_en_cours(False)
            self.attributs_jeu.mut_attaque_temps(0)
            for ligne in self.terrain.acc_grille():
                for elt in ligne:
                    if isinstance(elt, module_personnage.Personnage):
                        if elt.acc_endommage():
                            elt.mut_endommage()
    
    ######################################################
    ### Monstres :
    ######################################################
    
    def ajouter_tab_monstres(self) :
        '''
        Ajoute des monstres avec des coordonnées aléatoires dans le tableau en fonction de combien de Nuit sont passées.
        '''
        if self.attributs_jeu.acc_temps() == 'Nuit' and self.attributs_jeu.acc_monstre_active() :
            for _ in range(self.attributs_jeu.acc_nombre_tour() // 2) :
                #coordonnées au hasard
                x = random.randint(1, 20)
                y = random.randint(1, 20)
                #tant que la future case n'est pas libre, on rechoisit une case au hasard
                while self.terrain.acc_terrain(x, y) != ' ' :
                    x = random.randint(1, 20)
                    y = random.randint(1, 20)
                self.attributs_jeu.ajouter_monstre(module_personnage.Monstre(x, y, 2, 1))
            
            ##déplacements de chaque monstre du terrain
           # print('oui')
           # print('monstres : ', self.attributs_jeu.acc_tab_monstres())
            for monstre in self.attributs_jeu.acc_tab_monstres() :
                self.terrain.mut_terrain(monstre.acc_x(), monstre.acc_y(), monstre)
            self.attributs_jeu.mut_monstre_active(False)
    
    def deplacer_monstre(self, monstre):
        '''
        déplace le monstre aux nouvelles coordonnées
        : param monstre (Monstre)
        : pas de return
        '''
        prochaines_coordo = monstre.prochaines_coordonnees(self.terrain)
        self.terrain.mut_terrain(monstre.acc_x(), monstre.acc_y(), ' ') #un vide à la place de l'ancienne case
        monstre.deplacer(prochaines_coordo[0], prochaines_coordo[1])
        self.terrain.mut_terrain(monstre.acc_x(), monstre.acc_y(), monstre) #le monstre à sa nouvelle place
    
    def jouer_monstre(self):
        '''
        Déplace chaque monstre sur le plateau et gère leurs attaques.
        '''
        for monstre in self.attributs_jeu.acc_tab_monstres(): # pour chaque monstre sur le plateau
            # Attaque des monstres
            monstre.attaquer(self.terrain) # cherche un ennemi à attaquer à proximité
            if not monstre.attaquer_ennemi_proche() == None: # si une victime est trouvée
                victime = monstre.attaquer_ennemi_proche() #la victime qui est attaquée
                victime.est_attaque('monstre') #la victime perd des pv
                victime.mut_endommage() # blesse la victime
                self.attributs_jeu.mut_attaque_en_cours(True)
                self.attributs_jeu.mut_attaque_temps(0)
            else : # sinon on déplace le monstre
                self.deplacer_monstre(monstre)
                '''
                x, y = monstre.acc_x(), monstre.acc_y() #les coordonnées du monstre
                self.terrain.mut_terrain(x, y, ' ') # remplace l'ancienne position du monstre par une case vide
                self.attributs_jeu.monstres_a_deplacer.append(monstre)
                '''
        
    ######################################################
    ### Fonctions console :
    ######################################################
    
    def partie_commence_console(self) :
        '''
        Ajoute dans la console que l'équipe a changé.
        '''
        self.attributs_jeu.ajouter_console(['La partie commence !', 'noir'])
    
    def equipe_console(self, equipe) :
        '''
        Ajoute dans la console que l'équipe a changé.
        '''
        self.attributs_jeu.ajouter_console(['À l\'équipe ' + str(equipe) + ' de jouer !', 'noir'])
    
    def deplacement_console(self, perso) :
        '''
        Ajoute dans la console que le personnage (passé en paramètre) s'est déplacé.
        '''
        self.attributs_jeu.ajouter_console([str(perso.acc_personnage()) + ' s\'est déplacé.', perso.acc_equipe()])
        
    def attaque_console(self, perso_qui_attaque, perso_qui_subit) :
        '''
        Ajoute dans la console que le personnage attaque un personnage de l'équipe adverse.
        '''
        self.attributs_jeu.ajouter_console([str(perso_qui_attaque.acc_personnage()) + ' a attaqué ' + str(perso_qui_subit.acc_personnage()) + '.', perso_qui_attaque.acc_equipe()])
    
    ######################################################
    ### Evenements pendant une partie :
    ######################################################
    
    def effacer_actions(self) :
        '''
        Efface les indications d'attaques ou de déplacements
        '''
        self.attributs_jeu.mut_deplacements([]) # enleve les déplacements
        self.attributs_jeu.mut_deplacements_cavalier([])
        self.attributs_jeu.mut_attaques([]) # enleve les attaques
    
    def changer_personnage(self, selection) :
        '''
        Enlève le personnage selectionné et donc le change.
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
        Change l'équipe en cours
        '''
        dic_equipes = {'bleu' : 'rouge', 'rouge' : 'bleu'}
        self.attributs_jeu.mut_equipe_en_cours(dic_equipes[self.attributs_jeu.acc_equipe_en_cours()])
        self.effacer_actions()
        self.changer_personnage(' ') #rien en selection
        self.attributs_jeu.mut_nombre_action(0)
        self.attributs_jeu.mut_nombre_tour(1)
        self.equipe_console(self.attributs_jeu.acc_equipe_en_cours())
        
    def personnages_sont_mort(self):
        '''
        Vérifie si un personnage est mort. Si c'est le cas, supprime le
        '''
        for personnage in self.attributs_jeu.acc_tab_personnages() + self.attributs_jeu.acc_tab_monstres()  :
            
            if isinstance(personnage, module_personnage.Personnage) and personnage.est_mort():
                if personnage.personnage != 'monstre' :
                    if personnage.personnage == 'geant':
                        if personnage.numero_geant == 0:
                            self.attributs_jeu.mut_positions_tombes((personnage.acc_x() * 38 + 269, personnage.acc_y() * 38 + 19))
                    else :
                        self.attributs_jeu.mut_positions_tombes((personnage.acc_x() * 38 + 250, personnage.acc_y() * 38))
                try :
                    self.attributs_jeu.supprimer_personnage(personnage)
                    #pour ressusciter
                    if personnage.acc_equipe() == 'bleu':
                        self.attributs_jeu.mut_dernier_personnage_mort_bleu(personnage)
                    else:
                        self.attributs_jeu.mut_dernier_personnage_mort_rouge(personnage)
                except :
                    self.attributs_jeu.supprimer_monstre(personnage)
                self.terrain.mut_terrain(personnage.acc_x(), personnage.acc_y(), ' ')
                    
    def est_fini(self):
        '''
        Renvoie True s'il reste que des personnages d'une même équipe, False sinon
        return boolean
        '''
        bleu_present = False
        rouge_present = False
        y = 0
        while not (bleu_present and rouge_present) and y < len(self.terrain.acc_grille()):
            x = 0
            while not (bleu_present and rouge_present) and x < len(self.terrain.acc_grille()[y]):    
                perso = self.terrain.acc_terrain(x, y)
                if isinstance(perso, module_personnage.Personnage):      
                    if perso.acc_equipe() == 'bleu' :
                        bleu_present = True
                    else :
                        rouge_present = True
                x += 1
            y += 1
                 
        self.attributs_jeu.mut_partie_terminee(not (bleu_present and rouge_present)) 
        equipe_qui_gagne = self.qui_gagne(bleu_present, rouge_present)    
        try :
            self.attributs_jeu.mut_equipe_gagnante(equipe_qui_gagne)
        except :
            pass
        return self.attributs_jeu.acc_partie_terminee() 
    
    def qui_gagne(self, bleu_present, rouge_present) :
        '''
        Renvoie l'équipe qui a gagné 
        : params
            bleu_present (bool)
            rouge_present (bool)
        : return (str)
        '''
        gagnant = None
        if bleu_present and not rouge_present :
            gagnant = 'bleu'
        elif not bleu_present and rouge_present :
            gagnant = 'rouge'
        return gagnant
        
    ######################################################
    ### Fonctions Clique :
    ###################################################### 
    
    def est_clique(self):
        '''
        deroule les fonctions deplacement_est_clique et attaque_est_clique correctement
        '''
        if not (self.deplacement_est_clique() or self.attaque_est_clique()) : #Si aucun déplacement ou attaque a été éffectué, alors :
            self.personnage_est_selectionne() #Change de personnage par celui au coordonnées de la souris (si c'est un personnage !).
        
    def deplacement_est_clique(self):
        '''
        déplace le personnage en question sur ce cercle selon si il est "normal" ou si il est un geant.
        : return (bool) True si un deplacement a été effectué, False sinon
        '''
        position_case = self.clavier_souris.acc_position_case()
        #Si la souris est dans un cercle de déplacement :
        if self.attributs_jeu.est_meme_equipe() and position_case in self.attributs_jeu.acc_deplacements():
            
            #Si le personnage est un Géant :
            if self.attributs_jeu.acc_selection().acc_personnage() == 'geant':
                self.deplacer_geant(position_case[0], position_case[1])
            
            #Sinon (si le personnage est "normal")
            else:
                self.deplacer(position_case[0], position_case[1])
            
            self.deplacement_console(self.attributs_jeu.acc_selection())
            self.effacer_actions()
            self.attributs_jeu.mut_nombre_action(self.attributs_jeu.acc_nombre_action() + 1)
            self.jouer_monstre() #on fait jouer les monstres
            rep = True  
        else :
            rep = False
        return rep
            
    def attaque_est_clique(self):
        '''
        attaque le personnage en question selon si il est "normal" ou si il est un geant.
        : return (bool) True si une attaque a été effectuée, False sinon
        '''
        position_case = self.clavier_souris.acc_position_case()  
        if 0 <= position_case[0] <= 20 and 0 <= position_case[1] <= 20 :
            personnage_qui_subit = self.terrain.acc_terrain(position_case[0], position_case[1])
            
            
            #Si la souris est dans une case d'attaque :
            if position_case in self.attributs_jeu.acc_attaques() and personnage_qui_subit.acc_equipe() != self.attributs_jeu.acc_equipe_en_cours():
                
                #Si le personnage_qui_subit est le Géant :
                if personnage_qui_subit.acc_personnage() == 'geant':
                    if personnage_qui_subit.acc_equipe() == 'rouge' : #géant rouge
                        famille = self.famille_geant_rouge
                    else:
                        famille = self.famille_geant_bleu
                    for geant in famille : #pour chaque partie du géant
                        geant.est_attaque(self.attributs_jeu.acc_selection().acc_personnage())
                        geant.mut_endommage()
                        self.attributs_jeu.mut_attaque_en_cours(True)
                        self.attributs_jeu.mut_attaque_temps(0)
                        
                #Sinon (si le personnage est "normal")
                else :
                    personnage_qui_subit.est_attaque(self.attributs_jeu.acc_selection().acc_personnage())
                    personnage_qui_subit.mut_endommage()
                    self.attributs_jeu.mut_attaque_en_cours(True)
                    self.attributs_jeu.mut_attaque_temps(0)
                
                self.attaque_console(self.attributs_jeu.acc_selection(), personnage_qui_subit)
                self.changer_personnage(' ')
                self.attributs_jeu.mut_nombre_action(self.attributs_jeu.acc_nombre_action() + 1)
                self.jouer_monstre() #on fait jouer les monstres
                rep = True
            else :
                rep = False
            return rep

    def personnage_est_selectionne(self):
        '''
        Si un personnage est cliqué et qu'il est dans l'équipe qui joue, 
        alors calculs ces déplacements et ces attaques qui sont possibles.
        Sinon, on fait rien.
        '''
        position_case = self.clavier_souris.acc_position_case()
        if 0 <= position_case[0] <= 20 and 0 <= position_case[1] <= 20:
            selection = self.terrain.acc_terrain(position_case[0], position_case[1])
            self.changer_personnage(selection)
            
    def coffre_est_clique(self):
        '''
        si un coffre est cliqué et qu'il y a un joueur de l'équipe en cours autour du coffre, celui-ci s'ouvre
        : pas de return
        '''
        #vérification d'un joueur autour
        coffre = self.attributs_jeu.acc_coffre_selection()
        if not coffre.acc_est_ouvert(): #si le coffre n'a pas été ouvert
            alentour = coffre.alentour()
            present = False
            i = 0
            while not present and i < len(alentour):
                perso = self.terrain.acc_terrain(alentour[i][0], alentour[i][1])
                if isinstance(perso, module_personnage.Personnage): #si il y a un personnage
                    present = perso.acc_equipe() == self.attributs_jeu.acc_equipe_en_cours() #si un personnage de l'équipe en cours est à côté du coffre
                i += 1
            #si oui, ouverture du coffre
            if present :
                coffre.ouverture()
                self.ouverture_coffre(coffre)
                
    ########################################################
    #### Fonction Coffre :
    ########################################################
            
    def ouverture_coffre(self, coffre):
        '''
        réalise la bonne action en fonction du contenu du coffre
        : coffre (Coffre)
        '''
        self.attributs_jeu.mut_annonce_coffre(True)
        self.attributs_jeu.event_coffre = coffre.acc_contenu()
        
        ########################################################
        #### BONUS DE VIE POUR LE PERSONNAGE
        ########################################################
        
        if coffre.acc_contenu() == 1 :
            perso = self.attributs_jeu.acc_selection() #le personnage sélectionné
            perso.mut_pv(perso.acc_pv() + 10) #on augmente de 10 les pv du personnage
            
        ########################################################
        #### CHANGEMENT DE PERSONNAGE (aléatoire pour l'instant)
        ########################################################
        
        elif coffre.acc_contenu() == 3 :
            perso = self.attributs_jeu.acc_selection()
            personnages_plateau = ['monstre', 'mage', 'paladin', 'geant', 'sorciere', 'valkyrie', 'archere', 'poulet', 'cavalier', 'cracheur de feu', 'ivrogne', 'barbare']
            personnages_plateau.remove(perso.acc_personnage()) #il ne faut pas que le nouveau personnage soit l'ancien
            perso.mut_personnage(random.choice(personnages_plateau)) #on remplace au hasard le personnage
        
        ########################################################
        #### AUGMENTATION DES DEGATS DU PERSONNAGE
        ########################################################
        elif coffre.acc_contenu() == 5 :
            perso = self.attributs_jeu.acc_selection().acc_personnage() #le personnage sélectionné
            nouvelle_attaque = module_personnage.DIC_ATTAQUES[perso] + 5 #les nouveaux pv de dommage du personnage
            module_personnage.mut_dic_attaques(perso, nouvelle_attaque) #on change dans le dictionnaire
            
        ########################################################
        #### RESSUSCITATION DU DERNIER PERSONNAGE MORT
        ########################################################
        
        elif coffre.acc_contenu() == 8:
            #récupération du dernier personnage mort de la bonne équipe
            if self.attributs_jeu.acc_equipe_en_cours() == 'bleu':
                perso = self.attributs_jeu.acc_dernier_personnage_mort_bleu()
            else:
                perso = self.attributs_jeu.acc_dernier_personnage_mort_rouge()
            #ressuscitation du personnage
            if not perso == None :
                #si la case n'est pas libre
                if not self.terrain.est_possible(perso.acc_x(), perso.acc_y()) :
                    case = self.terrain.trouver_case_libre_proche(perso.acc_x(), perso.acc_y()) #on trouve une nouvelle case libre proche
                    perso.mut_pv(module_personnage.DIC_PV[perso.acc_personnage()]) #on réinitialise ses pv
                    print(case)
                    perso.deplacer(case[0], case[1]) #on change les coordonnées du personnage
                    self.attributs_jeu.ajouter_personnage(perso)
                #on ajoute le personnage ressuscité au terrain
                self.terrain.mut_terrain(perso.acc_x(), perso.acc_y(), perso)
            else :
                print('oups, pas de dernier perso mort ...')
     
    ######################################################
    ### Boutons :
    ######################################################  
          
    def deselectionner_bouton(self):
        '''
        Déséléctionne un bouton après 0.3 secondes et lance l'action du bouton
        '''
        if self.attributs_jeu.acc_bouton_clique() != None and time.time() - self.attributs_jeu.acc_temps_appui_bouton() > 0.3:
            
            if self.attributs_jeu.acc_bouton_clique() == 'jouer':
                self.placer()
                self.attributs_jeu.mut_menu(False) #Lance le jeu
                
            elif self.attributs_jeu.acc_bouton_clique() == 'quitter':
                self.attributs_jeu.mut_continuer(False)
                
            elif self.attributs_jeu.acc_bouton_clique() == 'rejouer':
                self.__init__()# faire redémarrer le jeu
                
            elif self.attributs_jeu.acc_bouton_clique() == 'sauvegarder':
                phrase = self.sauvegarde.sauvegarder()
                self.attributs_jeu.ajouter_console([phrase, "noir"])
            
            elif self.attributs_jeu.acc_bouton_clique() == 'charger':
                
                phrase = self.sauvegarde.charger()

                if phrase != "Erreur de Chargement !" :
                    self.clavier_souris = module_clavier_souris.Clavier_Souris(self.attributs_jeu)
                    self.terrain = module_terrain.Terrain(self.attributs_jeu, self.clavier_souris)
                    self.affichage = module_afficher.Affichage(self.attributs_jeu, self.terrain, self.ecran, self.clavier_souris)
                    self.attributs_jeu.console = module_lineaire.Pile()
                    self.placer()
                    
                self.attributs_jeu.ajouter_console([phrase, "noir"])
                
                
            elif self.attributs_jeu.acc_bouton_clique() == 'quitter_fin':
                self.attributs_jeu.mut_continuer(False)
                
            elif self.attributs_jeu.acc_bouton_clique() == 'quitter_menu':
                self.attributs_jeu.mut_continuer(False)
                
            elif self.attributs_jeu.acc_bouton_clique() == 'option':
                print('option')
                self.attributs_jeu.mut_option(True)
                
            elif self.attributs_jeu.acc_bouton_clique() == 'quitter_option':
                print('quitter_option')
                self.attributs_jeu.mut_option(False)
                
            self.attributs_jeu.mut_bouton_clique(None)
          
    ######################################################
    ### Fonction Boucle :
    ######################################################

    def boucle(self) :
        '''
        Ici on effectue tous les calculs et affichages nécessaires au jeu.
        '''
        while self.attributs_jeu.acc_continuer() :
            
            self.attributs_jeu.mut_compteur((self.attributs_jeu.acc_compteur() + 1) % 70)  # Quand le compteur arrive à 70, il repart à 0 règle a vitesse d'animation des personnages
            
            ######################################################
            ### Menu :
            ######################################################
            
            self.arreter_animation()
            if self.attributs_jeu.acc_menu() :
                
                ######################################################
                ### Clavier / Souris :
                ######################################################
                
                for evenement in pygame.event.get() :
                    self.clavier_souris.inputs_menu(evenement)

                ######################################################
                ### Calculs :
                ######################################################
                    
                
                    
                ######################################################
                ### Affichage :
                ######################################################

                self.affichage.afficher_menu()
            
            ######################################################
            ### Jeu :
            ######################################################
            
            if self.attributs_jeu.acc_menu() == False :
                
                #Si pas de déplacement de personnage :
                if not self.attributs_jeu.acc_deplacement_en_cours() and not self.attributs_jeu.acc_attaque_en_cours() :
                    self.personnages_sont_mort()
                    self.est_fini()
                    
                    #Change d'équipe au bout de 3 actions
                    if self.attributs_jeu.acc_nombre_action() == 3 :
                        self.changer_equipe()
                
                ######################################################
                ### Clavier / Souris :
                ######################################################
                
                for evenement in pygame.event.get() :
                    self.clavier_souris.inputs_jeu(evenement)
                    
                    if self.clavier_souris.acc_appuye() and not self.attributs_jeu.acc_partie_terminee() and not self.attributs_jeu.acc_deplacement_en_cours() and not self.attributs_jeu.acc_attaque_en_cours():
                        
                ######################################################
                ### Déroulement du jeu :
                ######################################################
                        
                        #Si un personnage est déjà selectionné :
                        if isinstance(self.attributs_jeu.acc_selection(), module_personnage.Personnage) :
                            self.est_clique()
                            #Si un coffre est sélectionné
                            if self.attributs_jeu.acc_coffre_selection() is not None :
                                print('coffre cliqué !')
                                self.coffre_est_clique()
                                self.attributs_jeu.mut_coffre_selection(None) #plus de coffre séléctionné
                                
                        #Sinon sélection un personnage :
                        else :
                            self.personnage_est_selectionne()
                            
                        
                
                self.attributs_jeu.enlever_console()
                self.ajouter_tab_monstres()
                
                ######################################################
                ### Affichage :
                ######################################################
                
                self.attributs_jeu.mut_temps_jeu() #modifie le jour quand le temps est venu
                self.affichage.afficher_jeu()

            ### désélectionne le bouton après 0.3 secondes
            self.deselectionner_bouton()
            
            ###### gère le temps d'animation des attaques
            self.gerer_animations_attaques()
            
            
            ######################################################
            ### Fréquence de 60 images par seconde :
            ###################################################### 
            pygame.display.flip()
            self.acc_horloge().tick(30)
        
        #Ferme la fenêtre Pygame :
        pygame.quit()
        
    ######################################################
    ### Initialisation du Jeu et de la fenêtre :
    ######################################################
        
    def jouer(self):
        '''
        Initialise la fenêtre et lance le jeu avec un taux de 60 rafraîchissements/calculs par seconde.
        '''
        pygame.init() #Initialise Pygame 
        pygame.display.set_caption('Medieval Heroes')
        pygame.mouse.set_visible(False)
        self.boucle()