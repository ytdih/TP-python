heures = int(input("Nombre d heure travaillé"))

if heures >160 <200:
    salaires = (1200*25/100)+1200
    print("Son sailaires est de ",salaires,"€")
elif heures >200:
    salaires = (1200*50/100)+1200
    print("Son sailaires est de ",salaires,"€")
else:
    print("Son sailaires est de 1200€")