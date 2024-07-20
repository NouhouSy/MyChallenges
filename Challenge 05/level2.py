#1. Déballez siblings et parents à partir de family_members.
siblings = ("Mariam", "Kadjatou","Malick", "Masaliou")
parents = ("Amadou", "Fatoumata")
sisters, brothers, father, mother = siblings[:2], siblings[2:], parents[0], parents[1]
print("1- Sœurs:", sisters)
print("1- Frères:", brothers)
print("1- Père:", father)
print("1- Mère:", mother)

#2. Créez des tuples fruits, vegetables et animal products. Joignez les trois tuples et assignez-les à une 
# variable appelée food_stuff_tp.
fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "broccoli", "lettuce")
animal_products = ("milk", "egg", "cheese")
food_stuff_tp = fruits + vegetables + animal_products
print("2- Food Stuff Tuple est : ", food_stuff_tp)

#3. Changez le tuple food_stuff_tp en une liste food_stuff_lt.
food_stuff_lt = list(food_stuff_tp)
print("3- La liste Food Stuff List est : ", food_stuff_lt)

#4. Coupez l'élément ou les éléments du milieu du tuple food_stuff_tp ou de la liste food_stuff_lt.
n = len(food_stuff_lt)
middle_elements = food_stuff_lt[n//2] if n % 2 != 0 else food_stuff_lt[n//2-1:n//2+1]
print("4- Lélément du milieu est : ", middle_elements)

#5. Coupez les trois premiers éléments et les trois derniers éléments de la liste food_stuff_lt.
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print("5- Les trois premiers éléments sont : ", first_three)
print("5- Les trois derniers éléments sont : ", last_three)

#6. Supprimez complètement le tuple food_stuff_tp.
del food_stuff_tp

#7. Vérifiez si un élément existe dans le tuple :
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Vérifiez si 'Estonia' est un pays nordique
is_estonia_nordic = 'Estonia' in nordic_countries
print("7- Estonia est un pays nordique:", is_estonia_nordic)
# Vérifiez si 'Iceland' est un pays nordique
is_iceland_nordic = 'Iceland' in nordic_countries
print("7- Iceland est un pays nordique:", is_iceland_nordic)