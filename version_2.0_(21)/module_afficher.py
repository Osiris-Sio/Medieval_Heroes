# -*- coding: utf-8 -*-

'''
-> Medieval Fight : Module pour la classe Affichage.

Auteurs : AMEDRO Louis / LAPÔTRE Marylou / MAILLET Paul 
'''

######################################################
### Importation Modules :
######################################################

import pygame, random, module_personnage, module_objets
from graphe import module_lineaire

######################################################
### Classe Pétale :
######################################################

class Petale():
    def __init__(self, position):
        
        self.size = random.randint(1, 3)
        self.position = position
        
        if self.position == 'haut_gauche':
            self.x = random.randint(317, 378)
            self.y = random.randint(225, 278)
                    
        elif self.position == 'haut_droit':
            self.x = random.randint(925, 975)
            self.y = random.randint(231, 277)
                    
        elif self.position == 'bas_gauche':
            self.x = random.randint(317, 378)
            self.y = random.randint(500, 550)
                    
        else :
            self.x = random.randint(925, 975)
            self.y = random.randint(500, 550)
                
        if self.position == 'bas_gauche' or self.position == 'bas_droit':
            self.distance_max = random.randint(595, 660)
        else :
            self.distance_max = random.randint(295, 360)
        

######################################################
### Classe Affichage :
######################################################

class Affichage():
    '''
    Une classe Affichage qui gére les objets à afficher.
    '''

    def __init__(self, attributs_jeu, terrain, ecran, clavier_souris):
        '''
        Initialise l'affichage
        '''
        # Attributs Paramètres :
        self.attributs_jeu = attributs_jeu
        self.terrain = terrain
        self.ecran = ecran
        self.clavier_souris = clavier_souris
        
        
        # Attributs Ressources (pour charger les ressources):
        # Menu :
        self.icone = pygame.image.load('medias/img_jeu.png')
        pygame.display.set_icon(self.icone) #Ajoute l'icone à la fenêtre
        
        self.menu = pygame.image.load("medias/menu4.png")
        self.fond_options = pygame.image.load("medias/menu_param.png")
        
        self.menu_fin = pygame.image.load("medias/menu_fin.png")
        # décor
        self.images_coffre = [pygame.image.load("medias/coffre/coffre_non_ouvert.png"), pygame.image.load("medias/coffre/c1.png"), pygame.image.load("medias/coffre/c2.png"), pygame.image.load("medias/coffre/c3.png"), pygame.image.load("medias/coffre/c4.png"), pygame.image.load("medias/coffre/c5.png"), pygame.image.load("medias/coffre/c6.png"), pygame.image.load("medias/coffre/c7.png"), pygame.image.load("medias/coffre/c8.png"), pygame.image.load("medias/coffre/c9.png"), pygame.image.load("medias/coffre/coffre_ouvert.png")]
        self.image_tombe = pygame.image.load("medias/tombe1.png")
        
        # Curseur :
        self.curseur_normal = pygame.image.load("medias/curseur0.png")
        self.curseur_appuye = pygame.image.load("medias/curseur1.png")

        self.attaques = pygame.image.load("medias/attaque_possible.png")
        self.deplacements = pygame.image.load("medias/deplacement.png")
        
        # Terrain :
        self.image_terrain = pygame.image.load("medias/21x21.png")
        
        # fond d'écran
        self.image_fond = pygame.image.load("medias/fond_menu.png")
        # cerisiers
        self.cerisier = pygame.image.load("medias/cerisier.png")
        self.petals = [Petale('haut_gauche'), Petale('haut_gauche'), Petale('haut_droit'),  Petale('haut_droit'), Petale('bas_gauche'), Petale('bas_gauche'), Petale('bas_droit'),  Petale('bas_droit')]
        self.distance_max = random.randint(300, 360)
        
        #Filtres
        
        self.transition = 0
        
        self.temps_annonce = 0
        self.opacite = 100
        self.direction = 'diminution'
        
        #Sol (contour du personnage) :
        
        self.sol_personnages = {
            'rouge' : pygame.image.load("medias/sol_r.png"),
            'bleu' : pygame.image.load("medias/sol_b.png"),
        }
        
        #reponses coffre
        self.rep_contenu = {1 : 'Bonus de vie',
                    2 : 'Meteorite',
                    3 : 'Changement de personnage',
                    4 : 'Nuage de fumee',
                    5 : "Degats d'attaque",
                    6 : "Geant allié",
                    7 : "Geant ennemi",
                    8 : "Necromancie",
                    }
        
        #Personnages :
        
        self.personnages = {
            'paladin': [
                [pygame.image.load("medias/paladin/paladin1.png"), pygame.image.load("medias/paladin/paladin2.png")],
                [pygame.image.load("medias/paladin/paladinb1.png"), pygame.image.load("medias/paladin/paladinb2.png")]
            ],
            'poulet': [
                [pygame.image.load("medias/poulet/pr1.png"), pygame.image.load("medias/poulet/pr2.png"), pygame.image.load("medias/poulet/pr3.png"), pygame.image.load("medias/poulet/pr2.png") , pygame.image.load("medias/poulet/pr2.png")],
                [pygame.image.load("medias/poulet/pb1.png"), pygame.image.load("medias/poulet/pb2.png"), pygame.image.load("medias/poulet/pb3.png"), pygame.image.load("medias/poulet/pb2.png"), pygame.image.load("medias/poulet/pb2.png")]
            ],
            'geant': [
                [
                    [pygame.image.load("medias/geant/gb1.png"), pygame.image.load("medias/geant/gb2.png"), pygame.image.load("medias/geant/gb3.png"), pygame.image.load("medias/geant/gb4.png")],
                    [pygame.image.load("medias/geant/gb11.png"), pygame.image.load("medias/geant/gb22.png"), pygame.image.load("medias/geant/gb33.png"), pygame.image.load("medias/geant/gb44.png")]
                ],
                [
                    [pygame.image.load("medias/geant/gr1.png"), pygame.image.load("medias/geant/gr2.png"), pygame.image.load("medias/geant/gr3.png"), pygame.image.load("medias/geant/gr4.png")],
                    [pygame.image.load("medias/geant/gr11.png"), pygame.image.load("medias/geant/gr22.png"), pygame.image.load("medias/geant/gr33.png"), pygame.image.load("medias/geant/gr44.png")]
                ]
            ],
            'cavalier': [
                [pygame.image.load("medias/cavalier/cr1.png"), pygame.image.load("medias/cavalier/cr2.png"), pygame.image.load("medias/cavalier/cr3.png"), pygame.image.load("medias/cavalier/cr4.png"), pygame.image.load("medias/cavalier/cr5.png"), pygame.image.load("medias/cavalier/cr6.png"), pygame.image.load("medias/cavalier/cr7.png"), pygame.image.load("medias/cavalier/cr8.png")],
                [pygame.image.load("medias/cavalier/cb1.png"), pygame.image.load("medias/cavalier/cb2.png"), pygame.image.load("medias/cavalier/cb3.png"), pygame.image.load("medias/cavalier/cb4.png"), pygame.image.load("medias/cavalier/cb5.png"), pygame.image.load("medias/cavalier/cb6.png"), pygame.image.load("medias/cavalier/cb7.png"), pygame.image.load("medias/cavalier/cb8.png")]
            ],
            'archere': [
                [pygame.image.load("medias/archere/ar2.png"),pygame.image.load("medias/archere/ar1.png")],
                [pygame.image.load("medias/archere/ab1.png"),pygame.image.load("medias/archere/ab2.png")]],
            'sorciere': [
                [pygame.image.load("medias/sorciere/sor1.png"),pygame.image.load("medias/sorciere/sor2.png")],
                [pygame.image.load("medias/sorciere/sob1.png"),pygame.image.load("medias/sorciere/sob2.png")]],
            'ivrogne': [
                [pygame.image.load("medias/ivrogne/ir1.png"), pygame.image.load("medias/ivrogne/ir2.png"), pygame.image.load("medias/ivrogne/ir3.png"), pygame.image.load("medias/ivrogne/ir4.png"), pygame.image.load("medias/ivrogne/ir3.png"), pygame.image.load("medias/ivrogne/ir2.png")],
                [pygame.image.load("medias/ivrogne/ib1.png"), pygame.image.load("medias/ivrogne/ib2.png"), pygame.image.load("medias/ivrogne/ib3.png"), pygame.image.load("medias/ivrogne/ib4.png"), pygame.image.load("medias/ivrogne/ib3.png"),pygame.image.load("medias/ivrogne/ib2.png"),]],
            'barbare': [
                [pygame.image.load("medias/barbare/br1.png"), pygame.image.load("medias/barbare/br2.png")],
                [pygame.image.load("medias/barbare/bb1.png"), pygame.image.load("medias/barbare/bb2.png")]],
            'cracheur de feu': [
                [pygame.image.load("medias/cracheur_de_feu/rouge/c66.png"), pygame.image.load("medias/cracheur_de_feu/rouge/c55.png"), pygame.image.load("medias/cracheur_de_feu/rouge/c44.png"), pygame.image.load("medias/cracheur_de_feu/rouge/c33.png"), pygame.image.load("medias/cracheur_de_feu/rouge/c22.png"), pygame.image.load("medias/cracheur_de_feu/rouge/c11.png"), pygame.image.load("medias/cracheur_de_feu/rouge/c1.png"), pygame.image.load("medias/cracheur_de_feu/rouge/c2.png"), pygame.image.load("medias/cracheur_de_feu/rouge/c3.png"), pygame.image.load("medias/cracheur_de_feu/rouge/c4.png"), pygame.image.load("medias/cracheur_de_feu/rouge/c5.png"),pygame.image.load("medias/cracheur_de_feu/rouge/c6.png")],
                [pygame.image.load("medias/cracheur_de_feu/bleu/c66.png"), pygame.image.load("medias/cracheur_de_feu/bleu/c55.png"), pygame.image.load("medias/cracheur_de_feu/bleu/c44.png"), pygame.image.load("medias/cracheur_de_feu/bleu/c33.png"), pygame.image.load("medias/cracheur_de_feu/bleu/c22.png"), pygame.image.load("medias/cracheur_de_feu/bleu/c11.png"), pygame.image.load("medias/cracheur_de_feu/bleu/c1.png"), pygame.image.load("medias/cracheur_de_feu/bleu/c2.png"), pygame.image.load("medias/cracheur_de_feu/bleu/c3.png"), pygame.image.load("medias/cracheur_de_feu/bleu/c4.png"), pygame.image.load("medias/cracheur_de_feu/bleu/c5.png"),pygame.image.load("medias/cracheur_de_feu/bleu/c6.png")]],
            'valkyrie': [
                [pygame.image.load("medias/valkyrie/vr1.png"), pygame.image.load("medias/valkyrie/vr2.png")],
                [pygame.image.load("medias/valkyrie/vb1.png"), pygame.image.load("medias/valkyrie/vb2.png")]],
            'mage': [
                [pygame.image.load("medias/mage/rouge/sr1.png"), pygame.image.load("medias/mage/rouge/sr2.png"), pygame.image.load("medias/mage/rouge/sr3.png"), pygame.image.load("medias/mage/rouge/sr4.png"), pygame.image.load("medias/mage/rouge/sr5.png"), pygame.image.load("medias/mage/rouge/sr6.png"), pygame.image.load("medias/mage/rouge/sr7.png"), pygame.image.load("medias/mage/rouge/sr8.png"), pygame.image.load("medias/mage/rouge/sr9.png"), pygame.image.load("medias/mage/rouge/sr10.png"), pygame.image.load("medias/mage/rouge/sr11.png"), pygame.image.load("medias/mage/rouge/sr12.png"), pygame.image.load("medias/mage/rouge/sr13.png"), pygame.image.load("medias/mage/rouge/sr14.png"), pygame.image.load("medias/mage/rouge/sr15.png"), pygame.image.load("medias/mage/rouge/sr16.png"), pygame.image.load("medias/mage/rouge/sr17.png"), pygame.image.load("medias/mage/rouge/sr18.png"), pygame.image.load("medias/mage/rouge/sr19.png"), pygame.image.load("medias/mage/rouge/sr20.png"), pygame.image.load("medias/mage/rouge/sr21.png"), pygame.image.load("medias/mage/rouge/sr22.png"), pygame.image.load("medias/mage/rouge/sr23.png"), pygame.image.load("medias/mage/rouge/sr24.png"), pygame.image.load("medias/mage/rouge/sr25.png"), pygame.image.load("medias/mage/rouge/sr26.png"), pygame.image.load("medias/mage/rouge/sr27.png"), pygame.image.load("medias/mage/rouge/sr28.png"), pygame.image.load("medias/mage/rouge/sr29.png"), pygame.image.load("medias/mage/rouge/sr30.png"), pygame.image.load("medias/mage/rouge/sr31.png"), pygame.image.load("medias/mage/rouge/sr32.png"), pygame.image.load("medias/mage/rouge/sr33.png"), pygame.image.load("medias/mage/rouge/sr32.png"), pygame.image.load("medias/mage/rouge/sr31.png"), pygame.image.load("medias/mage/rouge/sr30.png"), pygame.image.load("medias/mage/rouge/sr29.png"), pygame.image.load("medias/mage/rouge/sr28.png"), pygame.image.load("medias/mage/rouge/sr27.png"), pygame.image.load("medias/mage/rouge/sr26.png"), pygame.image.load("medias/mage/rouge/sr25.png"), pygame.image.load("medias/mage/rouge/sr24.png"), pygame.image.load("medias/mage/rouge/sr23.png"), pygame.image.load("medias/mage/rouge/sr22.png"), pygame.image.load("medias/mage/rouge/sr21.png"), pygame.image.load("medias/mage/rouge/sr20.png"), pygame.image.load("medias/mage/rouge/sr19.png"), pygame.image.load("medias/mage/rouge/sr18.png"), pygame.image.load("medias/mage/rouge/sr17.png"), pygame.image.load("medias/mage/rouge/sr16.png"), pygame.image.load("medias/mage/rouge/sr15.png"), pygame.image.load("medias/mage/rouge/sr14.png"), pygame.image.load("medias/mage/rouge/sr13.png"), pygame.image.load("medias/mage/rouge/sr12.png"), pygame.image.load("medias/mage/rouge/sr11.png"), pygame.image.load("medias/mage/rouge/sr10.png"), pygame.image.load("medias/mage/rouge/sr9.png"), pygame.image.load("medias/mage/rouge/sr8.png"), pygame.image.load("medias/mage/rouge/sr7.png"), pygame.image.load("medias/mage/rouge/sr6.png"), pygame.image.load("medias/mage/rouge/sr5.png"), pygame.image.load("medias/mage/rouge/sr4.png"), pygame.image.load("medias/mage/rouge/sr3.png"), pygame.image.load("medias/mage/rouge/sr2.png"), pygame.image.load("medias/mage/rouge/sr1.png")],
                [pygame.image.load("medias/mage/bleu/sb1.png"), pygame.image.load("medias/mage/bleu/sb2.png"), pygame.image.load("medias/mage/bleu/sb3.png"), pygame.image.load("medias/mage/bleu/sb4.png"), pygame.image.load("medias/mage/bleu/sb5.png"), pygame.image.load("medias/mage/bleu/sb6.png"), pygame.image.load("medias/mage/bleu/sb7.png"), pygame.image.load("medias/mage/bleu/sb8.png"), pygame.image.load("medias/mage/bleu/sb9.png"), pygame.image.load("medias/mage/bleu/sb10.png"), pygame.image.load("medias/mage/bleu/sb11.png"), pygame.image.load("medias/mage/bleu/sb12.png"), pygame.image.load("medias/mage/bleu/sb13.png"), pygame.image.load("medias/mage/bleu/sb14.png"), pygame.image.load("medias/mage/bleu/sb15.png"), pygame.image.load("medias/mage/bleu/sb16.png"), pygame.image.load("medias/mage/bleu/sb17.png"), pygame.image.load("medias/mage/bleu/sb18.png"), pygame.image.load("medias/mage/bleu/sb19.png"), pygame.image.load("medias/mage/bleu/sb20.png"), pygame.image.load("medias/mage/bleu/sb21.png"), pygame.image.load("medias/mage/bleu/sb22.png"), pygame.image.load("medias/mage/bleu/sb23.png"), pygame.image.load("medias/mage/bleu/sb24.png"), pygame.image.load("medias/mage/bleu/sb25.png"), pygame.image.load("medias/mage/bleu/sb26.png"), pygame.image.load("medias/mage/bleu/sb27.png"), pygame.image.load("medias/mage/bleu/sb28.png"), pygame.image.load("medias/mage/bleu/sb29.png"), pygame.image.load("medias/mage/bleu/sb30.png"), pygame.image.load("medias/mage/bleu/sb31.png"), pygame.image.load("medias/mage/bleu/sb32.png"), pygame.image.load("medias/mage/bleu/sb33.png"),  pygame.image.load("medias/mage/bleu/sb32.png"), pygame.image.load("medias/mage/bleu/sb31.png"), pygame.image.load("medias/mage/bleu/sb30.png"), pygame.image.load("medias/mage/bleu/sb29.png"), pygame.image.load("medias/mage/bleu/sb28.png"), pygame.image.load("medias/mage/bleu/sb27.png"), pygame.image.load("medias/mage/bleu/sb26.png"), pygame.image.load("medias/mage/bleu/sb25.png"), pygame.image.load("medias/mage/bleu/sb24.png"), pygame.image.load("medias/mage/bleu/sb23.png"), pygame.image.load("medias/mage/bleu/sb22.png"), pygame.image.load("medias/mage/bleu/sb21.png"), pygame.image.load("medias/mage/bleu/sb20.png"), pygame.image.load("medias/mage/bleu/sb19.png"), pygame.image.load("medias/mage/bleu/sb18.png"), pygame.image.load("medias/mage/bleu/sb17.png"), pygame.image.load("medias/mage/bleu/sb16.png"), pygame.image.load("medias/mage/bleu/sb15.png"), pygame.image.load("medias/mage/bleu/sb14.png"), pygame.image.load("medias/mage/bleu/sb13.png"), pygame.image.load("medias/mage/bleu/sb12.png"), pygame.image.load("medias/mage/bleu/sb11.png"), pygame.image.load("medias/mage/bleu/sb10.png"), pygame.image.load("medias/mage/bleu/sb9.png"), pygame.image.load("medias/mage/bleu/sb8.png"), pygame.image.load("medias/mage/bleu/sb7.png"), pygame.image.load("medias/mage/bleu/sb6.png"), pygame.image.load("medias/mage/bleu/sb5.png"), pygame.image.load("medias/mage/bleu/sb4.png"), pygame.image.load("medias/mage/bleu/sb3.png"), pygame.image.load("medias/mage/bleu/sb2.png"), pygame.image.load("medias/mage/bleu/sb1.png")]],
            'monstre': [
                [pygame.image.load("medias/monstre/avant/mb1.png"), pygame.image.load("medias/monstre/avant/mb2.png"), pygame.image.load("medias/monstre/avant/mb3.png"), pygame.image.load("medias/monstre/avant/mb4.png"), pygame.image.load("medias/monstre/avant/mb5.png"), pygame.image.load("medias/monstre/avant/mb6.png"), pygame.image.load("medias/monstre/avant/mb5.png"), pygame.image.load("medias/monstre/avant/mb4.png"), pygame.image.load("medias/monstre/avant/mb3.png"), pygame.image.load("medias/monstre/avant/mb2.png")],
                [pygame.image.load("medias/monstre/m1.png"), pygame.image.load("medias/monstre/m1.png"), pygame.image.load("medias/monstre/m2.png"), pygame.image.load("medias/monstre/m3.png"), pygame.image.load("medias/monstre/m4.png"), pygame.image.load("medias/monstre/m4.png"), pygame.image.load("medias/monstre/m4.png"), pygame.image.load("medias/monstre/m3.png"), pygame.image.load("medias/monstre/m2.png"), pygame.image.load("medias/monstre/m1.png")]]
                }
        
        #Cadres de personnages :

        self.cadre = pygame.image.load("medias/cadres/cadre_personnage.png")

        self.cadres_personnages = {
            'paladin': [[pygame.image.load("medias/selection/Jour/pr.png"), pygame.image.load("medias/selection/Jour/pb.png")], [pygame.image.load("medias/selection/Nuit/prn1.png"), pygame.image.load("medias/selection/Nuit/pbn.png")]],
            'poulet': [[pygame.image.load("medias/selection/Jour/por.png"), pygame.image.load("medias/selection/Jour/pob.png")], [pygame.image.load("medias/selection/Nuit/pourn.png"), pygame.image.load("medias/selection/Nuit/poubn.png")]],
            'geant': [[pygame.image.load("medias/selection/Jour/gr.png"), pygame.image.load("medias/selection/Jour/gb.png")], [pygame.image.load("medias/selection/Nuit/grn.png"), pygame.image.load("medias/selection/Nuit/gbn.png")]],
            'cavalier': [[pygame.image.load("medias/selection/Jour/cr.png"), pygame.image.load("medias/selection/Jour/cb.png")], [pygame.image.load("medias/selection/Nuit/crn.png"), pygame.image.load("medias/selection/Nuit/cbn.png")]],
            'archere': [[pygame.image.load("medias/selection/Jour/ar.png"), pygame.image.load("medias/selection/Jour/ab.png")], [pygame.image.load("medias/selection/Nuit/arn.png"), pygame.image.load("medias/selection/Nuit/abn.png")]],
            'sorciere': [[pygame.image.load("medias/selection/Jour/sor.png"), pygame.image.load("medias/selection/Jour/sob.png")], [pygame.image.load("medias/selection/Nuit/sorn.png"), pygame.image.load("medias/selection/Nuit/sobn.png")]],
            'cracheur de feu' : [[pygame.image.load("medias/selection/Jour/crr.png"), pygame.image.load("medias/selection/Jour/crb.png")], [pygame.image.load("medias/selection/Nuit/crrn.png"), pygame.image.load("medias/selection/Nuit/crbn.png")]],
            'valkyrie' : [[pygame.image.load("medias/selection/Jour/vr.png"), pygame.image.load("medias/selection/Jour/vb.png")], [pygame.image.load("medias/selection/Nuit/vrn.png"), pygame.image.load("medias/selection/Nuit/vbn.png")]],
            'ivrogne' : [[pygame.image.load("medias/selection/Jour/ir.png"), pygame.image.load("medias/selection/Jour/ib.png")], [pygame.image.load("medias/selection/Nuit/irn.png"), pygame.image.load("medias/selection/Nuit/ibn.png")]],
            'barbare' : [[pygame.image.load("medias/selection/Jour/br.png"), pygame.image.load("medias/selection/Jour/bb.png")], [pygame.image.load("medias/selection/Nuit/brn.png"), pygame.image.load("medias/selection/Nuit/bbn.png")]],
            'mage' : [[pygame.image.load("medias/selection/Jour/sr.png"), pygame.image.load("medias/selection/Jour/sb.png")], [pygame.image.load("medias/selection/Nuit/mrn.png"), pygame.image.load("medias/selection/Nuit/mbn.png")]],
            'monstre' : [pygame.image.load("medias/selection/Jour/mj.png"), pygame.image.load("medias/selection/Nuit/mn.png")]
        }
        
        
        self.personnage_endommage = {
            'paladin': [pygame.image.load("medias/degats/pr.png"), pygame.image.load("medias/degats/pb.png")],
            'poulet': [pygame.image.load("medias/degats/por.png"), pygame.image.load("medias/degats/pob.png")],
            'geant': [[pygame.image.load("medias/degats/gr1.png"), pygame.image.load("medias/degats/gr2.png"), pygame.image.load("medias/degats/gr3.png"), pygame.image.load("medias/degats/gr4.png")], [pygame.image.load("medias/degats/gb1.png"), pygame.image.load("medias/degats/gb2.png"), pygame.image.load("medias/degats/gb3.png"), pygame.image.load("medias/degats/gb4.png")]],
            'cavalier': [pygame.image.load("medias/degats/cr.png"), pygame.image.load("medias/degats/cb.png")],
            'archere': [pygame.image.load("medias/degats/ar.png"), pygame.image.load("medias/degats/ab.png")],
            'sorciere': [pygame.image.load("medias/degats/sor.png"), pygame.image.load("medias/degats/sob.png")],
            'cracheur de feu' : [pygame.image.load("medias/degats/crr.png"), pygame.image.load("medias/degats/crb.png")],
            'valkyrie' : [pygame.image.load("medias/degats/vr.png"), pygame.image.load("medias/degats/vb.png")],
            'ivrogne' : [pygame.image.load("medias/degats/ir.png"), pygame.image.load("medias/degats/ib.png")],
            'barbare' : [pygame.image.load("medias/degats/br.png"), pygame.image.load("medias/degats/bb.png")],
            'mage' : [pygame.image.load("medias/degats/sr.png"), pygame.image.load("medias/degats/sb.png")],
            'monstre' : [pygame.image.load("medias/degats/m.png")]
        }
        
        self.personnages_deplacement = {
            'paladin': [pygame.image.load("medias/en_deplacement/pr.png"), pygame.image.load("medias/en_deplacement/pb.png")],
            'poulet': [pygame.image.load("medias/en_deplacement/por.png"), pygame.image.load("medias/en_deplacement/pob.png")],
            'geant': [],
            'cavalier': [pygame.image.load("medias/en_deplacement/cr.png"), pygame.image.load("medias/en_deplacement/cb.png")],
            'archere': [pygame.image.load("medias/en_deplacement/ar.png"), pygame.image.load("medias/en_deplacement/ab.png")],
            'sorciere': [pygame.image.load("medias/en_deplacement/sor.png"), pygame.image.load("medias/en_deplacement/sob.png")],
            'cracheur de feu' : [pygame.image.load("medias/en_deplacement/crr.png"), pygame.image.load("medias/en_deplacement/crb.png")],
            'valkyrie' : [pygame.image.load("medias/en_deplacement/vr.png"), pygame.image.load("medias/en_deplacement/vb.png")],
            'ivrogne' : [pygame.image.load("medias/en_deplacement/ir.png"), pygame.image.load("medias/en_deplacement/ib.png")],
            'barbare' : [pygame.image.load("medias/en_deplacement/br.png"), pygame.image.load("medias/en_deplacement/bb.png")],
            'mage' : [pygame.image.load("medias/en_deplacement/sr.png"), pygame.image.load("medias/en_deplacement/sb.png")],
            'monstre' : [pygame.image.load("medias/en_deplacement/m.png")]
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
            'option1' : [pygame.image.load("medias/cadres/active.png"), pygame.image.load("medias/cadres/desactive.png")],
            'barre_fps' : pygame.image.load("medias/cadres/fps_barre.png"),
            'pointeur_fps' : pygame.image.load("medias/cadres/pointeur_fps.png")
        }
        

    def afficher_curseur(self):
        '''
        Affiche le curseur en fonction de l'état (appuyé ou non)
        '''
        if self.clavier_souris.acc_appuye() :
            self.ecran.blit(self.curseur_appuye, pygame.mouse.get_pos())  # récupère la position de la souris 0 <= x <= 1500, 0 <= y <= 700)
        else :
            self.ecran.blit(self.curseur_normal, pygame.mouse.get_pos())  # récupère la position de la souris 0 <= x <= 1500, 0 <= y <= 700)

        
    def afficher_terrain(self):
        '''
        Affiche le terrain
        '''
        self.ecran.blit(self.menu, (0, 0))
        self.ecran.blit(self.image_terrain, (250, 0))
        self.ecran.blit(self.menu, (1050, 0))



    def afficher_personnages_plateau(self):
        '''
        Affiche les personnages (+ contour de couleur pour chaque perso de l'équipe en cours)
        '''
        for ligne in self.terrain.acc_grille():
            for elt in ligne:
                ##Coffre
                if isinstance(elt, module_objets.Coffre):
                    x = elt.x * 38 + 250
                    y = elt.y * 38
                    image_objet = self.images_coffre[0]
                    if elt.est_ouvert:
                        image_objet = self.images_coffre[elt.avancement_ouverture]
                        if elt.avancement_ouverture < 10 and self.attributs_jeu.acc_compteur() % 3 ==  0:
                            elt.avancement_ouverture += 1
                    self.ecran.blit(image_objet, (x, y))
                ##Personnage
                elif isinstance(elt, module_personnage.Personnage):
                    x = elt.x * 38 + 250
                    y = elt.y * 38
                    perso = self.personnages[elt.personnage]
                    perso_endommage = self.personnage_endommage[elt.personnage] 
                    #Contour de couleur :   
                    if elt.acc_equipe() == self.attributs_jeu.acc_equipe_en_cours() :
                        self.ecran.blit(self.sol_personnages[elt.acc_equipe()], (x , y))

                    if elt.acc_endommage():
                        if elt.equipe == 'rouge' or elt.equipe == 'neutre':
                            image_personnage = perso_endommage[0]
                        else :
                            image_personnage = perso_endommage[1]
                        if elt.personnage == 'geant':
                            if elt.equipe == 'rouge':
                                image_personnage = perso_endommage[0][elt.numero_geant]
                            else :
                                image_personnage = perso_endommage[1][elt.numero_geant]
                        elif elt.personnage == 'monstre':
                            image_personnage = perso_endommage[0]
                    else:
                        nb_images = len(perso[0])
                        index_image = int(self.attributs_jeu.acc_compteur() / 70 * nb_images)
                        if elt.personnage == 'geant':
                            if elt.equipe == 'bleu':
                                images_personnage = perso[0][index_image]
                            else:
                                images_personnage = perso[1][index_image]
                            image_personnage = images_personnage[elt.numero_geant]
                        elif elt.personnage == 'monstre':
                            if elt.etat == 'bebe':
                                image_personnage = perso[0][index_image]
                            else:
                                image_personnage = perso[1][index_image]
                        else:
                            if elt.equipe == 'rouge' :
                                image_personnage = perso[0][index_image]
                            else :
                                image_personnage = perso[1][index_image]

                    self.ecran.blit(image_personnage, (x, y))
        
    def afficher_deplacements(self):
        '''
        affiche les déplacements possibles sur la grille
        '''
        #les déplacements
        tab = self.attributs_jeu.acc_deplacements()
        #on affiche
        for coord in tab:
            case_x = coord[0] * 38 + 250
            case_y = coord[1] * 38
            self.ecran.blit(self.deplacements, (case_x, case_y, 38, 38))

    def afficher_attaques(self):
        '''
        affiche les déplacements possibles sur la grille
        '''
        for coord in self.attributs_jeu.acc_attaques():
            case_x = coord[0] * 38 + 250
            case_y = coord[1] * 38
            self.ecran.blit(self.attaques, (case_x, case_y, 38, 38))
            
    def afficher_console(self):
        '''
        affiche le console où sera écrit chaque action des équipes.
        '''
        #fond
         
        police = pygame.font.Font("medias/police_console.ttf", 16)
        pile = self.attributs_jeu.acc_console()
        stock = module_lineaire.Pile()
        hauteur = 570
        
        while not pile.est_vide() :
            tab = pile.depiler()
            stock.empiler(tab)
            if tab[1] == 'bleu':
                texte = police.render(tab[0] , 1, (42, 51, 176))
            elif tab[1] == 'rouge' :
                texte = police.render(tab[0], 1, (237, 28, 36))
            else : #noir
                texte = police.render(tab[0], 1, (0, 0, 0))
            hauteur -= 19
            self.ecran.blit(texte, (1070, hauteur))
            
        while not stock.est_vide() :
            pile.empiler(stock.depiler())
                
       
    
    def afficher_personnage_selection(self):
        '''
        Affiche les personnages
        '''
        if self.attributs_jeu.acc_selection() != None and type(self.attributs_jeu.acc_selection()) != str:
            selection = self.attributs_jeu.acc_selection()
            if self.attributs_jeu.acc_temps() == 'Jour':
                index = 0
            else :
                index = 1
            if isinstance(selection, module_personnage.Personnage):
                if selection.personnage == 'monstre':
                    image = self.cadres_personnages[selection.personnage][0]
                else :
                    if selection.equipe == 'rouge' :
                        image = self.cadres_personnages[selection.personnage][index][0]
                    else :
                        image = self.cadres_personnages[selection.personnage][index][1]

                self.ecran.blit(image, (11, 12))
                self.ecran.blit(self.cadre, (6, 10))
            
            
                ######### Informations
                police = pygame.font.Font("medias/pixelec.ttf", 17)
                texte = police.render("Type : " , 1, (152, 82, 51))
                self.ecran.blit(texte, (10, 150))
                
                texte = police.render(selection.personnage , 1, (152, 82, 51))
                self.ecran.blit(texte, (10, 175))
                
                texte2 = police.render("Points de vie : ", 1, (152, 82, 51))
                self.ecran.blit(texte2, (10, 200))
                
                texte2 = police.render(str(selection.pv) , 1, (152, 82, 51))
                self.ecran.blit(texte2, (10, 225))
                
                texte3 = police.render("Attaque : " , 1, (152, 82, 51))
                self.ecran.blit(texte3, (10, 250))
                
                texte3 = police.render(str(module_personnage.DIC_ATTAQUES[selection.personnage]) , 1, (152, 82, 51))
                self.ecran.blit(texte3, (10, 275))
        
    def afficher_equipe(self):
        '''
        affiche le tour de l'équipe en cours
        '''
        police = pygame.font.Font("medias/pixelec.ttf", 17)
        texte = police.render("Tour du joueur :" , 1, (152, 82, 51))
        self.ecran.blit(texte, (10, 740))
        if self.attributs_jeu.acc_equipe_en_cours() == 'bleu':
            texte = police.render('Bleu ' + str(self.attributs_jeu.acc_nombre_action()) , 1, (42, 51, 176))
        else :
            texte = police.render('Rouge ' + str(self.attributs_jeu.acc_nombre_action()), 1, (237, 28, 36))
        self.ecran.blit(texte, (10, 760))

    def afficher_cerisier(self):
        '''
        affiche les cerisiers sur la carte
        '''
        self.ecran.blit(self.cerisier, (250, 0))

        for petal in self.petals:
            petal.y += 1
            petal.x -= 1
            pygame.draw.rect(self.ecran, (252, 235, 237), (int(petal.x), petal.y, petal.size, petal.size))

            if petal.y >= petal.distance_max or petal.x < 250:
                
                self.petals.append(Petale(petal.position))
                self.petals.remove(petal)
                
    def afficher_filtre(self):
        '''
        ajoute un effet filtre au jeu si c'est la nuit
        '''
        if self.attributs_jeu.acc_temps() == 'Nuit':
            if self.transition < 70:
                self.transition += 1
        elif self.attributs_jeu.acc_temps() == 'Jour' :
            if self.transition != 0:
                self.transition -= 1
        filtre_bleu = pygame.Surface((800, 800), pygame.SRCALPHA)
        filtre_bleu.fill((19, 32, 76, self.transition))  # (r, g, b, alpha ) l'alpha = transparence
        self.ecran.blit(filtre_bleu, (250, 0))
             
    def afficher_boutons_option(self):
        '''
        affiche les différents boutons du menu
        '''
        police = pygame.font.Font("medias/pixelec.ttf", 21)
        bouton_clique = self.attributs_jeu.acc_bouton_clique()
        #####option 1 :
        ###si l'option1 est activée
        bouton_option1 = self.boutons['option1'][0]
        ### sinon
        bouton_option1 = self.boutons['option1'][1]

        self.ecran.blit(bouton_option1, (475, 360))
        
        ###si l'option1 est activée
        bouton_option2 = self.boutons['option1'][0]
        ### sinon
        bouton_option2 = self.boutons['option1'][1]

        self.ecran.blit(bouton_option2, (475, 415))
        
        ###si l'option3 est activée
        bouton_option3 = self.boutons['option1'][0]
        ### sinon
        bouton_option3 = self.boutons['option1'][1]

        self.ecran.blit(bouton_option3, (475, 470))
        
        
        
        #### barre des fps
        bouton_option_fps = self.boutons['barre_fps']
        self.ecran.blit(bouton_option_fps, (475, 525))
        
        pointeur_barre = self.boutons['pointeur_fps']
        self.ecran.blit(pointeur_barre, (575, 525))
        
        ####
        
        if bouton_clique == 'quitter_option':
            bouton_quitter = self.boutons['quitter_fin'][1]
            texte1 = police.render("Quitter" , 1, (224, 85, 92))
        else :
            bouton_quitter = self.boutons['quitter_fin'][0]
            texte1 = police.render("Quitter" , 1, (179, 12, 36))
            
        self.ecran.blit(bouton_quitter, (515, 650)) 
        self.ecran.blit(texte1, (580, 670))
        
    def afficher_boutons_menu(self):
        '''
        affiche les différents boutons du menu
        '''
        police = pygame.font.Font("medias/pixelec.ttf", 21)
        bouton_clique = self.attributs_jeu.acc_bouton_clique()

        if bouton_clique == 'jouer':
            bouton_jouer = self.boutons['jouer'][1]
            texte1 = police.render("Jouer" , 1, (200, 165, 80))
        else :
            bouton_jouer = self.boutons['jouer'][0]
            texte1 = police.render("Jouer" , 1, (196, 144, 4))
            
        self.ecran.blit(bouton_jouer, (450, 340)) 
        self.ecran.blit(texte1, (620, 360))
        
        if bouton_clique == 'option':
            bouton_jouer = self.boutons['jouer'][1]
            texte1 = police.render("Options" , 1, (224, 165, 80))
        else :
            bouton_jouer = self.boutons['jouer'][0]
            texte1 = police.render("Options" , 1, (196, 144, 4))
            
            
        self.ecran.blit(bouton_jouer, (450, 420)) 
        self.ecran.blit(texte1, (600, 440))
        
        
        if bouton_clique == 'quitter_menu':
            bouton_quitter = self.boutons['quitter_menu'][1]
            texte2 = police.render("Quitter" , 1, (224, 85, 92))
        else :
            bouton_quitter = self.boutons['quitter_menu'][0]
            texte2 = police.render("Quitter" , 1, (179, 12, 36))
        
        self.ecran.blit(bouton_quitter, (450, 500)) 
        self.ecran.blit(texte2, (590, 520))

    def afficher_boutons_jeu(self):
        '''
        affiche les différents boutons du jeu
        '''
        police = pygame.font.Font("medias/pixelec.ttf", 21)
        bouton_clique = self.attributs_jeu.acc_bouton_clique()
        
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
            print('ok')
            bouton_sauvegarde = self.boutons['sauvegarder'][1]
            texte2 = police.render("Sauvegarder" , 1, (145, 173, 73))
        else :
            bouton_sauvegarde = self.boutons['sauvegarder'][0]
            texte2 = police.render("Sauvegarder" , 1, (106, 143, 20))   
        self.ecran.blit(bouton_sauvegarde, (1056, 585)) # 5 d'écart avec charger
        self.ecran.blit(texte2, (1087, 605))

            
    def afficher_fond(self):
        '''
        affiche le fond d'ecran
        '''
        self.ecran.blit(self.image_fond, (0, 0))

    def afficher_menu(self) :
        '''
        Affiche tous les objets du menu sur la fenêtre pygame.
        '''
        self.afficher_fond()
        if not self.attributs_jeu.acc_option() :  
            self.afficher_boutons_menu()
        else :
            police = pygame.font.Font("medias/pixelec.ttf", 21)
            texte = police.render("Options" , 1, (152, 82, 51))
            self.ecran.blit(self.fond_options, (455, 290)) 
            self.ecran.blit(texte, (580, 310))
            self.afficher_boutons_option()
        self.afficher_curseur()
        
        
    def afficher_personnage_en_deplacement(self):
        '''
        affiche le personnage en déplacement
        '''
        if self.attributs_jeu.acc_deplacement_en_cours() and self.attributs_jeu.acc_selection() != None :
            print('bouge !')
            if self.attributs_jeu.acc_indice_courant() < len(self.attributs_jeu.acc_chemin()) - 1:
                destination = self.attributs_jeu.acc_chemin()[self.attributs_jeu.acc_indice_courant() + 1]
                x, y = self.attributs_jeu.acc_coordonnees_personnage()

                # calcule le vecteur de déplacement

                dx = min(max(destination[0] - x, -3), 3)
                dy = min(max(destination[1] - y, -3), 3)
                
                # met à jour les coordonnées du personnage
                self.attributs_jeu.mut_coordonnees_personnage((x + dx, y + dy))
                ## affichage du personnage :
                perso = self.personnages_deplacement[self.attributs_jeu.acc_personnage_en_deplacement()[0]]
                if self.attributs_jeu.acc_personnage_en_deplacement()[1] == 'rouge' :
                    image_personnage = perso[0]
                else :
                    image_personnage = perso[1]
                self.ecran.blit(image_personnage, self.attributs_jeu.acc_coordonnees_personnage())
                # Vérifier si le personnage atteint la destination
                if self.attributs_jeu.acc_coordonnees_personnage() == destination:
                    self.attributs_jeu.indice_courant += 1
                    
    def afficher_monstres_en_deplacement(self):
        '''
        affiche les monstres en déplacement
        '''
        for monstre in self.attributs_jeu.monstres_a_deplacer : #chaque monstre à déplacer
            if monstre.futur_x == None and monstre.futur_y == None:
                monstre.futur_x, monstre.futur_y = monstre.prochaines_coordonnees(self.terrain)
                monstre.futur_coord_x = 250 + monstre.futur_x * 38
                monstre.futur_coord_y = monstre.futur_y * 38
                
            if monstre.coord_x != monstre.futur_coord_x :
                dx = min(max(monstre.futur_coord_x - monstre.coord_x, -3), 3)
                monstre.coord_x += dx
            if monstre.coord_y != monstre.futur_coord_y :
                dy = min(max(monstre.futur_coord_y - monstre.coord_y, -3), 3)
                monstre.coord_y += dy

            # affichage du monstre :
            image_monstre = self.personnages_deplacement['monstre'][0]
            self.ecran.blit(image_monstre, (monstre.coord_x, monstre.coord_y))
            if monstre.coord_x == monstre.futur_coord_x and monstre.coord_y == monstre.futur_coord_y :
                monstre.deplacer(monstre.futur_x, monstre.futur_y) # déplace le monstre
                self.terrain.mut_terrain(monstre.x, monstre.y, monstre) # place le monstre à sa nouvelle position
                self.attributs_jeu.monstres_a_deplacer.remove(monstre)
                monstre.futur_x = None
                monstre.futur_y = None
        
        
    def afficher_attaque_en_cours(self):
        '''
        affiche l'attaque en cours
        '''
        if self.attributs_jeu.acc_attaque_en_cours() == True :
            print('attaque en cours')
        
    def afficher_tombes(self):
        '''
        affiche des tombes sur la case sur laquelle un personnage est mort
        '''
        for elt in self.attributs_jeu.acc_positions_tombes():
            self.ecran.blit(self.image_tombe, (elt[0], elt[1]))
                    
    def afficher_fin_jeu(self):
        '''
        affiche le menu de la fin du jeu
        '''
        if self.attributs_jeu.acc_partie_terminee() :
            if self.attributs_jeu.acc_position_y_menu_fin() != 204 :
                self.attributs_jeu.mut_position_y_menu_fin(3)
            ###affichage cadre
            self.ecran.blit(self.menu_fin, (455, self.attributs_jeu.acc_position_y_menu_fin()))
            ### affichage texte
            police = pygame.font.Font("medias/pixelec.ttf", 30)
            if self.attributs_jeu.equipe_gagnante == 'bleu':
                annonce = police.render("L'equipe bleue" , 1, (42, 51, 176))
                annonce2 = police.render("gagne !" , 1, (42, 51, 176))
                self.ecran.blit(annonce, (470, self.attributs_jeu.acc_position_y_menu_fin() + 20))
                self.ecran.blit(annonce2, (570, self.attributs_jeu.acc_position_y_menu_fin() + 50))
            else :
                annonce = police.render("L'equipe rouge" , 1, (237, 28, 36))
                annonce2 = police.render("gagne !" , 1, (237, 28, 36))
                self.ecran.blit(annonce, (470, self.attributs_jeu.acc_position_y_menu_fin() + 20))
                self.ecran.blit(annonce2, (570, self.attributs_jeu.acc_position_y_menu_fin() + 50))
            ##affichage boutons :
            police2 = pygame.font.Font("medias/pixelec.ttf", 21)
            if self.attributs_jeu.acc_bouton_clique() == 'rejouer':
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
            
    def afficher_annonce_coffre(self):
        '''
        affiche l'annonce du coffre une fois celui-ci ouvert
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
            
            couleur_texte = (255, 0, 0, 100 - int(self.opacite))# Couleur du texte (rouge) avec une transparence de 128 (sur 255)
            police = pygame.font.Font("medias/pixelec.ttf", 30)
            texte_surface = police.render(self.rep_contenu[self.attributs_jeu.event_coffre], True, couleur_texte) #le True, est pour l'antialiasing, pour rendre les bords du texte plus lisses en ajoutant des pixels semi-transparents autour des bords
            position_texte = (300, 300)
            self.ecran.blit(texte_surface, position_texte)
            
        
            
    def afficher_jeu(self):
        '''
        Affiche tous les objets du jeu sur la fenêtre pygame.
        '''
        self.afficher_terrain()
        self.afficher_boutons_jeu()
        self.afficher_tombes()
        self.afficher_personnages_plateau()
        self.afficher_personnage_en_deplacement()
        self.afficher_monstres_en_deplacement()
        self.afficher_attaque_en_cours()
        self.afficher_deplacements()
        self.afficher_attaques()
        self.afficher_personnage_selection()
        self.afficher_equipe()
        self.afficher_cerisier()
        self.afficher_filtre()
        self.afficher_annonce_coffre()
        self.afficher_fin_jeu()
        self.afficher_console()
        self.afficher_curseur()
        
        

        