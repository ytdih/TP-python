# Déclare la liste d'entiers
liste = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

# Recherche l'élément le plus fréquent
element_le_plus_frequent = None
frequence_la_plus_haute = 0
for nombre in liste:
  frequence = liste.count(nombre)
  if frequence > frequence_la_plus_haute:
    element_le_plus_frequent = nombre
    frequence_la_plus_haute = frequence

# Affiche le résultat
print(f"L'élément le plus fréquent est le {element_le_plus_frequent} et sa fréquence d'apparition est {frequence_la_plus_haute}.")
