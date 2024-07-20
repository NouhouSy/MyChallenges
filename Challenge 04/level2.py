#1. Voici une liste des âges de 10 étudiants :
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Triez la liste et trouvez l'âge minimum et maximum.
ages.sort()
ages_min = ages[0]
ages_max = ages[-1]
print(f"- La liste triée est : {ages}")
print(f"- L'âge minimale est : {ages_min}")
print(f"- L'âge maximale est : {ages_max}")

#- Ajoutez de nouveau l'âge minimum et l'âge maximum à la liste.
ages.append(ages_min)
ages.append(ages_max)
print(f"- La liste après ajout de l'âge minimum et maximum est : {ages}")

#- Trouvez l'âge médian (un élément du milieu ou deux éléments du milieu divisés par deux).
ages.sort()
n = len(ages)
if n % 2 == 0:
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median = ages[n // 2]
print(f"- L'âge médian est : {median}")

#- Trouvez l'âge moyen (somme de tous les éléments divisée par leur nombre).
age_moyen = sum(ages) / n
print(f"- L'âge moyen est : {age_moyen}")

#- Trouvez l'écart des âges (max moins min).
ecart_age = ages_max - ages_min
print(f"- L'écart des âges est : {ecart_age}")

#- Comparez la valeur de (min - moyenne) et (max - moyenne), utilisez la méthode _abs()_.
comparaison_min_moyenne = abs(ages_min - age_moyen)
comparaison_max_moyenne = abs(ages_max - age_moyen)
print(f"- La différence absolue entre âge minimum et moyenne est : {comparaison_min_moyenne}")
print(f"- La différence absolue entre âge maximum et moyenne est : {comparaison_max_moyenne}")