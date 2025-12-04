nbr = float(input("Vous chercher la table de multiplication de quel nombre ? "))
L = []
for i in range(10):
    L.append(nbr*float(i))
    print(f"{nbr} * {i} = {L[i]}")