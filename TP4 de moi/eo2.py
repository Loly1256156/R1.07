nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
somme= 0.0
moyenne = 0.0

notes = []
for i in range(nombreEtudiants):
    note=int(input("Donnez la note de l'étudiant"))
    notes.append(note)
    somme += note
moyenne += somme/nombreEtudiants
for i in range(nombreEtudiants ) :
    print(f"Note etudiant {i} : {notes[i]}")


print(f"Moyenne de classe : {moyenne}")


for i in range(nombreEtudiants):
    print(f"Numéro de l’Etudiant | note | ecart a la moyenne")



