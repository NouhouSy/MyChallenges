import math
#1. Déclarez une fonction _add_two_numbers_. Elle prend deux paramètres et renvoie une somme.
def add_two_numbers(num1, num2):
    return num1 + num2
somme = add_two_numbers(5, 3)
print("1- La somme est : ", somme)

#2. L'aire d'un cercle se calcule comme suit : area = π x r x r. 
# Écrivez une fonction qui calcule _area_of_circle_.
def area_of_circle(r):
    return math.pi * r * r
rayon = 3
aire = area_of_circle(rayon)
print(f"2- L'aire d'un cercle de rayon {rayon} est: {aire}")

#3. Écrivez une fonction appelée add_all_nums qui prend un nombre arbitraire d'arguments et les additionne. 
# Vérifiez si tous les éléments de la liste sont de type nombre. Sinon, donnez un retour d'information raisonnable.
def add_all_nums(*args):
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return "3- Tous les arguments doivent être des nombres."
        total += arg
    return total
#print(f"La somme des argument arguments est : {add_all_nums(1, 2, 3, 4.5)}")
print(add_all_nums(1, 'a', 3))  

#4. La température en °C peut être convertie en °F en utilisant cette formule : °F = (°C x 9/5) + 32. 
# Écrivez une fonction qui convertit °C en °F, _convert_celsius_to_fahrenheit_.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(f"4- La conversion de dégré celsius(°C) en fahrenheit(°F) est : {convert_celsius_to_fahrenheit(25)}°F")

#5. Écrivez une fonction appelée check-season, elle prend un paramètre de mois et renvoie la saison : 
# Automne, Hiver, Printemps ou Été.
def check_season(month):
    month = month.lower()
    if month in ['décembre', 'janvier', 'février']:
        return "Hiver"
    elif month in ['mars', 'avril', 'mai']:
        return "Printemps"
    elif month in ['juin', 'juillet', 'août']:
        return "Été"
    elif month in ['septembre', 'octobre', 'novembre']:
        return "Automne"
    else:
        return "Mois invalide"
print(f"5- La saison pour ce mois est : {check_season("Octobre")}")

#6. Écrivez une fonction appelée calculate_slope qui renvoie la pente d'une équation linéaire.
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "La pente est infinie (ligne verticale)"
    slope = (y2 - y1) / (x2 - x1)
    return slope
print(f"6- Le résultat de cette équation linéaire est : {calculate_slope(2, 3, 5, 7)}")

#7. Une équation quadratique se calcule comme suit : ax² + bx + c = 0. 
# Écrivez une fonction qui calcule l'ensemble des solutions d'une équation quadratique, _solve_quadratic_eqn_.
import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        s1 = (-b + math.sqrt(discriminant)) / (2*a)
        s2 = (-b - math.sqrt(discriminant)) / (2*a)
        return s1, s2
    elif discriminant == 0:
        s = -b / (2*a)
        return s,
    else:
        return "Pas de solution réelle"
print(f"7- Le résultat de léquation (ax² + bx + c) est : {solve_quadratic_eqn(1, -5, 3)}")

#8. Déclarez une fonction nommée print_list. 
# Elle prend une liste comme paramètre et affiche chaque élément de la liste.
def print_list(liste):
    for item in liste:
        print(item)
print_list(("8- L'ensemble des élément de la listes est :", '\tmangue', '\tbanane', '\torange', '\tavocat')) 

#9. Déclarez une fonction nommée reverse_list. 
# Elle prend un tableau comme paramètre et renvoie le tableau inversé (utilisez des boucles).
def reverse_list(lst):
    liste_renverse = []
    for i in range(len(lst)-1, -1, -1):
        liste_renverse.append(lst[i])
    return liste_renverse
liste_original = [1, 2, 3, 4, 5]
liste_renverse = reverse_list(liste_original)
print(f"9- La liste renversé est : {liste_renverse}")
print("9- La liste renversé est : ", reverse_list(["A", "B", "C"]))

#10. Déclarez une fonction nommée  `capitalize_list_items`. 
# Elle prend une liste comme paramètre et renvoie une liste d'éléments en majuscules.
def capitalize_list_items(liste):
    return [item.upper() for item in liste]
items = ['orange', 'banane', 'pomme']
capitalized_items = capitalize_list_items(items)
print("10- La liste en majuscule est : ", capitalized_items)

#11. Déclarez une fonction nommée `add_item`. Elle prend une liste et un paramètre d'élément. 
# Elle renvoie une liste avec l'élément ajouté à la fin.
def add_item(liste, item):
    liste.append(item)
    return liste

items = ['orange', 'banane', 'pomme']
new_item = 'avocat'
liste_mis_a_jour = add_item(items, new_item)
print("11- La nouvelle liste mis à jour est : ", liste_mis_a_jour)

#12. Déclarez une fonction nommée `remove_item`. 
# Elle prend une liste et un paramètre d'élément. 
# Elle renvoie une liste avec l'élément supprimé.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
items = ['orange', 'banane', 'pomme']
supprime_element = 'banane'
liste_mis_a_jour = remove_item(items, supprime_element)
print("12- La nouvelle liste mis à jour est : ",liste_mis_a_jour)

#13. Déclarez une fonction nommée sum_of_numbers. 
# Elle prend un paramètre de nombre et additionne tous les nombres dans cette plage.
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
resultat = sum_of_numbers(5)
print("13- Le résultat de cette somme de nombres est : ", resultat)

#14. Déclarez une fonction nommée sum_of_odds. 
# Elle prend un paramètre de nombre et additionne tous les nombres impairs dans cette plage.
def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total
resultat = sum_of_odds(30)
print("14- Le résultat de cette somme de nombres impairs est : ", resultat)

#15. Déclarez une fonction nommée sum_of_even. 
# Elle prend un paramètre de nombre et additionne tous les nombres pairs dans cette plage.
def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total
resultat = sum_of_odds(10)
print("15- Le résultat de cette somme de nombres pairs est : ", resultat)