X = float(input("Entrez une valeur X (supérieure à 1) : "))

while X <= 1:
    X = float(input("X doit être > 1. Entrez une nouvelle valeur : "))

# Calcul de N
somme = 0
N = 0

while True:
    if somme + N > X:     # si ajouter N dépasse X, on s'arrête
        break
    somme += N
    N += 1

# À la fin, N a été incrémenté 1 fois en trop → on retire 1
N -= 1

print(f"Le plus grand nombre N tel que la somme 0+1+...+N <= {X} est : {N}")