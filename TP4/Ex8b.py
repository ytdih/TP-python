dic = {"name":"toto","firstname":"titi","promo":2022,"group":202}

# Affichage des clés
print("Les clés du dictionnaire sont :")
for key in dic.keys():
    print("-" + key)

# Affichage des valeurs
print("Les valeurs du dictionnaire sont :")
for value in dic.values():
    print("-" + str(value))

# Affichage des tuplets
print("Les tuplets du dictionnaire sont :")
for key, value in dic.items():
    print("-('" + key + "', " + str(value) + ")")
