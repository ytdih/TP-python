valeurs = int(input("entrer une somme d argent"))

cent = (valeurs//100)

cinquante = int((valeurs - (cent*100))//50)

dix = int(((valeurs-100*cent) - 50*cinquante)//10)

deux = int((((valeurs - 100*cent)-50*cinquante )-10*dix)//2)

un = (((((valeurs -100*cent)-50*cinquante) -10*dix) -2*deux)//1)

print(f"{valeurs} euros , c est donc {cent} billets de 100, {cinquante} billets de 50,{dix}billets de 10,{deux}pieces de 2, {un}pieces de 1")