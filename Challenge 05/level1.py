#1. Créez Tuple vide
tuple_vide = ()
print("1- Tuple vide est : ", tuple_vide)

#2. Créez un tuple contenant les noms de vos sœurs et de vos frères (des frères et sœurs imaginaires sont acceptables).
sisters = ("Mariam", "Kadjatou")
brothers = ("Malick", "Masaliou")
print("2- Mes sœurs:", sisters)
print("2- Mes frères:", brothers)

#3. Joignez les tuples des frères et sœurs et assignez-le à siblings.
siblings = sisters + brothers
print("3- Mes frères et sœurs sont : ", siblings)

#4. Combien de frères et sœurs avez-vous ?
num_siblings = len(siblings)
print("4- Le nombre de frères et sœurs est : ", num_siblings)

#5. Modifiez le tuple siblings et ajoutez le nom de votre père et de votre mère et assignez-le à family_members.
parents = ("Père", "Mère")
family_members = siblings + parents
print("5- Les membres de la famille sont : ", family_members)