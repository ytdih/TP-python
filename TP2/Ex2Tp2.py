import datetime
print("Donnez votre age :")
age=int(input())
anneencour = datetime.datetime.now()
date = anneencour.date()
annee = int(date.strftime("%Y"))
print("Votre annee de naissane est:",(annee-age))