# Création du dictionnaire pour la première personne
person1 = {"name":"toto","firstname":"titi","promo":2022,"group":202}

# Création du dictionnaire pour la seconde personne
person2 = {"name":"zero","firstname":"tata","promo":2022,"group":202}

# création du dicionnaire binome 
binome = {"person1":person1,"person2":person2}

# Affichage des clés
print("Les clés du dictionnaire sont :")
for key in binome.keys():
    print("-" + key)

# Affichage des valeurs
print("Les valeurs du dictionnaire sont :")
for key in binome.keys():
    print(f'-{binome[key]["name"]}, {binome[key]["firstname"]}')
    print(f'-{binome[key]["promo"]}, {binome[key]["group"]}')

# Affichage des tuplets
print("Les tuplets du dictionnaire sont :")
for key in binome.keys():
    for key1,value in binome[key].items():
        print(f"-('{key1}', {value})" )
