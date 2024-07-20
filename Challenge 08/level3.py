
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#Vérifiez si le dictionnaire person a la clé `skills`, si oui, imprimez la compétence du milieu dans la liste `skills`.
# if 'skills' in person:
#     skills = person['skills']
#     middle_index = len(skills) // 2
#     middle_skill = skills[middle_index]
#     print("La compétence du milieu est : ", middle_skill)
# else:
#     print("La clé 'skills' n'existe pas dans le dictionnaire.")
    

#Vérifiez si le dictionnaire person a la clé `skills`, si oui, vérifiez si 
# la personne a la compétence 'Python' et imprimez le résultat.

# if 'skills' in person:
#     skills = person['skills']
#     if 'Python' in skills:
#         print("La personne a la compétence 'Python'.")
#     else:
#         print("La personne n'a pas la compétence 'Python'.")
# else:
#     print("La clé 'skills' n'existe pas dans le dictionnaire.")

#Si les compétences de la personne incluent uniquement JavaScript et React, imprimez 
# 'Il est un développeur front end', si les compétences de la personne incluent 
# `Node`, `Python`, `MongoDB`, imprimez 'Il est un développeur back end', si les compétences 
# de la personne incluent `React`, `Node` et `MongoDB`, imprimez 'Il est un développeur fullstack', 
# sinon imprimez 'titre inconnu' - pour des résultats plus précis, d'autres conditions peuvent être imbriquées !

# if 'skills' in person:
#     skills = person['skills']
#     if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
#         print("Il est un développeur front end")
#     elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
#         print("Il est un développeur back end")
#     elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
#         print("Il est un développeur fullstack")
#     else:
#         print("Titre inconnu")
# else:
#     print("La clé 'skills' n'existe pas dans le dictionnaire.")
    
# Si la personne est mariée et vit en Finlande, imprimez les informations dans le format suivant :
# Asabeneh Yetayeh lives in Finland. He is married.

if 'is_marred' and 'country' in person:
    is_married = person['is_marred']
    country = person['country']
    if is_married and 'Finland' in country:
        print(f"Asabeneh Yetayeh lives in Finland. He is married.")
    else:
        print("Asabeneh Yetayeh is not married and don't lives in Finland")
else:
    print("Asabeneh Yetayeh is not married and don't lives in Finland")