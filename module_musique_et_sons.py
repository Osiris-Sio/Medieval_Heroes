'''
-> Medieval Heroes

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
''' 

######################################################
### Importation Modules :
######################################################
import pygame

######################################################
### GestionnaireSon :
######################################################

class GestionnaireSon:
    '''
    une classe pour la gestion du son du jeu
    '''
    def __init__(self, volume = 0.5):
        '''
        initialise le gestionnaire de sons
        : param volume (int), par défaut, il vaut 0.5
        '''
        pygame.mixer.init()
        self.volume = volume
        self.musique_fond = [pygame.mixer.music.load("medias/musiques/1.MP3"), pygame.mixer.music.load("medias/musiques/2.MP3")]
        self.effets_sonores = {"feu" : pygame.mixer.Sound("medias/sons/feu.WAV"),
                               "lame" : pygame.mixer.Sound("medias/sons/lame.WAV"),
                               "potion" : pygame.mixer.Sound("medias/sons/potion.WAV"),
                               "marche" : pygame.mixer.Sound("medias/sons/marche.WAV")
                               }
        self.regler_volume()

    def boucle_musique(self):
        '''
        lance la boucle des musiques de fond
        : pas de return
        '''
        for musique in self.musique_fond:
            pygame.mixer.music.play()

    def jouer_effet_sonore(self, nom):
        '''
        joue un effet sonore
        : param nom (str)
        : pas de return
        '''
        #Assertion
        assert isinstance(nom, str), "le nom doit être une chaîne de caractères"
        #Code
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
        : param volume (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(volume, int), "le volume doit être un entier"
        #Code
        self.volume = volume
        self.regler_volume()
    
    def arreter_tous_les_sons(self):
        '''
        arrête tous les sons du jeu
        : pas de return
        '''
        pygame.mixer.stop()

if __name__ == "__main__":
    pygame.init()

    gestionnaire_son = GestionnaireSon()

    # lance la boucle des musiques de fond
    gestionnaire_son.boucle_musique()
    pygame.time.wait(500)
    gestionnaire_son.jouer_effet_sonore("lame")
    '''

    # attend un certain temps pour laisser la musique jouer
   
    
    # joue un effet sonore
    gestionnaire_son.jouer_effet_sonore("lame")
    # modifie le volume du jeu
    gestionnaire_son.mut_volume(0.2)

    # attend un certain temps pour laisser la musique jouer avec le nouveau volume
    pygame.time.wait(5000)

    # arrête tous les sons du jeu
    gestionnaire_son.arreter_tous_les_sons()

    pygame.quit()
    '''