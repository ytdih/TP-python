# On demande à l'utilisateur de choisir la boucle à utiliser
choix = input("Choisissez la boucle à utiliser (for ou while) : ")

# On demande à l'utilisateur de saisir un entier
n = int(input("Entrez un entier : "))

# Si l'utilisateur a choisi la boucle for
if choix == "for":
  # On initialise la factorielle à 1
  fact = 1
  # On boucle de 1 à n
  for i in range(1, n+1):
    # On multiplie la factorielle par i
    fact *= i
    # On affiche l'évolution de la factorielle
    print("Iteration", i, ": fact =", fact)

# Si l'utilisateur a choisi la boucle while
elif choix == "while":
  # On initialise la factorielle à 1 et le compteur à 1
  fact = 1
  i = 1
  # On boucle tant que le compteur est inférieur ou égal à n
  while i <= n:
    # On multiplie la factorielle par i
    fact *= i
    # On affiche l'évolution de la factorielle
    print("Iteration", i, ": fact =", fact)
    # On incrémente le compteur
    i += 1

# Si l'utilisateur a saisi une valeur incorrecte
else:
  print("Vous devez choisir entre for et while.")

# On affiche le résultat final
print("Factorielle de", n, ":", fact)