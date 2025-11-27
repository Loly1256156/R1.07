nMAx = 3
v1 = []
v2 = []

n = int(input("Entrez la taille effective des vecteurs : "))

while n < 1 or n > nMAx:
    print("Ce n'est pas la bonne valeur.")
    n = int(input("Réentrez la taille effective des vecteurs : "))

print("\nSaisie du premier vecteur :")
for i in range(n):
    v1.append(float(input(f"v1[{i}] = ")))

print("\nSaisie du second vecteur :")
for i in range(n):
    v2.append(float(input(f"v2[{i}] = ")))

produit = 0
for i in range(n):
    produit += v1[i] * v2[i]

print(f"Le produit scalaire de v1 par v2 vaut {produit}")