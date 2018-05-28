from tkinter import *

# Variables globales
pile = []  # Contenu de la pile
entree_en_cours = ""  # Chaine de caractères représentant les chiffres entrés par l'utilisateur (input)
                      # Celle-ci est convertie en float lorsque l'utilisateur presse Entrée
                      # ou un bouton d'opération (e.g., +, *, -, /)

# Constantes définissant des les opérations de base
OP_ADD = 0 # Addition
OP_SOU = 1 # Soustraction
OP_MUL = 2 # Multiplication
OP_DIV = 3 # Division

# Ajoute un chiffre à ceux déjà entrés par l'utilisateur
def entre_chiffre(nb):
    global entree_en_cours
    entree_en_cours += str(nb)
    met_a_jour_affichage()


# Ajoute l'entrée en cours à la pile
def empile():
    global entree_en_cours
    if entree_en_cours != "":
        pile.append(float(entree_en_cours)) # Conversion de l'entrée en cours en nombre et ajout à la pile
    entree_en_cours = "" # Réinitialisation de l'entrée en cours
    met_a_jour_affichage()


# Ajoute un point aux chiffres déjà entrés par l'utilisateur
def point():
    global entree_en_cours
    entree_en_cours += "."
    met_a_jour_affichage()


# Efface l'entrée en cours, ou la pile
def clear():
    global entree_en_cours, pile
    if entree_en_cours == "":
        # Si l'entrée en cours est vide, on suppose que l'utilisateur veut effacer la pile
        pile = []
    else:
        entree_en_cours = ""
    met_a_jour_affichage()

# Mise à jours de l'affichage de la calculatrice (3 premières lignes de la pile)
def met_a_jour_affichage():
    global pile
    message = "" # On construit une chaine de charactère à afficher
    if len(pile) >= 5:
         for i in range(len(pile) -5, len(pile)):
             message += str(pile[i]) + "\n"
    else:
        for i in range(len(pile)):
            message += str(pile[i]) + "\n"
    if len(pile) > 0:
        message += "---\n"
    message += entree_en_cours
    texte_affichage["text"] = message


# Traitement d'une opération arithmétique
def operation(op):
    global pile
    empile() # On ajoute d'abord la pile ce que l'utilisateur pourrait avoir entré
    if len(pile) >= 2:
        x = pile.pop()
        y = pile.pop()
        if op == OP_ADD:
            pile.append(y + x)
        elif op == OP_SOU:
            pile.append(y - x)
        elif op == OP_MUL:
            pile.append(y * x)
        elif op == OP_DIV:
            pile.append(y / x)
        else:
            print("Operation inconnue.")
    met_a_jour_affichage()

# Crée la fenêtre principale
main = Tk()
main.geometry("500x510+553+90")
main.config(background="grey")
main.title("Calculatrice NPI")

# Ajoute un élément pour afficher la pile et l'entrée en cours
frame = Frame(main, borderwidth=9, relief=RIDGE)
frame.place(x=60, y=20)
texte_affichage = Label(frame)
texte_affichage.config(width=30, height=7, justify=RIGHT, anchor=NE, font=("Helvetica", 16))
texte_affichage.pack(padx=5, pady=5)
met_a_jour_affichage()

# Ajoute les boutons
Button(main, text="0", command=lambda: entre_chiffre(0)).place(x=140, y=400, width=50, height=30)
Button(main, text="1", command=lambda: entre_chiffre(1)).place(x=60,  y=250, width=50, height=30)
Button(main, text="2", command=lambda: entre_chiffre(2)).place(x=140, y=250, width=50, height=30)
Button(main, text="3", command=lambda: entre_chiffre(3)).place(x=220, y=250, width=50, height=30)
Button(main, text="4", command=lambda: entre_chiffre(4)).place(x=60,  y=300, width=50, height=30)
Button(main, text="5", command=lambda: entre_chiffre(5)).place(x=140, y=300, width=50, height=30)
Button(main, text="6", command=lambda: entre_chiffre(6)).place(x=220, y=300, width=50, height=30)
Button(main, text="7", command=lambda: entre_chiffre(7)).place(x=60,  y=350, width=50, height=30)
Button(main, text="8", command=lambda: entre_chiffre(8)).place(x=140, y=350, width=50, height=30)
Button(main, text="9", command=lambda: entre_chiffre(9)).place(x=220, y=350, width=50, height=30)

Button(main, text=".", command=point).place(x=60, y=400, width=50, height=30)
Button(main, text="CLS", command=clear).place(x=220, y=400, width=50, height=30)

Button(main, text="+", command=lambda: operation(OP_ADD)).place(x=300, y=400, width=50, height=30)
Button(main, text="-", command=lambda: operation(OP_SOU)).place(x=300, y=350, width=50, height=30)
Button(main, text="x", command=lambda: operation(OP_MUL)).place(x=300, y=250, width=50, height=30)
Button(main, text="/", command=lambda: operation(OP_DIV)).place(x=300, y=300, width=50, height=30)

Button(main, text="ENTRER", command=empile).place(x=380, y=350, width=80, height=30)

#Button(main, text="PILE", command=met_a_jour_affichage).place(x=380, y=425, width=80, height=30)

# Affiche la fenêtre principale construite et lance la boucle du programme
main.mainloop()
