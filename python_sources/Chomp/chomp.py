from resolver import *
from random import randrange
from pylab import ones
import numpy

"""
    crée aleatoirement une situation de jeu.
    par defaut, crée un jeu de 3 tablettes avec 5 lignes et 5 colonnes maximum
    Entrée :
        maxC le nombre maximal de colonnes voulu pour toutes les tablettes
        maxL le nombre maximal de lignes voulu pour toutes les tablettes
        nbT le nombre de tablettes voulu pour le jeu
"""
def aleaGame(maxC=5, maxL=5, nbT = 3) :
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
        return (0, 1, 1)

    #on test pour toutes les matrices du jeu un coup jusqu’à trouver le coup gagnant
    for i in range(0, len(p)) :
        #on test pour toutes les colonnes de la matrice si le coup est gagnant
        for j in range(1, getColNb(p[i])) :
            tmp = p.copy()
            tmp.pop(i)
            tmp.extend(chompC(p[i], j))
            #si jamais le coup j dans la matrice p[i] est gagnant, on sait ou jouer
            if f(tmp) == 0 :
                return (i, j, 0)

        #on test pour toutes les lignes de la matrice si le coup est gagnant
        for j in range(1, getRowNb(p[i])) :
            tmp = p.copy()
            tmp.pop(i)
            tmp.extend(chompL(p[i], j))
            #si jamais le coup j dans la matrice p[i] est gagnant, on sait ou jouer
            if f(tmp) == 0 :
                return (i, j, 1)

    #si on ne sait pas ou jouer pour pouvoir obtenir un coup gagnant selon la définition de f(p)
    return (0, 1, 1)
def main() :
    ag = aleaGame()
    for i in range(0, len(ag)) :
        print(ag[i], "\n")
    joueur = 1
    while ag != [] :
        joueur = (joueur + 1) % 2
        if joueur == 0 :
            (i, n, s) = getWinningStrat(ag)
            ag.pop(i)
            if s == 0 :
                chompC(ag[i], n)
            else :
                ag.extend(chompL(ag[i], n))
        else :
            #choix de la matrice ou l'on veut supprimer une ligne ou une colonne
            m = -1
            while m == -1:
                try :
                    m = int(input("choisissez une matrice (1 - {}) :".format(len(ag) + 1)))
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
            ag.pop(m - 1)
            if s == 'h' :
                ag.extend(chompL(ag[m - 1], n))
            else :
                ag.extend(chompC(ag[m - 1], n))



if __name__ == '__main__' :
    main()
