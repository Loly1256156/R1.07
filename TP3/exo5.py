def lire_heure(prompt):
    while True:
        try:
            h = int(input(prompt))
            if 0 <= h <= 24:
                return h
            else:
                print("Les heures doivent être comprises entre 0 et 24 !\n")
        except ValueError:
            print("⚠ Veuillez entrer un entier valide.\n")

# Lecture des heures
debut = lire_heure("Donnez l’heure de début de la location (un entier) : ")
fin = lire_heure("Donnez l’heure de fin de la location (un entier) : ")

# Vérification des erreurs
if debut == fin:
    print("Attention ! l’heure de fin est identique à l’heure de début.\n")
elif debut > fin:
    print("Attention ! le début de la location est après la fin ...\n")
else:
    # Calcul des heures selon les tarifs
    tarif1 = 1.0   # de 0h à 7h et de 17h à 24h
    tarif2 = 2.0   # de 7h à 17h

    heures_tarif1 = 0
    heures_tarif2 = 0

    # Boucle sur chaque heure de location
    for h in range(debut, fin):
        if 0 <= h < 7 or 17 <= h < 24:
            heures_tarif1 += 1
        else:
            heures_tarif2 += 1

    montant = heures_tarif1 * tarif1 + heures_tarif2 * tarif2

    # Affichage du résultat
    print("\nVous avez loué votre vélo pendant")
    if heures_tarif1 > 0:
        print(f"{heures_tarif1} heure(s) au tarif horaire de {tarif1} euro(s)")
    if heures_tarif2 > 0:
        print(f"{heures_tarif2} heure(s) au tarif horaire de {tarif2} euro(s)")

    print(f"Le montant total à payer est de {montant} euro(s).")