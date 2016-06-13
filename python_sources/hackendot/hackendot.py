#!/usr/bin/python3

""" 
    jeu de la foret pour la méthode de résolution de l'article de
    j. Ulehla.
"""

from winningStratUle import iaUlehla
from forest import forest

print("hackendot")

#on crée une nouvelle foret
f = forest()
#on s'assure que f est bien une foret
try :
    assert type(f) == forest
except AssertionError :
    print("erreur création arbre")
    quit()

#on crée une nouvelle ia pour le calcul du coup gagnant si il existe
ia = iaUlehla(f)
#on s'assure que ia est bien une ia
try :
    assert type(ia) == iaUlehla
except AssertionError :
    print("erreur création ia")
    quit()

joueur = 1
#tant que f n'est pas vide, le jeu n'est pas fini
while not f.isEmptyForest() :
    #on met a jour le joueur pour savoir qui doit jouer
    joueur = (joueur + 1) % 2
    #on affiche la foret
    f.printForest()
    node = -1
    if joueur == 0 :
        #si jamais c'est a l'ia de jouer, on calcul la stratégie gagnante pour f
        node = ia.getWinningStrat(f)
    else :
        #sinon le joueur donne un nœud tant qu'il n'a pas donné un nœud valide (nb qui appartient bien a cette foret)
        while node == -1 :
            try :
                node = int(input("nœud a enlever : "))
                assert node in f.getPrefixList()
            except AssertionError :
                print("valeur incorrect recommencez")
                node = -1
            except ValueError :
                print("valeur non conforme recommencez")
                node = -1

    print("le nœud {} est supprime par joueur {}".format(node, joueur))
    #on supprime le nœud au sens du jeu c'est a dire on supprime le nœud menant de la racine au nœud choisi
    f.delNodeToRoot(node)

print("joueur {} a gagne".format(joueur))