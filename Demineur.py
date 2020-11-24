"Robin Boulet"
import random

tableau = [ [0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0] ]

i = 0

#Random bombs placement
while i <8:
  ligne= random.randint(0,4)
  colonne= random.randint(0,4)
  if (tableau[ligne][colonne] != "b"):
    tableau[ligne][colonne] = "b"
    i += 1

#Array print
print("0 1 2 3 4 5")
for i in range(0,5):
  print(i, end=" ")
  for y in range(0,5):

    
    
    print(tableau[i][y], end=" ")
  print("")


print('Choisir case colonne :', end=" ")
x = int(input())

print('Choisir case ligne :', end=" ")
y = int(input())

print(tableau[x][y])




"""for i in range(-1,1):
    for y in range(-1,1):
      if(tableau[ligne+i][colonne+y] != "b" and ligne+i>=0 and ligne+i <5 and colonne+y >=0 and colonne+y <5):
        tableau[ligne+i][colonne+y] +=1"""
