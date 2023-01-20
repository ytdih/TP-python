# Demande à l'utilisateur de saisir un nombre
nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

# Initialisation de la liste de résultats
resultats = []

# Boucle pour calculer les résultats de la table de multiplication
for i in range(1,11):
  resultat = nombre * i
  resultats.append(resultat)

# Affiche les résultats en parcourant la liste
for i in range(10):
  print(f"{nombre} * {i+1} = {resultats[i]}")
