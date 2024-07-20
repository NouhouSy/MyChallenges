A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


#1. Joignez A et B.
union_de_A_et_B = A | B
print("1- L'union de A et B est : ", union_de_A_et_B)

#2. Trouvez l'intersection de A et B.
intersection_A_B = A & B
print("2- L'intersection de A et B est : ", intersection_A_B)

#3. A est-il un sous-ensemble de B ?
is_A_subset_B = A.issubset(B)
print("3- A est un sous-ensemble de B : ", is_A_subset_B)

#4. A et B sont-ils des ensembles disjoints ?
are_A_et_B_disjoint = A.isdisjoint(B)
print("4- A et B sont des ensembles disjoints : ", are_A_et_B_disjoint)

#5. Joignez A avec B et B avec A.
join_A_with_B = A | B
join_B_with_A = B | A
print("5- Joindre A avec B : ", join_A_with_B)
print("5- Joindre B avec A : ", join_B_with_A)

#6. Quelle est la différence symétrique entre A et B ?
diff_symmetric_A_B = A.symmetric_difference(B)
print("6- La différence symétrique entre A et B est : ", diff_symmetric_A_B)

#7. Supprimez complètement les ensembles.
del A
del B
try:
    print(A)
except NameError:
    print("6- L'ensemble A a été supprimé.")

try:
    print(B)
except NameError:
    print("6- L'ensemble B a été supprimé.")