from resolver import *
from random import randrange
from pylab import ones
import numpy
"""
    Jeu de Chomp revisité
    Principe du jeu :
        être le dernier a enlever un carré du jeu

    Plateau de jeu :
        un ensemble de tablettes représenté par des matrices 2D

    Règles :
        on choisi un carreau d'une tablette et on enlève soit la ligne soit la colonne sur laquelle est présente le carreau choisi

    Nb :
        sur un jeu a une tablette la méthode de résolution implanté dans le fichier resolver.py fonctionne, cependant lorsque l'on passe
        a un jeu avec plus d'une tablette, la méthode de résolution de fonctionne plus.
        Ceci vient du fait que le jeu ne prend pas en compte les tablettes se ressemblant, il cherche simplement a résoudre le jeu en considérant
        l'ensemble des tablettes en une seule tablette contenant l'ensemble.
"""

#FONCTIONS
"""
    crée aléatoirement une situation de jeu.
    par défaut, crée un jeu de 3 tablettes avec 5 lignes et 5 colonnes maximum
    Entrée :
        maxC le nombre maximal de colonnes voulu pour toutes les tablettes
        maxL le nombre maximal de lignes voulu pour toutes les tablettes
        nbT le nombre de tablettes voulu pour le jeu
"""
def aleaGame(maxC=5, maxL=5, nbT=1) :
    i = 0
    res = []
    while i < nbT :
        l = randrange(1, maxL + 1)
        c = randrange(1, maxC + 1)
        li = []
        for j in range(0, l) :
            li.append(ones(c))

        res.append(array(li))
        i += 1

    return res

"""
    fonction qui permet de calculer le coup gagnant si il existe.
    Retourne un tuple de la forme (i, x, y) avec
            i l'indice de la tablette dans laquelle il faut jouer 
            x la ligne a supprimer si y == 1
            x la colonne a supprimer si y == 0
    si jamais le coup gagnant n'existe pas, retourne (0, 1, 1) (première ligne a supprimer)
    retourne (-1, -1, -1) en cas d'erreur
    Entrée :
        p une position du jeu 
"""
def getWinningStrat(p) :
    if f(p) == 0 :
        print("par defaut")
        return (0, 1, 1)

    #on test pour toutes les matrices du jeu un coup jusqu’à trouver le coup gagnant
    for i in range(0, len(p)) :
        #on test pour toutes les colonnes de la matrice si le coup est gagnant
        for j in range(1, getColNb(p[i]) + 1) :
            tmp = p.copy()
            tmp.pop(i)
            tmp.extend(chompC(p[i], j))
            #si jamais le coup j dans la matrice p[i] est gagnant, on sait ou jouer
            if f(tmp) == 0 :
                return (i, j, 0)

        #on test pour toutes les lignes de la matrice si le coup est gagnant
        for k in range(1, getRowNb(p[i]) + 1) :
            tmp = p.copy()
            tmp.pop(i)
            tmp.extend(chompL(p[i], k))
            #si jamais le coup j dans la matrice p[i] est gagnant, on sait ou jouer
            if f(tmp) == 0 :
                return (i, k, 1)
        print(i,j)
    #si on ne sait pas ou jouer pour pouvoir obtenir un coup gagnant selon la définition de f(p)
    return (0, 1, 1)

"""
    fonction principale du jeu
    crée une situation aléatoire de jeu en appelant la fonction aleaGame() sans argument
    
    Possibilité d’amélioration : proposer au joueur de donner les arguments a donner a la fonction aleaGame
"""
def main() :
    ag = aleaGame()
    """
        situation de jeu problématique 
        le calcul ne prend pas en compte les composantes connexes identiques
        Peut être un tri de l'ensemble des tablettes par formes identiques?
    """
    #ag = [array([[1,1]]), array([[1]]), array([[1,1]]), array([[1]])]
    """
        dans cette situation a une tablette unique avec un nombre impair de colonnes et de lignes
        le calcul du coup gagnant fonctionne
    """
    #ag = [array([[1,1,1]])]
    joueur = 1
    while ag != [] :
        for i in range(0, len(ag)) :
            print(ag[i], "\n")
        
        joueur = (joueur + 1) % 2
        
        if joueur == 0 :
            (i, n, s) = getWinningStrat(ag)
            
            if s == 0 :
                tmp = chompC(ag[i], n)
                print("l'ia joue dans la matrice {} en enlevant la colonne {}".format(i + 1, n))
            else :
                tmp = chompL(ag[i], n)
                print("l'ia joue dans la matrice {} en enlevant la ligne {}".format(i + 1, n))

            ag.pop(i)
            (l, c) = tmp[0].shape
            if l != 0 and c != 0:
                ag.extend(tmp)
        
        else :
            #choix de la matrice ou l'on veut supprimer une ligne ou une colonne
            m = -1
            while m == -1:
                try :
                    m = int(input("choisissez une matrice (1 - {}) :".format(len(ag))))
                    assert m >= 1 and m <= len(ag) + 1
                except AssertionError :
                    print("matrice invalide recommencez :")
                    m = -1
                except ValueError :
                    print("valeur non conforme recommencez :")
                    m = -1

            #choix du sens de suppression
            #h horizontal
            #v vertical
            s = ""
            while s == "" :
                try :
                    s = input("choisissez un sens (h - v) :")
                    assert s == 'h' or s == 'v'
                except AssertionError :
                    print("valeur invalide recommencez :")
                    s = ""

            #choix de la ligne ou de la colonne a supprimer
            n = -1
            while n == -1 :
                try :
                    if s == 'h' :
                        n = int(input("choisissez une ligne (1 - {}) :".format(getRowNb(ag[m - 1]))))
                        assert n >= 1 and n <= getRowNb(ag[m - 1])
                    else :
                        n = int(input("choisissez une colonne (1 - {}) :".format(getColNb(ag[m - 1]))))
                        assert n >= 1 and n <= getColNb(ag[m - 1])
                
                except AssertionError :
                    print("valeur invalide recommencez :")
                    n = -1
                except ValueError :
                    print("valeur non conforme recommencez :")
                    n = -1

            #on peut supprimer la ligne ou la colonne choisie
            if s == 'h' :
                tmp = chompL(ag[m - 1], n)
                print("vous jouez dans la matrice {} en enlevant la ligne {}".format(m, n))

            else :
                tmp = chompC(ag[m - 1], n)
                print("vous jouez dans la matrice {} en enlevant la colonne {}".format(m, n))

            ag.pop(m - 1)
            (l, c) = tmp[0].shape
            if l != 0 and c != 0:
                ag.extend(tmp)
    if joueur == 0 :
        print("l'ia a gagné...")
    else :
        print("vous avez gagné !")

#POINT DE DEPART DU JEU
if __name__ == '__main__' :
    main()
