import os.path
import datetime


f1 = input("Entrez le nom du premier fichier : ")
f2 = input("Entrez le nom du second fichier : ")


def infos_fichier(nom_fichier):
    if os.path.isfile(nom_fichier):
        taille = os.path.getsize(nom_fichier)
        mtime = os.path.getmtime(nom_fichier)
        date_modif = datetime.datetime.fromtimestamp(mtime)

        print(f"\nFichier : {nom_fichier}")
        print(f"  - Taille : {taille} octets")
        print(f"  - Dernière modification : {date_modif}")

        return mtime
    else:
        print(f"\n⚠ Le fichier '{nom_fichier}' n'existe pas.")
        return None


mtime1 = infos_fichier(f1)
mtime2 = infos_fichier(f2)


if mtime1 is not None and mtime2 is not None:
    print("\n--- Comparaison des fichiers ---")
    if mtime1 > mtime2:
        print(f"Le fichier le plus récent est : {f1}")
    elif mtime2 > mtime1:
        print(f"Le fichier le plus récent est : {f2}")
    else:
        print("Les deux fichiers ont la même date de modification.")
        #