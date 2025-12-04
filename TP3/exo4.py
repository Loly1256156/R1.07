n = int(input("Entrez un entier positif pour calculer sa factorielle : "))

while n < 0:
    n = int(input("⚠ L'entier doit être positif. Réessayez : "))

# Choix du type de boucle
print("Choisissez le type de boucle :")
print("1 - Boucle FOR")
print("2 - Boucle WHILE")

choix = input("Votre choix (1 ou 2) : ")

while choix not in ['1', '2']:
    choix = input("Choix invalide. Veuillez entrer 1 ou 2 : ")

# Calcul et affichage de la factorielle
fact = 1

if choix == '1':
    print("\n--- Factorielle avec boucle FOR ---")
    for i in range(1, n+1):
        fact *= i
        print(f"Après multiplication par {i}, factorielle = {fact}")
else:
    print("\n--- Factorielle avec boucle WHILE ---")
    i = 1
    while i <= n:
        fact *= i
        print(f"Après multiplication par {i}, factorielle = {fact}")
        i += 1

print(f"\nLa factorielle de {n} est : {fact}")