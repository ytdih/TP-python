N = int(input("Entrez le nombre N: "))
somme = 0

for i in range(N+1):
    somme += i
print("La somme des entiers naturels de 0 à N est:", somme)