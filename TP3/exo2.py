import time

# Saisie du nombre
n = int(input("Entrez un nombre entier positif : "))

# Sécurisation
while n < 0:
    n = int(input("Le nombre doit être positif. Essayez encore : "))

print("\n--- Compte à rebours (FOR) ---")

# Boucle for décroissante
for i in range(n, -1, -1):
    print(i)
    time.sleep(1)   # pause d'une seconde

    import time

    # Saisie du nombre
    n = int(input("Entrez un nombre entier positif : "))

    # Sécurisation
    while n < 0:
        n = int(input("Le nombre doit être positif. Essayez encore : "))

    print("\n--- Compte à rebours (WHILE) ---")

    # Boucle while
    i = n
    while i >= 0:
        print(i)
        time.sleep(1)  # pause d'une seconde
        i -= 1