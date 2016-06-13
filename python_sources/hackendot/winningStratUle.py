"""
    méthode reposant sur une fonction de Nim particulière décrite par
    j. Ulehla en 1979 dans son article
       A complete Analysis of Von Neumann's Hackendot
    La méthode consiste a diviser le jeu de la foret en n jeux de la foret
    avec n le nombre d'arbre présent dans la foret initiale et calculer
    l'existence d'un coup gagnant pour chacun de ces arbres afin d'additionner
    les résultats d’après la fonction de Nim de Ulehla
    Si jamais la fonction de Nim vaut 0 pour une position donnée,
    le joueur n'a pas de stratégie gagnante, on retourne donc le premier
    nœud de la liste préfixe de la foret
    sinon le joueur a une stratégie gagnante et on retourne le premier coup
    gagnant que l'on trouve a l'aide de la méthode de Ulehla sous la forme 
    (num) ou num est le numéro du nœud a supprimer pour entrer dans une 
    stratégie gagnante
"""

from forest import forest

#variable global pour les couleurs
BLANC = 0
NOIR = 1

class iaUlehla :
    #foret que l'on utilise
    forest = None

    """
        constructeur de la classe
        entrée :
            f une foret quelconque de type forest

        si jamais f n'est pas de type forest, retourne une exception de type
        ValueError
    """
    def __init__(self, f) :
        try :
            assert type(f) == forest
        except AssertionError :
            raise  ValueError("invalid type, f must be forest type")

        self.forest = f.getForest()
    """
        fonction principale de la classe.
        Permet de retourner le coup gagnant, si il existe.
        si jamais le coup gagnant n'existe pas, retourne le premier nœud
        de la liste préfixe de la foret étudiée
    """
    def getWinningStrat(self, forest) :
        f = forest.getForest()
        forestL = [forest.getForest()]
        while not f.isEmptyForest() :
            self.lFunction(f)
            forestL.append(f.getForest())

        i = -1
        k = len(forestL) - 1
        while k > 0 and i == -1 :
            f = forestL[k]
            if self.ripFunction(f) == 1 :
                #on est dans la dernière foret avec rip(f) = 1
                i = forestL.index(f)
            k -= 1

        if i == -1 :
            return forest.getPrefixList()[0]
        if i == 0 :
            cg = self.getNodeForWin(forestL[0])
        else :
            cg = self.getNodeForWin(forestL[:i+1])

        if cg == [] :
            return forest.getPrefixList[0]
        else :
            return cg[0]

    """
        fonction de dénoyautage définie dans l'article de Ulehla comme étant
        la fonction L
    """
    def lFunction(self, f) :
        whiteNode = []
        #recherche des nœuds BLANC
        #aucun besoin de calculer la couleur de tous les nœuds, il faut seulement
        #être capable de pouvoir être sur de la couleur

        for i in f.getPrefixList() :
            if colorNode(f, i) == BLANC :
                whiteNode.append(i)

        #dénoyautage de la foret, on supprime tous les nœuds BLANC
        for i in whiteNode :
            f.delNode(i)

    """
        fonction qui calcule la parité de la foret.
        Cette fonction est la fonction Rip du papier de Ulehla
        C'est la fonction qui permet de pouvoir appliquer le théorème
        de Sprague-Grundy sur le jeu de la foret
    """
    def ripFunction(self, forest) :
        nbRW = 0
        for i in forest.getPrefixList() :
            if forest.getPredNode(i) == 0 and colorNode(forest, i) == BLANC :
               nbRW += 1

        return (nbRW % 2)

    """
        fonction qui calcul et retourne le premier noeud qui permet de gagner
        cette fonction est le raisonnement de Ulehla dans son papier et pour pouvoir
        trouver le coup gagnant, il suffit de parcourir la liste des forets dénoyautées
        en partant de la fin et en réduisant les nœuds possibles pour être un coup gagnant
    """
    def getNodeForWin(self, forestL) :
        f = forestL[len(forestL) - 1]
        tmp = f.getRoots()

        root = []
        #on enlève toutes les racines non blanches de la dernière foret
        for r in tmp :
            if colorNode(f, r) == BLANC :
                root.append(r)

        i = len(forestL) - 1
        #on pose comme nœud candidat pour être coup gagnant toutes les racines noir de la dernière foret
        possibility = root

        #tant que l'on a pas vu toutes les forets
        while i >= 0 :
            #on copie la foret au rang i de forestL
            f = forestL[i].getForest()
            #on copie la liste des candidats
            tmp = possibility.copy()
            
            #pour tous les candidats, on ajoute a la liste les fils de ces candidat
            for p in possibility :
                tmp.extend(f.getSuccNode(p))

            j = 0
            b = True
            #tant qu'il reste une possibilité
            #il existe forcement un coup gagnant d’après la définition de noyau d'un graphe
            while j < len(tmp) and b :
                ff = f.getForest()
                #on supprime un candidat
                ff.delNodeToRoot(tmp[j])

                if self.ripFunction(ff) == 0 :
                    #si jamais la fonction rip est égale a 0, on a un coup gagnant pour cette foret 
                    b = False
                    tmp = [tmp[j]]
                j += 1

            #on remet a jour la liste des candidats pour le coup gagnant et on passe a la foret précédente
            possibility = tmp.copy()
            i -= 1

        #on retourne le coup gagnant que l'on a calculé
        return possibility


#FONCTIONS POUR COLORATION
"""
    fonction qui permet de retourner la couleur d'un nœud en fonction de ses
    successeurs.
"""
def colorNodeSucc(succList) :
    b = True
    result =[]

    i = 0
    while i < len(succList) and b :
        if i == BLANC :
            b = False

    return BLANC if b == True else NOIR

"""
    fonction qui permet de colorer le nœud node
"""
def colorNode(forest, node) :
    l = forest.getSuccNode(node)

    if l == [] :
        return BLANC
    
    colorList = []
    for i in l :
        colorList.append(colorNode(forest, i))

    return colorNodeSucc(colorList)