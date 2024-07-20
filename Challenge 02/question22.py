#22. Écrivez un script qui demande à l'utilisateur d'entrer un nombre d'années. 
#Calculez le nombre de secondes qu'une personne peut vivre. Supposons qu'une personne puisse vivre cent ans.
nb_seconde_par_an = 365 * 24 * 60 * 60
nb_annees = int(input("Entrez le nombre d'années de vie de la personne : "))
nb_secondes = nb_annees * nb_seconde_par_an
print(f"Le nombre de seconde de vie de cette personne est : {nb_seconde_par_an} secondes")