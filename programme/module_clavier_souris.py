# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Clavier_Souris.

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''

######################################################
### Importation Modules :
######################################################

import pygame, time

######################################################
### Classe Affichage :
######################################################

class Clavier_Souris() :
    '''
    Une classe Clavier_Souris qui gére les inputs du clavier et de la souris.
    '''
    
    def __init__(self, attributs_jeu) :
        '''
        Initialise les attributs pour gérer les inputs
        :param attributs_jeu (Attributs_Jeu) module
        '''
        #Attributs des Importations :
        self.attributs_jeu = attributs_jeu

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
    ### Différents Inputs (Quitter / Menu / Jeu) :
    ######################################################
        
    def quitter(self, evenement) :
        '''
        Permet de quitter le jeu.
        : param evenement (input)
        '''
        #Croix Rouge :
        if evenement.type == pygame.QUIT :
            self.attributs_jeu.mut_continuer(False)

        #Echap :
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_ESCAPE:
                self.attributs_jeu.mut_continuer(False)
                

    def inputs_menu(self, evenement) :
        '''
        Contrôle les inputs du clavier et de la souris et qui donne les actions demandées dans le menu.
        : param evenement (input)
        '''
        position_curseur = self.acc_position_curseur()
        
        #Permet de fermer la fenêtre pygame :
        self.quitter(evenement)

        #Bouton Souris :
        if evenement.type == pygame.MOUSEBUTTONDOWN : #Appuyé

            #Clique gauche :
            if evenement.button == 1 :
                self.appuye = True

                #Si l'état des boutons n'est pas appuyé :
                if self.attributs_jeu.acc_bouton_clique() == None :
                    
                    if not self.attributs_jeu.acc_option() :
                        
                        #Si la position de la souris est sur le bouton 'Jouer' :
                        if 450 <= position_curseur[0] <= 850 and 340 < position_curseur[1] < 405 :
                            self.attributs_jeu.mut_bouton_clique('jouer')
                            self.attributs_jeu.mut_temps_appui_bouton(time.time())
                            
                        if 450 <= position_curseur[0] <= 850 and 420 < position_curseur[1] < 485 :
                            self.attributs_jeu.mut_bouton_clique('option')
                            self.attributs_jeu.mut_temps_appui_bouton(time.time())
                            
                        if 450 <= position_curseur[0] <= 850 and 500 < position_curseur[1] < 570 :
                            self.attributs_jeu.mut_bouton_clique('quitter_menu')
                            self.attributs_jeu.mut_temps_appui_bouton(time.time())
                            
                        
                        
                    #Option :    
                    else :
                        
                        if 515 <= position_curseur[0] <= 753 and 650 < position_curseur[1] < 715 :
                            self.attributs_jeu.mut_bouton_clique('quitter_option')
                            self.attributs_jeu.mut_temps_appui_bouton(time.time())
                        

        if evenement.type == pygame.MOUSEBUTTONUP : #Relaché
            self.mut_appuye(False)

    def inputs_jeu(self, evenement) :
        '''
        Contrôle les inputs du clavier et de la souris et qui donne les actions demandées dans le jeu.
        : param evenement (input)
        '''
        position_curseur = self.acc_position_curseur()
        position_case = self.acc_position_case()
        
        #Permet de fermer la fenêtre pygame :
        self.quitter(evenement)
        
        #Boutons Souris :
        if evenement.type == pygame.MOUSEBUTTONDOWN : #Appuyé

            #Clique gauche :
            if evenement.button == 1 :
                self.appuye = True
                
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
                        
                        #si le joueur clique sur le bouton 'Sauvergarder' :
                        if 585 < position_curseur[1] < 650 :
                            self.attributs_jeu.mut_bouton_clique('sauvegarder')
                            self.attributs_jeu.mut_temps_appui_bouton(time.time())
                            
                    if 465 <= position_curseur[0] <= 795 and self.attributs_jeu.partie_terminee :
                        if self.attributs_jeu.position_y_menu_fin + 230 < position_curseur[1] < self.attributs_jeu.position_y_menu_fin + 295 :
                            self.attributs_jeu.mut_bouton_clique('rejouer')
                            self.attributs_jeu.mut_temps_appui_bouton(time.time())

                        if self.attributs_jeu.position_y_menu_fin + 310 < position_curseur[1] < self.attributs_jeu.position_y_menu_fin + 375 :
                            self.attributs_jeu.mut_bouton_clique('quitter_fin')
                            self.attributs_jeu.mut_temps_appui_bouton(time.time())

                #Test Print :
                print(self.acc_position_case())
                print(self.acc_position_curseur()[0], self.acc_position_curseur()[1])

        if evenement.type == pygame.MOUSEBUTTONUP : #Relaché
            self.appuye = False