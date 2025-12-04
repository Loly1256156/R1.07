
S1 = input("Veuillez entrer la note du module 1 et le coefficient correspondant : ")


S2 = S1.split(" ")
note = float(S2[0])
coef = float(S2[1])


moyenne = note * coef / coef


if moyenne > 8:
    print("L'étudiant est admis")
else:
    print("L'étudiant n'est pas admis")