entrer=int(input("Entrer un nombre entier :"))
if entrer != 0 and entrer % 2 ==0:
    if entrer > 0:
        print("le Nombre est positif et pair")
    else:
        print("Le nombre est negatif et pair")

elif entrer == 0:
    print("Le nombre est zéro (et il est pair)")
else:
    if entrer < 0:
        print("Le nombre est negatif et impaire")
    else:
        print("Le nombre est positif et impaire")

