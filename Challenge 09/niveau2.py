import statistics
#1.  Déclarez une fonction nommée evens_and_odds. 
# Elle prend un entier positif comme paramètre et compte le nombre de nombres pairs et impairs.
def evens_and_odds(n):
    count_even = 0
    count_odd = 0 
    for i in range(n + 1):
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1 
    return count_even, count_odd
n = 100
evens, odds = evens_and_odds(n)
print(f"1- Le nombre de nombres pairs est : {evens}")
print(f"1- Le nombre de nombres impairs est : {odds}")

#2. Appelez votre fonction factorial, elle prend un nombre entier 
# comme paramètre et renvoie la factorielle du nombre.

#Méthode A
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("2- Le résultat de la factorielle est : ", factorial(10))

#Méthode B
def evens_and_odds(entier):
    evens = len(list(filter(lambda n: n % 2 == 0, range(entier + 1))))
    odds = len(list(filter(lambda n: n % 2 != 0, range(entier + 1))))
    print(f"The number of odds are : {odds}")
    print(f"The number of evens are : {evens}")    

evens_and_odds(100)

#3.  Appelez votre fonction _is_empty_, elle prend un paramètre et vérifie s'il est vide ou non.
def is_empty(obj):
    if obj:
        return False
    else:
        return True

v = tuple()
print("3- Vérification si la variable est vide : ", is_empty(v))

#4. Écrivez différentes fonctions qui prennent des listes. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, 
# calculate_variance, calculate_std (standard deviation).
def calculate_mean(liste):
    return sum(liste) / len(liste)

def calculate_median(liste):
    liste.sort()
    taille = len(liste)
    if taille % 2 == 0:
        return liste[taille / 2]
    else:
        elm1 = liste[int((taille - 1) / 2)]
        elm2 = liste[int((taille + 1) / 2)]
        return (elm1 + elm2) / 2
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("La médianne est : ", calculate_median(liste))
print("La statistique est : ", statistics.median(liste))

