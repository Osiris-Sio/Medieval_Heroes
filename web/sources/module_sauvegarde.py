# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour les Sauvegardes et les Chargements de partie

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################

import module_jeu, module_attributs_jeu, module_personnage, module_objets

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
        pass
        
    def sauvegarder(self, attributs_jeu) :
        '''
        Sauvegarde la partie
        : return (str), une phrase qui sera ajouté dans la console du jeu.
        '''
        pass
        
    def convertir_chaine_list(self, chaine) :
        '''
        Convertit la chaîne de caractères passé en paramètre en tableau
        : param chaine (str)
        : return (list)
        '''
        pass
        
    def restaurer_partie(self, tab) :
        '''
        Restaure la partie grâce au tableau passé en paramètre
        : param tab (list)
        '''
        pass
        
    def charger(self) :
        '''
        Charge la partie
        : pas de return, effet de bord
        '''
        pass
        
        