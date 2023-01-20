# Déclare la taille maximale des vecteurs
nMax = 10

# Déclare les listes vides pour les vecteurs
v1 = []
v2 = []

# Demande à l'utilisateur la taille effective des vecteurs
n = int(input("Quelle est la taille de vos vecteurs [entre 1 et {}] ? ".format(nMax)))

# Vérifie que n est compris entre 1 et nMax
while n < 1 or n > nMax:
  print("La taille doit être comprise entre 1 et {}.".format(nMax))
  n = int(input("Quelle est la taille de vos vecteurs [entre 1 et {}] ? ".format(nMax)))

# Demande les composantes des vecteurs à l'utilisateur
print("Saisie du premier vecteur :")
for i in range(n):
  v1.append(int(input("v1[{}] = ".format(i))))

print("Saisie du second vecteur :")
for i in range(n):
  v2.append(int(input("v2[{}] = ".format(i))))

# Calcule le produit scalaire de v1 et v2
produit = 0
for i in range(n):
  produit += v1[i] * v2[i]

# Affiche le résultat
print("Le produit scalaire de v1 par v2 vaut {}.".format(produit))
