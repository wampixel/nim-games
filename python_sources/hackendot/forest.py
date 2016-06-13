import copy
from dyckword import getForestList

class forest:
  """
    Une foret est définie par sa liste préfixe et sa liste suffixe
    Cette idée vient de Samuel Giraudo et Cédric Leroy qui l'ont implémenté dans leur projet annuel de
    théorie des graphes en 2006-2007
    Grâce a ce travail, nous pouvons prouver que connaitre a liste préfixe et suffixe d'une foret est suffisant pour le jeu du Hackendot
    Par construction, les listes préfixe et suffixe de la foret ont toujours la même longueur et ont les mêmes valeurs.
    Aucune valeur dans une liste n'apparait deux fois par construction, chacune des valeurs est unique.
  """

  #liste préfixe de la foret
  prefixe = []
  #liste suffixe de la foret
  suffixe = []

  """ 
    constructeur de la classe
    On fait appel a la fonction définie dans dyckword.py permettant de générer les listes préfixes et suffixe d'un mot aléatoire de Dyck.
    La grammaire définie pour les mots de Dyck dans dyckword.py permet de générer une foret afin d'initialiser les listes préfixe 
    et suffixe de notre foret.
  """
  def __init__(self):
   self.prefixe, self.suffixe = getForestList()
  
  """
    retourne true si la foret est vide false sinon
  """
  def isEmptyForest(self) :
    return self.forestSize() == 0

  """
    retourne la taille de la foret (nb le nombre de nœud qu'elle comprend)
  """
  def forestSize(self) :
    return len(self.prefixe)

  """
    retourne une copie de la foret
  """
  def getForest(self) :
    return copy.deepcopy(self)

  """
    retourne la liste des racines de la foret
  """
  def getRoots(self) :
    result = []
    for i in self.prefixe :
      if self.getPredNode(i) == 0 :
        result.append(i)

    return result

  """
    affiche la foret sur la sortie standard
    Pour le moment affiche seulement les listes préfixe et suffixe sur la sortie standard
  """
  def printForest(self) :
    i = 0
    print(self.prefixe, self.suffixe)

  """
    permet de supprimer le nœud de valeur value dans la foret
    Entrée :
       value la valeur que l'on veut effacer
  """
  def delNode(self, value) :
    #on a juste a supprimer la première occurrence de value dans les listes préfixes et suffixes si elle est présente dans la liste.
    if value in self.prefixe :
      (self.prefixe).remove(value)
      (self.suffixe).remove(value)

  """
    permet de supprimer tous les nœuds du chemin entre le nœud de valeur
    value et la racine
    Entrée :
      value la dernière valeur du chemin que l'on veut effacer
  """
  def delNodeToRoot(self, value) :
    nodes = self.getPredNodeList(value)
    #pour tous les predecesseurs p de ce noeud, on supprime p
    for i in nodes:
      self.delNode(i)

    self.delNode(value)
  
  """
    retourne une copie de la liste préfixe de la foret
  """
  def getPrefixList(self) :
    return (self.prefixe).copy()

  """
    retourne la liste des nœuds prédécesseurs du nœud node dans cette foret (nb tous les nœuds présent sur le chemin de la racine au nœud node)
  """
  def getPredNodeList(self, node) :
    rets = getS((self.suffixe), node)
    retp = getPInv((self.prefixe), node)
    
    if len(retp) == 0 or len(rets) == 0:
      #on est une racine, on n'a pas de père
      return []

    #on a au moins un prédécesseur, on construit donc la liste de tous les prédécesseurs
    result = []
    for i in retp :
      for j in rets :
        if i == j :
          result.append(i)

    return result

  """
    retourne le prédécesseur direct du nœud node dans la foret
  """
  def getPredNode(self, node) :
    rets = getS((self.suffixe), node)
    retp = getPInv((self.prefixe), node)
    if len(retp) == 0 or len(rets) == 0 :
      return 0

    i = 0
    for i in rets :
      if i in retp :
        return i

    return 0

  """
    retourne la liste des successeurs de node dans la foret
  """
  def getSuccNode(self, node) :
    result = []

    for i in self.prefixe :
      p = self.getPredNode(i)
      if p == node and i != node :
        result.append(i)

    return result

#NON ACCESSIBLE EN DEHORS
"""
  fonction qui retourne la liste suffixe de la foret a partir d'un nœud donné
"""
def getS(LSuffixe, node) :
  i = 0
  while i < len(LSuffixe) :
    if LSuffixe[i] == node :
      return LSuffixe[i + 1 :]
    i += 1

  return []

"""
  fonction qui retourne la liste prefixe de la foret jusqu'a un noeud donne
"""
def getPInv(LPrefixe, node) :
  i = 0 
  while i < len(LPrefixe) :
    if LPrefixe[i] == node :
      return LPrefixe[0 : i]
    i += 1

  return []