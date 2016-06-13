#!/usr/bin/python3

#specification :
#l'IA utilise dans ce jeu joue toujours en dernier (joueur 1)
#si jamais il n'y a pas de cout gagnant (nimber != 0) l'IA joue le Premier
#tas et enleve 1 unites

#le jeu prend fin sur la suppression de la derniere unite 
#et le joueur dont c'etait le tour gagne
from random import randrange
from ia import getwinningStrat
from ia import randomStrat

print("implementation jeu de nim (tas de maximum 50 unites) : ")

ntas = int(input("nombre de tas maximums : "))

# generation aleatoire de la situation de jeu
l = list()
for i in range(0, ntas):
    l.append(int(randrange(1, 50)))

continuer = 1
joueur = 0
#gestion du jeu
while continuer :
    print(l)
    #print("joueur {} a vous de jouer !".format(joueur))
    
    if joueur == 1:
        print("ia play")
        tas, k = getwinningStrat(l)
    else :
        # print("random play")
        # tas, k = randomStrat(l)
        print("choisissez un tas(valeur entre {} et {}) :".format(0, ntas -1))
        #choix du tas que l'on veut diminuer
        tas = -1
        while tas < 0:
            try :
              tas = int(input())
              assert tas >= 0
              assert tas < ntas
            except AssertionError :
              print("valeur non valide recommencez :")
              tas = -1

        #choix du nombre d'unite que l'on veut enlever
        k = -1
        print(\
        "choisissez le nombre a enlever du tas (entre {} et {}):".format(1, l[tas]))
        while k < 0 :
            try :
              k = int(input())
              assert k > 0
              assert k <= l[tas]
            except AssertionError :
              print("valeur non valide recommencez : ")
              k = -1
    
    print("dans le tas {} en elevant {} unite".format(tas, k))
    l[tas] -= k
    if l[tas] == 0 :
        l.remove(0)
        ntas -= 1

    if ntas == 0 :
        continuer = 0
        if joueur != 0 :
            print("joueur 1 gagne")
        else :
            print("joueur 1 perd!")

    joueur = (joueur + 1) % 2