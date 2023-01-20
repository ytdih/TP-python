L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** Completez le programme a partir d'ici.** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * 
# Déclare la liste d'entiers

# Crée un dictionnaire pour compter les occurrences de chaque élément
occurrences = {}

# Parcours la liste et compte les occurrences de chaque élément
for nombre in L1:
  if nombre in occurrences:
    occurrences[nombre] += 1
  else:
    occurrences[nombre] = 1

# Recherche l'élément le plus fréquent
element_le_plus_frequent = None
frequence_la_plus_haute = 0
for nombre, frequence in occurrences.items():
  if frequence > frequence_la_plus_haute:
    element_le_plus_frequent = nombre
    frequence_la_plus_haute = frequence

# Affiche le résultat
print(f"L'élément le plus fréquent est le {element_le_plus_frequent} et sa fréquence d'apparition est {frequence_la_plus_haute}.")

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** Ne rien modifier apres cette ligne.** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
