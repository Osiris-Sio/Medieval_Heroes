# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Clavier_Souris.

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''

######################################################
### Importation Modules :
######################################################

import pygame, module_jeu, module_attributs_jeu, module_sauvegarde, module_terrain, module_personnage, time

######################################################
### Classe Affichage :
######################################################

class Clavier_Souris() :
    '''
    Une classe Clavier_Souris qui gère les entrées du clavier et de la souris.
    '''
    
    def __init__(self, jeu, attributs_jeu, sauvegarde, terrain) :
        '''
        Initialise les attributs pour gérer les entrées.
        :params 
            jeu (module_jeu.Jeu)
            attributs_jeu (module.attributs_jeu.Attributs_Jeu)
            terrain (module_terrain.Terrain)
        '''
        #Assertions :
        assert isinstance(jeu, module_jeu.Jeu), 'jeu doit être de la classe Jeu du module_jeu !'
        assert isinstance(attributs_jeu, module_attributs_jeu.Attributs_Jeu), 'attributs_jeu doit être de la classe Attributs_Jeu du module_attributs_jeu !'
        assert isinstance(sauvegarde, module_sauvegarde.Sauvegarde), 'terrain doit être de la classe Terrain du module_terrain !'
        assert isinstance(terrain, module_terrain.Terrain), 'terrain doit être de la classe Terrain du module_terrain !'
        
        #Attributs des Paramètres :
        self.jeu = jeu
        self.attributs_jeu = attributs_jeu
        self.sauvegarde = sauvegarde
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
        Si un personnage est cliqué, alors calculs ses déplacements et ses attaques qui sont possibles
        Sinon, on fait rien
        '''
        position_case = self.acc_position_case()
        
        #Si la case cliqué est sur le terrain :
        if 0 <= position_case[0] <= 20 and 0 <= position_case[1] <= 20:
            selection = self.terrain.acc_terrain(position_case[0], position_case[1]) #Selectionne le personnage de la case
            self.jeu.changer_personnage(selection) #Change le personnage.
            
    def potion_est_clique(self, equipe_en_cours, equipe_perso):
        '''
        si une potion est cliquée, change la sélection
        : params
            equipe_en_cours (str), 'rouge' ou 'bleu'
            equipe_perso (str), 'rouge' ou 'bleu'
        : pas de return
        '''
        pos_cur = self.acc_position_curseur()
        if self.appuye : #si le joueur a cliqué sur quelque chose
            ##potion 1
            if 33 <= pos_cur[0] <= 121 and 286 <= pos_cur[1] <= 374 :
                if equipe_en_cours == 'bleu' and equipe_perso == 'bleu':
                    self.attributs_jeu.mut_potion_bleue_selectionnee(1)
                if equipe_en_cours == 'rouge' and equipe_perso == 'rouge':
                    self.attributs_jeu.mut_potion_rouge_selectionnee(1)
            
            ##potion 2
            elif 133 <= pos_cur[0] <= 220 and 286 <= pos_cur[1] <= 373 :
                if equipe_en_cours == 'bleu' and equipe_perso == 'bleu':
                    self.attributs_jeu.mut_potion_bleue_selectionnee(2)
                if equipe_en_cours == 'rouge' and equipe_perso == 'rouge':
                    self.attributs_jeu.mut_potion_rouge_selectionnee(2)
            
            ##potion 3
            elif 22 <= pos_cur[0] <= 117 and 400 <= pos_cur[1] <= 495 :
                if equipe_en_cours == 'bleu' and equipe_perso == 'bleu':
                    self.attributs_jeu.mut_potion_bleue_selectionnee(3)
                if equipe_en_cours == 'rouge' and equipe_perso == 'rouge':
                    self.attributs_jeu.mut_potion_rouge_selectionnee(3)
            
            ##potion 4
            elif 134 <= pos_cur[0] <= 230 and 400 <= pos_cur[1] <= 496 :
                if equipe_en_cours == 'bleu' and equipe_perso == 'bleu':
                    self.attributs_jeu.mut_potion_bleue_selectionnee(4)
                if equipe_en_cours == 'rouge' and equipe_perso == 'rouge':
                    self.attributs_jeu.mut_potion_rouge_selectionnee(4)
                    
        
        
    ######################################################
    ### Différents Boutons :
    ######################################################
    
    def deselectionner_bouton(self):
        '''
        Désélectionne un bouton après 0.3 secondes et lance l'action du bouton
        '''
        #Si le joueur a appuyé sur un bouton et que le temps après avoir appuyé est de 3 secondes :
        if self.attributs_jeu.acc_bouton_clique() != None and time.time() - self.attributs_jeu.acc_temps_appui_bouton() > 0.3:
            
            #Si le bouton est jouer, place les personnage et lance la partie
            if self.attributs_jeu.acc_bouton_clique() == 'jouer':
                self.jeu.placer()
                self.attributs_jeu.mut_menu(False)
                
            #Sinon si le bouton est quitter, ferme la fenêtre pygame en "désactivant" la boucle.
            elif self.attributs_jeu.acc_bouton_clique() == 'quitter':
                self.attributs_jeu.mut_continuer(False)
                
            #Sinon si le bouton est rejouer, réinitialise la classe Jeu du module_jeu.
            elif self.attributs_jeu.acc_bouton_clique() == 'rejouer':
                self.jeu.__init__()
                
            #Sinon si le bouton est sauvegarder, sauvegarde la partie en cours et signale au joueur par phrase dans la console du jeu (Succès ou Échec).
            elif self.attributs_jeu.acc_bouton_clique() == 'sauvegarder':
                phrase = self.sauvegarde.sauvegarder()
                self.attributs_jeu.ajouter_console([phrase, "noir"])
                
            #Sinon si le bouton est charger, charge la partie sélectionné et signale au joueur par phrase dans la console du jeu (Succès ou Échec).
            elif self.attributs_jeu.acc_bouton_clique() == 'charger':
                phrase = self.sauvegarde.charger()
                self.attributs_jeu.ajouter_console([phrase, "noir"])
                
            #Sinon si le bouton est option, ouvre la fenêtre de menu options.
            elif self.attributs_jeu.acc_bouton_clique() == 'option' :
                self.attributs_jeu.mut_option(True)
                
            #Sinon si le bouton est quitter_option, ferme la fenêtre du menu option.
            elif self.attributs_jeu.acc_bouton_clique() == 'retour_menu':
                self.attributs_jeu.mut_option(False)
                
            self.attributs_jeu.mut_bouton_clique(None) #Enlève le bouton sélectionné/cliqué
    
    def boutons_option(self) :
        '''
        Gère les différents boutons du menu.
        '''
        position_curseur = self.acc_position_curseur()
        
        #Si la position de la souris est dans la zone des boutons On/Off :
        if 675 <= position_curseur[0] <= 775 :
            
            #Sols de couleur :
            if 340 < position_curseur[1] < 390 :
                self.attributs_jeu.mut_sols_de_couleur(not self.attributs_jeu.acc_sols_de_couleur())
               
            #Deplacements/Attaques : 
            if 417 < position_curseur[1] < 467 :
                self.attributs_jeu.mut_deplacements_attaques(not self.attributs_jeu.acc_deplacements_attaques())
                
            #Console :
            if 470 < position_curseur[1] < 520 :
                self.attributs_jeu.mut_option_console(not self.attributs_jeu.acc_option_console())
        
        #Si la position de la souris est sur le bouton 'Retour' :
        if 515 <= position_curseur[0] <= 753 and 650 < position_curseur[1] < 715 :
            self.attributs_jeu.mut_bouton_clique('retour_menu')
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
                        self.attributs_jeu.mut_bouton_clique('charger')
                        self.attributs_jeu.mut_temps_appui_bouton(time.time()) 
                    
                    #Si la position de la souris est sur le bouton 'Option' :
                    if 500 < position_curseur[1] < 565 :
                        self.attributs_jeu.mut_bouton_clique('option')
                        self.attributs_jeu.mut_temps_appui_bouton(time.time())
                    
                    #Si la position de la souris est sur le bouton 'Quitter' :
                    if 580 < position_curseur[1] < 645 :
                        self.attributs_jeu.mut_bouton_clique('quitter')
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
            if 10 <= position_curseur[0] <= 248 : 
                
                #Si le joueur clique sur le bouton 'Menu' :
                if 655 < position_curseur[1] < 720 :
                    self.attributs_jeu.mut_bouton_clique('option')
                    self.attributs_jeu.mut_temps_appui_bouton(time.time())
                
                #Si le joueur clique sur le bouton 'Menu' :
                elif 725 < position_curseur[1] < 790 :
                    self.attributs_jeu.mut_bouton_clique('menu')
                    self.attributs_jeu.mut_temps_appui_bouton(time.time())
            
            #Si le joueur clique dans la zone des boutons de droit du jeu :
            elif 1056 <= position_curseur[0] <= 1294 : 
                
                #Si le joueur clique sur le bouton 'Quitter' :
                if 725 < position_curseur[1] < 790 :
                    self.attributs_jeu.mut_bouton_clique('quitter')
                    self.attributs_jeu.mut_temps_appui_bouton(time.time())
                
                #Si le joueur clique sur le bouton 'Charger' :
                elif 655 < position_curseur[1] < 720 : 
                    self.attributs_jeu.mut_bouton_clique('charger')
                    self.attributs_jeu.mut_temps_appui_bouton(time.time())
                
                #si le joueur clique sur le bouton 'Sauvegarder' :
                elif 585 < position_curseur[1] < 650 :
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
                    elif self.attributs_jeu.position_y_menu_fin + 310 < position_curseur[1] < self.attributs_jeu.position_y_menu_fin + 375 :
                        self.attributs_jeu.mut_bouton_clique('quitter')
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
        : param evenement (input)
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