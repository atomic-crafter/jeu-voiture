from pygame import *
import random

init()


GameOver = False

longeur = 1200
largeur = 1000

screen = display.set_mode((longeur, largeur))

def differenceSuivante(x):
	return x+random.randint(-10,10)
def construitListe(hauteur,nombre):
	solList = []
	solList.append((hauteur,0))
	for i in range(1,nombre):		
		dernierElement = solList[-1]
		h = dernierElement[0]
		v = dernierElement[1]
		z = differenceSuivante(v)
		solList.append((h+z,z))
	return solList
def afficheListe(l,i,s):
	element = l[i]
	elementSuivant = l[i+1]


	draw.line(s,(255,0,0),(i*10,element[0]),((i+1)*10,elementSuivant[0]))



liste = construitListe(100,20)
afficheListe(liste,0,screen)
#while not GameOver:
#	def setUpSol():
#		solList = []
