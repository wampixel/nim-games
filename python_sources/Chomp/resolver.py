from numpy import array
from pylab import *

"""
    notation :
        +n : addition de Nim standard

    Le jeu  Chomp (aussi appelé jeu  de la tablette de chocolat) est un jeu de Nim.
    On sait que pour le joueur 1, il existe une solution gagnante mais on se sait pas laquelle.
    
    On se propose ici d'essayer une stratégie sur un jeu similaire.
    Les règles de ce jeu sont :
        - on choisi un carré de la tablette et on supprime soit la ligne soit la colonne de ce carré
        - si jamais la tablette est séparé en deux, on garde bien les deux composantes, on ne les rassembles pas

    Posons la situation de jeu de façon a avoir T une tablette NxM

    et posons la fonction f(T) de la façon suivante :
        f(T) == 1 si et seulement si N est impair ou M est impair (position perdante, on peux gagner d'après théorème Sprague-Grundy)
        f(T) == 0 sinon (position gagnante, on ne peux pas gagner d'après le théorème de Sprague-Grundy)

    étendons cette fonction  a une position P d'un jeu a n tablettes noté T1, T2, ..., Tn :
        f(P) == 1 si sum(N de ti) est impair ou sum(M de ti) est impair pour tout i entre 1 et n
        f(P) == 0 sinon
"""

#FONCTIONS
"""
    fonction f d'une position p
    Entrée :
        p une liste de tablettes (avec au moins une tablette)
"""
def f(p) :
    sumC = 0
    sumL = 0
    #pour toute tablette t de la position p, on calcul la fonction f de celle ci
    for t in p :
        sumC += getColNb(t)
        sumL += getRowNb(t)
    
    if sumC % 2 != 0 or sumL % 2 != 0 :
        return 1
    
    return 0

"""
    retourne le nombre de colonnes de la tablette t
"""
def getColNb(t) :
    (l, c) = t.shape
    return c

"""
    retourne le nombre de lignes de la tablette t
"""
def getRowNb(t) :
    (l, c) = t.shape
    return l

"""
    retourne la tablette découpée par rapport a une colonne.
    dans cette fonction, la colonne attendu est naturelle, c'est a dire que l'on attend un entier compris entre 
    1 et getColNb(t) (pour faciliter l'appel a cette fonction pour l'utilisateur)
    Entrée :
        t une matrice représentant une tablette
        c une colonne de la tablette compris entre 1 et getColNb(t)
"""
def chompC(t, c) :
    if c - 1 < 0 or c > getColNb(t) :
        raise(ValueError("erreur"))
    if c - 1 == 0 :
        return [array(t[:, c:])]
    if c == getColNb(t):
        return [array(t[:, :c - 1])]
    else :
        return [array(t[:, :c-1]), array(t[:, c:])]

"""
    retourne la tablette découpée par rapport a une ligne.
    Dans cette fonction, la ligne attendue est naturelle, c'est a dire que l'on attend un entier compris entre
    1 et getRowNb(t) (pour faciliter l'appel a cette fonction pour l'utilisateur)
    Entrée :
        t une matrice représentant une tablette
        l une ligne de la tablette compris entre 1 et getRowNb(t)
"""
def chompL(t, l) :
    if l - 1 < 0 or l > getRowNb(t) :
        raise(ValueError("erreur"))
    if l - 1 == 0 :
        return [array(t[l:, :])]
    if l == getRowNb(t):
        return [array(t[:l - 1, :])]
    else :
        return [array(t[:l - 1, :]), array(t[l:, :])]



#TESTS
"""
    on pose les positions de jeu suivantes :
    
    P :
        _ _ _    _ _
       |_|_|_|  |_|_|
       |_|_|_|  |_|_|
         T1      T2
    
    p2 :
        _ _ _    _ _ _
       |_|_|_|  |_|_|_|
       |_|_|_|  |_|_|_|
         T1       T1

    quand le carré existe bien dans la tablette, la case de la matrice le représentant est a 1
"""
if __name__ == '__main__' :
    #essai fonction f
    t1 = array([ones(3), ones(3)])
    t2 = array([ones(2), ones(2)])

    p = [t1, t2]
    print("f(p) =", f(p))

    p2 = [t1, t1]
    print("f(p2) =", f(p2))

    #essai fonctions chompC et chompL
    t1 = array([ones(3), ones(3), ones(3)])
    ct1 = chompC(t1, 2)
    lt1 = chompL(t1, 2)
    print("chomped C t1 :\n", ct1)
    print("chomped L t1 :\n", lt1)

    #essai de suppression d'une colonne après la suppression d'une ligne
    lct1 = chompC(lt1[0], 2)
    lct1.append(lt1[1]) 
    print("chomped l lt1[0] :\n", lct1)
