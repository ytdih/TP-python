# Enregistrement des logins dans le tuplet "binome"
login1 = input("Entrez votre login : ")
login2 = input("Entrez le login de votre voisin de tp : ")
binome = (login1, login2)

# Affichage des logins dans une chaîne de caractères
print("L'étudiant " + binome[0] + " est en binome avec l'étudiant " + binome[1])

# Demander si l'utilisateur souhaite changer de binôme
change_binome = input("Voulez-vous changer de binôme? (oui/non)")
if change_binome == "oui":
    # Saisie du nouveau login
    new_login = input("Entrez le nouveau login : ")

    # Modification du second élément du tuplet "binome"
    binome = (binome[0], new_login)

    # Affichage des logins dans une chaîne de caractères
    print("L'étudiant " + binome[0] + " est en binome avec l'étudiant " + binome[1])
else:
    print("Aucun changement de binôme effectué.")
