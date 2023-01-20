# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []

# Boucle pour remplir la liste de notes et calculer la somme des notes
for i in range(nombreEtudiants):
  # Demande la note de l'étudiant à l'utilisateur
  note = float(input(f"Note étudiant {i}: "))
  # Vérifie que la note est comprise entre 0 et 20
  while note < 0 or note > 20:
    print("La note doit être comprise entre 0 et 20.")
    note = float(input(f"Note étudiant {i}: "))
  # Ajoute la note à la liste et à la somme
  notes.append(note)
  moyenne += note

# Calcule la moyenne de classe
moyenne = moyenne / nombreEtudiants

# Affiche les résultats
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
  ecart = notes[i] - moyenne
  print(f"{i} | {notes[i]} | {ecart}")
