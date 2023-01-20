# Enregistrement des informations dans un dictionnaire
info = {"firstname": input("Entrez votre prénom : "),
        "name": input("Entrez votre nom : "),
        "promo": input("Entrez votre promotion : "),
        "group": input("Entrez votre groupe de tp : ")}

# Affichage des informations
print("votre nom est '{name}', prénom est '{firstname}', vous faites partie de la promo '{promo}' et votre groupe est '{group}'".format(**info))
