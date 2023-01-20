import random

# On tire une valeur aléatoire entre 0 et 100
x = random.randint(0, 100)

# On initialise le compteur à 0
n = 0

# On boucle tant que l'utilisateur n'a pas trouvé le nombre mystère
while True:
  # On demande à l'utilisateur de deviner le nombre
  devine = int(input("Devinez le nombre entier entre 0 et 100 : "))
  
  # On incrémente le compteur
  n += 1
  
  # Si la valeur est inférieure
  if devine < x:
    print("Le nombre à deviner est plus grand.")
  # Si la valeur est supérieure
  elif devine > x:
    print("Le nombre à deviner est plus petit.")
  # Si la valeur est égale
  else:
    # On sort de la boucle
    break

# On affiche le résultat
print("Bravo, vous avez trouvé le nombre mystère en", n, "coups !")