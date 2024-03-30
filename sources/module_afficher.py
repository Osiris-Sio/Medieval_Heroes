# -*- coding: utf-8 -*-

'''
-> Medieval Heroes : Module pour la classe Affichage

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''

######################################################
### Importation Modules :
######################################################

import pygame, random, module_attributs_jeu, module_souris, module_terrain, module_personnage, module_jeu
from graphe import module_lineaire

######################################################
### Classe Pétale :
######################################################

class Petale():
    '''
    Une classe Petale qui gère les petites pétales des cerisiers
    '''
    def __init__(self, position):
        '''
        Initialise la classe
        : param position (str), 'haut_gauche' ou 'haut_droit' ou 'bas_gauche' ou 'bas_droit'
        '''
        #Assertion :
        assert position in ['haut_gauche', 'haut_droit', 'bas_gauche', 'bas_droit'], "Le paramètre doit être soit 'haut_gauche' ou 'haut_droit' ou 'bas_gauche' ou 'bas_droit' !"
        
        #Attributs :       
        self.taille = random.randint(1, 3)
        self.position = position
        
        if self.position == 'haut_gauche':
            self.x = random.randint(317, 378)
            self.y = random.randint(225, 278)
            self.distance_max = random.randint(295, 360)
                    
        elif self.position == 'haut_droit':
            self.x = random.randint(925, 975)
            self.y = random.randint(231, 277)
            self.distance_max = random.randint(295, 360)
                    
        elif self.position == 'bas_gauche':
            self.x = random.randint(317, 378)
            self.y = random.randint(500, 550)
            self.distance_max = random.randint(595, 660)
                    
        else :
            self.x = random.randint(925, 975)
            self.y = random.randint(500, 550)
            self.distance_max = random.randint(595, 660)
        
    #################################
    ### Accesseurs :
    #################################
            
    def acc_x(self):
        '''
        renvoie l'attribut x du pétale
        : return (int)
        '''
        return self.x
    
    def acc_y(self):
        '''
        renvoie l'attribut y du pétale
        : return (int)
        '''
        return self.y
    
    def acc_position(self):
        '''
        renvoie l'attribut position
        : return (str)
        '''
        return self.position
    
    def acc_distance_max(self):
        '''
        renvoie l'attribut distance_max
        : return (int)
        '''
        return self.distance_max
    
    #################################
    ### Mutateurs :
    #################################
    
    def mut_x(self, nb):
        '''
        modifie l'attribut x du pétale
        : param nb (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(nb, int), "le nombre doit être un entier !"
        #Code
        self.x += nb
        
    def mut_y(self, nb):
        '''
        modifie l'attribut y du pétale
        : param nb (int)
        : pas de return
        '''
        #Assertion
        assert isinstance(nb, int), "le nombre doit être un entier !"
        #Code
        self.y += nb
        
######################################################
### Classe Affichage :
######################################################

class Affichage():
    '''
    Une classe Affichage qui gére les objets à afficher.
    '''

    def __init__(self, jeu, attributs_jeu, terrain, ecran, souris):
        '''
        Initialise l'affichage
        : params
            attributs_jeu (module.attributs_jeu.Attributs_Jeu)
            terrain (module_terrain.Terrain)
            ecran (pygame.display)
            souris (module_souris.Souris)
        '''
        #Assertions :
        assert isinstance(jeu, module_jeu.Jeu), 'jeu doit être de la classe Jeu du module_jeu !'
        assert isinstance(attributs_jeu, module_attributs_jeu.Attributs_Jeu), 'attributs_jeu doit être de la classe Attributs_Jeu du module_attributs_jeu !'
        assert isinstance(terrain, module_terrain.Terrain), 'terrain doit être de la classe Terrain du module_terrain !'
        assert isinstance(souris, module_souris.Souris), 'souris doit être de la classe Souris du module_souris !'
        
        #Attributs des Paramètres :
        self.jeu = jeu
        self.attributs_jeu = attributs_jeu
        self.terrain = terrain
        self.ecran = ecran
        self.souris = souris
        
        #Attributs Ressources (pour charger les ressources):
        
        
        
        #Menu/options :
        self.menu = pygame.image.load("medias/menu/menu4.png")
        self.image_fond = pygame.image.load("medias/menu/fond_menu.png")
        self.fond_options = pygame.image.load("medias/menu/menu_param.png")
        
        #Modes :
        self.local = pygame.image.load("medias/menu/jeu_local.png")
        self.robot = pygame.image.load("medias/menu/jeu_robot.png")
        
        #Terrain :
        self.image_terrain = pygame.image.load("medias/terrain/terrain_niveau1.png")
        
        #Décors :
        self.images_coffre = [
            pygame.image.load("medias/coffre/coffre_non_ouvert.png"), 
            pygame.image.load("medias/coffre/c1.png"), 
            pygame.image.load("medias/coffre/c2.png"), 
            pygame.image.load("medias/coffre/c3.png"), 
            pygame.image.load("medias/coffre/c4.png"), 
            pygame.image.load("medias/coffre/c5.png"), 
            pygame.image.load("medias/coffre/c6.png"), 
            pygame.image.load("medias/coffre/c7.png"), 
            pygame.image.load("medias/coffre/c8.png"), 
            pygame.image.load("medias/coffre/c9.png"), 
            pygame.image.load("medias/coffre/coffre_ouvert.png")
            ]
        self.image_tombe = pygame.image.load("medias/terrain/tombe.png")
        
        # Curseurs :
        self.curseur_normal = pygame.image.load("medias/curseurs/curseur0.png")
        self.curseur_appuye = pygame.image.load("medias/curseurs/curseur1.png")

        #Déplacements/Attaques :
        self.deplacements = pygame.image.load("medias/attaque_deplacement/deplacement.png")
        self.attaques = [pygame.image.load("medias/attaque_deplacement/attaque_possible.png"),
                         pygame.image.load("medias/attaque_deplacement/guerison_possible.png")]
        
        #Cerisiers :
        self.cerisier = pygame.image.load("medias/terrain/cerisier.png")
        self.tab_petales = [
            Petale('haut_gauche'), 
            Petale('haut_gauche'), 
            Petale('haut_droit'),  
            Petale('haut_droit'), 
            Petale('bas_gauche'), 
            Petale('bas_gauche'), 
            Petale('bas_droit'),  
            Petale('bas_droit')
            ]
        
        #Filtres
        self.transition = 0
        self.temps_annonce = 0
        self.opacite = 100
        self.direction = 'diminution'
        
        #Sol (contour du personnage) :
        self.sol_personnages = {
            'rouge' : pygame.image.load("medias/terrain/sol_r.png"),
            'bleu' : pygame.image.load("medias/terrain/sol_b.png"),
            }
        self.sol_geants = {
            'rouge' : pygame.image.load("medias/terrain/sol_r_geant.png"),
            'bleu' : pygame.image.load("medias/terrain/sol_b_geant.png")
            }
        
        #Réponses coffre
        self.rep_contenu = {1 : 'Bonus de vie',
                            2 : 'Changement de personnage',
                            3 : 'Bonus de dégâts',
                            4 : 'Nécromancie claire',
                            5 : 'Nécromancie obscure',
                            6 : "Potions de soin",
                            7 : "Potion de mort",
                            8 : "Potions jaunes",
                            9 : "Potions de mort adverses",
                            10 : "Bonus de dégâts adverse"
                            }
        
        #Personnages :
        self.personnages = {
            'paladin': [
                [pygame.image.load("medias/personnages/paladin/paladin1.png"), pygame.image.load("medias/personnages/paladin/paladin2.png")],
                [pygame.image.load("medias/personnages/paladin/paladinb1.png"), pygame.image.load("medias/personnages/paladin/paladinb2.png")]
            ],
            'poulet': [
                [pygame.image.load("medias/personnages/poulet/pr1.png"), pygame.image.load("medias/personnages/poulet/pr2.png"), pygame.image.load("medias/personnages/poulet/pr3.png"), pygame.image.load("medias/personnages/poulet/pr2.png") , pygame.image.load("medias/personnages/poulet/pr2.png")],
                [pygame.image.load("medias/personnages/poulet/pb1.png"), pygame.image.load("medias/personnages/poulet/pb2.png"), pygame.image.load("medias/personnages/poulet/pb3.png"), pygame.image.load("medias/personnages/poulet/pb2.png"), pygame.image.load("medias/personnages/poulet/pb2.png")]
            ],
            'geant': [
                [
                    [pygame.image.load("medias/personnages/geant/gb1.png"), pygame.image.load("medias/personnages/geant/gb2.png"), pygame.image.load("medias/personnages/geant/gb3.png"), pygame.image.load("medias/personnages/geant/gb4.png")],
                    [pygame.image.load("medias/personnages/geant/gb11.png"), pygame.image.load("medias/personnages/geant/gb22.png"), pygame.image.load("medias/personnages/geant/gb33.png"), pygame.image.load("medias/personnages/geant/gb44.png")]
                ],
                [
                    [pygame.image.load("medias/personnages/geant/gr1.png"), pygame.image.load("medias/personnages/geant/gr2.png"), pygame.image.load("medias/personnages/geant/gr3.png"), pygame.image.load("medias/personnages/geant/gr4.png")],
                    [pygame.image.load("medias/personnages/geant/gr11.png"), pygame.image.load("medias/personnages/geant/gr22.png"), pygame.image.load("medias/personnages/geant/gr33.png"), pygame.image.load("medias/personnages/geant/gr44.png")]
                ]
            ],
            'cavalier': [
                [pygame.image.load("medias/personnages/cavalier/cr1.png"), pygame.image.load("medias/personnages/cavalier/cr2.png"), pygame.image.load("medias/personnages/cavalier/cr3.png"), pygame.image.load("medias/personnages/cavalier/cr4.png"), pygame.image.load("medias/personnages/cavalier/cr5.png"), pygame.image.load("medias/personnages/cavalier/cr6.png"), pygame.image.load("medias/personnages/cavalier/cr7.png"), pygame.image.load("medias/personnages/cavalier/cr8.png")],
                [pygame.image.load("medias/personnages/cavalier/cb1.png"), pygame.image.load("medias/personnages/cavalier/cb2.png"), pygame.image.load("medias/personnages/cavalier/cb3.png"), pygame.image.load("medias/personnages/cavalier/cb4.png"), pygame.image.load("medias/personnages/cavalier/cb5.png"), pygame.image.load("medias/personnages/cavalier/cb6.png"), pygame.image.load("medias/personnages/cavalier/cb7.png"), pygame.image.load("medias/personnages/cavalier/cb8.png")]
            ],
            'archere': [
                [pygame.image.load("medias/personnages/archere/ar2.png"),pygame.image.load("medias/personnages/archere/ar1.png")],
                [pygame.image.load("medias/personnages/archere/ab1.png"),pygame.image.load("medias/personnages/archere/ab2.png")]],
            'sorciere': [
                [pygame.image.load("medias/personnages/sorciere/sor1.png"),pygame.image.load("medias/personnages/sorciere/sor2.png")],
                [pygame.image.load("medias/personnages/sorciere/sob1.png"),pygame.image.load("medias/personnages/sorciere/sob2.png")]],
            'ivrogne': [
                [pygame.image.load("medias/personnages/ivrogne/ir1.png"), pygame.image.load("medias/personnages/ivrogne/ir2.png"), pygame.image.load("medias/personnages/ivrogne/ir3.png"), pygame.image.load("medias/personnages/ivrogne/ir4.png"), pygame.image.load("medias/personnages/ivrogne/ir3.png"), pygame.image.load("medias/personnages/ivrogne/ir2.png")],
                [pygame.image.load("medias/personnages/ivrogne/ib1.png"), pygame.image.load("medias/personnages/ivrogne/ib2.png"), pygame.image.load("medias/personnages/ivrogne/ib3.png"), pygame.image.load("medias/personnages/ivrogne/ib4.png"), pygame.image.load("medias/personnages/ivrogne/ib3.png"),pygame.image.load("medias/personnages/ivrogne/ib2.png"),]],
            'barbare': [
                [pygame.image.load("medias/personnages/barbare/br1.png"), pygame.image.load("medias/personnages/barbare/br2.png")],
                [pygame.image.load("medias/personnages/barbare/bb1.png"), pygame.image.load("medias/personnages/barbare/bb2.png")]],
            'cracheur de feu': [
                [pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c66.png"), pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c55.png"), pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c44.png"), pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c33.png"), pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c22.png"), pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c11.png"), pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c1.png"), pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c2.png"), pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c3.png"), pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c4.png"), pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c5.png"),pygame.image.load("medias/personnages/cracheur_de_feu/rouge/c6.png")],
                [pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c66.png"), pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c55.png"), pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c44.png"), pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c33.png"), pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c22.png"), pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c11.png"), pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c1.png"), pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c2.png"), pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c3.png"), pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c4.png"), pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c5.png"),pygame.image.load("medias/personnages/cracheur_de_feu/bleu/c6.png")]],
            'valkyrie': [
                [pygame.image.load("medias/personnages/valkyrie/vr1.png"), pygame.image.load("medias/personnages/valkyrie/vr2.png")],
                [pygame.image.load("medias/personnages/valkyrie/vb1.png"), pygame.image.load("medias/personnages/valkyrie/vb2.png")]],
            'mage': [
                [pygame.image.load("medias/personnages/mage/rouge/sr1.png"), pygame.image.load("medias/personnages/mage/rouge/sr2.png"), pygame.image.load("medias/personnages/mage/rouge/sr3.png"), pygame.image.load("medias/personnages/mage/rouge/sr4.png"), pygame.image.load("medias/personnages/mage/rouge/sr5.png"), pygame.image.load("medias/personnages/mage/rouge/sr6.png"), pygame.image.load("medias/personnages/mage/rouge/sr7.png"), pygame.image.load("medias/personnages/mage/rouge/sr8.png"), pygame.image.load("medias/personnages/mage/rouge/sr9.png"), pygame.image.load("medias/personnages/mage/rouge/sr10.png"), pygame.image.load("medias/personnages/mage/rouge/sr11.png"), pygame.image.load("medias/personnages/mage/rouge/sr12.png"), pygame.image.load("medias/personnages/mage/rouge/sr13.png"), pygame.image.load("medias/personnages/mage/rouge/sr14.png"), pygame.image.load("medias/personnages/mage/rouge/sr15.png"), pygame.image.load("medias/personnages/mage/rouge/sr16.png"), pygame.image.load("medias/personnages/mage/rouge/sr17.png"), pygame.image.load("medias/personnages/mage/rouge/sr18.png"), pygame.image.load("medias/personnages/mage/rouge/sr19.png"), pygame.image.load("medias/personnages/mage/rouge/sr20.png"), pygame.image.load("medias/personnages/mage/rouge/sr21.png"), pygame.image.load("medias/personnages/mage/rouge/sr22.png"), pygame.image.load("medias/personnages/mage/rouge/sr23.png"), pygame.image.load("medias/personnages/mage/rouge/sr24.png"), pygame.image.load("medias/personnages/mage/rouge/sr25.png"), pygame.image.load("medias/personnages/mage/rouge/sr26.png"), pygame.image.load("medias/personnages/mage/rouge/sr27.png"), pygame.image.load("medias/personnages/mage/rouge/sr28.png"), pygame.image.load("medias/personnages/mage/rouge/sr29.png"), pygame.image.load("medias/personnages/mage/rouge/sr30.png"), pygame.image.load("medias/personnages/mage/rouge/sr31.png"), pygame.image.load("medias/personnages/mage/rouge/sr32.png"), pygame.image.load("medias/personnages/mage/rouge/sr33.png"), pygame.image.load("medias/personnages/mage/rouge/sr32.png"), pygame.image.load("medias/personnages/mage/rouge/sr31.png"), pygame.image.load("medias/personnages/mage/rouge/sr30.png"), pygame.image.load("medias/personnages/mage/rouge/sr29.png"), pygame.image.load("medias/personnages/mage/rouge/sr28.png"), pygame.image.load("medias/personnages/mage/rouge/sr27.png"), pygame.image.load("medias/personnages/mage/rouge/sr26.png"), pygame.image.load("medias/personnages/mage/rouge/sr25.png"), pygame.image.load("medias/personnages/mage/rouge/sr24.png"), pygame.image.load("medias/personnages/mage/rouge/sr23.png"), pygame.image.load("medias/personnages/mage/rouge/sr22.png"), pygame.image.load("medias/personnages/mage/rouge/sr21.png"), pygame.image.load("medias/personnages/mage/rouge/sr20.png"), pygame.image.load("medias/personnages/mage/rouge/sr19.png"), pygame.image.load("medias/personnages/mage/rouge/sr18.png"), pygame.image.load("medias/personnages/mage/rouge/sr17.png"), pygame.image.load("medias/personnages/mage/rouge/sr16.png"), pygame.image.load("medias/personnages/mage/rouge/sr15.png"), pygame.image.load("medias/personnages/mage/rouge/sr14.png"), pygame.image.load("medias/personnages/mage/rouge/sr13.png"), pygame.image.load("medias/personnages/mage/rouge/sr12.png"), pygame.image.load("medias/personnages/mage/rouge/sr11.png"), pygame.image.load("medias/personnages/mage/rouge/sr10.png"), pygame.image.load("medias/personnages/mage/rouge/sr9.png"), pygame.image.load("medias/personnages/mage/rouge/sr8.png"), pygame.image.load("medias/personnages/mage/rouge/sr7.png"), pygame.image.load("medias/personnages/mage/rouge/sr6.png"), pygame.image.load("medias/personnages/mage/rouge/sr5.png"), pygame.image.load("medias/personnages/mage/rouge/sr4.png"), pygame.image.load("medias/personnages/mage/rouge/sr3.png"), pygame.image.load("medias/personnages/mage/rouge/sr2.png"), pygame.image.load("medias/personnages/mage/rouge/sr1.png")],
                [pygame.image.load("medias/personnages/mage/bleu/sb1.png"), pygame.image.load("medias/personnages/mage/bleu/sb2.png"), pygame.image.load("medias/personnages/mage/bleu/sb3.png"), pygame.image.load("medias/personnages/mage/bleu/sb4.png"), pygame.image.load("medias/personnages/mage/bleu/sb5.png"), pygame.image.load("medias/personnages/mage/bleu/sb6.png"), pygame.image.load("medias/personnages/mage/bleu/sb7.png"), pygame.image.load("medias/personnages/mage/bleu/sb8.png"), pygame.image.load("medias/personnages/mage/bleu/sb9.png"), pygame.image.load("medias/personnages/mage/bleu/sb10.png"), pygame.image.load("medias/personnages/mage/bleu/sb11.png"), pygame.image.load("medias/personnages/mage/bleu/sb12.png"), pygame.image.load("medias/personnages/mage/bleu/sb13.png"), pygame.image.load("medias/personnages/mage/bleu/sb14.png"), pygame.image.load("medias/personnages/mage/bleu/sb15.png"), pygame.image.load("medias/personnages/mage/bleu/sb16.png"), pygame.image.load("medias/personnages/mage/bleu/sb17.png"), pygame.image.load("medias/personnages/mage/bleu/sb18.png"), pygame.image.load("medias/personnages/mage/bleu/sb19.png"), pygame.image.load("medias/personnages/mage/bleu/sb20.png"), pygame.image.load("medias/personnages/mage/bleu/sb21.png"), pygame.image.load("medias/personnages/mage/bleu/sb22.png"), pygame.image.load("medias/personnages/mage/bleu/sb23.png"), pygame.image.load("medias/personnages/mage/bleu/sb24.png"), pygame.image.load("medias/personnages/mage/bleu/sb25.png"), pygame.image.load("medias/personnages/mage/bleu/sb26.png"), pygame.image.load("medias/personnages/mage/bleu/sb27.png"), pygame.image.load("medias/personnages/mage/bleu/sb28.png"), pygame.image.load("medias/personnages/mage/bleu/sb29.png"), pygame.image.load("medias/personnages/mage/bleu/sb30.png"), pygame.image.load("medias/personnages/mage/bleu/sb31.png"), pygame.image.load("medias/personnages/mage/bleu/sb32.png"), pygame.image.load("medias/personnages/mage/bleu/sb33.png"),  pygame.image.load("medias/personnages/mage/bleu/sb32.png"), pygame.image.load("medias/personnages/mage/bleu/sb31.png"), pygame.image.load("medias/personnages/mage/bleu/sb30.png"), pygame.image.load("medias/personnages/mage/bleu/sb29.png"), pygame.image.load("medias/personnages/mage/bleu/sb28.png"), pygame.image.load("medias/personnages/mage/bleu/sb27.png"), pygame.image.load("medias/personnages/mage/bleu/sb26.png"), pygame.image.load("medias/personnages/mage/bleu/sb25.png"), pygame.image.load("medias/personnages/mage/bleu/sb24.png"), pygame.image.load("medias/personnages/mage/bleu/sb23.png"), pygame.image.load("medias/personnages/mage/bleu/sb22.png"), pygame.image.load("medias/personnages/mage/bleu/sb21.png"), pygame.image.load("medias/personnages/mage/bleu/sb20.png"), pygame.image.load("medias/personnages/mage/bleu/sb19.png"), pygame.image.load("medias/personnages/mage/bleu/sb18.png"), pygame.image.load("medias/personnages/mage/bleu/sb17.png"), pygame.image.load("medias/personnages/mage/bleu/sb16.png"), pygame.image.load("medias/personnages/mage/bleu/sb15.png"), pygame.image.load("medias/personnages/mage/bleu/sb14.png"), pygame.image.load("medias/personnages/mage/bleu/sb13.png"), pygame.image.load("medias/personnages/mage/bleu/sb12.png"), pygame.image.load("medias/personnages/mage/bleu/sb11.png"), pygame.image.load("medias/personnages/mage/bleu/sb10.png"), pygame.image.load("medias/personnages/mage/bleu/sb9.png"), pygame.image.load("medias/personnages/mage/bleu/sb8.png"), pygame.image.load("medias/personnages/mage/bleu/sb7.png"), pygame.image.load("medias/personnages/mage/bleu/sb6.png"), pygame.image.load("medias/personnages/mage/bleu/sb5.png"), pygame.image.load("medias/personnages/mage/bleu/sb4.png"), pygame.image.load("medias/personnages/mage/bleu/sb3.png"), pygame.image.load("medias/personnages/mage/bleu/sb2.png"), pygame.image.load("medias/personnages/mage/bleu/sb1.png")]],
            'monstre': [
                [pygame.image.load("medias/personnages/monstre/avant/mb1.png"), pygame.image.load("medias/personnages/monstre/avant/mb2.png"), pygame.image.load("medias/personnages/monstre/avant/mb3.png"), pygame.image.load("medias/personnages/monstre/avant/mb4.png"), pygame.image.load("medias/personnages/monstre/avant/mb5.png"), pygame.image.load("medias/personnages/monstre/avant/mb6.png"), pygame.image.load("medias/personnages/monstre/avant/mb5.png"), pygame.image.load("medias/personnages/monstre/avant/mb4.png"), pygame.image.load("medias/personnages/monstre/avant/mb3.png"), pygame.image.load("medias/personnages/monstre/avant/mb2.png")],
                [pygame.image.load("medias/personnages/monstre/m1.png"), pygame.image.load("medias/personnages/monstre/m1.png"), pygame.image.load("medias/personnages/monstre/m2.png"), pygame.image.load("medias/personnages/monstre/m3.png"), pygame.image.load("medias/personnages/monstre/m4.png"), pygame.image.load("medias/personnages/monstre/m4.png"), pygame.image.load("medias/personnages/monstre/m4.png"), pygame.image.load("medias/personnages/monstre/m3.png"), pygame.image.load("medias/personnages/monstre/m2.png"), pygame.image.load("medias/personnages/monstre/m1.png")]]
                }
        
        #Cadres de personnages :
        self.cadre = pygame.image.load("medias/cadres/cadre_personnage.png")

        self.cadres_personnages = {
            'paladin': [[pygame.image.load("medias/perso_selection/Jour/pr.png"), pygame.image.load("medias/perso_selection/Jour/pb.png")], [pygame.image.load("medias/perso_selection/Nuit/prn1.png"), pygame.image.load("medias/perso_selection/Nuit/pbn.png")]],
            'poulet': [[pygame.image.load("medias/perso_selection/Jour/por.png"), pygame.image.load("medias/perso_selection/Jour/pob.png")], [pygame.image.load("medias/perso_selection/Nuit/pourn.png"), pygame.image.load("medias/perso_selection/Nuit/poubn.png")]],
            'geant': [[pygame.image.load("medias/perso_selection/Jour/gr.png"), pygame.image.load("medias/perso_selection/Jour/gb.png")], [pygame.image.load("medias/perso_selection/Nuit/grn.png"), pygame.image.load("medias/perso_selection/Nuit/gbn.png")]],
            'cavalier': [[pygame.image.load("medias/perso_selection/Jour/cr.png"), pygame.image.load("medias/perso_selection/Jour/cb.png")], [pygame.image.load("medias/perso_selection/Nuit/crn.png"), pygame.image.load("medias/perso_selection/Nuit/cbn.png")]],
            'archere': [[pygame.image.load("medias/perso_selection/Jour/ar.png"), pygame.image.load("medias/perso_selection/Jour/ab.png")], [pygame.image.load("medias/perso_selection/Nuit/arn.png"), pygame.image.load("medias/perso_selection/Nuit/abn.png")]],
            'sorciere': [[pygame.image.load("medias/perso_selection/Jour/sor.png"), pygame.image.load("medias/perso_selection/Jour/sob.png")], [pygame.image.load("medias/perso_selection/Nuit/sorn.png"), pygame.image.load("medias/perso_selection/Nuit/sobn.png")]],
            'cracheur de feu' : [[pygame.image.load("medias/perso_selection/Jour/crr.png"), pygame.image.load("medias/perso_selection/Jour/crb.png")], [pygame.image.load("medias/perso_selection/Nuit/crrn.png"), pygame.image.load("medias/perso_selection/Nuit/crbn.png")]],
            'valkyrie' : [[pygame.image.load("medias/perso_selection/Jour/vr.png"), pygame.image.load("medias/perso_selection/Jour/vb.png")], [pygame.image.load("medias/perso_selection/Nuit/vrn.png"), pygame.image.load("medias/perso_selection/Nuit/vbn.png")]],
            'ivrogne' : [[pygame.image.load("medias/perso_selection/Jour/ir.png"), pygame.image.load("medias/perso_selection/Jour/ib.png")], [pygame.image.load("medias/perso_selection/Nuit/irn.png"), pygame.image.load("medias/perso_selection/Nuit/ibn.png")]],
            'barbare' : [[pygame.image.load("medias/perso_selection/Jour/br.png"), pygame.image.load("medias/perso_selection/Jour/bb.png")], [pygame.image.load("medias/perso_selection/Nuit/brn.png"), pygame.image.load("medias/perso_selection/Nuit/bbn.png")]],
            'mage' : [[pygame.image.load("medias/perso_selection/Jour/sr.png"), pygame.image.load("medias/perso_selection/Jour/sb.png")], [pygame.image.load("medias/perso_selection/Nuit/mrn.png"), pygame.image.load("medias/perso_selection/Nuit/mbn.png")]],
            'monstre' : [pygame.image.load("medias/perso_selection/Jour/mj.png"), pygame.image.load("medias/perso_selection/Nuit/mn.png")]
        }
        #Rouge quand ils sont endommagés
        self.personnages_endommages = {
            'paladin': [pygame.image.load("medias/perso_endommages/pr.png"), pygame.image.load("medias/perso_endommages/pb.png")],
            'poulet': [pygame.image.load("medias/perso_endommages/por.png"), pygame.image.load("medias/perso_endommages/pob.png")],
            'geant': [[pygame.image.load("medias/perso_endommages/gr1.png"), pygame.image.load("medias/perso_endommages/gr2.png"), pygame.image.load("medias/perso_endommages/gr3.png"), pygame.image.load("medias/perso_endommages/gr4.png")], [pygame.image.load("medias/perso_endommages/gb1.png"), pygame.image.load("medias/perso_endommages/gb2.png"), pygame.image.load("medias/perso_endommages/gb3.png"), pygame.image.load("medias/perso_endommages/gb4.png")]],
            'cavalier': [pygame.image.load("medias/perso_endommages/cr.png"), pygame.image.load("medias/perso_endommages/cb.png")],
            'archere': [pygame.image.load("medias/perso_endommages/ar.png"), pygame.image.load("medias/perso_endommages/ab.png")],
            'sorciere': [pygame.image.load("medias/perso_endommages/sor.png"), pygame.image.load("medias/perso_endommages/sob.png")],
            'cracheur de feu' : [pygame.image.load("medias/perso_endommages/crr.png"), pygame.image.load("medias/perso_endommages/crb.png")],
            'valkyrie' : [pygame.image.load("medias/perso_endommages/vr.png"), pygame.image.load("medias/perso_endommages/vb.png")],
            'ivrogne' : [pygame.image.load("medias/perso_endommages/ir.png"), pygame.image.load("medias/perso_endommages/ib.png")],
            'barbare' : [pygame.image.load("medias/perso_endommages/br.png"), pygame.image.load("medias/perso_endommages/bb.png")],
            'mage' : [pygame.image.load("medias/perso_endommages/sr.png"), pygame.image.load("medias/perso_endommages/sb.png")],
            'monstre' : [pygame.image.load("medias/perso_endommages/m.png")]
        }
        #Vert quand ils sont soignés
        self.personnages_soins = {
            'paladin': [pygame.image.load("medias/perso_soins/pr.png"), pygame.image.load("medias/perso_soins/pb.png")],
            'poulet': [pygame.image.load("medias/perso_soins/por.png"), pygame.image.load("medias/perso_soins/pob.png")],
            'geant': [[pygame.image.load("medias/perso_soins/gr1.png"), pygame.image.load("medias/perso_soins/gr2.png"), pygame.image.load("medias/perso_soins/gr3.png"), pygame.image.load("medias/perso_soins/gr4.png")], [pygame.image.load("medias/perso_soins/gb1.png"), pygame.image.load("medias/perso_soins/gb2.png"), pygame.image.load("medias/perso_soins/gb3.png"), pygame.image.load("medias/perso_soins/gb4.png")]],
            'cavalier': [pygame.image.load("medias/perso_soins/cr.png"), pygame.image.load("medias/perso_soins/cb.png")],
            'archere': [pygame.image.load("medias/perso_soins/ar.png"), pygame.image.load("medias/perso_soins/ab.png")],
            'sorciere': [pygame.image.load("medias/perso_soins/sor.png"), pygame.image.load("medias/perso_soins/sob.png")],
            'cracheur de feu' : [pygame.image.load("medias/perso_soins/crr.png"), pygame.image.load("medias/perso_soins/crb.png")],
            'valkyrie' : [pygame.image.load("medias/perso_soins/vr.png"), pygame.image.load("medias/perso_soins/vb.png")],
            'ivrogne' : [pygame.image.load("medias/perso_soins/ir.png"), pygame.image.load("medias/perso_soins/ib.png")],
            'barbare' : [pygame.image.load("medias/perso_soins/br.png"), pygame.image.load("medias/perso_soins/bb.png")],
            'mage' : [pygame.image.load("medias/perso_soins/sr.png"), pygame.image.load("medias/perso_soins/sb.png")],
            'monstre' : [pygame.image.load("medias/perso_soins/m.png")]
        }
        #Pour animations attaque   
        self.personnages_attaque = {
            'archere': [[pygame.image.load("medias/personnages/archere/attaque/tir1.png"), pygame.image.load("medias/personnages/archere/attaque/tir2.png"), pygame.image.load("medias/personnages/archere/attaque/tir3.png"), pygame.image.load("medias/personnages/archere/attaque/tir4.png")],
                        [pygame.image.load("medias/personnages/archere/attaque/tirb1.png"), pygame.image.load("medias/personnages/archere/attaque/tirb2.png"), pygame.image.load("medias/personnages/archere/attaque/tirb3.png"), pygame.image.load("medias/personnages/archere/attaque/tirb4.png")]],
            }
        #Lors de leur déplacement
        self.personnages_deplacement = {
            'paladin': [pygame.image.load("medias/perso_en_deplacement/pr.png"), pygame.image.load("medias/perso_en_deplacement/pb.png")],
            'poulet': [pygame.image.load("medias/perso_en_deplacement/por.png"), pygame.image.load("medias/perso_en_deplacement/pob.png")],
            'geant': [],
            'cavalier': [pygame.image.load("medias/perso_en_deplacement/cr.png"), pygame.image.load("medias/perso_en_deplacement/cb.png")],
            'archere': [pygame.image.load("medias/perso_en_deplacement/ar.png"), pygame.image.load("medias/perso_en_deplacement/ab.png")],
            'sorciere': [pygame.image.load("medias/perso_en_deplacement/sor.png"), pygame.image.load("medias/perso_en_deplacement/sob.png")],
            'cracheur de feu' : [pygame.image.load("medias/perso_en_deplacement/crr.png"), pygame.image.load("medias/perso_en_deplacement/crb.png")],
            'valkyrie' : [pygame.image.load("medias/perso_en_deplacement/vr.png"), pygame.image.load("medias/perso_en_deplacement/vb.png")],
            'ivrogne' : [pygame.image.load("medias/perso_en_deplacement/ir.png"), pygame.image.load("medias/perso_en_deplacement/ib.png")],
            'barbare' : [pygame.image.load("medias/perso_en_deplacement/br.png"), pygame.image.load("medias/perso_en_deplacement/bb.png")],
            'mage' : [pygame.image.load("medias/perso_en_deplacement/sr.png"), pygame.image.load("medias/perso_en_deplacement/sb.png")],
            'monstre' : [pygame.image.load("medias/perso_en_deplacement/m.png")]
        }
        #Potions :
        self.potions = [pygame.image.load("medias/potions/retirer.png"), pygame.image.load("medias/potions/soin.png"), pygame.image.load("medias/potions/tuer.png"), pygame.image.load("medias/potions/changer.png"),
                        pygame.image.load("medias/potions/soin_vide.png"), pygame.image.load("medias/potions/tuer_vide.png"), pygame.image.load("medias/potions/changer_vide.png")]
        #Bulles
        self.bulles = {
            'bleu' : [pygame.image.load("medias/bulles/bleu/0.png"), pygame.image.load("medias/bulles/bleu/1.png"), pygame.image.load("medias/bulles/bleu/2.png"), pygame.image.load("medias/bulles/bleu/3.png"), pygame.image.load("medias/bulles/bleu/4.png"), pygame.image.load("medias/bulles/bleu/5.png"), pygame.image.load("medias/bulles/bleu/6.png"), pygame.image.load("medias/bulles/bleu/7.png"), pygame.image.load("medias/bulles/bleu/8.png")],
            'rouge' : [pygame.image.load("medias/bulles/rouge/0.png"), pygame.image.load("medias/bulles/rouge/1.png"), pygame.image.load("medias/bulles/rouge/2.png"), pygame.image.load("medias/bulles/rouge/3.png"), pygame.image.load("medias/bulles/rouge/4.png"), pygame.image.load("medias/bulles/rouge/5.png"), pygame.image.load("medias/bulles/rouge/6.png"), pygame.image.load("medias/bulles/rouge/7.png"), pygame.image.load("medias/bulles/rouge/8.png")],
            'jaune' : [pygame.image.load("medias/bulles/jaune/0.png"), pygame.image.load("medias/bulles/jaune/1.png"), pygame.image.load("medias/bulles/jaune/2.png"), pygame.image.load("medias/bulles/jaune/3.png"), pygame.image.load("medias/bulles/jaune/4.png"), pygame.image.load("medias/bulles/jaune/5.png"), pygame.image.load("medias/bulles/jaune/6.png"), pygame.image.load("medias/bulles/jaune/7.png"), pygame.image.load("medias/bulles/jaune/8.png")],
            'vert' : [pygame.image.load("medias/bulles/vert/0.png"), pygame.image.load("medias/bulles/vert/1.png"), pygame.image.load("medias/bulles/vert/2.png"), pygame.image.load("medias/bulles/vert/3.png"), pygame.image.load("medias/bulles/vert/4.png"), pygame.image.load("medias/bulles/vert/5.png"), pygame.image.load("medias/bulles/vert/6.png"), pygame.image.load("medias/bulles/vert/7.png"), pygame.image.load("medias/bulles/vert/8.png")]
            }
        #bulles    
        self.dic_couleurs = {1 : 'bleu',
                        2 : 'vert',
                        3 : 'rouge',
                        4 : 'jaune'
                        }

        #Boutons :
        self.boutons = {
            'jouer' : [pygame.image.load("medias/cadres/cadre_jouer0.png"), 
                        pygame.image.load("medias/cadres/cadre_jouer1.png")],
            'quitter_menu' : [pygame.image.load("medias/cadres/cadre_quitter_menu0.png"), 
                        pygame.image.load("medias/cadres/cadre_quitter_menu1.png")],
            'quitter' : [pygame.image.load("medias/cadres/cadre_quitter0.png"), 
                        pygame.image.load("medias/cadres/cadre_quitter1.png")],
            'quitter_fin' : [pygame.image.load("medias/cadres/cadre_quitter0.png"), 
                        pygame.image.load("medias/cadres/cadre_quitter1.png")],
            'charger' : [pygame.image.load("medias/cadres/cadre_charger0.png"), 
                        pygame.image.load("medias/cadres/cadre_charger1.png")],
            'sauvegarder' : [pygame.image.load("medias/cadres/cadre_sauvegarder0.png"), 
                        pygame.image.load("medias/cadres/cadre_sauvegarder1.png")],
            'rejouer' : [pygame.image.load("medias/cadres/cadre_sauvegarder0.png"), 
                        pygame.image.load("medias/cadres/cadre_sauvegarder1.png")],
            'on_off' : [pygame.image.load("medias/cadres/active.png"), pygame.image.load("medias/cadres/desactive.png")],
            'barre_son' : pygame.image.load("medias/cadres/son_barre.png"),
            'pointeur_son' : pygame.image.load("medias/cadres/pointeur_son.png"),
            'options_menu' : [pygame.image.load("medias/cadres/cadre_options_menu0.png"),
                              pygame.image.load("medias/cadres/cadre_options_menu1.png")],
            'charger_menu' : [pygame.image.load("medias/cadres/cadre_charger_menu0.png"),
                              pygame.image.load("medias/cadres/cadre_charger_menu1.png")],
            'options' : [pygame.image.load("medias/cadres/cadre_options0.png"),
                         pygame.image.load("medias/cadres/cadre_options1.png")]
        }
        
        #Menu de fin de partie :
        self.menu_fin = pygame.image.load("medias/menu/menu_fin.png")
        
    ########################################
    ### Affichage Principale :
    ########################################
    
    def afficher_curseur(self):
        '''
        Affiche le curseur en fonction de l'état (appuyé ou non) et affiche sa position dans l'écran si il est dans le plateau de jeu
        : pas de return
        '''
        position_souris = self.souris.acc_position_curseur() #Position de la souris sur la fenêtre Pygame.
        
        #Si le joueur appuie sur le clique gauche de la souris, affiche le curseur appuyé :
        if self.souris.acc_appuye() :
            self.ecran.blit(self.curseur_appuye, position_souris)  
        
        #Sinon, affiche le curseur non-appuyé :
        else :
            self.ecran.blit(self.curseur_normal, position_souris)
            
    ########################################
    ### Affichages Menu/options :
    ########################################
    
    def afficher_fond(self):
        '''
        affiche le fond d'ecran
        : pas de return
        '''
        self.ecran.blit(self.image_fond, (0, 0))
        
    def afficher_boutons_menu(self):
        '''
        affiche les différents boutons du menu
        : pas de return
        '''
        police = pygame.font.Font("medias/polices/pixelec.ttf", 21)
        bouton_clique = self.attributs_jeu.acc_bouton_clique()

        #Bouton Jouer :
        if bouton_clique == 'jouer':
            bouton_jouer = self.boutons['jouer'][1]
            texte_jouer = police.render("Jouer" , 1, (200, 165, 80))
        else :
            bouton_jouer = self.boutons['jouer'][0]
            texte_jouer = police.render("Jouer" , 1, (196, 144, 4))
            
        self.ecran.blit(bouton_jouer, (450, 340)) 
        self.ecran.blit(texte_jouer, (615, 360))
        
        #Bouton Charger :
        if bouton_clique == 'charger':
            bouton_charger = self.boutons['charger_menu'][1]
            texte_charger = police.render("Charger" , 1, (255, 171, 92))
        else :
            bouton_charger = self.boutons['charger_menu'][0]
            texte_charger = police.render("Charger" , 1, (196, 144, 4))
            
        self.ecran.blit(bouton_charger, (450, 420)) 
        self.ecran.blit(texte_charger, (600, 440))
        
        #Bouton options :
        if bouton_clique == 'options':
            bouton_jouer = self.boutons['options_menu'][1]
            texte_options = police.render("Options" , 1, (77, 148, 219))
        else :
            bouton_jouer = self.boutons['options_menu'][0]
            texte_options = police.render("Options" , 1, (15, 75, 117))   
            
        self.ecran.blit(bouton_jouer, (450, 500)) 
        self.ecran.blit(texte_options, (600, 520))
        
        #Bouton Quitter (fermer la fenêtre pygame) :
        if bouton_clique == 'quitter':
            bouton_quitter = self.boutons['quitter_menu'][1]
            texte_quitter = police.render("Quitter" , 1, (224, 85, 92))
        else :
            bouton_quitter = self.boutons['quitter_menu'][0]
            texte_quitter = police.render("Quitter" , 1, (179, 12, 36))
        
        self.ecran.blit(bouton_quitter, (450, 580)) 
        self.ecran.blit(texte_quitter, (597, 600))
            
    def afficher_boutons_options(self):
        '''
        Affiche les différents boutons du menu options
        : pas de return
        '''
        police = pygame.font.Font("medias/polices/pixelec.ttf", 21)
        bouton_clique = self.attributs_jeu.acc_bouton_clique()
        
        #Texte On/Off
        texte_on = police.render("On" , 1, (0, 0, 0))
        texte_off = police.render("Off" , 1, (224, 85, 92))
        
        #Sol de couleur :
        #On :
        if self.jeu.acc_sols_de_couleur() :
            bouton_sols_de_couleur = self.boutons['on_off'][0]
            self.ecran.blit(texte_on, (715, 357))
        #Off :
        else :
            bouton_sols_de_couleur = self.boutons['on_off'][1]
            self.ecran.blit(texte_off, (707, 357))
            
        self.ecran.blit(bouton_sols_de_couleur, (680, 345))
        
        #Deplacement/Attaque :
        #On :
        if self.jeu.acc_deplacements_attaques() :
            bouton_sols_de_couleur = self.boutons['on_off'][0]
            self.ecran.blit(texte_on, (715, 422))
        #Off :
        else :
            bouton_sols_de_couleur = self.boutons['on_off'][1]
            self.ecran.blit(texte_off, (707, 422))
            
        self.ecran.blit(bouton_sols_de_couleur, (680, 410))
        
        #Console :
        #On :
        if self.jeu.acc_option_console() :
            bouton_sols_de_couleur = self.boutons['on_off'][0]
            self.ecran.blit(texte_on, (715, 487))
        #Off :
        else :
            bouton_sols_de_couleur = self.boutons['on_off'][1]
            self.ecran.blit(texte_off, (707, 487))
            
        self.ecran.blit(bouton_sols_de_couleur, (680, 475))
        
        
        #Barre son :
        bouton_option_son = self.boutons['barre_son']
        self.ecran.blit(bouton_option_son, (480, 580))
        
        pointeur_barre = self.boutons['pointeur_son']
        self.ecran.blit(pointeur_barre, (self.jeu.acc_x_pointeur(), 580))
        
        #Retour :
        if bouton_clique == 'retour_menu':
            bouton_retour = self.boutons['quitter_fin'][1]
            texte1 = police.render("Retour" , 1, (224, 85, 92))
        else :
            bouton_retour = self.boutons['quitter_fin'][0]
            texte1 = police.render("Retour" , 1, (179, 12, 36))
            
        self.ecran.blit(bouton_retour, (515, 650)) 
        self.ecran.blit(texte1, (580, 670))
        
    def afficher_menu_options(self) :
        '''
        Affiche le menu options
        : pas de return
        '''
        police = pygame.font.Font("medias/polices/pixelec.ttf", 21)
        
        self.ecran.blit(self.fond_options, (455, 290)) 
        self.ecran.blit(police.render("Options" , 1, (152, 82, 51)), (580, 310))
        
        #Textes statiques :
        texte_sols_de = police.render("Sols de" , 1, (152, 82, 51))
        texte_couleur = police.render("couleur" , 1, (152, 82, 51))
        texte_deplacements = police.render("Deplacements" , 1, (152, 82, 51))
        texte_attaques = police.render("/ Attaques" , 1, (152, 82, 51))
        texte_console = police.render("Console" , 1, (152, 82, 51))
        texte_barre_son = police.render("Volume :" , 1, (152, 82, 51))
        
        #Affiche les Textes statiques :
        self.ecran.blit(texte_sols_de, (470, 350))
        self.ecran.blit(texte_couleur, (470, 365))
        self.ecran.blit(texte_deplacements, (470, 418))
        self.ecran.blit(texte_attaques, (470, 435))
        self.ecran.blit(texte_console, (470, 485))
        self.ecran.blit(texte_barre_son, (470, 550))
        
        self.afficher_boutons_options()
        
    def afficher_menu_modes(self) :
        '''
        Affiche les différents modes de jeu à la disposition des joueurs
        : pas de return
        '''
        police = pygame.font.Font("medias/polices/pixelec.ttf", 21)
        bouton_clique = self.attributs_jeu.acc_bouton_clique()
        
        #Cadres :
        self.ecran.blit(self.local, (250, 250))
        self.ecran.blit(self.robot, (770, 250))
        
        #Textes :
        texte_joueur_bleu = police.render('Joueur', 1, (42, 51, 176))
        texte_joueur_rouge = police.render('Joueur', 1, (237, 28, 36))
        texte_vs = police.render('VS', 1, (152, 82, 51))
        texte_robot = police.render('Robot', 1, (237, 28, 36))
        
        self.ecran.blit(texte_joueur_bleu, (280, 410))
        self.ecran.blit(texte_vs, (373, 440))
        self.ecran.blit(texte_joueur_rouge, (400, 470))
        
        self.ecran.blit(texte_joueur_bleu, (800, 410))
        self.ecran.blit(texte_vs, (895, 440))
        self.ecran.blit(texte_robot, (930, 470))
        
        ###### Boutons Lancer :
        #Local :
        if bouton_clique == 'local':
            bouton_local = self.boutons['sauvegarder'][1]
            texte_lancer = police.render("Lancer" , 1, (200, 165, 80))
        else :
            bouton_local = self.boutons['sauvegarder'][0]
            texte_lancer = police.render("Lancer" , 1, (196, 144, 4))
            
        self.ecran.blit(bouton_local, (270, 510))
        self.ecran.blit(texte_lancer, (340, 530))
            
        #Robot :
        if bouton_clique == 'robot':
            bouton_robot = self.boutons['sauvegarder'][1]
            texte_lancer = police.render("Lancer" , 1, (200, 165, 80))
        else :
            bouton_robot = self.boutons['sauvegarder'][0]
            texte_lancer = police.render("Lancer" , 1, (196, 144, 4))
            
        self.ecran.blit(bouton_robot, (790, 510))
        self.ecran.blit(texte_lancer, (865, 530))
        
        #Retour :
        if bouton_clique == 'retour_menu':
            bouton_retour = self.boutons['quitter_menu'][1]
            texte1 = police.render("Retour" , 1, (224, 85, 92))
        else :
            bouton_retour = self.boutons['quitter_menu'][0]
            texte1 = police.render("Retour" , 1, (179, 12, 36))
            
        self.ecran.blit(bouton_retour, (450, 650)) 
        self.ecran.blit(texte1, (600, 670))
        
    ########################################
    ### Affichages Jeu :
    ########################################
     
    def afficher_filtre(self):
        '''
        Ajoute un effet filtre au jeu selon s'il fait Jour ou Nuit :
        : pas de return
        '''
        temps = self.attributs_jeu.acc_temps()
        #S'il fait Nuit :
        if temps == 'Nuit' :
            if self.transition < 70:
                self.transition += 1
                
        #S'il fait Jour :
        else :
            if self.transition != 0:
                self.transition -= 1
                
        filtre_bleu = pygame.Surface((800, 800), pygame.SRCALPHA)
        filtre_bleu.fill((19, 32, 76, self.transition))  # (r, g, b, alpha ) l'alpha = transparence
        self.ecran.blit(filtre_bleu, (250, 0))
        
    def afficher_terrain(self):
        '''
        Affiche le terrain
        : pas de return
        '''
        self.ecran.blit(self.image_terrain, (250, 0))
        
    def afficher_bandes(self) :
        '''
        Affiche les bandes sur les côtés gauche et droit de la fenêtre
        : pas de return
        '''
        self.ecran.blit(self.menu, (0, 0))
        self.ecran.blit(self.menu, (1050, 0))
        
    def afficher_cerisier(self):
        '''
        Affiche les cerisiers sur le terrain
        : pas de return
        '''
        self.ecran.blit(self.cerisier, (250, 0)) #Affiche le cerisier

        #Pour chaque pétale dans le tableau de pétales, désigne un rectangle rose à ces coordonnées
        for petale in self.tab_petales :
            petale.mut_y(1)
            petale.mut_x(-1)
            pygame.draw.rect(self.ecran, (252, 235, 237), (int(petale.acc_x()), petale.acc_y(), petale.taille, petale.taille))

            #Si la pétale dépasse ce cadre, on la supprime du tableau des pétales :
            if petale.acc_y() >= petale.acc_distance_max() or petale.acc_x() < 250:
                self.tab_petales.append(Petale(petale.acc_position()))
                self.tab_petales.remove(petale)
                
    def afficher_personnage_selection(self):
        '''
        Affiche le personnage sélectionné avec son image (Jour/Nuit) et des informations sur lui (Type/PV/Attaque)
        : pas de return
        '''
        perso_selection = self.attributs_jeu.acc_selection()
        if isinstance(perso_selection, module_personnage.Personnage): #si c'est un personnage
            #Index pour l'image
            if self.attributs_jeu.acc_temps() == 'Jour':
                index = 0
            else :
                index = 1
            #Image
            personnage = perso_selection.acc_personnage()
            if personnage == 'monstre':
                image = self.cadres_personnages[personnage][index]
            else :
                if perso_selection.acc_equipe() == 'rouge' :
                    image = self.cadres_personnages[personnage][index][0]
                else :
                    image = self.cadres_personnages[personnage][index][1]

            self.ecran.blit(image, (11, 12))
            self.ecran.blit(self.cadre, (6, 10))
        
            ######### Informations concernant le personnage
            ##type
            police = pygame.font.Font("medias/polices/pixelec.ttf", 17)
            texte = police.render("Type : " , 1, (152, 82, 51))
            self.ecran.blit(texte, (10, 150))
            
            texte = police.render(perso_selection.acc_personnage() , 1, (152, 82, 51))
            self.ecran.blit(texte, (10, 175))
            
            ##pv
            texte2 = police.render("Points de vie : ", 1, (152, 82, 51))
            self.ecran.blit(texte2, (10, 200))
            
            texte2 = police.render(str(perso_selection.acc_pv()) , 1, (152, 82, 51))
            self.ecran.blit(texte2, (10, 225))
            
            if personnage == 'sorciere':
                ##vérifie si le joueur clique sur une autre potion
                self.souris.potion_est_clique(self.attributs_jeu.acc_equipe_en_cours(), self.attributs_jeu.acc_selection().acc_equipe())
                #affichage des potions pour la sorciere
                texte3 = police.render("Potions : " , 1, (152, 82, 51))
                self.ecran.blit(texte3, (10, 250))
                
                ####longueur des files (nombre de potion)
                if perso_selection.acc_equipe() == 'bleu' : #équipe bleue
                    l = str(self.attributs_jeu.acc_potions_bleues()[2].acc_longueur())
                    l2 = str(self.attributs_jeu.acc_potions_bleues()[3].acc_longueur())
                    l3 = str(self.attributs_jeu.acc_potions_bleues()[4].acc_longueur())
                    potion_s = self.attributs_jeu.acc_potion_bleue_selectionnee()
                else: #équipe rouge
                    l = str(self.attributs_jeu.acc_potions_rouges()[2].acc_longueur())
                    l2 = str(self.attributs_jeu.acc_potions_rouges()[3].acc_longueur())
                    l3 = str(self.attributs_jeu.acc_potions_rouges()[4].acc_longueur())
                    potion_s = self.attributs_jeu.acc_potion_rouge_selectionnee()
                
                #potion 1 infinie visible par tous
                infini = pygame.image.load("medias/potions/infini.png")
                self.ecran.blit(infini,(70, 350))
                
                ###SORCIERE DE L'EQUIPE QUI JOUE
                if perso_selection.acc_equipe() == self.attributs_jeu.acc_equipe_en_cours() : #le joueur ne peut regarder que ses personnages
                    ##en haut à gauche
                    self.ecran.blit(self.potions[0], (47, 290))
                    ##en haut à droite
                    if l == '0' :
                        self.ecran.blit(self.potions[4], (156, 290)) #grisâtre pour montrer que c'est vide
                    else :
                        self.ecran.blit(self.potions[1], (156, 290))
                    self.ecran.blit(police.render(l , 1, (0, 0, 0)), (195, 372))
                    ##en bas à gauche
                    if l2 == '0':
                        self.ecran.blit(self.potions[5], (40, 404)) #grisâtre pour montrer que c'est vide
                    else:
                        self.ecran.blit(self.potions[2], (40, 404))
                    self.ecran.blit(police.render(l2 , 1, (0, 0, 0)), (90, 495))
                    ##en bas à droite
                    if l3 == '0':
                        self.ecran.blit(self.potions[6], (154, 404)) #grisâtre pour montrer que c'est vide
                    else :
                        self.ecran.blit(self.potions[3], (154, 404))
                    self.ecran.blit(police.render(l3 , 1, (0, 0, 0)), (200, 495))
                    
                    ###POTION perso_selectionNEE
                    dic_position_rec = {1 : (33, 286, 88),
                                    2 : (133, 286, 87),
                                    3 : (22, 400, 95),
                                    4 : (134, 400, 96)
                                    }
                    rectangle = pygame.Rect(dic_position_rec[potion_s][0], dic_position_rec[potion_s][1], dic_position_rec[potion_s][2], dic_position_rec[potion_s][2])
                    #pour clignoter
                    if 0 <= self.attributs_jeu.acc_compteur() <= 48:
                        couleur = (0, 0, 0) #noir
                    else :
                        couleur = (224, 209, 146) #couleur de fond
                    pygame.draw.rect(self.ecran, couleur, rectangle, 2) #(surface, couleur, figure (x, y, longueur, hauteur), si contour → épaisseur)
                    ####INFOBULLE
                    dic_phrase = {1 : 'inflige des dégâts',
                                  2 : 'soigne',
                                  3 : 'tue',
                                  4 : "fait changer d'équipe"
                                 }
                    pos_souris = self.souris.acc_position_curseur()
                    
                    if rectangle.collidepoint(pos_souris): #si la souris est sur le rectangle
                        # Afficher une info-bulle
                        infobulle_texte = police.render(dic_phrase[potion_s], True, (0, 0, 0))
                        infobulle_rect = infobulle_texte.get_rect()
                        infobulle_rect.topleft = (pos_souris[0] - 4, pos_souris[1] - 18) #un peu en dessous du curseur
                        pygame.draw.rect(self.ecran, (152, 82, 51), infobulle_rect)
                        self.ecran.blit(infobulle_texte, infobulle_rect)
                
                ###SORCIERE ADVERSE
                else:
                    #point d'interrogation pour ne pas voir le nombre de potions
                    point_interrogation = pygame.image.load("medias/potions/point_interrogation.png")
                    self.ecran.blit(point_interrogation,(70, 350))
                    self.ecran.blit(point_interrogation,(195, 372))
                    self.ecran.blit(point_interrogation,(90, 495))
                    self.ecran.blit(point_interrogation,(210, 495))
                    ##en haut à gauche
                    self.ecran.blit(self.potions[0], (47, 290))
                    ##en haut à droite
                    self.ecran.blit(self.potions[1], (156, 290))
                    ##en bas à gauche
                    self.ecran.blit(self.potions[2], (40, 404))
                    ##en bas à droite
                    self.ecran.blit(self.potions[3], (154, 404))
                
            else :
                #si c'est un personnage lambda, on lui affiche ses dégâts d'attaque
                texte3 = police.render("Attaque : " , 1, (152, 82, 51))
                self.ecran.blit(texte3, (10, 250))
                if perso_selection.acc_equipe() == 'bleu' :
                    texte3 = police.render(str(module_personnage.DIC_ATTAQUES_BLEU[perso_selection.acc_personnage()]) , 1, (152, 82, 51))
                else:
                    texte3 = police.render(str(module_personnage.DIC_ATTAQUES_ROUGE[perso_selection.acc_personnage()]) , 1, (152, 82, 51))
                self.ecran.blit(texte3, (10, 275))
                
    def afficher_equipe_en_cours(self):
        '''
        Affiche l'équipe en cours avec le nombre d'action qui lui reste
        : pas de return
        '''
        police = pygame.font.Font("medias/polices/pixelec.ttf", 17)
        
        #Tour du Joueur :
        texte = police.render("Tour du joueur :" , 1, (152, 82, 51))
        self.ecran.blit(texte, (10, 600))
        
        #Si l'équipe en cours est l'équipe bleu, affiche la "phrase" en bleu :
        if self.attributs_jeu.acc_equipe_en_cours() == 'bleu':
            texte = police.render('Bleu n° ' + str(self.attributs_jeu.acc_nombre_action()) + ' / 3' , 1, (42, 51, 176))
        
        #Sinon, l'équipe en cours est l'équipe rouge, affiche la "phrase" en rouge :
        else :
            texte = police.render('Rouge n° ' + str(self.attributs_jeu.acc_nombre_action()) + ' / 3' , 1, (237, 28, 36))
        
        self.ecran.blit(texte, (10, 620))
        
    def afficher_console(self):
        '''
        affiche le console où sera écrit chaque action des équipes
        : pas de return
        '''
        police = pygame.font.Font("medias/polices/police_console.ttf", 13)
        pile = self.attributs_jeu.acc_console()
        stock = module_lineaire.Pile()
        hauteur = 570 #Hauteur où s'affiche la phrase sur la fenêtre pygame
        
        #Dépile la pile est affiche le texte avec la couleur demandé :
        while not pile.est_vide() :
            tab = pile.depiler() #Dépile la phrase et ses paramètres de la pile principale
            stock.empiler(tab) #Empile la phrase et ses paramètres dans le stock
            
            #Si la couleur demandée est bleu, change la couleur de la police en bleu :
            if tab[1] == 'bleu':
                texte = police.render(tab[0] , 1, (42, 51, 176))
                
            #Si la couleur demandée est rouge, change la couleur de la police en rouge :
            elif tab[1] == 'rouge' :
                texte = police.render(tab[0], 1, (237, 28, 36))
            
            #Sinon, la couleur demandée est noir, change la couleur de la police en noir :
            else :
                texte = police.render(tab[0], 1, (0, 0, 0))
            
            hauteur -= 19
            
            self.ecran.blit(texte, (1058, hauteur))
        
        #Rempile toutes les phrases (et leurs paramètres) stockés dans la pile principale
        while not stock.est_vide() :
            pile.empiler(stock.depiler())
            
    def afficher_annonce_coffre(self):
        '''
        Affiche l'annonce du coffre une fois celui-ci ouvert
        : pas de return
        '''
        if self.attributs_jeu.acc_annonce_coffre():
            if self.direction == 'diminution':
                self.opacite -= 2
                if self.opacite <= 0:
                    self.direction = 'augmentation'
            else:
                self.opacite += 2
                if self.opacite >= 100:
                    self.direction = 'diminution'
                    self.attributs_jeu.mut_annonce_coffre(False)
            
            filtre_annonce = pygame.Surface((800, 800), pygame.SRCALPHA)
            filtre_annonce.fill((0, 0, 0, 100 - int(self.opacite)))  
            self.ecran.blit(filtre_annonce, (250, 0))
            
            num = self.attributs_jeu.event_coffre
            if num in [5, 9, 10] : #malus
                couleur_texte = (205, 69, 40, 100 - int(self.opacite))#Couleur du texte (rouge) avec une transparence de 128 (sur 255)
            else :
                couleur_texte = (110, 218, 35, 100 - int(self.opacite)) #Vert
            police = pygame.font.Font("medias/polices/pixelec.ttf", 30)
            texte_surface = police.render(self.rep_contenu[num], True, couleur_texte) #le True, est pour l'antialiasing, pour rendre les bords du texte plus lisses en ajoutant des pixels semi-transparents autour des bords
            position_texte = (430, 400)
            self.ecran.blit(texte_surface, position_texte)
            
    def afficher_boutons_jeu(self):
        '''
        Affiche les différents boutons du jeu
        : pas de return
        '''
        police = pygame.font.Font("medias/polices/pixelec.ttf", 21)
        bouton_clique = self.attributs_jeu.acc_bouton_clique()
        
        if bouton_clique == 'options':
            bouton_options = self.boutons['options'][1]
            texte = police.render("Options" , 1, (77, 148, 219))
        else :
            bouton_options = self.boutons['options'][0]
            texte = police.render("Options" , 1, (15, 75, 117))
        self.ecran.blit(bouton_options, (6, 655))
        self.ecran.blit(texte, (78, 675))
        
        if bouton_clique == 'menu':
            bouton_menu = self.boutons['quitter'][1]
            texte = police.render("Menu" , 1, (224, 85, 92))
        else :
            bouton_menu = self.boutons['quitter'][0]
            texte = police.render("Menu" , 1, (237, 28, 36))
        self.ecran.blit(bouton_menu, (6, 725))
        self.ecran.blit(texte, (92, 745))
        
        if bouton_clique == 'quitter':
            bouton_quitter = self.boutons['quitter'][1]
            texte = police.render("Quitter" , 1, (224, 85, 92))
        else :
            bouton_quitter = self.boutons['quitter'][0]
            texte = police.render("Quitter" , 1, (237, 28, 36))
        self.ecran.blit(bouton_quitter, (1056, 725))
        self.ecran.blit(texte, (1115, 745))
        
        if bouton_clique == 'charger':
            bouton_charger = self.boutons['charger'][1]
            texte1 = police.render("Charger" , 1, (200, 165, 80))
        else :
            bouton_charger = self.boutons['charger'][0]
            texte1 = police.render("Charger" , 1, (196, 144, 4))
        self.ecran.blit(bouton_charger, (1056, 655)) #65 image + 5 écart avec quitter
        self.ecran.blit(texte1, (1117, 675))
            
        if bouton_clique == 'sauvegarder':
            bouton_sauvegarde = self.boutons['sauvegarder'][1]
            texte2 = police.render("Sauvegarder" , 1, (145, 173, 73))
        else :
            bouton_sauvegarde = self.boutons['sauvegarder'][0]
            texte2 = police.render("Sauvegarder" , 1, (106, 143, 20))   
        self.ecran.blit(bouton_sauvegarde, (1056, 585)) # 5 d'écart avec charger
        self.ecran.blit(texte2, (1087, 605))
        
    def afficher_personnages(self):
        '''
        Affiche les personnages et un contour de couleur pour chaque personnages de l'équipe en cours (si activé dans les options)
        : pas de return
        '''
        #Personnages/Monstres :
        for personnage in self.attributs_jeu.acc_tab_personnages() + self.attributs_jeu.acc_tab_monstres() :
            #Nom/Coordonnées/Equipe/Endommagé du personnage :
            nom = personnage.acc_personnage()
            x = personnage.acc_x() * 38 + 250
            y = personnage.acc_y() * 38
            equipe = personnage.acc_equipe()
            endommage = personnage.acc_endommage()
            soigne = personnage.acc_soigne()
            attaque = personnage.acc_attaque()
            
            #Contour de couleur (si l'option est activé, le personnage est de l'équipe en cours et que le personnage n'est pas en déplacement) :   
            if self.jeu.acc_sols_de_couleur() and equipe == self.attributs_jeu.acc_equipe_en_cours() and self.attributs_jeu.acc_personnage_en_deplacement() != personnage :
                if nom == 'geant':
                    if personnage.acc_numero_geant() == 0:
                        self.ecran.blit(self.sol_geants[equipe], (x, y))
                else :
                    self.ecran.blit(self.sol_personnages[equipe], (x , y))
            
            ##Si le personnage est en train d'attaque un autre personnage (seules les animations d'attaque de l'archère sont disponibles)            
            if attaque and nom == 'archere' :
                attaques = self.personnages_attaque[nom] #Appel les différentes images du personnage
                nb = self.attributs_jeu.acc_attaque_temps()
                #réglages pour l'animation
                if nb <= 1 or nb >= 17 :
                    nb = 0
                elif nb <= 3 or nb >= 15:
                    nb = 1
                elif nb <= 5 or nb >= 13:
                    nb = 2
                else :
                    nb = 3
                #Si le personnage est de l'équipe rouge :
                if equipe == 'rouge' :
                    self.ecran.blit(attaques[0][nb], (x , y))
                #Sinon, le personnage est de l'équipe bleu :
                else :
                    self.ecran.blit(attaques[1][nb], (x , y))
                    
            ##si le personnage est endommagé ou soigné :
            elif endommage or soigne :
                if endommage :
                    tableau = self.personnages_endommages[nom] #Appel les différentes images du personnage
                else :
                    tableau = self.personnages_soins[nom]
                #Si le personnage est un monstre :
                if nom == 'monstre' :
                    self.ecran.blit(tableau[0], (x , y))
                #Si le personnage est de l'équipe rouge :
                elif equipe == 'rouge' :
                    #Si le personnage est un Géant :
                    if nom == 'geant' :
                        self.ecran.blit(tableau[0][personnage.acc_numero_geant()], (x , y))   
                    #Sinon, le personnage est "classique"
                    else :
                        self.ecran.blit(tableau[0], (x , y))
                #Sinon, le personnage est de l'équipe bleu :
                else :
                    #Si le personnage est un Géant :
                    if nom == 'geant' :
                        self.ecran.blit(tableau[1][personnage.acc_numero_geant()], (x , y))   
                    #Sinon, le personnage est "classique"
                    else :
                        self.ecran.blit(tableau[1], (x , y))
                
            #Animations (sinon si le personnage n'est pas en déplacement):
            elif self.attributs_jeu.acc_personnage_en_deplacement() != personnage :
                images_personnage = self.personnages[nom] #Appelle les différentes images du personnage
                nombre_images = len(images_personnage[0])
                index_image = int(self.attributs_jeu.acc_compteur() / 70 * nombre_images)
                
                #Si le personnage est un monstre :
                if nom == 'monstre' and not personnage in self.attributs_jeu.acc_monstres_a_deplacer() :
                    #Si le monstre est sous terre :
                    if personnage.acc_etat() == 1: 
                        self.ecran.blit(images_personnage[0][index_image], (x, y))
                    #Sinon, le monstre est hors de la terre :
                    else: 
                        self.ecran.blit(images_personnage[1][index_image], (x, y))
                #Sinon, le personnage n'est pas un monstre
                elif nom != 'monstre' :   
                    #Si le personnage est de l'équipe rouge :
                    if equipe == 'rouge' :
                        #Si le personnage est un Géant :
                        if nom == 'geant' :
                            self.ecran.blit(images_personnage[1][index_image][personnage.numero_geant], (x, y))  
                        #Sinon, le personnage est "classique"
                        else :
                            self.ecran.blit(images_personnage[0][index_image], (x, y))      
                    #Sinon, le personnage est de l'équipe bleu :
                    else :
                        #Si le personnage est un Géant :
                        if nom == 'geant' :
                            self.ecran.blit(images_personnage[0][index_image][personnage.numero_geant], (x, y))  
                        #Sinon, le personnage est "classique"
                        else :
                            self.ecran.blit(images_personnage[1][index_image], (x, y))
                
        #Coffres :
        for coffre in self.attributs_jeu.acc_tab_coffres() :
            #Coordonnées/Etat/Images du coffre :
            x = coffre.acc_x() * 38 + 250
            y = coffre.acc_y() * 38
            etat_ouvert = coffre.acc_est_ouvert()
            #Si le coffre est dans son état ouverture :
            if etat_ouvert :
                self.ecran.blit(self.images_coffre[coffre.acc_avancement_ouverture()], (x, y))
                #Pour animation de l'ouverture
                if coffre.avancement_ouverture < 10 and self.attributs_jeu.acc_compteur() % 3 == 0 :
                    coffre.mut_avancement_ouverture(coffre.acc_avancement_ouverture() + 1) #Augmente l'avancement de l'ouverture du coffre de 1
            #Sinon, le coffre n'est pas ouvert :     
            else :
                self.ecran.blit(self.images_coffre[0], (x, y))
                
    def afficher_deplacements(self):
        '''
        Affiche les déplacements possibles sur la grille
        : pas de return
        '''
        #Pour chaque coordonnées des cases du tableau des déplacements que le personnage peut effectuer :
        
        for coordonnees in self.attributs_jeu.acc_deplacements_coord() :
            case_x = coordonnees[0]
            case_y = coordonnees[1]
            self.ecran.blit(self.deplacements, (case_x, case_y, 38, 38))
            
    def afficher_personnage_en_deplacement(self):
        '''
        Affiche le personnage en déplacement
        : pas de return
        '''
        #S'il y a un déplacement en cours et qu'il n'y a aucun personnage sélectionné :
        if self.attributs_jeu.acc_deplacement_en_cours() and self.attributs_jeu.acc_selection() != None :
            
            if self.attributs_jeu.acc_indice_courant() < len(self.attributs_jeu.acc_chemin()) - 1 :
                destination = self.attributs_jeu.acc_chemin()[self.attributs_jeu.acc_indice_courant() + 1]
                x, y = self.attributs_jeu.acc_coordonnees_personnage()

                #Calcule le vecteur de déplacement :
                dx = min(max(destination[0] - x, -3), 3)
                dy = min(max(destination[1] - y, -3), 3)
                
                #Met à jour les coordonnées du personnage:
                self.attributs_jeu.mut_coordonnees_personnage((x + dx, y + dy))
                
                #Affichage du personnage :
                perso = self.attributs_jeu.acc_personnage_en_deplacement()
                if isinstance(perso, module_personnage.Personnage):
                    image = self.personnages_deplacement[perso.acc_personnage()]
                    #Si l'équipe du personnage en déplacement est l'équipe rouge, affiche le personnage en rouge :
                    if perso.acc_equipe() == 'rouge' :
                        image_personnage = image[0]
                    
                    #Sinon, l'équipe du personnage en déplacement est l'équipe rouge, affiche le personnage en rouge :
                    else :
                        image_personnage = image[1]
                        
                    self.ecran.blit(image_personnage, self.attributs_jeu.acc_coordonnees_personnage())
                    
                    #Vérifier si le personnage atteint la destination
                    if self.attributs_jeu.acc_coordonnees_personnage() == destination :
                        self.attributs_jeu.mut_indice_courant(self.attributs_jeu.acc_indice_courant() + 1)
                    
    def afficher_monstres_en_deplacement(self):
        '''
        affiche les monstres en déplacement
        : pas de return
        '''
        for monstre in self.attributs_jeu.acc_monstres_a_deplacer() : #chaque monstre à déplacer
            
            
            if monstre.acc_futur_x() == None and monstre.acc_futur_y() == None:
                case = monstre.prochaines_coordonnees(self.terrain, self.attributs_jeu.acc_equipe_en_cours())
                monstre.mut_futur_x(case[0])
                monstre.mut_futur_y(case[1])
                monstre.mut_futur_coordonnees_x(250 + monstre.acc_futur_x() * 38)
                monstre.mut_futur_coordonnees_y(monstre.acc_futur_y() * 38)
                
            if monstre.coordonnees_x != monstre.futur_coordonnees_x :
                dx = min(max(monstre.futur_coordonnees_x - monstre.coordonnees_x, -3), 3)
                monstre.coordonnees_x += dx
            if monstre.coordonnees_y != monstre.futur_coordonnees_y :
                dy = min(max(monstre.futur_coordonnees_y - monstre.coordonnees_y, -3), 3)
                monstre.coordonnees_y += dy

            # affichage du monstre :
            image_monstre = self.personnages_deplacement['monstre'][0]
            self.ecran.blit(image_monstre, (monstre.acc_coordonnees_x(), monstre.acc_coordonnees_y()))
            
            if monstre.acc_coordonnees_x() == monstre.acc_futur_coordonnees_x() and monstre.acc_coordonnees_y() == monstre.acc_futur_coordonnees_y() :
                self.terrain.mut_terrain(monstre.acc_x(), monstre.acc_y(), ' ') #un vide à la place de l'ancienne case
                monstre.deplacer(monstre.acc_futur_x(), monstre.acc_futur_y()) # déplace le monstre
                self.terrain.mut_terrain(monstre.acc_x(), monstre.acc_y(), monstre) # place le monstre à sa nouvelle position
                self.attributs_jeu.enlever_monstres_a_deplacer(monstre)
                monstre.mut_futur_x(None)
                monstre.mut_futur_y(None)
            
            if self.attributs_jeu.acc_monstres_a_deplacer() == [] :
                self.attributs_jeu.mut_deplacement_en_cours(False)
            
    def afficher_attaques(self):
        '''
        Affiche les attaques possibles sur la grille
        : pas de return
        '''
        #Pour chaque coordonnées des cases du tableau des attaques que le personnage peut effectuer :
        for coordonnees in self.attributs_jeu.acc_attaques():
            case_x = coordonnees[0] * 38 + 250
            case_y = coordonnees[1] * 38
            perso = self.terrain.acc_terrain(coordonnees[0], coordonnees[1])
            if perso.acc_equipe() == self.attributs_jeu.acc_selection().acc_equipe() :
                image = self.attaques[1] #guérison
            else:
                image = self.attaques[0] #attaque
            ##géant
            if perso.acc_personnage() == 'geant':
                #ajustement pour atteindre la case en haut à droite
                if perso.acc_numero_geant() == 0:
                    case_x += 38
                elif perso.acc_numero_geant() == 2:
                    case_x += 38
                    case_y -= 38
                elif perso.acc_numero_geant() == 3:
                    case_y -= 38
            self.ecran.blit(image, (case_x, case_y, 38, 38)) #attaque
            
    def afficher_tombes(self):
        '''
        Affiche des tombes sur la case sur laquelle un personnage est mort
        : pas de return
        '''
        #Pour chaque tombe dans le tableau de tombes, on affiche une tombe à ses coordonnées x et y :
        for tombe in self.attributs_jeu.acc_positions_tombes():
            self.ecran.blit(self.image_tombe, (tombe[0], tombe[1]))
            
    def afficher_cases_potions(self):
        '''
        Affiche les cases où la potion a éclaté avec un effet de bulles
        : pas de return
        '''
        equipe = self.attributs_jeu.acc_equipe_en_cours()
        #potion sélectionnée
        if equipe == 'bleu':
            potion = self.attributs_jeu.acc_potion_bleue_selectionnee()
        else:
            potion = self.attributs_jeu.acc_potion_rouge_selectionnee()
        ##réglages pour l'animation
        attaque1 = self.attributs_jeu.acc_attaque_temps()
        attaque = attaque1 // 3
        if attaque1 > 23:
            attaque -= 8
        
        bulles = self.bulles
        #pour chaque case atteinte dans l'attribut cases_potions
        for case in self.attributs_jeu.acc_cases_potions():
            new_case = (case[0] * 38 + 250, case[1] *38)
            self.ecran.blit(bulles[self.dic_couleurs[potion]][attaque], new_case)

    def afficher_fin_jeu(self):
        '''
        affiche le menu de la fin du jeu
        : pas de return
        '''
        #Si le cadre ne descend pas trop bas (y <= 204)
        if self.attributs_jeu.acc_position_y_menu_fin() != 204 :
            self.attributs_jeu.ajouter_position_y_menu_fin(3)
        
        #Affichage le cadre :
        self.ecran.blit(self.menu_fin, (455, self.attributs_jeu.acc_position_y_menu_fin()))
        
        #Affichage le texte :
        police = pygame.font.Font("medias/polices/pixelec.ttf", 30)
        
        #Si l'équipe gagnante est l'équipe bleu, affiche la phrase et la couleur correspondante :
        if self.attributs_jeu.acc_equipe_gagnante() == 'bleu':
            annonce = police.render("L'equipe bleue" , 1, (42, 51, 176))
            annonce2 = police.render("gagne !" , 1, (42, 51, 176))
            self.ecran.blit(annonce, (470, self.attributs_jeu.acc_position_y_menu_fin() + 20))
            self.ecran.blit(annonce2, (570, self.attributs_jeu.acc_position_y_menu_fin() + 50))
        
        #Sinon, l'équipe gagnante est l'équipe rouge, affiche la phrase et la couleur correspondante :
        elif self.attributs_jeu.acc_equipe_gagnante() == 'rouge'  :
            annonce = police.render("L'equipe rouge" , 1, (237, 28, 36))
            annonce2 = police.render("gagne !" , 1, (237, 28, 36))
            self.ecran.blit(annonce, (470, self.attributs_jeu.acc_position_y_menu_fin() + 20))
            self.ecran.blit(annonce2, (570, self.attributs_jeu.acc_position_y_menu_fin() + 50))
        #Sinon, les monstres ont gagné !  
        else:
            annonce = police.render("Les monstres" , 1, (138, 131, 131))
            annonce2 = police.render("gagnent !" , 1, (138, 131, 131))
            self.ecran.blit(annonce, (470, self.attributs_jeu.acc_position_y_menu_fin() + 20))
            self.ecran.blit(annonce2, (570, self.attributs_jeu.acc_position_y_menu_fin() + 50))
        
        #Affichage les boutons :
        police2 = pygame.font.Font("medias/polices/pixelec.ttf", 21)
        
        if self.attributs_jeu.acc_bouton_clique() == 'menu':
            bouton_rejouer = self.boutons['rejouer'][1]
            texte2 = police2.render("Menu" , 1, (145, 173, 73))
        
        else :
            bouton_rejouer = self.boutons['rejouer'][0]
            texte2 = police2.render("Menu" , 1, (106, 143, 20))   
        
        self.ecran.blit(bouton_rejouer, (515, self.attributs_jeu.acc_position_y_menu_fin() + 230)) # 5 d'écart avec charger
        self.ecran.blit(texte2, (600, self.attributs_jeu.acc_position_y_menu_fin() + 250))
        
        if self.attributs_jeu.acc_bouton_clique() == 'quitter_fin':
            bouton_quitter = self.boutons['quitter_fin'][1]
            texte2 = police2.render("Quitter" , 1, (224, 85, 92))
        
        else :
            bouton_quitter = self.boutons['quitter_fin'][0]
            texte2 = police2.render("Quitter" , 1, (237, 28, 36))   
        
        self.ecran.blit(bouton_quitter, (515, self.attributs_jeu.acc_position_y_menu_fin() + 310)) # 5 d'écart avec charger
        self.ecran.blit(texte2, (580, self.attributs_jeu.acc_position_y_menu_fin() + 330))
        
    def afficher_position_souris(self) :
        '''
        Affiche les coordonnées de la case à la position de la souris
        : pas de return
        '''
        position_case = self.souris.acc_position_case()
        if position_case[0] >= 0 and position_case[0] <= 20 and position_case[1] >= 0 and position_case[1] <= 20:
            police = pygame.font.Font("medias/polices/pixelec.ttf", 17)
            texte = police.render("Case : (" + self.attributs_jeu.acc_dic_alphabet()[position_case[0]] + ", " + str(position_case[1]) + ")", 1, (152, 82, 51))
            
            self.ecran.blit(texte, (10, 570))
        
    ######################################################
    ### Affichages Globales :
    ######################################################
    
    def afficher_menu(self) :
        '''
        Affiche tous les objets du menu sur la fenêtre pygame
        : pas de return
        '''
        self.afficher_fond()
        
        
        if self.attributs_jeu.acc_menu_options() :  
            self.afficher_menu_options()
            
        elif self.attributs_jeu.acc_menu_modes() :
            self.afficher_menu_modes()
            
        else :
            self.afficher_boutons_menu()
        
        self.afficher_curseur()
            
    def afficher_jeu(self):
        '''
        Affiche tous les objets du jeu sur la fenêtre pygame
        : pas de return
        '''
        self.afficher_bandes()
        
        #Milieu :
        self.afficher_terrain()
        self.afficher_tombes()
        self.afficher_personnages()
        self.afficher_cases_potions()
        
        #Si l'option deplacement/attaques est activé, alors on affiche l'aide de déplacements/attaques :
        if self.jeu.acc_deplacements_attaques() :
            self.afficher_deplacements()
            self.afficher_attaques()
            
        self.afficher_personnage_en_deplacement()
        self.afficher_monstres_en_deplacement()
        self.afficher_cerisier()
        
        #Si la partie est terminée :
        if self.attributs_jeu.acc_partie_terminee() :
            self.afficher_fin_jeu()
        
        #Côté Droit :
        self.afficher_boutons_jeu()
        
        #Si l'option console est activé, alors on l'affiche :
        if self.jeu.acc_option_console() :   
            self.afficher_console()
        
        #Côté Gauche :
        self.afficher_personnage_selection()
        self.afficher_equipe_en_cours()
        self.afficher_position_souris()
        
        #Tout :
        self.afficher_filtre()
        self.afficher_annonce_coffre()
        
        #Si options :
        if self.attributs_jeu.acc_menu_options() :
            self.afficher_fond()
            self.afficher_menu_options()
        
        self.afficher_curseur()