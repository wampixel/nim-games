
from random import randrange

"""
    calcul le coup gagnant d'un jeu de Nim simple (jeu des tas)
    fait la somme de Nim de toutes les valeurs des tas et en déduit si il existe un coup gagnant

    si jamais le coup gagnant n'existe pas, retourne le tuple (0, 1) pour enlever dans le premier tas 1 alumette
    sinon retourne le coup gagnant
"""
def getwinningStrat(l) :
    s = 0
    for i in l:
        s += i
    s = num_add(l)
    if s == 0 :
        return 0, 1
    else :
        i = 0
        while i < len(l) :
            f = s ^ l[i]
            if f == 0 :
                return i, l[i]
            else :
                k = 0
                while k < l[i]:
                    if f ^ k == 0:
                        return i, (l[i] - k)
                    else :
                        k += 1
                i += 1

"""
    calcul et retourne la somme de Nim du jeu donné en entrée
"""
def num_add(l) :
    i = 0
    s = 0
    while i < len(l) :
        s = s ^ l[i]
        i += 1
    return s

"""
    retourne aléatoirement le coup a jouer
    cette fonction permet de ne suivre aucune méthode pour connaitre le coup gagnant
    si elle réussi a gagner, soit elle a trouvé aléatoirement le coup gagnant, soit le joueur n'as pas reussi a trouver 
    de stratégie gagnante.
"""
def randomStrat(l) :
    tas = randrange(len(l))
    k = randrange(1, l[tas] + 1)
    return tas, k
