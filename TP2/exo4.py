BASE=4
fromage=800.0
eau=2
ail=2
pain=400
nbConvives=int(input("Entrez le nombre de personne(s) conviées à la fondue :"))
new_fromage=(fromage*nbConvives)/BASE
new_eau=(eau*nbConvives)/BASE
new_ail=(ail*nbConvives)/BASE
new_pain=(pain*nbConvives)/BASE
print(f"Pour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut: \n - {new_fromage} gr de fromages \n - {new_eau} dl d'eau \n - {new_ail} gousse(s) d'ail \n - {new_pain} gr de pain")



