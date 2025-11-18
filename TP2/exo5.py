nb=int(input("Entrez un nombre entier:"))
if nb%2==0 and nb>0 :
    print("Le nombre est positif et pair")
elif nb==0 :
    print ("Le nombre est zéro (et il est pair")
elif nb%2==0 and nb<0:
    print("Le nombre est négatif et pair")
elif nb%2==1 and nb>0:
    print("Le nombre est positif et impair")
else:
    print("Le nombre est négatif et impair")

