import random

plateau = [" " for _ in range(9)]

#tableau
def afficher_plateau():
    print()
    print(plateau[0], "|",plateau[1], "|",plateau[2])
    print("--+---+--")
    print(plateau[3], "|",plateau[4], "|",plateau[5])
    print("--+---+--")
    print(plateau[6], "|",plateau[7], "|",plateau[8])
    print()

#verifier la victoire
def verifier(symbole):
    lignes = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for ligne in lignes:
        if plateau[ligne[0]] == symbole and plateau[ligne[1]]== symbole and plateau[ligne[2]]==symbole:
          return True
    return False

#tour du joueur
def joueur():
    choix=int(input("choisis une case (1 à 9) : "))
    choix = choix -1
    if plateau[choix] == " ":
        plateau[choix] = "X"
    else:
        print("case occupée, rejoue.")
        joueur()

#tour du robot
def robot():
    print("le robot joue...")
    choix = random.randint(0,8)
    while plateau[choix] != " ":
        choix = random.randint(0,8)
    plateau[choix] = "O"

#contre le joueur
def counter():
    print("le robot joue...")

    for i in range(9):
        if plateau[i] == " ":
            plateau[i] = "X"
            if verifier("X"):
                plateau[i]= "O"
                return
            plateau[i] = " "
    
    
    choix = random.choice([i for i in range(9) if plateau[i] == " "])
    plateau[choix] = "O"

#jeu pricipal
def jouer_ia():
    afficher_plateau()
    for tour in range(9):
        if tour % 2 == 0:
            joueur()
        else:
            counter()
        afficher_plateau()
        
        if verifier("X"):
            print("Victoire")
            return
        elif verifier("O"):
            print("Défaite")   
            return
    print("égalité")    

def jouer_normal():
    afficher_plateau()
    for tour in range(9):
        if tour % 2 == 0:
            joueur()
        else:
            robot()
        afficher_plateau()
        
        if verifier("X"):
            print("Victoire")
            return
        elif verifier("O"):
            print("Défaite")   
            return
    print("égalité")    

def jouer():
    ia=input("ia or normal : ")
    if ia == "ia":
        return jouer_ia()
    elif ia == "normal":
        return jouer_normal()
    else:
        print("invalid")
        return jouer ()
    
jouer()