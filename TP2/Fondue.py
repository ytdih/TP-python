Base = 4
fromage =800
eau=2
ail=2
pain=400
print("Entrer le nombre de convive:")

nbConvives=int(input())
print("Pour faire une fondue Fribourgeoise pour",nbConvives,"il vous faut:")
print("-",fromage*nbConvives/Base,"gr de fromage")
print("-",eau*nbConvives/Base,"dL d'eau")
print("-",ail*nbConvives/Base," gousse(s) d'ail")
print("-",pain*nbConvives/Base,"gr de pain")