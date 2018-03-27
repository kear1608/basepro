# Projet Tri - Base de la programmation - Eric Derasse (2017)
# Auteurs :Ariel Keutcha

# codage utilisé pour les accents
# coding=utf-8

import os  
import random
import time

#**********************************************************************
# Couche application (Graphique)
#**********************************************************************

# Selection des fonctions
def Menu(): 
    # Déclaration du tableau principal
    maTable = []
    reponse = 1

    while reponse < 9: 
			
        print("Menu : ")
        print("------")
        print("")
        print("01. Initialiser")
        print("02. Charger")
        print("03. Tri rapide")
        print("04. Reverse")
        print("09. Sauver")	
        print("10. Quitter")
		
	#nomFichier = ""
        reponse = int(input("Faites votre choix : "))
        
        if reponse == 1 : 
            selectMenuInit()
			
        elif reponse == 2 :
            selectMenuCharger(maTable)
				
        elif reponse == 3 :
            selectMenuTriRapide(maTable)

        elif reponse == 4 :
            selectMenuReverse(maTable)

        elif reponse == 9 :
            selectMenuSauvegarde(maTable)
		
        elif reponse == 10 :
            break
		
        input("Appuyez sur une touche pour continuer ... ")
        os.system('clear')
	
def selectMenuInit() :
	
    nomFichier = input("Quel est le nom de votre fichier ?  ")
    nb = int(input("Combien de nombre voulez-vous ? "))
	
    if not nomFichier.isalpha():
        nomFichier="iniTab.txt"
		
    initTab(nomFichier,nb)
	
def selectMenuCharger(maTable):
	nomFichier = input("Quel est le nom de votre fichier ? ")
	nb = int(input("Combien de nombre voulez-vous ? "))

	if not nomFichier.isalpha():
		nomFichier="iniTab.txt"
		
	loadTab(maTable,nomFichier,nb)
	print("Voici les nombres selectionnes : ",maTable)
    
def selectMenuTriRapide(maTable):
    data=open("./data.txt", "a")
    print ("Voici les nombres selectionnes : ")
    print (maTable)
    start_time = time.time()
    triRapide(maTable,0,len(maTable)-1)
    print("Voici les nombres tries : ")
    print (maTable)
    process=(time.time() - start_time)
    data.write(str(process) + " ; ")
    print (process)

def selectMenuReverse(maTable):
    print ("Voici les nombres selectionnes : ")
    print(maTable)
    print ("Voici les nombres inversés : ")
    Reverse(maTable)
    
def selectMenuSauvegarde(maTable) :
    nomFichier = input("Quel est le nom de votre fichier de sauvegarde ? ")
    saveTab(maTable,nomFichier)
	
	
#**********************************************************************
# Couche logique (Métier)
#**********************************************************************

def Reverse(maTable):
    x = len(maTable)-1
    i = 0
    while i < x:
        temp = maTable[i]
        maTable[i] = maTable[x]
        maTable[x] = temp
        i = i + 1
        x = x - 1
    print (maTable)

def triRapide(maTable, left, right, niveau = 0, position=""):
    if left < right:
        print("Niveau récursion {0}{1} - Indices {2} à {3}".format(niveau, position, left, right))
        splitpoint = partition(maTable, left, right)
        print("Point de coupure indice {0}".format(splitpoint))

        triRapide(maTable, left, splitpoint - 1, niveau + 1, position + ".gauche")
        triRapide(maTable, splitpoint + 1, right, niveau + 1, position + ".droite")
    else:
        print("Niveau {0}{1} - Rien à faire".format(niveau, position))

def afficheTableau(maTable):
    s = ""
    for k in range(0, len(maTable)):
        s += '{0: <{width}}|'.format(maTable[k], width=3)
    print(s)

def afficheIndex(maTable, indexpivot, left, right):
    if left < right:
        print("   |" * indexpivot + " X |" + "   |" * (left - indexpivot - 1) + " ^ " + "|   " * (
                    right - left - 1) + "| ^ " + "|   " * (len(maTable) - right))
    elif left == right:
        print("   |" * indexpivot + " X |" + "   |" * (left - indexpivot - 1) + " ^ " + "|   " * (
                    len(maTable) - right))

def partition(maTable, left, right):
    pivotvalue = maTable[left]
    print("Le pivot est:", pivotvalue)
    i = left + 1
    j = right
    afficheIndex(maTable, left, i, j)
    done = False
    while not done:
        while i <= j and maTable[i] <= pivotvalue:
            i = i + 1
            afficheIndex(maTable, left, i, j)
        while maTable[j] >= pivotvalue and j >= i:
            j = j - 1
            afficheIndex(maTable, left, i, j)
        if j < i:
            done = True
            print("Terminé avec le pivot ", pivotvalue)
        else:
            temp = maTable[i]
            maTable[i] = maTable[j]
            maTable[j] = temp
            print("Échange de {0} et {1} et on continue avec le même pivot".format(maTable[i], maTable[j]))
            afficheTableau(maTable)

    temp = maTable[left]
    maTable[left] = maTable[j]
    maTable[j] = temp
    print("Échange de {0} et {1}".format(maTable[left], maTable[j]))
    afficheTableau(maTable)
    return j

#**********************************************************************
# Couche données (Data)
#**********************************************************************			

# Génération des nombres entier aléatoires et sauvegarde dans un fichier

def initTab(fichier,nb):
	fichier = open(fichier,"w")
	for i in range(0,nb):
		nombre = random.randint(0,nb)
		print ((nombre), file = fichier)
	fichier.close()        
	
# Chargement du fichier dans un tableau en mémoire
def loadTab(maTable,fichier,nb):
	fichier = open(fichier,"r")
	for i in range(nb):
		var = fichier.readline()
		maTable.append(int(var))
	fichier.close()

# Sauvegarde du tableau en mémoire dans un fichier
def saveTab(maTable,fichier):
	fichier = open(fichier,"w")	
	for i in range(0,len(maTable)-1):
		print ((maTable[i]), file = fichier)
	fichier.close()  

#**********************************************************************
# Programme principal
#**********************************************************************	
Menu()
