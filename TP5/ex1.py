noms = []

for i in range(2):
    nom = str(input("Entrer le nom de la perssonne souhaité"))
    prenom = str(input("Entrer le prénom de la perssones souhaité"))
    noms.append([nom.upper(),prenom.capitalize()])
noms.sort()
for i in range(2):
    print(prenom,nom)

