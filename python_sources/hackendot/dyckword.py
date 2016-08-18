from random import randrange

"""
    défini les fonctions d'utilisation des mots de Dyck
    Un mot de Dyck est un mot bien parenthésé (nb pour chaque parenthèse
    ouvrante, il y a une parenthèse fermante qui la suit)
    on défini la grammaire des mots de Dyck de la façon :
        alphabet : {'(', ')'}
        S -> () | ()S | (S) | (S)S
              1    2     3      4
"""

"""
    permet de générer aléatoirement un mot de Dyck de façon récursive
    Sortie :
        mot de Dyck généré aléatoirement sur la grammaire définie
"""
def randomDyckWord():
    #valeur de la transition de la grammaire défini plus haut
    n = randrange(1, 5)
    if n == 1 :
        #premier car des transitions de S : ()
        return "()"

    if n == 2 :
        #2e cas des transitions de S : ()S
        return "()" + randomDyckWord()

    if n == 3 :
        #3e cas des transitions de S : (S)
        return "(" + randomDyckWord() + ")"
    
    if n == 4 :
        #4e cas des transitions de S : (S)S
        return "(" + randomDyckWord() + ")" + randomDyckWord()

"""
    permet de créer les listes préfixe et suffixe d'une foret à partir d'un mot de Dyck généré aléatoirement
    sortie :
        tuple de la forme (liste préfixe, liste suffixe)
"""
def getForestList() :
    #mot de Dyck définissant notre foret
    word =  randomDyckWord()
    #pile permettant de construire notre liste suffixe
    stack = []
    #liste préfixe de notre foret
    p = []
    #liste suffixe de notre foret
    s = []

    #numéro du  nœud
    count = 1
    for c in word :
        if c == '(' :
            #on commence un arbre
            p.append(count)
            stack.append(count)
            count += 1
        else :
            #on termine un arbre
            s.append(stack.pop())
            
    return p, s