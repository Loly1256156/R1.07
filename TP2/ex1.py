a = int(input("Entrer x:"))
b = int(input("Entrer y:"))
print(f"Avant permutation: \n x = {a} \n y = {b}")
c = a
a = b
b = c
print(f"Après permutation: \n x = {a} \n y = {b}")