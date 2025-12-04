
heures = float(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire : "))

salaire = 0


if heures <= 160:
    salaire = heures * salaire_horaire

else:
    salaire = 160 * salaire_horaire


    if heures <= 200:
        heures_25 = heures - 160
        salaire += heures_25 * salaire_horaire * 1.25

    else:
        heures_25 = 40
        salaire += heures_25 * salaire_horaire * 1.25


        heures_50 = heures - 200
        salaire += heures_50 * salaire_horaire * 1.50


print(f"Salaire total : {salaire:.2f} euros")