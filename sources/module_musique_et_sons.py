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
        pygame.mixer.init()
        self.volume = volume
        self.musique_fond = pygame.mixer.music.load("medias/musiques/musique_fond.mp3")
        self.effets_sonores = {"feu" : pygame.mixer.Sound("medias/sons/feu.WAV"),
                               "lame" : pygame.mixer.Sound("medias/sons/lame.WAV"),
                               "potion" : pygame.mixer.Sound("medias/sons/potion.WAV"),
                               "poing1" : pygame.mixer.Sound("medias/sons/poing1.MP3"),
                               "poing2" : pygame.mixer.Sound("medias/sons/poing2.MP3"),
                               "tir" : pygame.mixer.Sound("medias/sons/tir.WAV"),
                               }
        self.regler_volume()
        
    def lancer_musique_fond(self) :
        '''
        Lance la musique de fond
        :return, music
        '''
        music = self.musique_fond
        pygame.mixer.music.play()
        return music

    def boucle_musique(self, music):
        '''
        lance la boucle des musiques de fond
        : pas de return
        '''
        if pygame.mixer.music.get_pos() == -1 :
            self.lancer_musique_fond()

    def jouer_effet_sonore(self, nom):
        '''
        joue un effet sonore
        : param nom (str)
        : pas de return
        '''
        #Assertion
        assert isinstance(nom, str), "le nom doit être une chaîne de caractères"
        #Code
        if nom == "poing":
            x = random.randint(0, 2)
            if x == 0:
                self.effets_sonores["poing1"].play()
            else :
                self.effets_sonores["poing2"].play()
        if nom in self.effets_sonores:
            self.effets_sonores[nom].play()
    
    def regler_volume(self):
        '''
        ajuste le volume du jeu
        : pas de return
        '''
        pygame.mixer.music.set_volume(self.volume)
        for effet_sonore in self.effets_sonores.values():
            effet_sonore.set_volume(self.volume)

    def mut_volume(self, volume):
        '''
        modifie le volume du jeu
        : param volume (int or float)
        : pas de return
        '''
        #Assertion
        assert isinstance(volume, int) or isinstance(volume, float), "le volume doit être un entier ou un float"
        #Code
        self.volume = volume
        self.regler_volume()
    
    def arreter_tous_les_sons(self):
        '''
        arrête tous les sons du jeu
        : pas de return
        '''
        pygame.mixer.stop()
