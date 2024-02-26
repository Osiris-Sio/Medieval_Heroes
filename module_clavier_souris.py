# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Clavier_Souris.

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''

######################################################
### Importation Modules :
######################################################

import pygame, module_personnage, time

######################################################
### Classe Affichage :
######################################################

class Clavier_Souris() :
    '''
    Une classe Clavier_Souris qui gère les entrées du clavier et de la souris.
    '''
    
    def __init__(self, jeu, attributs_jeu, terrain) :
        '''
        Initialise les attributs pour gérer les entrées.
        :params 
            jeu (module_jeu.Jeu)
            attributs_jeu (module.attributs_jeu.Attributs_Jeu)
            terrain (module_terrain.Terrain)
        '''
        #Attributs des Paramètres :
        self.jeu = jeu
        self.attributs_jeu = attributs_jeu
        self.terrain = terrain

        #Autres Attributs :
        self.appuye = False
        
    ######################################################
    ### Accesseurs :
    ######################################################
        
    def acc_appuye(self):
        '''
        Renvoie l'attribut appuye
        '''
        return self.appuye
    
    def acc_position_curseur(self):
        '''
        Renvoie la position de la souris dans le terrain en pixel.
        :return (tuple)
        '''
        return pygame.mouse.get_pos()

    def acc_position_case(self):
        '''
        Renvoie la position de la souris dans le terrain en tuple de case.
        '''
        position_curseur = self.acc_position_curseur()
        return (round(((position_curseur[0] + 25) // 38) - 7), round(position_curseur[1] // 38))
    
    ######################################################
    ### Mutateurs :
    ######################################################

    def mut_appuye(self, valeur) :
        '''
        Modifie l'attribut appuye
        : param valeur (boolean) True ou False
        : pas de return, modifie l'attribut nb_deplacements_attaques
        '''
        #Assertion :
        assert isinstance(valeur, bool), "Le paramètre doit être un boolean (True ou False)"
        #Code :
        self.appuye = valeur
        
    ######################################################
    ### Fonctions Clique :
    ###################################################### 
    
    def est_clique(self):
        '''
        Déroule les fonctions deplacement_est_clique et attaque_est_clique correctement
        '''
        #Si aucun déplacement ou attaque a été effectué, alors change de personnage par celui au coordonnées de la souris (si c'est un personnage !) :
        if not (self.jeu.deplacement_est_clique() or self.jeu.attaque_est_clique()) : 
            self.personnage_est_selectionne()

    def personnage_est_selectionne(self):
        '''
        Si un personnage est cliqué, alors calculs ces déplacements et ces attaques qui sont possibles.
        Sinon, on fait rien.
        '''
        position_case = self.acc_position_case()
        
        #Si la case cliqué est sur le terrain :
        if 0 <= position_case[0] <= 20 and 0 <= position_case[1] <= 20:
            selection = self.terrain.acc_terrain(position_case[0], position_case[1]) #Selectionne le personnage de la case
            self.jeu.changer_personnage(selection) #Change le personnage.
        
    ######################################################
    ### Différents Boutons :
    ######################################################
    
    def boutons_option(self) :
        '''
        Gère les différents boutons du menu.
        '''
        position_curseur = self.acc_position_curseur()
        
        #Si la position de la souris est sur le bouton 'Quitter' :
        if 515 <= position_curseur[0] <= 753 and 650 < position_curseur[1] < 715 :
            self.attributs_jeu.mut_bouton_clique('quitter_option')
            self.attributs_jeu.mut_temps_appui_bouton(time.time())
    
    def boutons_menu(self) :
        '''
        Gère les différents boutons du menu.
        '''
        position_curseur = self.acc_position_curseur()
        
        #Si l'état des boutons n'est pas appuyé :
        if self.attributs_jeu.acc_bouton_clique() == None :
            
            #Si le joueur n'est pas dans les options :
            if not self.attributs_jeu.acc_option() :
                
                #Si le joueur est dans la zone verticale des boutons :
                if 450 <= position_curseur[0] <= 850 :
                
                    #Si la position de la souris est sur le bouton 'Jouer' :
                    if 340 < position_curseur[1] < 405 :
                        self.attributs_jeu.mut_bouton_clique('jouer')
                        self.attributs_jeu.mut_temps_appui_bouton(time.time()) 
                    
                    #Si la position de la souris est sur le bouton 'Option' :
                    if 420 < position_curseur[1] < 485 :
                        self.attributs_jeu.mut_bouton_clique('option')
                        self.attributs_jeu.mut_temps_appui_bouton(time.time())
                    
                    #Si la position de la souris est sur le bouton 'Quitter' :
                    if 500 < position_curseur[1] < 570 :
                        self.attributs_jeu.mut_bouton_clique('quitter_menu')
                        self.attributs_jeu.mut_temps_appui_bouton(time.time())
            
            #Sinon, le joueur est dans le menu option :
            else :
                self.boutons_option()
                
    def boutons_jeu(self) :
        '''
        Gère les différents boutons du jeu.
        '''
        position_curseur = self.acc_position_curseur()
        
        #Si l'état des boutons n'est pas appuyé :
        if self.attributs_jeu.acc_bouton_clique() == None :
            
            #Si le joueur clique dans la zone des boutons de gauche du jeu :
            if 1056 <= position_curseur[0] <= 1294 : 
                
                #Si le joueur clique sur le bouton 'Quitter' :
                if 725 < position_curseur[1] < 790 :
                    self.attributs_jeu.mut_bouton_clique('quitter')
                    self.attributs_jeu.mut_temps_appui_bouton(time.time())
                    self.attributs_jeu.mut_continuer(False)
                
                #Si le joueur clique sur le bouton 'Charger' :
                if 655 < position_curseur[1] < 720 : 
                    self.attributs_jeu.mut_bouton_clique('charger')
                    self.attributs_jeu.mut_temps_appui_bouton(time.time())
                
                #si le joueur clique sur le bouton 'Sauvegarder' :
                if 585 < position_curseur[1] < 650 :
                    self.attributs_jeu.mut_bouton_clique('sauvegarder')
                    self.attributs_jeu.mut_temps_appui_bouton(time.time())
                    
            #Si la partie est fini :
            if self.attributs_jeu.acc_partie_terminee() :

                    #Si le joueur clique dans la zone des boutons de fin (verticale) :
                    if 465 <= position_curseur[0] <= 795 :
                        
                        #Si le joueur clique sur le bouton 'Rejouer' :
                        if self.attributs_jeu.acc_position_y_menu_fin() + 230 < position_curseur[1] < self.attributs_jeu.acc_position_y_menu_fin() + 295 :
                            self.attributs_jeu.mut_bouton_clique('rejouer')
                            self.attributs_jeu.mut_temps_appui_bouton(time.time())
                        
                        #Si le joueur clique sur le bouton 'Quitter' :
                        if self.attributs_jeu.position_y_menu_fin + 310 < position_curseur[1] < self.attributs_jeu.position_y_menu_fin + 375 :
                            self.attributs_jeu.mut_bouton_clique('quitter_fin')
                            self.attributs_jeu.mut_temps_appui_bouton(time.time())

    ######################################################
    ### Différentes Entrées (Quitter / Menu / Jeu) :
    ######################################################
        
    def quitter(self, evenement) :
        '''
        Permet de quitter le jeu.
        : param evenement (input)
        '''
        #Croix Rouge :
        if evenement.type == pygame.QUIT :
            self.attributs_jeu.mut_continuer(False) #Arrête la boucle du jeu

        #Echap :
        if evenement.type == pygame.KEYDOWN : #Si c'est une touche :
            if evenement.key == pygame.K_ESCAPE : #Si c'est la touche "Echap" :
                self.attributs_jeu.mut_continuer(False) #Arrête la boucle du jeu
                
    def entrees_deroulement_jeu(self) :
        '''
        Gère les différentes entrées en lien avec la partie.
        C'est à dire la selection d'un personnage
        '''
        #Si la partie n'est pas terminée, qu'il n'y a aucun déplacement en cours et qu'il n'y a aucune attaque en cours :
        if not self.attributs_jeu.acc_partie_terminee() and not self.attributs_jeu.acc_deplacement_en_cours() and not self.attributs_jeu.acc_attaque_en_cours():
                        
            #Si un personnage est déjà sélectionné :
            if isinstance(self.attributs_jeu.acc_selection(), module_personnage.Personnage) :
                self.est_clique()
                
                #Si un coffre est sélectionné avec un personnage :
                if self.attributs_jeu.acc_coffre_selection() is not None :
                    self.jeu.coffre_est_clique()
                    self.attributs_jeu.mut_coffre_selection(None) #Plus aucun coffre est sélectionné
                    
            #Sinon sélection un personnage :
            else :
                self.personnage_est_selectionne()

    def entrees_menu(self, evenement) :
        '''
        Contrôle les entrées du clavier et de la souris et qui donne les actions demandées dans le menu.
        :param evenement (input)
        '''
        #Permet de fermer la fenêtre pygame :
        self.quitter(evenement)

        #Si un des bouton de la souris est appuyé :
        if evenement.type == pygame.MOUSEBUTTONDOWN :

            #Si le clique gauche est appuyé :
            if evenement.button == 1 :
                
                self.mut_appuye(True) #Appuyé est "activé"
                self.boutons_menu() #Vérifie si c'est un bouton du menu (ou du menu option en particulier)      
                        
        # Sinon, les boutons de la souris sont relâché :
        else :
            self.mut_appuye(False) #Appuyé est "désactivé"

    def entrees_jeu(self, evenement) :
        '''
        Contrôle les entrées du clavier et de la souris et qui donne les actions demandées dans le jeu.
        : param evenement (input)
        '''
        position_curseur = self.acc_position_curseur()
        position_case = self.acc_position_case()
        
        #Permet de fermer la fenêtre pygame :
        self.quitter(evenement)
        
        #Si un des bouton de la souris est appuyé :
        if evenement.type == pygame.MOUSEBUTTONDOWN : 

            #Si le clique gauche est appuyé :
            if evenement.button == 1 :
                
                self.mut_appuye(True) #Appuyé est "activé"
                self.boutons_jeu() #Vérifie si c'est un bouton du jeu
                self.entrees_deroulement_jeu()
                
        # Sinon, les boutons de la souris sont relâché :
        else :
            self.mut_appuye(False) #Appuyé est "désactivé"