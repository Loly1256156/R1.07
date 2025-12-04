import random

# Tirage aléatoire du nombre mystère entre 0 et 100
nombre_mystere = random.randint(0, 100)

# Initialisation du compteur
tentatives = 0

print("Bienvenue dans le jeu du nombre mystère !")
print("Essayez de deviner le nombre entre 0 et 100.")

# Boucle de jeu
while True:
    # Lecture de la proposition de l'utilisateur
    try:
        proposition = int(input("Votre proposition : "))
    except ValueError:
        print("⚠ Veuillez entrer un nombre entier !")
        continue

    tentatives += 1  # Incrémentation du compteur

    # Comparaison
    if proposition < nombre_mystere:
        print("C'est plus grand !")
    elif proposition > nombre_mystere:
        print("C'est plus petit !")
    else:
        print(f"Bravo ! Vous avez trouvé le nombre mystère {nombre_mystere} en {tentatives} coups.")
        break