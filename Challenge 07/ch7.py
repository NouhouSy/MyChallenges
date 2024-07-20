#1. Créez un dictionnaire vide appelé `dog`.
dog = {}
print("1- Le dictionnaire vide 'dog' est : ", dog )

#2. Ajoutez `name`, `color`, `breed`, `legs`, `age` au dictionnaire `dog`.
dog['name'] = 'Rex'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
print("2- Le nouveau dictionnaire non vide 'dog' est : ",dog)

#3. Créez un dictionnaire `student` et ajoutez `first_name`, `last_name`, `gender`, `age`, `marital_status`, 
# `skills`, `country`, `city` et `address` comme clés du dictionnaire.
student = {
    'first_name': 'Nouhou',
    'last_name': 'Sy',
    'gender': 'Male',
    'age': 24,
    'marital_status': 'célibataire',
    'skills': ['Python', 'JavaScript'],
    'country': 'Guinée',
    'city': 'Conakry',
    'address': 'Hafia'
}
print("Le dictionnaire 'student' est : ", student)

#4. Obtenez la longueur du dictionnaire `student`.
longueur_student = len(student)
print("La longueur du dictionnaire student est : ", longueur_student)

#5. Obtenez la valeur de `skills` et vérifiez le type de données, cela devrait être une liste.
skills = student['skills']
print("5- Valeur de skills est : ", skills)
print("5- Type de données de skills est : ", type(skills))

#6. Modifiez les valeurs de skills en ajoutant une ou deux compétences.
student['skills'].append('Django')
student['skills'].append('React')
print("6- Les compétences mises à jour sont : ", student['skills'])

#7. Obtenez les clés du dictionnaire sous forme de liste.
keys_list = list(student.keys())
print("7- Les clés du dictionnaire student sont : ", keys_list)

#8. Obtenez les valeurs du dictionnaire sous forme de liste.
values_list = list(student.values())
print("8- Les valeurs du dictionnaire student sont  : ", values_list)

#9. Changez le dictionnaire en une liste de tuples en utilisant la méthode _items()_.
items_list = list(student.items())
print("9- Dictionnaire converti en liste de tuples:", items_list)

#10. Supprimez un des éléments du dictionnaire.
student.pop('address')
print("10- Dictionnaire après suppression de 'address':", student)

#11. Supprimez un des dictionnaires.
del dog
print("11- Le dictionnaire 'dog' a été supprimé.")