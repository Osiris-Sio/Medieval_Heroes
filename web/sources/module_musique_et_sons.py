'''
-> Medieval Heroes

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################
import pygame, random

######################################################
### GestionnaireSon :
######################################################

class Gestionnaire_Son:
    '''
    une classe pour la gestion du son du jeu
    '''
    def __init__(self, volume = 0.2):
        '''
        initialise le gestionnaire de sons
        : param volume (int), par défaut, il vaut 0.2
        '''
        pass
        
    def lancer_musique_fond(self) :
        '''
        Lance la musique de fond
        :return, music
        '''
        pass

    def boucle_musique(self, music):
        '''
        lance la boucle des musiques de fond
        : pas de return
        '''
        pass

    def jouer_effet_sonore(self, nom):
        '''
        joue un effet sonore
        : param nom (str)
        : pas de return
        '''
        #Assertion
        pass
    
    def regler_volume(self):
        '''
        ajuste le volume du jeu
        : pas de return
        '''
        pass

    def mut_volume(self, volume):
        '''
        modifie le volume du jeu
        : param volume (int or float)
        : pas de return
        '''
        pass
    
    def arreter_tous_les_sons(self):
        '''
        arrête tous les sons du jeu
        : pas de return
        '''
        pass
