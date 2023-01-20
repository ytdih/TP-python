x=0
moins10=0
moins15=0
plus15=0
while x!=10:
    val=int(input("Etrer une valeurs"))
    if val > 21 or val < 0:
        print("La valeurs n'est pas bonne")
    else:
        x=x+1
        if val>0 and val<10:
            moins10=moins10+1
        elif val>9 and val<15:
            moins15=moins15+1
        else:
            plus15=plus15+1
print("il y a",moins10,"valeurs inferieur a 10 et ",moins15,"inferieur a 15 et ",plus15,"superieur a 15")


