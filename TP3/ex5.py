# On demande à l'utilisateur de saisir l'heure de début de location
debut = int(input("Donnez l'heure de début de la location (un entier) : "))

# On demande à l'utilisateur de saisir l'heure de fin de location
fin = int(input("Donnez l'heure de fin de la location (un entier) : "))

# Si l'heure de début ou l'heure de fin sont incorrectes
if debut < 0 or debut > 24 or fin < 0 or fin > 24:
  print("Les heures doivent être comprises entre 0 et 24 !\n")

# Si les heures de début et de fin sont identiques
elif debut == fin:
  print("Attention ! l'heure de fin est identique à l'heure de début.\n")

# Si l'heure de début est supérieure à l'heure de fin
elif debut > fin:
  print("Attention ! le début de la location est après la fin ...\n")

# Si les données sont correctes
else:
  # On initialise le tarif à 0
  tempstot = fin - debut
  if tempstot < 7:
    print(tempstot,"heure(s) au tarif horaire de 1.0 euro (s)")
    print("Le montant total à payer est de ",tempstot,"euro (s)")
  else:
    print(tempstot,"heure(s) au tarif horaire de 2.0 euro (s)")
    print("Le montant total à payer est de ",tempstot*2,"euro (s)")

  tarif = 0
  # On initialise le nombre d'
