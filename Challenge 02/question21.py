#21. Écrivez un script qui demande à l'utilisateur d'entrer les heures et le taux par heure. Calculez le salaire de la personne.
heures = int(input("Entrez le nombre d'heures de travail : "))
taux_horaire = int(input("Entrez le taux d'horaire de travail : "))
salaire = heures * taux_horaire
print(f"Le salaire de cette personne est : {salaire}")