# -*- coding: utf-8 -*-
'''
    Module graphe avec un dictionnaire
    : Auteur
        LAPÔTRE Marylou
'''

from graphe import module_graphe_dic
from graphe import module_lineaire

G = { 0 : [3, 4, 2],
      1 : [2],
      2 : [1, 0],
      3 : [0, 4],
      4 : [3, 0],
      5 : []
     }

def construire_graphe(dic) :
    '''
    renvoie le graphe construit à partir de son dictionnaire
    : param dic (dict)
    : return (Graphe_non_oriente_dic)
    '''
    nouveau_graphe = module_graphe_dic.Graphe_non_oriente_dic()
    for sommet in dic :
        for voisin in dic[sommet] :
            nouveau_graphe.ajouter_arete(sommet, voisin)
    return nouveau_graphe

mon_graphe = construire_graphe(G)

def parcourir_largeur(graphe, sommet):
    '''
    renvoie une liste de sommets obtenus par parcours en largeur du graphe à partir du sommet de départ
    : param graphe (Graphe..) un graphe orienté ou non
    : param sommet (?) le sommet de départ
    : return (list) liste de sommets
    '''
    liste_sommets_parcourus = []
    f = module_lineaire.File() #une file vide
    f.enfiler(sommet)
    while not f.est_vide(): #tant que le file n'est pas vide
        sommet = f.defiler()
        if not sommet in liste_sommets_parcourus : #si le sommet n'est pas déjà dans la liste des sommets parcourus
            liste_sommets_parcourus.append(sommet)
            voisins = graphe.voisins(sommet)
            for voisin in voisins :
                f.enfiler(voisin) #on enfile chaque voisin du sommet dans la file
    return liste_sommets_parcourus

def rechercher_parent(graphe, sommet, destination):
    '''
    renvoie un dictionnaire permettant de trouver le chemin le plus court entre le sommet et la destination dans le graphe
    : params
        graphe (Graphe...)
        sommet (?) le sommet de départ 
        destination (?) le sommet à atteindre
    : return (dict)
    '''
    f = module_lineaire.File()
    f.enfiler(sommet)
    parent = {sommet : None}
    while not f.est_vide() and not sommet == destination:
        sommet = f.defiler()
        for voisin in graphe.voisins(sommet):
            if not voisin in parent : #si il n'a pas encore été visité
                f.enfiler(voisin)
                parent[voisin] = sommet
    return parent

def construire_pile(parent, destination):
    '''
    renvoie une pile dans laquelle on a empilé les parents en partant de la destination
    : param parent (dict)    
    : param destination (?) le sommet de destination
    : return (Pile)
    '''
    p = module_lineaire.Pile()
    destination = (destination[0], destination[1])
    p.empiler(destination)
    while not parent[destination] == None:
        destination = parent[destination]
        p.empiler(destination)
    return p
    
    
def depiler_chemin(graphe, sommet, destination):
    '''
    renvoie la liste correspondant au chemin le plus court dans le graphe su sommet à la destination
    : params
        graphe (Graphe...)
        sommet (?) le sommet de départ 
        destination (?) le sommet à atteindre
    : return le chemin (list)
    '''
    chemin = []
    parent = rechercher_parent(graphe, sommet, destination)
    pile_sommets = construire_pile(parent, destination)
    while not pile_sommets.est_vide():
        elt = pile_sommets.depiler()
        chemin.append(elt)
    return chemin
    
    
