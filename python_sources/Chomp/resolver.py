"""
	notation :
		+n : addition de Nim standard

	Le jeu  Chomp (aussi appelé jeu  de la tablette de chocolat) est un jeu de Nim.
	On sait que pour le joueur 1, il existe une solution gagnante mais on se sait pas laquelle.
	
	On se propose ici d'essayer une stratégie sur un jeu similaire.
	Les règles de ce jeu sont :
		- on choisi un carré de la tablette et on supprime soit la ligne soit la colonne de ce carré
		- si jamais la tablette est séparé en deux, on garde bien les deux composantes, on ne les rassembles pas

	Posons la situation de jeu de façon a avoir T une tablette NxM

	et posons la fonction f(T) de la façon suivante :
		f(T) == 1 si et seulement si N est impair ou M est impair
		f(T) == 0 sinon

	étendons cette fonction  a une position P d'un jeu a n tablettes noté T1, T2, ..., Tn :
		f(P) = f(T1) +n f(T2) +n ... +n f(Tn)
"""

"""
	fonction f d'une position p
	Entrée :
		p une liste de tablettes (avec au moins une tablette)
"""
def f(p) :
	#fp est le resultat de la fonction
	fp = 0

	#pour toute tablette t de la position p, on calcul la fonction f de celle ci
	for t in p :
		if getColNb(t) % 2 != 0 or getRowNb(t) % 2 != 0 :
			fp = fp ^ 1

	return fp
"""
	retourne le nombre de colonnes de la tablette t
"""
def getColNb(t) :
	return len(t)
"""
	retourne le nombre de lignes de la tablette t
"""
def getRowNb(t) :
	return len(t[0])

"""
	retourne la tablette découpée par rapport a une colonne.
	dans cette fonction, la colonne attendu est naturelle, c'est a dire que l'on attend un entier compris entre 
	1 et len(t) (pour faciliter l'appel a cette fonction pour l'utilisateur)
	Entrée :
		t une liste représentant une tablette
		c une colonne de la tablette compris entre 1 et len(t)
"""
def chompC(t, c) :
	if c - 1 < 0 :
		raise(ValueError("erreur"))
	res = [t[0:c - 1], t[c:]]
	if [] in res:
		res.remove([])

	return res


#test :
"""
	on pose les positions de jeu suivantes :
	
	P :
		_ _ _    _ _
	   |_|_|_|  |_|_|
	   |_|_|_|  |_|_|
		 T1      T2
	
	p2 :
		_ _ _    _ _ _
	   |_|_|_|  |_|_|_|
	   |_|_|_|  |_|_|_|
		 T1       T1

	quand le carré existe bien dans la tablette, la case de la matrice le représentant est a 1
"""
#test pour la fonction chompC on prend une tablette quelconque (dans notre cas t1)
t = [[1,1], [1,1],[1,1]]
t = chompC(t, 2)
# print("t =", t)

#matrice pour T1
t1 = [[1,1], [1,1],[1,1]]
#matrice pour T2
t2 = [[1,1], [1,1]]

#matrice pour P c'est a dire une matrice regroupant les deux matrices :
p = [t1, t2]
print("p  =", p)
print("f(p) =", f(p))

#matrice pour P2 c'est a dire une matrice regroupant les deux matrices :
p2 = [t1, t1]
print("p2  =", p2)
print("f(p2) =", f(p2))
