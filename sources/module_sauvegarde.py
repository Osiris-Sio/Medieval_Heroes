# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour les Sauvegardes et les Chargements de partie

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################

import module_jeu, module_attributs_jeu, module_personnage, module_objets, tkinter
from tkinter import filedialog

######################################################
### Classe Sauvegarde :
######################################################

class Sauvegarde() :
    '''
    Une classe Sauvegarde qui gère le chargement et la sauvegarde d'une partie dans un fichier texte
    '''
    def __init__(self, jeu, attributs_jeu) :
        '''
        Initialise la classe
        : params
            jeu (module_jeu.Jeu)
            attributs_jeu (module.attributs_jeu.Attributs_Jeu)
        '''
        #Assertions :
        assert isinstance(jeu, module_jeu.Jeu), 'jeu doit être de la classe Jeu (module_jeu) !'
        assert isinstance(attributs_jeu, module_attributs_jeu.Attributs_Jeu), 'attributs_jeu doit être de la classe Attributs_Jeu (module_attributs_jeu) !'
        
        #Attributs des Paramètres :
        self.jeu = jeu
        self.attributs_jeu = attributs_jeu
        
    def generer_chaines(self) :
        '''
        Renvoie un tableau de chaînes de caractères qui sera sauvegarder dans le fichier texte
        : return (list of str)
        '''
        tab_chaines = []
        
        # Personnages :
        chaine_personnages = '['
        for personnage in self.attributs_jeu.acc_tab_personnages() :
            
            if isinstance(personnage, module_personnage.Geant) :
                chaine_personnages = chaine_personnages + '[' + personnage.acc_equipe() + ',' + str(personnage.acc_x()) + ',' + str(personnage.acc_y()) + ',' + str(personnage.acc_numero_geant()) + ',' + str(personnage.acc_pv()) + ']'
            
            else :
                chaine_personnages = chaine_personnages + '[' + personnage.acc_personnage() + ',' + personnage.acc_equipe() + ',' + str(personnage.acc_x()) + ',' + str(personnage.acc_y()) + ',' + str(personnage.acc_pv()) + ']'
        
        chaine_personnages += ']'
        tab_chaines.append(chaine_personnages)
        
        # Monstres :
        chaine_monstres = '['
        for monstre in self.attributs_jeu.acc_tab_monstres() :
            chaine_monstres = chaine_monstres + '[' + str(monstre.acc_x()) + ',' + str(monstre.acc_y()) + ',' + str(monstre.acc_pv()) + ',' + str(monstre.acc_etat()) + ']'
        chaine_monstres += ']'
        tab_chaines.append(chaine_monstres)
        
        # Coffres :
        chaine_coffres = '['
        for coffre in self.attributs_jeu.acc_tab_coffres() :
            chaine_coffres = chaine_coffres + '[' + str(coffre.acc_x()) + ',' + str(coffre.acc_y()) + ']'
        chaine_coffres += ']' 
        tab_chaines.append(chaine_coffres)  
            
        # Equipe / Action / Tour / Nombre_Monstres / PV_Monstres / Robot :
        tab_chaines.append('[' + self.attributs_jeu.acc_equipe_en_cours() + ',' + str(self.attributs_jeu.acc_nombre_action()) + ',' + str(self.attributs_jeu.acc_nombre_tour()) + ',' + str(self.attributs_jeu.acc_nombre_monstre_a_ajoute()) + ',' + str(self.attributs_jeu.acc_pv_monstre()) + ',' + str(self.attributs_jeu.acc_mode_robot()) + ']')

        # Tombes :
        chaine_tombes = '['
        for tombe in self.attributs_jeu.acc_positions_tombes() :
            chaine_tombes = chaine_tombes + '[' + str(tombe[0]) + ',' + str(tombe[1]) + ']'
        chaine_tombes += ']'
        tab_chaines.append(chaine_tombes)
        
        return tab_chaines
        
    def sauvegarder(self, attributs_jeu) :
        '''
        Sauvegarde la partie
        : return (str), une phrase qui sera ajouté dans la console du jeu.
        '''
        #Demande le chemin où sera sauvegardé le fichier :
        self.attributs_jeu = attributs_jeu
        fichier = filedialog.asksaveasfilename(
        defaultextension = ".txt",
        filetypes = [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        
        if not fichier :
            self.attributs_jeu.ajouter_console(["·Aucun chemin sélectionné", "noir"])
        
        else :
            tab_chaines = self.generer_chaines()
            try :
                ecriture = open(fichier,'w',encoding='utf_8')
                for elt in tab_chaines :
                    ecriture.write(elt + '\n')
                ecriture.close()
                self.attributs_jeu.ajouter_console(["·Partie Sauvegardé !", "noir"])
            
            except :
                self.attributs_jeu.ajouter_console(["·Erreur de Sauvegarde !", "noir"])
        
    def convertir_chaine_list(self, chaine) :
        '''
        Convertit la chaîne de caractères passé en paramètre en tableau
        : param chaine (str)
        : return (list)
        '''
        #Assertion
        assert isinstance(chaine, str), "la chaîne doit être de type str"
        #Code
        elt_important = ''
        tab_important = []
        tab_complet = []
        for elt in chaine :
            if elt == ',' :
                tab_important.append(elt_important)
                elt_important = ''
            elif elt == ']' :
                if elt_important != '' :
                    tab_important.append(elt_important)
                    tab_complet.append(tab_important)
                elt_important = ''
                tab_important = []
            elif elt != '[' :
                elt_important += elt
        return tab_complet
        
    def restaurer_partie(self, tab) :
        '''
        Restaure la partie grâce au tableau passé en paramètre
        : param tab (list)
        '''
        #Assertion
        assert isinstance(tab, list), 'Le paramètre doit être un tableau (list) !'
        #Code
        tab_converti = []
        for chaine in tab :
            tab_converti.append(self.convertir_chaine_list(chaine[:-1]))
        
        # Personnages :
        tab_personnages = tab_converti[0]
        
        geant_bleu = []
        geant_rouge = []
        
        for personnage in tab_personnages :
            #géant
            if personnage[0] in ['bleu', 'rouge'] :
                geant = module_personnage.Geant(personnage[0], int(personnage[1]), int(personnage[2]), int(personnage[3]), int(personnage[4]))
                self.attributs_jeu.ajouter_personnage(geant)
                if personnage[0] == 'rouge' :    
                    geant_rouge.append(geant)
                else :
                    geant_bleu.append(geant)
            #personnage "normal"
            else :
                self.attributs_jeu.ajouter_personnage(module_personnage.Personnage(personnage[0], personnage[1], int(personnage[2]), int(personnage[3]), int(personnage[4])))
                
            if len(geant_bleu) == 4 :
                self.attributs_jeu.ajouter_famille_geant_bleu(geant_bleu)
                geant_bleu = []
                
            if len(geant_rouge) == 4 :
                self.attributs_jeu.ajouter_famille_geant_rouge(geant_rouge)
                geant_rouge = []
        
        # Monstre :
        tab_monstres = tab_converti[1]
        self.attributs_jeu.mut_tab_monstres([])
        for monstre in tab_monstres :
            self.attributs_jeu.tab_monstres.append(module_personnage.Monstre(int(monstre[0]), int(monstre[1]), int(monstre[2]), int(monstre[3])))
        
        # Coffre :
        tab_coffres = tab_converti[2]
        self.attributs_jeu.mut_tab_coffres([])
        for coffre in tab_coffres :
            self.attributs_jeu.tab_coffres.append(module_objets.Coffre(int(coffre[0]), int(coffre[1])))
        
        # Equipe / Action / Tour / Nombres_Monstres / PV_Monstres / Robot :
        tab_param = tab_converti[3][0]
        
        self.attributs_jeu.mut_equipe_en_cours(tab_param[0])
        self.attributs_jeu.mut_nombre_action(int(tab_param[1]))
        self.attributs_jeu.mut_nombre_tour(int(tab_param[2]))
        self.attributs_jeu.mut_nombre_monstre_a_ajoute(int(tab_param[3]))
        self.attributs_jeu.mut_pv_monstre(int(tab_param[4]))
        
        dic = {'True' : True, 'False' : False}
        self.attributs_jeu.mut_mode_robot(dic[tab_param[5]])
        
        #Si il y a eu un multiple de 4 tours passé :
        if self.attributs_jeu.acc_nombre_tour() % 8 in [4, 5, 6, 7] and self.attributs_jeu.acc_nombre_tour() != 0 :
            self.attributs_jeu.mut_temps('Nuit')
        
        # Tombe :
        tab_tombes = tab_converti[4]
        self.attributs_jeu.mut_positions_tombes([])
        
        for tombe in tab_tombes :
            self.attributs_jeu.ajouter_positions_tombes((int(tombe[0]), int(tombe[1])))
        
    def charger(self) :
        '''
        Charge la partie
        : pas de return, effet de bord
        '''
        #Demande le chemin du fichier qui sera chargé :
        fichier = filedialog.askopenfilename(
        filetypes = [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        
        if not fichier :
            self.attributs_jeu.ajouter_console(["·Aucun fichier sélectionné", "noir"])
        
        else :
            try :
                attributs_importation, nouveau_attributs_jeu = self.jeu.reinitialiser_attributs() #Réinitialise la partie
                self.attributs_jeu = nouveau_attributs_jeu #Donne les nouveaux attributs du jeu
                lecture = open(fichier,'r',encoding='utf_8')
                tab = lecture.readlines()
                lecture.close()
                self.restaurer_partie(tab) #Charge la partie du fichier texte
                self.jeu.placer()
                self.attributs_jeu.mut_menu(False)
                self.attributs_jeu.ajouter_console(["·Partie Chargée !", "noir"])
            
            except :
                self.attributs_jeu = self.jeu.restaurer_attributs_importation(attributs_importation) #Restaure l'ancienne partie en cas d'erreur de fichier texte
                self.attributs_jeu.ajouter_console(["·Erreur de Chargement !" , "noir"])
        
        