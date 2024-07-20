#1. Écrivez une fonction appelée is_prime, qui vérifie si un nombre est premier.
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_num = int(num ** 0.5) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True
print("1- Ce nombre est-il premier : ", is_prime(8))

#2. Écrivez des fonctions qui vérifient si tous les éléments sont uniques dans la liste.
def all_unique(liste):
    return len(liste) == len(set(liste))
print("2- Vérification si tous les éléments sont uniques : ", all_unique([1, 2, 3, 4, 5]))

#3. Écrivez une fonction qui vérifie si tous les éléments de la liste sont du même type de données.
def all_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)
print("3- Vérification si tous les éléments sont de même type : ",all_same_type([1, 2, 3]))

#5. Allez dans le dossier data et accédez au fichier countries-data.py.
"""..................
"""

#6. Créez une fonction appelée les langues les plus parlées dans le monde. 
# Elle doit renvoyer les 10 ou 20 langues les plus parlées dans le monde par ordre décroissant.
