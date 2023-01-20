from time import sleep
# On demande à l'utilisateur de saisir un entier positif
i = int(input("Entrez un entier positif : "))
# On initialise le compteur à n
# On boucle tant que le compteur est supérieur ou égal à 0
while i >= 0:
  print(i)
  sleep(0.2)
  # On décrémente le compteur
  i -= 1