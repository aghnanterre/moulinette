#!/usr/bin/python 
# -*- coding: iso-8859-1 -*-

import os

#####################################################################
#Fonction enregistreTexte(nomFichier,texte) qui crée un fichier du nom indiqué, dans lequel on met la chaîne de caractères que contient la variable texte
  
def enregistreTexte(nomFichier,texte):
	try : fichierSortie=open(nomFichier, "w+")
	except IOError:
		print 'Cannot open file %s for writing (fontion enregistreListe).' % fichierSortie
	fichierSortie.seek(0)
	fichierSortie.write(texte)
	fichierSortie.close()


#####################################################################
#Fonction afficheTemp() fonction qui affiche en print le contenu du fichier tmp

def afficheTemp():
	try :fo = open("/Users/aguha/Documents/CNRS/Modyco/Programmation/Python/tmp", "r+")
	except IOError:
		print 'Cannot open file %s for reading' % fo
	for ligne in fo.readlines():
		print(ligne)
	fo.close()

#####################################################################
#Fonction stats(fichier) , qui renvoie le nombre de lignes, nombre de mots, et nombre de lettres

def stats(NomDeFichier):
	try :fichier = open(NomDeFichier, "r+")
	except IOError:
		print 'Je n\'arrive pas à ouvrir le fichier %s pour lecture' % fichier
	cptLignes=0
	cptMots=0
	for ligne in fichier.readlines():
		cptLignes+=1
		cptMots+=len(ligne.split())
	return (cptLignes,cptMots)


#####################################################################
# Classe monFichier : l'
#Exemple d'instanciation : 
#ff=monFichier("fichierTest.txt"<nom du fichier>,"."<répertoire>,texte<string>)


class monFichier:
	def __init__(self,n='tmp',r=str(os.getcwdu()),cont=""):
		self.nom=n
		self.repertoire=str(os.getcwdu())
		self.contenu=cont
		try : fichier=open(self.repertoire+"/"+self.nom, "w+")
		except IOError:
			print 'Je n\'arrive pas a ouvrir %s pour ecriture.' % self.nom
		if cont != "":
			fichier.write(cont)




