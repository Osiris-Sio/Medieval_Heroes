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
        assert isinstance(jeu, module_jeu.Jeu), 'jeu doit être de la classe Jeu du module_jeu !'
        assert isinstance(attributs_jeu, module_attributs_jeu.Attributs_Jeu), 'attributs_jeu doit être de la classe Attributs_Jeu du module_attributs_jeu !'
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
            
            elif isinstance(personnage, module_personnage.Cavalier) :
                chaine_personnages = chaine_personnages + '[' + personnage.acc_equipe() + ',' + str(personnage.acc_x()) + ',' + str(personnage.acc_y()) + ',' + str(personnage.acc_pv()) + ']'
            
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
            
        # Equipe / Action / Tour / Robot :
        tab_chaines.append('[' + self.attributs_jeu.acc_equipe_en_cours() + ',' + str(self.attributs_jeu.acc_nombre_action()) + ',' + str(self.attributs_jeu.acc_nombre_tour()) + ',' + str(self.attributs_jeu.acc_mode_robot()) + ']')

        # Tombes :
        chaine_tombes = '['
        for tombe in self.attributs_jeu.acc_positions_tombes() :
            chaine_tombes = chaine_tombes + '[' + str(tombe[0]) + ',' + str(tombe[1]) + ']'
        chaine_tombes += ']'
        tab_chaines.append(chaine_tombes)
        
        return tab_chaines
        
    def sauvegarder(self) :
        '''
        Sauvegarde la partie
        : return (str), une phrase qui sera ajouté dans la console du jeu.
        '''
        #Demande le chemin où sera sauvegardé le fichier :
        fichier = filedialog.asksaveasfilename(
        defaultextension = ".txt",
        filetypes = [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        
        if not fichier :
            return "Aucun fichier sélectionné."
        
        tab_chaines = self.generer_chaines()
        try :
            ecriture = open(fichier,'w',encoding='utf_8')
            for elt in tab_chaines :
                ecriture.write(elt + '\n')
            ecriture.close()
            return "Partie Sauvegardé !"
        
        except :
            return "Erreur de Sauvegarde !"
        
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
        
    def restorer_partie(self, tab) :
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
            
        self.attributs_jeu.mut_selection(' ')
        self.attributs_jeu.mut_deplacements([])
        self.attributs_jeu.mut_deplacements_cavalier([])
        self.attributs_jeu.mut_attaques([])
        
        # Personnages :
        tab_personnages = tab_converti[0]
        self.attributs_jeu.mut_tab_personnages([])
        self.attributs_jeu.mut_famille_geant_bleu([])
        self.attributs_jeu.mut_famille_geant_rouge([])
        
        geant_bleu = []
        geant_rouge = []
        
        for personnage in tab_personnages :
            
            if personnage[0] in ['bleu', 'rouge'] :
                if len(personnage) == 5 :
                    geant = module_personnage.Geant(personnage[0], int(personnage[1]), int(personnage[2]), int(personnage[3]))
                    geant.mut_pv(int(personnage[4]))
                    self.attributs_jeu.ajouter_personnage(geant)
                    if personnage[0] == 'rouge' :    
                        geant_rouge.append(geant)
                    else :
                        geant_bleu.append(geant)
                else :
                    cavalier = module_personnage.Cavalier(personnage[0], int(personnage[1]), int(personnage[2]))
                    cavalier.mut_pv(int(personnage[3]))
                    self.attributs_jeu.ajouter_personnage(cavalier)
            else :
                perso = module_personnage.Personnage(personnage[0], personnage[1], int(personnage[2]), int(personnage[3]))
                perso.mut_pv(int(personnage[4]))
                self.attributs_jeu.ajouter_personnage(perso)
                
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
        self.attributs_jeu.tab_coffres = []
        for coffre in tab_coffres :
            self.attributs_jeu.tab_coffres.append(module_objets.Coffre(int(coffre[0]), int(coffre[1])))
        
        # Equipe / Action / Tour / Robot :
        tab_param = tab_converti[3][0]
        
        self.attributs_jeu.mut_equipe_en_cours(tab_param[0])
        self.attributs_jeu.mut_nombre_action(int(tab_param[1]))
        self.attributs_jeu.mut_nombre_tour(int(tab_param[2]))
        
        dic = {'True' : True, 'False' : False}
        self.attributs_jeu.mut_mode_robot(dic[tab_param[3]])
        
        # Tombe :
        tab_tombes = tab_converti[4]
        self.attributs_jeu.positions_tombes = []
        
        for tombe in tab_tombes :
            self.attributs_jeu.positions_tombes.append([int(tombe[0]), int(tombe[1])])
        
    def charger(self) :
        '''
        Charge la partie
        : return (str), une phrase qui sera ajouté dans la console du jeu
        '''
        #Demande le chemin du fichier qui sera chargé :
        fichier = filedialog.askopenfilename(
        filetypes = [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        
        if not fichier :
            return "Aucun fichier sélectionné."
        
        try :
            lecture = open(fichier,'r',encoding='utf_8')
            tab = lecture.readlines()
            lecture.close()
            self.restorer_partie(tab)
            self.jeu.reinitialiser_attributs() #Réinitialise les attributs du jeu
            return "Partie Chargé !" 
        except :
            return "Erreur de Chargement !" 