# On demande la valeur de X à l'utilisateur
x = float(input("Entrez un nombre supérieur à 1 : "))

# On initialise le compteur à 0
n = 0
# On initialise la somme à 0
somme = 0

# On boucle tant que la somme est inférieure ou égale à X
while somme <= x:
  # On incrémente la somme
  somme += n
  # On incrémente le compteur
  print(n)
  n += 1

# On décrémente le compteur car la dernière itération a fait la somme dépasser X
print("2",n)
n -= 2

# On affiche le résultat
print("Le plus grand nombre N tel que ∑𝑖𝑁𝑖=0 ≤ 𝑋 est", n)