#Challenge 1

# Demander les valeurs à l'utilisateur
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))

# Générer la liste des multiples
multiples = [number * i for i in range(1, length + 1)]

# Afficher le résultat
print(multiples)




#Challenge 2

# Demande à l'utilisateur d'entrer un mot
mot = input("Entrez un mot : ")

# Variable qui va contenir le nouveau mot sans doublons consécutifs
resultat = ""

# Parcours de chaque lettre du mot
for lettre in mot:
    
    # Vérifie si le résultat est vide
    # ou si la lettre actuelle est différente de la dernière lettre ajoutée
    if resultat == "" or lettre != resultat[-1]:
        resultat += lettre  # Ajoute la lettre au résultat

# Affiche le mot transformé
print("Nouveau mot :", resultat)
        
