inferieur_10 = 0
entre_10_15 = 0
superieur_15 = 0

for i in range(10):
    # Lecture avec contrôle
    while True:
        val = float(input(f"Entrez la valeur réelle n°{i+1} (entre 0 et 20) : "))
        if 0 <= val <= 20:
            break
        print("⚠ Valeur incorrecte ! Elle doit être comprise entre 0 et 20.")

    # Comptage dans les intervalles
    if val < 10:
        inferieur_10 += 1
    elif val < 15:          # donc >= 10 automatiquement
        entre_10_15 += 1
    else:                   # donc >= 15
        superieur_15 += 1