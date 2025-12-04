

T = input("Entrez une chaîne : ")


taille = 0
for c in T:
    taille += 1

print(f"1) Taille de la chaîne : {taille}")


voyelles = "aeiouyAEIOUY"
nb_voyelles = 0

for c in T:
    if c in voyelles:
        nb_voyelles += 1

pourcentage = (nb_voyelles / taille) * 100 if taille > 0 else 0

print(f"2) Pourcentage de voyelles : {pourcentage:.2f}%")


mot = "wagon"
long_mot = 0
for c in mot:
    long_mot += 1

premiere_occ = -1

for i in range(taille - long_mot + 1):
    j = 0
    correspond = True
    while j < long_mot:
        if T[i + j].lower() != mot[j]:
            correspond = False
            break
        j += 1
    if correspond:
        premiere_occ = i
        break

if premiere_occ != -1:
    print(f"3) 'wagon' apparaît dans T, première occurrence à l'indice : {premiere_occ}")
else:
    print("3) 'wagon' n'apparaît pas dans T.")


nb_occ = 0

for i in range(taille - long_mot + 1):
    j = 0
    correspond = True
    while j < long_mot:
        if T[i + j].lower() != mot[j]:
            correspond = False
            break
        j += 1
    if correspond:
        nb_occ += 1

print(f"4) Nombre d'occurrences de 'wagon' : {nb_occ}")