
chaine = input("Entrer une chaine de caractere")
characters = "'!?,;:§^¨£$¤*µ=+-_1324567890&\è|()[]}{#~²<>/. "

for x in range(len(characters)):
    chaine = chaine.replace(characters[x],"")

min = chaine.lower()
phrase = [min]
print(phrase)
if phrase == phrase[::-1]:
    print("C est un palindrome")
else:
    print("ce n est pas un palindrome")
