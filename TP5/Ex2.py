# Initialisation des variables
notes = [] # liste pour stocker les notes
coefs = [] # liste pour stocker les coefficients
moyenne = 0 # variable pour stocker la moyenne générale

# Boucle pour demander les notes et coefficients
for i in range(5):
    input_string = input(f"Veuillez entrer la note du module {i+1} et le coefficient correspondant : ")
    note, coef = input_string.split(" ")
    notes.append(float(note))
    coefs.append(int(coef))

# Calcul de la moyenne générale
for i in range(5):
    moyenne += notes[i] * coefs[i]
moyenne = moyenne / sum(coefs)

# Evaluation de l'étudiant
if moyenne > 10:
    if all(note >= 8 for note in notes):
        print("L'étudiant est admis.")
    else:
        print("L'étudiant n'est pas admis.")
else:
    print("L'étudiant n'est pas admis.")
