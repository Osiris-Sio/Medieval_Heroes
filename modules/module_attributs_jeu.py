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
        self.option = False
        self.compteur = 0 #Compte le nombre de boucle
        self.tab_personnages = []
        self.tab_monstres = []
        self.tab_coffres = []
        self.deplacements = [] #Tableau de tuples (x, y) pour chaque coordonnées des cases de déplacement possible
        self.deplacements_invisibles_cavalier = [] #Tableau de tuples (x, y) pour chaque coordonnées des cases de déplacement possible seulement pour les cavaliers
        self.attaques = [] #Tableau de tuples (x, y) pour chaque coordonnées des cases d'attaque possible
        self.selection = ' ' #' ' = Case vide sinon (autre caractère (str)) un personnage de la classe Personnage du module_personnage 
        self.equipe_en_cours = 'bleu' #Chaine de caractères de l'équipe qui joue
        self.coffre_selection = None #le coffre sélectionné
        
        #Bouton :
        self.bouton_clique = None #Si None, c'est que aucun bouton du jeu ou du menu a été cliqué. Sinon, prend la chaine de caractères correspondante (exemple : Le bouton 'jouer' a été cliqué, alors bouton_cliqué = 'jouer')
        self.temps_appui_bouton = 0 #Le temps passé après qu'un bouton a été cliqué
        
        #Jour/Nuit :
        self.temps = 'Jour' #Le temps du jeu
        self.temps_active = False
        self.monstre_active = False #True si des monstres doivent apparaître et False sinon
        
        #Action/Tour :
        self.nombre_action = 0 #Le nombre d'action qu'une équipe a faite pendant son tour
        self.nombre_tour = 0 #Le nombre de tour passé.
        
        #Console (pile) :
        self.console = module_lineaire.Pile() #Une pile où sera ajouté des tableaux contenant une phrase et sa couleur pour ensuite l'afficher.
        
        #Attributs pour le déplacement avec le chemin (graphe) :
        self.chemin = []
        self.coordonnees_personnage = None
        self.personnage_en_deplacement = None
        self.indice_courant = 0
        self.deplacement_en_cours = False
        self.nouvelles_coord = None
        self.nb_actions = 0
        
        # Attributs pour le déplacement des monstres
        self.chemin_monstre = []
        self.coordonnees_monstre = None
        self.monstre_en_deplacement = None
        self.deplacement_en_cours_monstre = False
        self.nouvelles_coord = None
         
        self.monstres_a_deplacer = []
        
        #Attributs pour les attaques :
        self.attaque_en_cours = False
        self.attaque_temps = 0
        
        #Coffre :
        self.dernier_personnage_mort_bleu = None
        self.dernier_personnage_mort_rouge = None
        self.annonce_coffre = False
        self.event_coffre = 0
        
        #Eléments du décor
        self.positions_tombes = [] #Tableau de tuples (x, y) des coordonnées de chaque tombe 
        
        #Fin du jeu
        self.partie_terminee = False #True si la partie est terminée, False sinon 
        self.position_y_menu_fin = 0
        self.equipe_gagnante = None #None si la partie n'est pas terminée, 'bleu' ou 'rouge' (str) pour savoir quelle équipe a gagné.

    ######################################################
    ### Accesseurs :
    ######################################################
    
    def acc_annonce_coffre(self):
        '''
        Renvoie l'attribut annoce_coffre
        '''
        return self.annonce_coffre
    
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
    
    def acc_option(self):
        '''
        Renvoie l'attribut option
        '''
        return self.option
    
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
    
    def acc_monstre_active(self):
        '''
        Renvoie l'attribut monstre_active
        '''
        return self.monstre_active
    
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
        return self.deplacement_en_monstre
    
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
    
    ######################################################
    ### Mutateurs :
    ######################################################
    def mut_annonce_coffre(self, etat):
        '''
        Modifie l'attribut annonce_coffre
        : param valeur (boolean)
        : pas de return, modifie l'attribut menu
        '''
        #Assertion :
        assert isinstance(etat, bool), 'Le paramètre doit être soit True, soit False !'
        
        self.annonce_coffre = etat
        
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
        
    def mut_option(self, valeur) :
        '''
        Modifie l'attribut option
        : param valeur (boolean)
        : pas de return, modifie l'attribut option
        '''
        #Assertion :
        assert isinstance(valeur, bool), 'Le paramètre doit être soit True, soit False !'
        #Code :
        self.option = valeur
        
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
        : pas de return, modifie l'attribut temps_appui_bonton
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
        
    def mut_monstre_active(self, valeur) :
        '''
        Modifie l'attribut monstre_active
        : param valeur (bool)
        : pas de return, modifie l'attribut monstre_active
        '''
        #Assertion :
        assert isinstance(valeur, bool), "Le paramètre doit être un booléen (bool) !"
        #Code :
        self.monstre_active = valeur

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
        Modifie l'attribut nombre_action (addition !)
        : param valeur (int)
        '''
        #Précondition :
        assert isinstance(valeur, int), 'Le paramètre doit être un entier (int) !'
        #Code :
        self.nombre_tour += valeur
        
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
        : param coordonees (tuple or None)
        '''
        #Précondition :
        assert isinstance(coordonnees, tuple) or coordonnees == None, 'Le paramètre doit être un tuple ou None !'
        #Code :
        self.coordonnees_personnage = coordonnees
        
    def mut_coordonnees_monstre(self, coordonnees) :
        '''
        Modifie l'attribut coordonnees
        : param coordonees (tuple or None)
        '''
        #Précondition :
        assert isinstance(coordonnees, tuple) or coordonnees == None, 'Le paramètre doit être un tuple ou None !'
        #Code :
        self.coordonnees_monstre = coordonnees
    
    def mut_personnage_en_deplacement(self, tab) :
        '''
        Modifie l'attribut personnage_en_deplacement
        : param tab (list or None)
        '''
        #Précondition :
        assert isinstance(tab, list) or tab == None, 'Le paramètre doit être un tableau (list) ou None !'
        #Code :
        self.personnage_en_deplacement = tab
        
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
        assert isinstance(valeur, int), 'Le paramètre doit être un entien (int) !'
        #Code :
        self.nb_actions = valeur
       
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
                
    def mut_equipe_gagnante(self, chaine) :
        '''
        Modifie l'attribut equipe_gagnante
        : param chaine (str) 'rouge' ou 'bleu'
        '''
        #Précondition :
        assert chaine in ['rouge', 'bleu'], 'Le paramètre doit être soir \'rouge\' ou \'bleu\' !'
        #Code :
        self.equipe_gagnante = chaine          
                
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
    
    def mut_temps_jeu(self):
        '''
        modifie le temps de la journee si un certain nombre de déplacements/attaques a été effectué
        '''
        if self.acc_nombre_tour() % 4 == 0 and self.acc_nombre_tour() != 0:
            if not self.acc_temps_active() :
                temps = {'Jour': 'Nuit', 'Nuit': 'Jour'}
                phrase = {
                    'Jour' : 'Le soleil se lève !',
                    'Nuit' : 'Le soleil se couche !'
                }
                print(self.temps)
                self.mut_temps(temps[self.temps])
                self.ajouter_console([phrase[self.acc_temps()], 'noir'])
                self.mut_temps_active(True)
                self.mut_monstre_active(True)
        else :
            self.mut_temps_active(False)
            
    def ajouter_console(self, tab) :
        '''
        Ajoute dans la pile du console la chaine de caractères
        :param tab (list of str) [str, str] -> phrase et equipe
        : pas de return, effet de bord sur la pile !
        '''
        #Précondition :
        assert isinstance(tab, list) and len(tab) == 2 and isinstance(tab[0], str) and tab[1] in ['rouge', 'bleu', 'noir', 'neutre'], 'Le paramètre doit être un tableau (list) comprenant deux chaines de caractères (str) comme éléments (phrase et equipe) !'
        #Code :
        self.console.empiler(tab)
        
    def enlever_console(self) :
        '''
        Si la pile dépasse 24 chaines de caractère, enlève les premiers messages ajoutés da la pile.
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
                
    