#1. Obtenez l'entrée utilisateur en utilisant input("Enter your age: "). Si l'utilisateur a 18 ans ou plus, donnez un retour :
# `You are old enough to learn to drive.`. Si l'utilisateur a moins de 18 ans, 
# donnez un retour pour indiquer le nombre d'années 

# age = int(input("Entrez vôtre âge : "))
# if age >= 18:
#     print("1- You are old enough to learn to drive")
# else:
#     n = 18 - age
#     print(f"1- You need {n} more years to learn to drive")
    
#2. Comparez les valeurs de my_age et your_age en utilisant if ... else. 
# Qui est le plus âgé (moi ou vous) ? Utilisez input("Enter your age: ") pour obtenir l'âge en entrée. 
# Vous pouvez utiliser une condition imbriquée pour imprimer 'year' pour une différence d'un an, 
# 'years' pour des différences plus importantes, et un texte personnalisé si my_age = your_age.

# ton_age = int(input("Entrez votre age : "))
# mon_age = 24
# if ton_age == mon_age:
#     print(f"2- On a le même âge !!")
# elif ton_age > mon_age:
#     print(f"2- Tu as {ton_age - mon_age} de plus que moi")
# else:
#     print(f"2- J'ai {mon_age - ton_age} de plus que toi")
    
#3. Obtenez deux nombres de l'utilisateur en utilisant une invite d'entrée. 
# Si a est plus grand que b, renvoyez a is greater than b, si a est plus petit que b,
# renvoyez a is smaller than b, sinon renvoyez a is equal to b.

a = int(input("Entrez la valeur de a : "))
b = int(input("Entrez la valeur de b : "))
if a > b:
    print(f"3- {a} is greater than {b}")
elif a < b:
    print(f"3- {a} is smaller than {b}")
else:
    print(f"3- {a} is equal to {b}")