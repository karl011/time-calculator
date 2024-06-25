from fonctions import *

# Saisie des deux durées
print("Saisie de la première durée :")
duree1 = saisir_duree()
print("\nSaisie de la deuxième durée :")
duree2 = saisir_duree()

# Choix de l'opération
operation = input("\nChoisissez l'opération (+ ou -) : ")
while operation not in ["+", "-"]:
    operation = input("Opération invalide. Choisissez l'opération (+ ou -) : ")

# Calcul et affichage du résultat
resultat = calcul_duree(duree1, duree2, operation)
if resultat is not None:
    print("\nRésultat :")
    afficher_duree(resultat)