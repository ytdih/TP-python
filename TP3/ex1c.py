compteur_inf_10 = 0
compteur_sup_10_inf_15 = 0
compteur_sup_15 = 0

for i in range(10):
    val = int(input("Entrez une valeur: "))
    while val < 0 or val > 20:
        val = int(input("Entrez une valeur valide: "))
    if val>0 or val <20:
        if val < 10:
            compteur_inf_10 = (compteur_inf_10+ 1)
        elif val >= 10 and val < 15:
            compteur_sup_10_inf_15 = (compteur_sup_10_inf_15 + 1)
        else:
            compteur_sup_15 = (compteur_sup_15 + 1)

print("Nombre de valeurs inférieures à 10:", compteur_inf_10)
print("Nombre de valeurs supérieures ou égales à 10 et inférieures strictement à 15:", compteur_sup_10_inf_15)
print("Nombre de valeurs supérieures ou égales à 15:", compteur_sup_15)