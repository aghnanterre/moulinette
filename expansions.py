#!/usr/bin/python 
# -*- coding: utf-8 -*-
	
#####################################################################
#Fonction expansion(chaine) qui renvoie une collection de strings qui est l'expansion de la chaîne (au sens des moteurs de recherche). Si cette fonction ne définit pas explicitement le contenu de l'expansion pour chaine, alors elle renvoie une collection contenant un élément : la chaine.
#
#

def expansion(chaine):
	expansion=list()
	expansion.append(chaine) #à décommenter si on veut que l'argument de sélection... soit aussi un terme de requête.

	if chaine=="*tuvois":
		expansion.append("tu vois")
		expansion.append("Tu vois")
		
	elif chaine=="*style":
		expansion.append("style")
		expansion.append("Style")
	elif chaine=="*mere":
		expansion.append("ma mère")
		expansion.append("ta mère")
		expansion.append("sa mère")
		expansion.append("notre mère")
		expansion.append("votre mère")
		expansion.append("leur mère")
		expansion.append("ma reum")
		expansion.append("ta reum")
		expansion.append("sa reum")
		expansion.append("notre reum")
		expansion.append("votre reum")
		expansion.append("leur reum")
#		expansion.append(("leur mère")
	elif chaine=="*vasy":
		expansion.append("vas-y")
		expansion.append("Vas-y")

	elif chaine=="*putain":
		expansion.append("putain")
		expansion.append("Putain")

	elif chaine=="*ne":
		expansion.append(" n\'")
		expansion.append("N\'")
		expansion.append(" ne ")
		expansion.append("Ne ")

	elif chaine=="*genre":
		expansion.append("genre")
		expansion.append("Genre")
		
	elif chaine==("*bluff"):
		expansion.append("bluff")
		expansion.append("Bluff")
		
	elif chaine=='*wesh':
		expansion.append('wesh')
		expansion.append('wech')
		expansion.append('Wesh')
		expansion.append('Wech')

	elif chaine=='*zaama':
		expansion.append('zaama')
		expansion.append('Zaama')
		expansion.append('zama')
		expansion.append('Zama')
		expansion.append('zarma')		
		expansion.append('Zarma')		
		
	elif chaine=="*comme":
		expansion.append(" comme ")
		expansion.append("Comme ")
	
	elif chaine=='*etTout':
		expansion.append('et tout')
		expansion.append('et caetera')
		expansion.append('etc')
		expansion.append('na na na')
		expansion.append('nanana')		
		expansion.append('et bla bla bla')		
		expansion.append('Et tout')
		expansion.append('Et caetera')
		expansion.append('Etc')
		expansion.append('Na na na')
		expansion.append('Nanana')		
		expansion.append('Et bla bla bla')
		
	elif chaine=="*crari":
		expansion.append("crari")
		expansion.append("Crari")
		expansion.append("krari")

	elif chaine=="*bluff":
		expansion.append("Bluf")
		expansion.append("bluf")
	
	elif chaine== "nous*":
			expansion.append(" nous ")
			expansion.append("Nous ")
			expansion.append(" nous.")
			expansion.append("Nous.")

	elif chaine=="nouson*":
			expansion.append("Nous on ")
			expansion.append(" nous on ")
			
	elif chaine=="lon":
			expansion.append("L'on ")
			expansion.append("l'on ")

	return expansion 
	
