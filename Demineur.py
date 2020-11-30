"Robin Boulet"
import random

gameOver = False

bombe = False

plateau = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

affichagePlateau = [[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."],[".",".",".",".",".","."]]

def affichage(affichagePlateau):

  print("  0 1 2 3 4 5")
  print("  _ _ _ _ _ _ ")
  for ligne in range(0,6):
    print(ligne, end="|")
    for colonne in range(0,6):
      print(affichagePlateau[ligne][colonne], end=" ")
    print("")


while bombe == False:

    for i in range(len(plateau)):
        
        for j in range(len(plateau[i])):

            plateau[i][j] = random.randint(1,5)
            if(plateau[i][j] == 5):
                plateau[i][j] = "B"
                bombe = True
            else:
                plateau[i][j] = 0


while gameOver == False:

    affichage(affichagePlateau)
    ligne = int(input("ligne (0-5) : "))
    colonne = int(input("colonne (0-5) : "))

    if(colonne in range(len(plateau)) and ligne in range(len(plateau))):

      if(plateau[ligne][colonne] == "B"):
          gameOver = True
          
          print("Perdu !")
          print("-")
          affichage(plateau)
          print("-")

      sideBomb = 0
      
      if(colonne != 2):
          if(plateau[ligne][colonne] == "B"):
              sideBomb=sideBomb+1
              
      if(colonne != 0):
          if(plateau[ligne][colonne-1] == "B"):
              sideBomb=sideBomb+1
              

      if(ligne != 0):
          if(plateau[ligne-1][colonne] == "B"):
              sideBomb=sideBomb+1
          
          if(colonne != 0):
              if(plateau[ligne-1][colonne-1] == "B"):
                  sideBomb=sideBomb+1
              
          if(colonne != 2):
              if(plateau[ligne-1][colonne] == "B"):
                  sideBomb=sideBomb+1

      if(ligne !=2):
          if(plateau[ligne][colonne] == "B"):
              sideBomb=sideBomb+1

          if(colonne != 0):
              if(plateau[ligne][colonne-1] == "B"):
                  sideBomb=sideBomb+1

          if(colonne != 2):
            if(plateau[ligne][colonne] == "B"):
                  sideBomb=sideBomb+1


      affichagePlateau[ligne][colonne] =sideBomb


      """
      print("-")
      affichage(plateau)
      print("-")
      """
