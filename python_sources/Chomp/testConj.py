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
            return 1

        nimbers = []
        # succ = getSucc(tabl)
        # for i in succ :
        #     nimber.append(exhaustive(i))

        # for i in (0, max(nimbers)):
        #     if i not in nimbers :
        #         return i

"""
    calcul et retourne la liste des successeurs
"""
def getSucc(tabl) :
    nbL, nbC = tabl.shape
    res = []
    for i in (1, nbL) :
        

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

#test de la conjecture

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


#TESTS
t = createTable(1,3)

print(t)
print(getNimber(t))
print(conjecture(t))