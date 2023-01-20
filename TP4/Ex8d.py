# Création du dictionnaire pour le premier étudiant
student1 = {"name":"toto","firstname":"titi","promo":2022,"group":202}

# Création du dictionnaire pour le second étudiant
student2 = {"name":"zero","firstname":"tata","promo":2022,"group":202}

# Création du dictionnaire binome
binome = {"123": student1, "456": student2}

# Affichage des informations des étudiants dans le binôme
for key, value in binome.items():
    print("Etudiant avec l'id " + key + " :")
    for key1, value1 in value.items():
        print(key1 + " : " + str(value1))
