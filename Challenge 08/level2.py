#1. Écrivez un code qui attribue une note aux étudiants en fonction de leurs scores :
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

# note = int(input("Entrez votre note : "))
# if note >= 80 and note <= 100:
#     print(f"1- Votre score est : A")
# elif note >= 70 and note <= 89:
#     print(f"1- Votre score est : B")
# elif note >= 60 and note <= 69:
#     print(f"1- Votre score est : C")
# elif note >= 50 and note <= 59:
#     print(f"1- Votre score est : D")
# elif note >= 0 and note <= 49:
#     print(f"1- Votre score est : F")
# else:
#     print(f"1- Vous n'avez pas de score")

#2. Vérifiez si la saison est Automne, Hiver, Printemps ou Été. Si l'utilisateur saisit :
# Septembre, Octobre ou Novembre, la saison est Automne.
# Décembre, Janvier ou Février, la saison est Hiver.
# Mars, Avril ou Mai, la saison est Printemps.
# Juin, Juillet ou Août, la saison est Été.

# mois = input("Veuillez saisir le mois svp : ")
# if mois == 'Septembre' or  mois == 'Octobre' or mois == 'Novembre':
#     print("La saison est Automne")
# elif mois == 'Décembre' or mois == 'Janvier' or mois == 'Févrie':
#     print("La saison est Hiver")
# elif mois == 'Mars' or mois == 'Avri' or mois == 'Mai':
#     print("La saison est Printemps")
# else:
#     print("La saison est Ete")

#3.  La liste suivante contient quelques fruits :
#Si un fruit n'existe pas dans la liste, ajoutez-le à la liste et imprimez la liste modifiée. 
# Si le fruit existe, imprimez 'Ce fruit existe déjà dans la liste.')

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Entrez le nom d'un fruit: ").lower()
if new_fruit in fruits:
    print("Ce fruit existe déjà dans la liste.")
else:
    fruits.append(new_fruit)
    print("Le fruit a été ajouté à la liste.")
    print("Liste modifiée des fruits:", fruits)