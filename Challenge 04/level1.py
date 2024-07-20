#1.Déclarez une liste vide.
liste_vide = list()
print(f"1- Ma liste vide est : {liste_vide}")

#2.Déclarez une liste avec plus de 5 éléments.
ma_liste = list((1, "Nouhou", 5.3, 9, "Ahmed", 6.5))
print(f"2- Ma liste avec plus de 5 éléments est : {ma_liste}")

#3.Trouvez la longueur de votre liste.
longueur_liste = len(ma_liste)
print(f"3- La longueur de ma liste est : {longueur_liste}")

#4.Obtenez le premier élément, l'élément du milieu et le dernier élément de la liste.
ma_liste = list((1, "Nouhou", 5.3, 9, "Ahmed", 6.5))
premier_element = ma_liste[0]
element_du_milieu = len(ma_liste) // 2
dernier_element = ma_liste[-1]
print(f"4- Le prémier élément de la liste est : {premier_element}")
print(f"4- L'élément du milieu de la liste est : {element_du_milieu}")
print(f"4- Le dernier élément de la liste est : {dernier_element}")

#5.Déclarez une liste appelée mixed_data_types, mettez-y votre(name, age, height, marital status, address)
mixed_data_types = list(("Sy", 24, 1.67, "célibataire", "Hafia/Conakry"))
print(f"5- Ma liste 'mixed_data_types' est : {mixed_data_types}")

#6.Déclarez une variable de liste nommée it_companies et assignez-lui les valeurs initiales : 
# Facebook, Google, Microsoft, Apple, IBM, Oracle et Amazon.
it_companies = list(("Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"))

#7.Imprimez la liste en utilisant print()
print(f"6- Ma liste 'it_companies' est : {it_companies}")

#8.Imprimez le nombre d'entreprises dans la liste.
nombre_entreprise = len(it_companies)
print(f"8- Le nombre d'entreprises dans la liste est : {nombre_entreprise}")

#9.Imprimez la première, la moyenne et la dernière entreprise.
premiere = it_companies[0]
moyenne = len(it_companies) // 2
dernier = it_companies[-1]
print(f"9- La première entreprise est : {premiere}")
print(f"9- La moyenne de l'entreprise est : {moyenne}")
print(f"9- La dernière entreprise est : {dernier}")

#10.Imprimez la liste après avoir modifié l'une des entreprises.
it_companies[4] = "Tiktok"
print(f"10- Ma nouvelle liste d'entreprises après modification est : {it_companies}")

#11.Ajoutez une entreprise IT à it_companies.
it_companies.append("MySQL")
print(f"11- La nouvelle liste d'entreprise après ajout est : {it_companies}")

#12.Insérez une entreprise IT au milieu de la liste des entreprises.
it_companies.insert(4, "Tesla")
print(f"12- La nouvelle liste d'entreprise après insertion est : {it_companies}")

#13.Changez l'un des noms des it_companies en majuscules (IBM excluded!)
it_companies[4] = it_companies[4].upper()
print(f"13- La nouvelle liste avec le 4ème élément en majuscule est : {it_companies}")

#14.Joignez les it_companies avec une chaîne de caractères '#;  '
join_it_companies = ' #; '.join(it_companies)
print(f"14- La nouvelle d'entreprise avec '#; ' est : {join_it_companies}")

#15.Vérifiez si une certaine entreprise existe dans la liste it_companies.
if "Facebook" in it_companies:
    print(f"15- 'Facebook' existe dans la liste : {it_companies}")
else:
    print(f"15- Cette entreprise n'existe pas dans la liste : {it_companies}")
    
#16.Triez la liste en utilisant la méthode sort().
it_companies.sort()
print(f"16- La nouvelle liste trier avec la méthode 'short()' est : {it_companies}")

#17.Inversez la liste dans l'ordre décroissant en utilisant la méthode reverse().
it_companies.sort(reverse=True)
print(f"17- La nouvelle liste trier avec la méthode 'reverse()' est : {it_companies}")

#18.Coupez les 3 premières entreprises de la liste.
nom_couper = it_companies[:3]
print(f"18- La nouvelle liste d'entreprise avec les 3 premières coupé est : {nom_couper}")

#19.Coupez les 3 dernières entreprises de la liste.
noms_coupe = it_companies[-3:]
print(f"19- La nouvelle liste d'entreprise avec les 3 dernières coupé est : {noms_coupe}")

#20.Coupez l'entreprise ou les entreprises IT du milieu de la liste.
milieu = len(it_companies) // 2
premier_milieu = it_companies[:milieu]
deuxieme_milieu = it_companies[milieu:]
print(f"20- La première moitié de la liste est : {premier_milieu}")
print(f"20- La deuxième moitié de la liste est : {deuxieme_milieu}")

#21.Supprimez la première entreprise IT de la liste.
it_companies.pop(0)
print(f"21- La nouvelle chaine après avoir supprimer la première entreprise est : {it_companies}")

#22. Supprimez l'entreprise ou les entreprises IT du milieu de la liste.
milieu_entreprise = len(it_companies) // 2
it_companies.pop(milieu_entreprise)
print(f"22- La nouvelle chaîne après suppression de l'entreprise du milieu est : {it_companies}")

#23. Supprimez la dernière entreprise IT de la liste.
it_companies.pop(-1)
print(f"23- La nouvelle chaine après avoir supprimer la dernière entreprise est : {it_companies}")

#24. Supprimez toutes les entreprises IT de la liste.
it_companies.clear()
print(f"La nouvelle chaîne après avoir supprimer toutes les entreprises est : {it_companies}")

#25. Détruisez la liste des entreprises IT.
del it_companies
try:
    print(f"25- Après suppression : {it_companies} ")
except NameError:
    print("25- La liste a été détruite et n'existe plus !!")
    
#26. Joignez les listes suivantes :
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    front_end.extend(back_end)
print(f"26- La nouvelle liste est : {front_end}")

#27. Après avoir joint les listes dans la question 26. Copiez la liste jointe et assignez-la à une variable full_stack. 
# Ensuite, insérez `Python` et `SQL` après `Redux`.
full_stack = front_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(f"27- La nouvelle chaine 'full_stack' est : {full_stack}")