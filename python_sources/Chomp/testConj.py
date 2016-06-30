from random import randrange
from pylab import ones
from numpy import array
import numpy
from resolver import *

"""
    Fichier de test pour la conjecture effectué sur le jeu de Chomp revisité

    Nous avons prouvé que 
        -Nimber(1xn) = Nimber(nx1) = n
        -Nimber(2nx2m) = 0

    et nous voulons tester que si on a une tablette mxn avec m et n != 1
    et m ou n impair, alors on a :
        nimber(mxn) = 1 si m+n impair
                      2 sinon

    le premier test a été effectué pour les 66 premières matrices de maximum 11 lignes 
    et 11 colonnes et nous n'avons pas eu de contre exemple.

    une idée d’amélioration serait de faire un dictionnaire pour les tablettes calculées
    c'est a dire :
        mémoriser l'association d'une tablette a son nimber

    Ceci permettrai de pouvoir aller beaucoup plus loin dans les tests (110 secondes pour les 66 premières matrices)
"""

#calcul du nimber de façon exhaustive
"""
    calcul du nimber d'une position donné avec une ou plusieurs tablettes
"""
def exhaustive(tabl) :
    nimber = 0
    for i in tabl :
        n = getNimber(i)
        nimber = nimber ^ n
    
    return nimber

"""
    calcul du nimber d'une tablette unique
"""
def  getNimber(tabl) :
        nbL, nbC = tabl.shape
        #premiere conjecture
        if nbL == 1 or nbC == 1 :
            return nbC if nbL == 1 else nbL        
        #deuxieme conjecture
        if nbL % 2 == 0 and nbC % 2 == 0 :
            return 0

        nimbers = []
        succ = getSucc(tabl)
        for i in succ :
            nimbers.append(exhaustive(i))

        # print(nimbers)
        # print(succ)
        # print(max(nimbers) + 1)
        for i in range(0, max(nimbers) + 2):
            if i not in nimbers :
                return i

        return -1
"""
    calcul et retourne la liste des successeurs
"""
def getSucc(tabl) :
    nbL, nbC = tabl.shape
    res = []
    for l in range(1, int(nbL / 2) + 2) :
        tmp = chompL(tabl, l)
        (ll,cc) = tmp[0].shape
        if ll != 0 and cc != 0 :
            res.append(tmp)
       
    for c in range(1, int (nbC / 2) + 2) :
        tmp = chompC(tabl, c)
        (ll,cc) = tmp[0].shape
        if ll != 0 and cc != 0 :
            res.append(tmp)
        else :
            #cas d'une matrice vide important a prendre en compte car nimber 
            #d'une matrice vide = 0
            res.append([])
       
    return res

#calcul du nimber d’après notre conjecture
"""
    calcul du nimber d’après la conjecture faite
"""
def conjecture(tabl) :
    nbL, nbC = tabl.shape

    #premiere conjecture
    if nbL == 1 or nbC == 1 :
        return nbC if nbL == 1 else nbL
    
    #deuxieme conjecture
    if nbL % 2 == 0 and nbC % 2 == 0 :
        return 0

    #troisieme conjecture
    return 2 if (nbL + nbC) % 2 == 0 else 1

#creation de la tablette
"""
    génère une tablette de maxC colonnes et maxL lignes
    par défaut crée une tablette 5x5
"""
def createTable(maxC=5, maxL=5) :
    i = 0
    li = []
    for j in range(0, maxL) :
        li.append(ones(maxC))

    return array(li)

#point d’entrée du programme
"""
    fonction qui test toutes les tablettes de la forme
    1x1, 1x2, ... 1xmaxC, 2x2,...maxLxmacC
"""
def main(maxL, maxC) :
    for i in range(1, maxL + 1) :
        for j in range(i, maxC + 1) :
            t = createTable(j, i)
            e = getNimber(t)
            c = conjecture(t)
            print("matrice {}x{}".format(i, j))
            print(e == c, "nimberE =", e, "nimberC =", c)      

if __name__ == '__main__' :
    main(11, 11)