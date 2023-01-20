date = input("Entrez une date sous la forme jjmmaaaa : ")

if len(date) != 8:
    print("La date doit être au format jjmmaaaa")
else:
    jour = int(date[0:2])
    mois = int(date[2:4])
    annee = int(date[4:8])
    
    if annee < 0:
        print("L'année ne peut pas être négative")
    elif mois < 1 or mois > 12:
        print("Le mois doit être compris entre 1 et 12")
    elif jour < 1 or jour > 31:
        print("Le jour doit être compris entre 1 et 31")
    elif mois == 2:
        if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
            if jour > 29:
                print("Février ne peut pas avoir plus de 29 jours dans une année bissextile")
            else:
                print("Date valide")
        elif jour > 28:
            print("Février ne peut pas avoir plus de 28 jours dans une année commune")
        else:
            print("Date valide")
    elif mois in [4, 6, 9, 11] and jour > 30:
        print("Ce mois ne peut pas avoir plus de 30 jours")
    else:
        print("Date valide")
