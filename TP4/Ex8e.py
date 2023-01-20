student1 = {"name":"toto","firstname":"titi","promo":2022,"group":202}

# Création du dictionnaire pour le second étudiant
student2 = {"name":"zero","firstname":"tata","promo":2022,"group":202}

# Création du dictionnaire binome
binome = {"123": student1, "456": student2}

# Affichage des étudiants dans le binôme
print("Les étudiants formant le binôme sont :")
for key, value in binome.items():
    print(f"- L'étudiant {value['name']} {value['firstname']} du groupe {value['group']}")
