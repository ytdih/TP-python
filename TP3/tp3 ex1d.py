somme =0
x=0
n=0
choix=int(input("Entrer une valeurs superieur a 1"))
if choix < 1:
    print("la veleurs n est pas bonne")
else:
    while somme <= choix:
        n+=1
        x=x+1
        somme += x
print(somme-n)
