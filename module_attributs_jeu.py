# -*- coding: utf-8 -*-

'''
-> Medieval Heroes : Module pour la classe Attributs_Jeu.

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################

import module_personnage, module_objets
from graphe import module_lineaire

######################################################
### Classe Jeu :
######################################################

class Attributs_Jeu() :
    '''
    Une classe Attributs_Jeu qui gère les attributs importants pour un bon déroulement du jeu avec des accesseurs et des mutateurs principalement.
    '''
    
    def __init__(self) :
        '''
        Initialise les attributs du jeu
        '''
        #Attributs Jeu:
        self.continuer = True #Si la boucle du jeu continue
        self.menu = True #True si on est dans le menu, False sinon
        self.menu_modes = False 
        self.menu_options = False #True si on est dans le menu options, False sinon
        self.compteur = 0 #Compte le nombre de boucle (de 0 à 70) (principalement pour les animations)
        self.tab_personnages = [] #Un tableau avec tous les personnages (qui sont leur pv strictement au dessus de 0)
        self.tab_monstres = [] #Un tableau avec tous les monstres (qui sont leur pv strictement au dessus de 0)
        self.tab_coffres = [] #Un tableau avec tous les coffres (non ouvert)
        self.deplacements = [] #Tableau de tuples (x, y) pour chaque coordonnées des cases de déplacement possible
        self.deplacements_invisibles_cavalier = [] #Tableau de tuples (x, y) pour chaque coordonnées des cases de déplacement possible (seulement pour les cavaliers)
        self.attaques = [] #Tableau de tuples (x, y) pour chaque coordonnées des cases d'attaque possible
        self.selection = ' ' #' ' = Case vide sinon si '#' = Obstacle sinon (autre caractère (str)) un personnage, monstre ou coffre
        self.equipe_en_cours = 'bleu' #Chaine de caractères de l'équipe qui joue
        self.coffre_selection = None #le coffre sélectionné
        
        #Bouton :
        self.bouton_clique = None #Si None, c'est que aucun bouton du jeu ou du menu a été cliqué. Sinon, prend la chaine de caractères correspondante (exemple : Le bouton 'jouer' a été cliqué, alors bouton_cliqué = 'jouer')
        self.temps_appui_bouton = 0 #Le temps passé après qu'un bouton a été cliqué
        
        #Jour/Nuit :
        self.temps = 'Jour' #Le temps du jeu
        self.temps_active = False #Booléen qui permet de bloquer le Jour/Nuit pendant une condition vrai. C'est le cas dans la fonction mut_temps_jeu()
        self.monstres_active = False #True si des monstres doivent apparaître et False sinon
        
        #Mode Robot :
        self.mode_robot = False
        
        #Action/Tour :
        self.nombre_action = 0 #Le nombre d'action qu'une équipe a faite pendant son tour
        self.nombre_tour = 0 #Le nombre de tour passé.
        
        self.dic_alphabet = {
            0 : 'A',
            1 : 'B',
            2 : 'C',
            3 : 'D',
            4 : 'E',
            5 : 'F',
            6 : 'G',
            7 : 'H',
            8 : 'I',
            9 : 'J',
            10 : 'K',
            11 : 'L',
            12 : 'M',
            13 : 'N',
            14 : 'O',
            15 : 'P',
            16 : 'Q',
            17 : 'R',
            18 : 'S',
            19 : 'T',
            20 : 'U'
        }
        
        #Console (pile) :
        self.console = module_lineaire.Pile() #Une pile où sera ajouté des tableaux contenant une phrase et sa couleur pour ensuite l'afficher.
        
        #Options :
        self.sols_de_couleur = True
        self.deplacements_attaques = True
        self.option_console = True
        self.x_pointeur = 625
        
        #Attributs pour le déplacement avec le chemin (graphe) :
        self.chemin = []
        self.coordonnees_personnage = None
        self.personnage_en_deplacement = None
        self.indice_courant = 0
        self.deplacement_en_cours = False
        self.nouvelles_coord = None
        self.nb_actions = 0
        
        #Attributs pour le déplacement des monstres
        self.chemin_monstre = []
        self.coordonnees_monstre = None
        self.monstre_en_deplacement = None
        self.deplacement_en_cours_monstre = False
        self.nouvelles_coord = None
        self.monstres_deja_deplaces = False
        self.monstres_a_deplacer = []
        
        #Attributs pour les attaques :
        self.attaque_en_cours = False
        self.attaque_temps = 0
        
        #Coffre :
        self.dernier_personnage_mort_bleu = None
        self.dernier_personnage_mort_rouge = None
        self.annonce_coffre = False
        self.annonce_coffre_console = True
        self.event_coffre = 0
        
        #Potions :
        self.cases_potions = [] #les cases où les effets de potions s'appliquent
        ####file rouge
        #potion -pv
        f1r = module_lineaire.File()
        f1r.enfiler(module_objets.Potion(1))
        #potion vie
        f2r = module_lineaire.File()
        for _ in range(5):
            f2r.enfiler(module_objets.Potion(2))
        #potion mort
        f3r = module_lineaire.File()
        for _ in range(2):
            f3r.enfiler(module_objets.Potion(3))
        #potion d'équipe
        f4r = module_lineaire.File()
        for _ in range(3):
            f4r.enfiler(module_objets.Potion(4)) 
        ####file bleue
        #potion -pv
        f1b = module_lineaire.File()
        f1b.enfiler(module_objets.Potion(1))
        #potion vie
        f2b = module_lineaire.File()
        for _ in range(5):
            f2b.enfiler(module_objets.Potion(2))
        #potion mort
        f3b = module_lineaire.File()
        for _ in range(2):
            f3b.enfiler(module_objets.Potion(3))
        #potion d'équipe
        f4b = module_lineaire.File()
        for _ in range(3):
            f4b.enfiler(module_objets.Potion(4))
        ##dic
        self.potions_rouges = {1 : f1r, 
                               2 : f2r,
                               3 : f3r,
                               4 : f4r
                               }
        self.potions_bleues = {1 : f1b, 
                               2 : f2b,
                               3 : f3b,
                               4 : f4b
                               }
        self.potion_rouge_selectionnee = 1 #la première file
        self.potion_bleue_selectionnee = 1 #la première file
        
        #Éléments du décor
        self.positions_tombes = [] #Tableau de tuples (x, y) des coordonnées de chaque tombe 
        
        #Fin du jeu
        self.partie_terminee = False #True si la partie est terminée, False sinon 
        self.position_y_menu_fin = 0 #Permet de lier l'animation du fin de jeu et les interactions
        self.equipe_gagnante = None #None si la partie n'est pas terminée, 'bleu' ou 'rouge' (str) pour savoir quelle équipe a gagné.

    ######################################################
    ### Accesseurs :
    ######################################################
    def acc_x_pointeur(self):
        '''
        renvoie l'attribut x_pointeur
        '''
        return self.x_pointeur
        
    def acc_mode_robot(self):
        '''
        Renvoie l'attribut mode_robot
        '''
        return self.mode_robot
    
    def acc_menu_modes(self):
        '''
        Renvoie l'attribut menu_modes
        '''
        return self.menu_modes
    
    def acc_dic_alphabet(self):
        '''
        Renvoie l'attribut dic_alphabet
        '''
        return self.dic_alphabet
    
    def acc_sols_de_couleur(self):
        '''
        Renvoie l'attribut sols_de_couleur
        '''
        return self.sols_de_couleur
    
    def acc_deplacements_attaques(self):
        '''
        Renvoie l'attribut deplacements_attaques
        '''
        return self.deplacements_attaques
    
    def acc_option_console(self):
        '''
        Renvoie l'attribut option_console
        '''
        return self.option_console
    
    def acc_annonce_coffre(self):
        '''
        Renvoie l'attribut annonce_coffre
        '''
        return self.annonce_coffre
    
    def acc_annonce_coffre_console(self):
        '''
        Renvoie l'attribut annonce_coffre_console
        '''
        return self.annonce_coffre_console
    
    def temps_annonce(self):
        '''
        Renvoie l'attribut continuer
        '''
        return self.temps_annonce
    
    def acc_continuer(self):
        '''
        Renvoie l'attribut continuer
        '''
        return self.continuer
    
    def acc_menu(self):
        '''
        Renvoie l'attribut menu
        '''
        return self.menu
    
    def acc_menu_options(self):
        '''
        Renvoie l'attribut menu_options
        '''
        return self.menu_options
    
    def acc_compteur(self):
        '''
        Renvoie l'attribut compteur
        '''
        return self.compteur
    
    def acc_tab_personnages(self):
        '''
        Renvoie l'attribut tab_personnages
        '''
        return self.tab_personnages
    
    def acc_tab_monstres(self):
        '''
        Renvoie l'attribut tab_monstres
        '''
        return self.tab_monstres
    
    def acc_tab_coffres(self):
        '''
        Renvoie l'attribut tab_coffres
        '''
        return self.tab_coffres
    
    def acc_deplacements(self):
        '''
        Renvoie l'attribut deplacements
        '''
        return self.deplacements
    
    def acc_deplacements_cavalier(self):
        '''
        renvoie l'attribut deplacements_affichage_cavalier
        '''
        return self.deplacements_invisibles_cavalier
    
    def acc_attaques(self):
        '''
        Renvoie l'attribut attaques
        '''
        return self.attaques
    
    def acc_selection(self):
        '''
        Renvoie l'attribut selection
        '''
        return self.selection
    
    def acc_coffre_selection(self):
        '''
        renvoie l'attribut coffre_selection
        : return (Coffre)
        '''
        return self.coffre_selection
    
    def acc_equipe_en_cours(self):
        '''
        Renvoie l'attribut equipe_en_cours
        '''
        return self.equipe_en_cours
    
    def acc_bouton_clique(self):
        '''
        Renvoie le bouton cliqué
        '''
        return self.bouton_clique
    
    def acc_temps_appui_bouton(self):
        '''
        Renvoie le temps appui bouton
        '''
        return self.temps_appui_bouton
    
    def acc_temps(self):
        '''
        Renvoie l'attribut temps
        '''
        return self.temps
    
    def acc_temps_active(self):
        '''
        Renvoie l'attribut temps_active
        '''
        return self.temps_active
    
    def acc_monstres_active(self):
        '''
        Renvoie l'attribut monstres_active
        '''
        return self.monstres_active
    
    def acc_nombre_action(self):
        '''
        Renvoie le nombre d'action pendant le tour
        '''
        return self.nombre_action
    
    def acc_nombre_tour(self):
        '''
        Renvoie le nombre d'action pendant le tour
        '''
        return self.nombre_tour
    
    def acc_console(self):
        '''
        Renvoie la pile qui gère la console.
        '''
        return self.console
    
    def acc_chemin(self):
        '''
        Renvoie l'attribut chemin
        '''
        return self.chemin
    
    def acc_chemin_monstre(self):
        '''
        Renvoie l'attribut chemin
        '''
        return self.chemin_monstre
    
    def acc_coordonnees_personnage(self):
        '''
        Renvoie l'attribut coordonnees_personnage
        '''
        return self.coordonnees_personnage
    
    def acc_coordonnees_monstre(self):
        '''
        Renvoie l'attribut coordonnees_personnage
        '''
        return self.coordonnees_monstre
    
    def acc_personnage_en_deplacement(self):
        '''
        Renvoie l'attribut personnage_en_deplacement
        '''
        return self.personnage_en_deplacement
    
    def acc_monstre_en_deplacement(self):
        '''
        Renvoie l'attribut personnage_en_deplacement
        '''
        return self.monstre_en_deplacement
    
    def acc_indice_courant(self):
        '''
        Renvoie l'attribut indice_courant
        '''
        return self.indice_courant
    
    def acc_deplacement_en_cours(self):
        '''
        Renvoie l'attribut deplacement_en_cours
        '''
        return self.deplacement_en_cours
    
    def acc_deplacement_en_cours_monstre(self):
        '''
        Renvoie l'attribut deplacement_en_cours_monstre
        '''
        return self.deplacement_en_cours_monstre
    
    def acc_dernier_personnage_mort_rouge(self):
        '''
        renvoie le dernier_personnage_mort de l'équipe rouge
        : return (Perso)
        '''
        return self.dernier_personnage_mort_rouge
    
    def acc_dernier_personnage_mort_bleu(self):
        '''
        renvoie le dernier_personnage_mort de l'équipe bleue
        : return (Perso)
        '''
        return self.dernier_personnage_mort_bleu
    
    def acc_nouvelles_coord(self):
        '''
        Renvoie l'attribut nouvelles_coord
        '''
        return self.nouvelles_coord
    
    def acc_nb_actions(self):
        '''
        Renvoie l'attribut nb_actions
        '''
        return self.nb_actions
    
    def acc_monstres_deja_deplaces(self):
        '''
        Renvoie l'attribut monstres_deja_deplaces
        '''
        return self.monstres_deja_deplaces
    
    def acc_monstres_a_deplacer(self):
        '''
        Renvoie l'attribut monstres_a_deplacer
        '''
        return self.monstres_a_deplacer
    
    def acc_attaque_en_cours(self):
        '''
        Renvoie l'attribut attaque_en_cours
        '''
        return self.attaque_en_cours
    
    def acc_attaque_temps(self):
        '''
        Renvoie l'attribut attaque_temps
        '''
        return self.attaque_temps
    
    def acc_positions_tombes(self):
        '''
        Renvoie l'attribut positions_tombes
        '''
        return self.positions_tombes
    
    def acc_partie_terminee(self):
        '''
        Renvoie l'attribut partie_terminee
        '''
        return self.partie_terminee
    
    def acc_position_y_menu_fin(self):
        '''
        Renvoie l'attribut position_y_menu_fin
        '''
        return self.position_y_menu_fin
    
    def acc_equipe_gagnante(self):
        '''
        Renvoie l'attribut equipe_gagnante
        '''
        return self.equipe_gagnante
    
    def acc_potions_rouges(self):
        '''
        renvoie l'attribut potions_rouges
        : return (dic)
        '''
        return self.potions_rouges
    
    def acc_potions_bleues(self):
        '''
        renvoie l'attribut potions_bleues
        : return (dic)
        '''
        return self.potions_bleues
    
    def acc_potion_rouge_selectionnee(self):
        '''
        renvoie l'attribut potion_rouge_selectionnee
        : return (module_lineaire.File)
        '''
        return self.potion_rouge_selectionnee
    
    def acc_potion_bleue_selectionnee(self):
        '''
        renvoie l'attribut potion_bleue_selectionnee
        : return (module_lineaire.File)
        '''
        return self.potion_bleue_selectionnee
    ######################################################
    ### Mutateurs :
    ######################################################
    
    def mut_x_pointeur(self, x):
        '''
        modifie le x de l'attribut x_pointeur
        '''
        self.x_pointeur = x
    
    def mut_mode_robot(self, valeur) :
        '''
        Modifie l'attribut mode_robot
        : param valeur (boolean)
        : pas de return, modifie l'attribut mode_robot
        '''
        #Assertion :
        assert isinstance(valeur, bool), 'Le paramètre doit être soit True, soit False !'
        #Code :
        self.mode_robot = valeur
    
    def mut_menu_modes(self, valeur) :
        '''
        Modifie l'attribut menu_modes
        : param valeur (boolean)
        : pas de return, modifie l'attribut menu_modes
        '''
        #Assertion :
        assert isinstance(valeur, bool), 'Le paramètre doit être soit True, soit False !'
        #Code :
        self.menu_modes = valeur
    
    def mut_potion_rouge_selectionnee(self, contenu):
        '''
        modifie l'attribut potion_rouge_selectionnee (on séléctionne une file)
        : contenu (int), catégorie de la potion séléctionnée (1, 2, 3, ou 4)
        : pas de return
        '''
        #assertion
        assert isinstance(contenu, int) and contenu in [1, 2, 3, 4], "le contenu de la potion doit être un entier compris entre 1 et 4 inclus"
        #code
        self.potion_rouge_selectionnee = contenu
        
    def mut_potion_bleue_selectionnee(self, contenu):
        '''
        modifie l'attribut potion_bleue_selectionnee (on séléctionne une file)
        : contenu (int), catégorie de la potion séléctionnée (1, 2, 3, ou 4)
        : pas de return
        '''
        #assertion
        assert isinstance(contenu, int) and contenu in [1, 2, 3, 4], "le contenu de la potion doit être un entier compris entre 1 et 4 inclus"
        #code
        self.potion_bleue_selectionnee = contenu
    
    def mut_ajoute_potions_rouges(self, potion):
        '''
        modifie l'attribut potions_rouges en augmentant ou en baissant le nombre de potions de la potion passée en paramètre
        : params
            potion (Potion)
        : pas de return
        '''
        #assertion
        assert isinstance(potion, module_objets.Potion), "le paramètre doit être une potion !"
        #code
        contenu = potion.acc_contenu()
        self.potions_rouges[contenu].enfiler(potion)
        
    def mut_ajoute_potions_bleues(self, potion):
        '''
        modifie l'attribut potions_bleues en augmentant ou en baissant le nombre de potions de la potion passée en paramètre
        : params
            potion (Potion)
        : pas de return
        '''
        #assertion
        assert isinstance(potion, module_objets.Potion), "le paramètre doit être une potion !"
        #code
        contenu = potion.acc_contenu()
        self.potions_bleues[contenu].enfiler(potion)
        
    def mut_enleve_potions_rouges(self):
        '''
        modifie l'attribut potions_rouges enlevant la première potion de la file sélectionnée
        : return (Potion)
        '''
        return self.potion_rouge_selectionnee.defiler()
        
    def mut_enleve_potions_bleues(self):
        '''
        modifie l'attribut potions_bleues enlevant la première potion de la file sélectionnée
        : return (Potion)
        '''
        return self.potion_bleue_selectionnee.defiler()

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
        
    def mut_continuer(self, valeur) :
        '''
        Modifie l'attribut menu
        : param valeur (boolean)
        : pas de return, modifie l'attribut continuer
        '''
        #Assertion :
        assert isinstance(valeur, bool), 'Le paramètre doit être soit True, soit False !'
        #Code :
        self.continuer = valeur
    
    def mut_menu(self, valeur) :
        '''
        Modifie l'attribut menu
        : param valeur (boolean)
        : pas de return, modifie l'attribut menu
        '''
        #Assertion :
        assert isinstance(valeur, bool), 'Le paramètre doit être soit True, soit False !'
        #Code :
        self.menu = valeur
        
    def mut_menu_options(self, valeur) :
        '''
        Modifie l'attribut menu_options
        : param valeur (boolean)
        : pas de return, modifie l'attribut menu_options
        '''
        #Assertion :
        assert isinstance(valeur, bool), 'Le paramètre doit être soit True, soit False !'
        #Code :
        self.menu_options = valeur
        
    def mut_dernier_personnage_mort_bleu(self, perso):
        '''
        modifie l'attribut dernier_personnage_mort de l'équipe bleue
        : pas de return
        '''
        self.dernier_personnage_mort_bleu = perso
        
    def mut_dernier_personnage_mort_rouge(self, perso):
        '''
        modifie l'attribut dernier_personnage_mort de l'équipe rouge
        : pas de return
        '''
        self.dernier_personnage_mort_rouge = perso
        
    def mut_annonce_coffre(self, etat):
        '''
        Modifie l'attribut annonce_coffre
        : param valeur (boolean)
        : pas de return, modifie l'attribut menu
        '''
        #Assertion :
        assert isinstance(etat, bool), 'Le paramètre doit être soit True, soit False !'
        self.annonce_coffre = etat
        
    def mut_annonce_coffre_console(self, etat):
        '''
        Modifie l'attribut annonce_coffre_console
        : param valeur (boolean)
        : pas de return, modifie l'attribut menu
        '''
        #Assertion :
        assert isinstance(etat, bool), 'Le paramètre doit être soit True, soit False !'
        self.annonce_coffre_console = etat
        
    def mut_compteur(self, valeur) :
        '''
        Modifie l'attribut compteur
        : param valeur (int)
        : pas de return, modifie l'attribut compteur
        '''
        #Assertion :
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int)'
        #Code :
        self.compteur = valeur
        
    def mut_tab_personnages(self, tab) :
        '''
        Modifie l'attribut tab_personnages
        : param tab (list)
        : pas de return, modifie l'attribut tab_personnages
        '''
        #Assertion :
        assert isinstance(tab, list), 'Le paramètre doit être un tableau (list)'
        #Code :
        self.tab_personnages = tab
        
    def mut_tab_monstres(self, tab) :
        '''
        Modifie l'attribut tab_monstres
        : param tab (list)
        : pas de return, modifie l'attribut tab_monstres
        '''
        #Assertion :
        assert isinstance(tab, list), 'Le paramètre doit être un tableau (list)'
        #Code :
        self.tab_monstres = tab
        
    def mut_tab_coffres(self, tab) :
        '''
        Modifie l'attribut tab_coffres
        : param tab (list)
        : pas de return, modifie l'attribut tab_coffres
        '''
        #Assertion :
        assert isinstance(tab, list), 'Le paramètre doit être un tableau (list)'
        #Code :
        self.tab_coffres = tab
        
    def supprime_tab_coffres(self, coffre):
        '''
        enlève du tableau tab_coffres le coffre passé en paramètres
        : pas de return, modifie l'attribut tab_coffres
        '''
        #Assertion :
        assert isinstance(coffre, module_objets.Coffre), 'Le paramètre doit être un coffre du module_coffre !'
        #Code :
        self.tab_coffres.remove(coffre)
        
    def ajoute_tab_coffres(self, coffre):
        '''
        ajoute au tableau tab_coffres le coffre passé en paramètres
        : pas de return, modifie l'attribut tab_coffres
        '''
        #Assertion :
        assert isinstance(coffre, module_objets.Coffre), 'Le paramètre doit être un coffre du module_coffre !'
        #Code :
        self.tab_coffres.append(coffre)

    def mut_deplacements(self, tab) :
        '''
        Modifie l'attribut deplacements
        : param tab (list)
        : pas de return, modifie l'attribut deplacements
        '''
        #Assertion :
        assert isinstance(tab, list), 'Le paramètre doit être un tableau (list)'
        #Code :
        self.deplacements = tab
        
    def mut_deplacements_cavalier(self, tab):
        '''
        modifie l'attribue deplacements_affichage_cavalier
        : param tab (list)
        : pas de return, modifie l'attribut deplacements_affichage_cavalier
        '''
        #Assertion :
        assert isinstance(tab, list), 'Le paramètre doit être un tableau (list)'
        #Code :
        self.deplacements_invisibles_cavalier = tab
        
    def mut_attaques(self, tab) :
        '''
        Modifie l'attribut attaques
        : param tab (list)
        : pas de return, modifie l'attribut attaques
        '''
        #Assertion :
        assert isinstance(tab, list), 'Le paramètre doit être un tableau (list)'
        #Code :
        self.attaques = tab
        
    def mut_selection(self, coordonnées) :
        '''
        Modifie l'attribut selection
        : param coordonnées (???)
        : pas de return, modifie l'attribut selection
        '''
        self.selection = coordonnées
        
    def mut_coffre_selection(self, nouveau_coffre) :
        '''
        Modifie l'attribut coffre_selection
        : param nouveau_coffre (Coffre)
        : pas de return, modifie l'attribut selection
        '''
        self.coffre_selection = nouveau_coffre
        
    def mut_equipe_en_cours(self, equipe) :
        '''
        Modifie l'attribut equipe_en_cours
        : param equipe (str)
        : pas de return, modifie l'attribut equipe_en_cours
        '''
        #Assertion :
        assert isinstance(equipe, str) and equipe in ['bleu', 'rouge'], "Le paramètre doit être une chaine de caractères (str) égal à 'bleu' ou 'rouge' !"
        #Code :
        self.equipe_en_cours = equipe
        
    def mut_bouton_clique(self, valeur) :
        '''
        Modifie l'attribut bouton_clique
        : param valeur (str or None)
        : pas de return, modifie l'attribut bouton_clique
        '''
        #Assertion :
        assert isinstance(valeur, str) or valeur == None, "Le paramètre doit être une chaine de caractères (str) égal à 'bleu' ou 'rouge' !"
        #Code :
        self.bouton_clique = valeur  
        
    def mut_temps_appui_bouton(self, valeur) :
        '''
        Modifie l'attribut bouton_clique
        : param valeur (float)
        : pas de return, modifie l'attribut temps_appui_bouton
        '''
        #Assertion :
        assert isinstance(valeur, float), "Le paramètre doit être du type float !"
        #Code :
        self.temps_appui_bouton = valeur
        
    def mut_temps(self, chaine) :
        '''
        Modifie l'attribut bouton_clique
        : param chaine (str)
        : pas de return, modifie l'attribut bouton_clique
        '''
        #Assertion :
        assert isinstance(chaine, str), "Le paramètre doit être une chaine de caractères (str) !"
        #Code :
        self.temps = chaine
        
    def mut_temps_active(self, valeur) :
        '''
        Modifie l'attribut temps_active
        : param valeur (bool)
        : pas de return, modifie l'attribut temps_active
        '''
        #Assertion :
        assert isinstance(valeur, bool), "Le paramètre doit être un booléen (bool) !"
        #Code :
        self.temps_active = valeur
        
    def mut_monstres_active(self, valeur) :
        '''
        Modifie l'attribut monstres_active
        : param valeur (bool)
        : pas de return, modifie l'attribut monstres_active
        '''
        #Assertion :
        assert isinstance(valeur, bool), "Le paramètre doit être un booléen (bool) !"
        #Code :
        self.monstres_active = valeur

    def mut_nombre_action(self, valeur) :
        '''
        Modifie l'attribut nombre_action
        : param valeur (int)
        '''
        #Précondition :
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int) !'
        #Code :
        self.nombre_action = valeur
    
    def mut_nombre_tour(self, valeur) :
        '''
        Modifie l'attribut nombre_action
        : param valeur (int)
        '''
        #Précondition :
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int) !'
        #Code :
        self.nombre_tour = valeur
        
    def mut_console(self, valeur) :
        '''
        Modifie l'attribut console
        : param valeur (module_lineaire.Pile)
        '''
        #Précondition :
        assert isinstance(valeur, module_lineaire.Pile), 'Le paramètre doit être de la classe Pile (module_lineaire) !'
        #Code :
        self.console = valeur
        
    def mut_chemin(self, tab) :
        '''
        Modifie l'attribut chemin
        : param tab (list)
        '''
        #Précondition :
        assert isinstance(tab, list), 'Le paramètre doit être un tableau (list) !'
        #Code :
        self.chemin = tab
        
    def mut_chemin_monstre(self, tab) :
        '''
        Modifie l'attribut chemin
        : param tab (list)
        '''
        #Précondition :
        assert isinstance(tab, list), 'Le paramètre doit être un tableau (list) !'
        #Code :
        self.chemin_monstre = tab
        
    def mut_coordonnees_personnage(self, coordonnees) :
        '''
        Modifie l'attribut coordonnees
        : param coordonnees (tuple or None)
        '''
        #Précondition :
        assert isinstance(coordonnees, tuple) or coordonnees == None, 'Le paramètre doit être un tuple ou None !'
        #Code :
        self.coordonnees_personnage = coordonnees
        
    def mut_coordonnees_monstre(self, coordonnees) :
        '''
        Modifie l'attribut coordonnees
        : param coordonnees (tuple or None)
        '''
        #Précondition :
        assert isinstance(coordonnees, tuple) or coordonnees == None, 'Le paramètre doit être un tuple ou None !'
        #Code :
        self.coordonnees_monstre = coordonnees
    
    def mut_personnage_en_deplacement(self, personnage) :
        '''
        Modifie l'attribut personnage_en_deplacement
        : param personnage (module_personnage.Personnage or None)
        '''
        #Précondition :
        assert isinstance(personnage, module_personnage.Personnage) or personnage == None, 'Le paramètre doit être un personnage de la classe Personnage ou None !'
        #Code :
        self.personnage_en_deplacement = personnage
        
    def mut_monstre_en_deplacement(self, tab) :
        '''
        Modifie l'attribut personnage_en_deplacement
        : param tab (list or None)
        '''
        #Précondition :
        assert isinstance(tab, list) or tab == None, 'Le paramètre doit être un tableau (list) ou None !'
        #Code :
        self.monstre_en_deplacement = tab
    
    def mut_indice_courant(self, valeur) :
        '''
        Modifie l'attribut current_index
        : param valeur (int)
        '''
        #Précondition :
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int) !'
        #Code :
        self.indice_courant = valeur
    
    def mut_deplacement_en_cours(self, valeur) :
        '''
        Modifie l'attribut deplacement_en_cours
        : param valeur (bool)
        '''
        #Précondition :
        assert isinstance(valeur, bool), 'Le paramètre doit être un booléen (bool) !'
        #Code :
        self.deplacement_en_cours = valeur
    
    def mut_nouvelles_coord(self, coordonnees) :
        '''
        Modifie l'attribut nouvelles_coord
        : param coordonnees (tuple or None)
        '''
        #Précondition :
        assert isinstance(coordonnees, tuple) or coordonnees == None, 'Le paramètre doit être un tuple ou None !'
        #Code :
        self.nouvelles_coord = coordonnees
    
    def mut_nb_actions(self, valeur) :
        '''
        Modifie l'attribut nb_actions
        : param valeur (int)
        '''
        #Précondition :
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int) !'
        #Code :
        self.nb_actions = valeur
        
    def mut_monstres_deja_deplaces(self, valeur) :
        '''
        Modifie l'attribut monstres_deja_deplaces
        : param valeur (bool)
        '''
        #Précondition :
        assert isinstance(valeur, bool), 'Le paramètre doit être un booléen (bool) !'
        #Code :
        self.monstres_deja_deplaces = valeur
        
    def mut_monstres_a_deplacer(self, tab) :
        '''
        Modifie l'attribut monstres_a_deplacer
        : param tab (list)
        '''
        #Précondition :
        assert isinstance(tab, list), 'Le paramètre doit être un tableau (list) !'
        #Code :
        self.monstres_a_deplacer = tab
        
    def mut_positions_tombes(self, valeur) :
        '''
        Modifie l'attribut positions_tombes
        : param valeur (tuple)
        '''
        #Précondition :
        assert isinstance(valeur, tuple), 'Le paramètre doit être un tuple !'
        #Code :
        self.positions_tombes = valeur
       
    def mut_attaque_en_cours(self, valeur) :
        '''
        Modifie l'attribut attaque_en_cours
        : param valeur (bool)
        '''
        #Précondition :
        assert isinstance(valeur, bool), 'Le paramètre doit être un booléen (bool) !'
        #Code :
        self.attaque_en_cours = valeur   
       
    def mut_attaque_temps(self, valeur) :
        '''
        Modifie l'attribut attaque_temps
        : param valeur (int)
        '''
        #Précondition :
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int) !'
        #Code :
        self.attaque_temps = valeur
       
    def mut_positions_tombes(self, coordonnees) :
        '''
        Modifie l'attribut positions_tombes (ajouté ! (append))
        : param coordonnees (tuple)
        '''
        #Précondition :
        assert isinstance(coordonnees, tuple), 'Le paramètre doit être un tableau (list) !'
        #Code :
        self.positions_tombes.append(coordonnees)
                
    def mut_partie_terminee(self, valeur) :
        '''
        Modifie l'attribut partie_terminee
        : param valeur (bool)
        '''
        #Précondition :
        assert isinstance(valeur, bool), 'Le paramètre doit être un booléen (bool) !'
        #Code :
        self.partie_terminee = valeur        
                
    def mut_position_y_menu_fin(self, valeur) :
        '''
        Modifie l'attribut position_y_menu_fin
        : param valeur (int)
        '''
        #Précondition :
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int) !'
        #Code :
        self.position_y_menu_fin += valeur          
                
    def mut_equipe_gagnante(self, valeur) :
        '''
        Modifie l'attribut equipe_gagnante
        : param valeur (str) 'rouge' ou 'bleu' (ou None en cas de chargement d'une partie)
        '''
        #Précondition :
        assert valeur in ['rouge', 'bleu', None], 'Le paramètre doit être soit \'rouge\' ou \'bleu\' ou None !'
        #Code :
        self.equipe_gagnante = valeur          
                
    ######################################################
    ### Autres Accesseurs :
    ######################################################
                
    def est_meme_equipe(self):
        '''
        Renvoie True si l'équipe du personnage et l'équipe en cours sont les mêmes,
        False sinon.
        : return (bool)
        '''
        if isinstance(self.acc_selection(), module_personnage.Personnage) :
            return self.acc_selection().acc_equipe() == self.acc_equipe_en_cours()
   
    ######################################################
    ### Autres Mutateurs :
    ######################################################
    
    def ajouter_personnage(self, perso):
        '''
        modifie l'attribut tab_personnage en y ajoutant le personnage passé en paramètre
        : param perso (Personnage)
        : pas de return, modifie l'attribut tab_personnages
        '''
        #assertion
        assert isinstance(perso, module_personnage.Personnage), 'Le paramètre doit être un Personnage !'
        #code
        self.tab_personnages.append(perso)
        
    def supprimer_personnage(self, personnage) :
        '''
        Supprime le personnage passé en paramètre du tableau des personnages
        : param personnage (module_personnage.Personnage)
        : pas de return, modifie l'attribut tab_personnages
        '''
        #Assertion :
        assert isinstance(personnage, module_personnage.Personnage), 'Le paramètre doit être un personnage (module_personnage.Personnage) !'
        #Code :
        self.tab_personnages.remove(personnage)

    def ajouter_monstre(self, monstre) :
        '''
        Modifie l'attribut tab_monstres (ajoute !)
        : param monstre (module_personnage.Monstre)
        : pas de return, modifie l'attribut tab_monstres
        '''
        #Assertion :
        assert isinstance(monstre, module_personnage.Monstre), 'Le paramètre doit être un monstre (module_personnage.Monstre)'
        #Code :
        self.tab_monstres.append(monstre)
        
    def supprimer_monstre(self, monstre) :
        '''
        Supprime le monstre passé en paramètre du tableau des monstres.
        : param monstre (module_personnage.Monstre)
        : pas de return, modifie l'attribut tab_monstres
        '''
        #Assertion :
        assert isinstance(monstre, module_personnage.Monstre), 'Le paramètre doit être un monstre (module_personnage.Monstre) !'
        #Code :
        self.tab_monstres.remove(monstre)
        
    def ajouter_coffre(self, coffre) :
        '''
        Modifie l'attribut tab_coffres (ajoute !)
        : param coffre (module_objets.Coffre)
        : pas de return, modifie l'attribut tab_coffres
        '''
        #Assertion :
        assert isinstance(coffre, module_objets.Coffre), 'Le paramètre doit être un coffre (module_objets.Coffre) !'
        #Code :
        self.tab_coffres.append(coffre)
        
    def supprimer_coffre(self, coffre) :
        '''
        Supprime le coffre passé en paramètre du tableau des coffres.
        : param coffre (module_objets.Coffre)
        : pas de return, modifie l'attribut tab_coffres
        '''
        #Assertion :
        assert isinstance(coffre, module_objets.Coffre), 'Le paramètre doit être un coffre (module_objets.Coffre) !'
        #Code :
        self.tab_coffres.remove(coffre)  
    
    def changer_temps_jeu(self):
        '''
        modifie le temps de la journée si un certain nombre de déplacements/attaques a été effectué
        : pas de return
        '''
        #Si il y a eu un multiple de 4 tours passé :
        if self.acc_nombre_tour() % 4 == 0 and self.acc_nombre_tour() != 0 :
            #Si le "changement" de temps est activé :
            if not self.acc_temps_active() :
                dic = {'Jour': 'Nuit', 'Nuit': 'Jour'}
                phrase = {
                    'Jour' : '·Le soleil se lève !',
                    'Nuit' : '·Le soleil se couche !'
                }
                self.mut_temps(dic[self.temps]) #Change le temps (par le contraire grâce au dictionnaire)
                self.ajouter_console([phrase[self.acc_temps()], 'noir']) #Ajoute la phrase adapté dans la console du jeu.
                self.mut_temps_active(True) #Le "changement" de temps est activé
           
        ##Temps pour les monstres d'apparaître ?
        elif self.acc_nombre_tour() % 4 == 2 and self.acc_temps() == 'Jour':
            
            #Si l'apparition des monstres est désactivé et qu'ils n'ont pas encore été déplacés
            if not self.acc_monstres_active() and not self.acc_monstres_deja_deplaces() :
                self.mut_monstres_active(True) #Le "placement" de monstres est activé
            #Sinon :
            else :
                self.mut_monstres_active(False) #Le "placement" de monstres est désactivé
                
        #Sinon :
        else :
            self.mut_temps_active(False) #Le "changement" de temps est désactivé
            self.mut_monstres_deja_deplaces(False)
            
    def ajouter_console(self, tab) :
        '''
        Ajoute dans la pile du console la chaine de caractères
        :param tab (list of str) [str, str] -> phrase et equipe
        : pas de return, effet de bord sur la pile !
        '''
        #Précondition :
        assert isinstance(tab, list) and len(tab) == 2 and isinstance(tab[0], str) and tab[1] in ['rouge', 'bleu', 'noir'], 'Le paramètre doit être un tableau (list) comprenant deux chaînes de caractères (str) comme éléments (phrase et equipe) !'
        #Code :
        if len(tab[0]) > 28 : 
            chaine = tab[0]
            i = len(chaine) - (len(chaine) - 28)
            est_espace = False
            while i != 0 and not est_espace :
                if chaine[i] == ' ' :
                    est_espace = True
                else :
                    i -= 1
            self.console.empiler([chaine[:i], tab[1]])
            self.console.empiler([chaine[i + 1:], tab[1]])
        else :
            self.console.empiler(tab)
        
    def enlever_console(self) :
        '''
        Si la pile dépasse 24 chaînes de caractère, enlève les premiers messages ajoutés da la pile.
        '''
        pile = self.acc_console()
        stock = module_lineaire.Pile()
        compteur = 0
        
        while not pile.est_vide() :
            tab = pile.depiler()
            compteur += 1
            stock.empiler(tab)
            
        while not stock.est_vide() :
            if compteur >= 30 :   
                stock.depiler()
                compteur -= 1
            else :
                pile.empiler(stock.depiler())
                
    def augmente_nombre_tour(self) :
        '''
        Ajoute 1 à l'attribut nombre_tour
        : param valeur (int)
        '''
        self.nombre_tour += 1
        
    def ajouter_positions_tombes(self, coordonnees) :
        '''
        Ajoute une tombe dans l'attribut positions_tombes 
        : param coordonnees (tuple)
        '''
        #Précondition :
        assert isinstance(coordonnees, tuple), 'Le paramètre doit être un tuple !'
        #Code :
        self.positions_tombes.append(coordonnees)
        
    def supprimer_positions_tombes(self, coordonnees) :
        '''
        Supprime une tombe dans l'attribut positions_tombes 
        : param coordonnees (tuple)
        '''
        #Précondition :
        assert isinstance(coordonnees, tuple), 'Le paramètre doit être un tuple !'
        #Code :
        self.positions_tombes.remove(coordonnees)