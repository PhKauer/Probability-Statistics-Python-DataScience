"""
Sets: The Inclusion-Exclusion Principle
Problem 1
Problem 1.1
 The inclusion-exclusion principle states that for two sets A and B,
|A∪B|=|A|+|B|−|A∩B|.

Write the following functions to determine |A∪B| in two different ways.

A function union that determines first A∪B and then evaluates the union's size. Output the ordered pair (A∪B,|A∪B|).

* Sample run *

A = {1, 2, 3}
B = {3, -6, 2, 0}
print union(A, B)
* Expected Output *

({-6, 0, 1, 2, 3}, 5)

[12]
0s
"""


# modify this cell
def union(A, B):
   
    # Comprimentos de A e B
    length_a = len(A)
    length_b = len(B)
    
    # 1. UNIÃO: elementos em A ou B (sem repetições)
    union_list = []
    
    # Adiciona todos os elementos de A
    for item_a in A:
        # Verifica se já não está na união
        encontrou = False
        for item_u in union_list:
            if item_a == item_u:  # Comparação fundamental
                encontrou = True
                break
        if not encontrou:
            union_list.append(item_a)
    
    # Adiciona elementos de B que não estão na união
    for item_b in B:
        encontrou = False
        for item_u in union_list:
            if item_b == item_u:  # Outra comparação
                encontrou = True
                break
        if not encontrou:
            union_list.append(item_b)
    
    union_list = set(union_list)
    length_union = len(union_list)
    
       
    return union_list, length_union

A = {1,4,-3, "bob"}
B = {2,1,-3,"jill"}
print(union(A,B))
assert union(A,B) == ({-3, 1, 2, 4, 'bob', 'jill'}, 6)

#
# AUTOGRADER TEST - DO NOT REMOVE
#

"""
Problem 1.2
A function inclusion_exclusion that first deterimines |A|, |B|, A∩B, and |A∩B|, and then uses the inclusion-exclusion formula to determine |A∪B|. Output the tuple (|A|,|B|,|A∩B|,|A∪B|).

 * **Sample run:** * ```python A = {1, 2, 3} B = {3, -6, 2, 0} print inclusion_exclusion(A, B) print "notice: 3 + 4 - 2 == 5" ```
* Expected Output: *

(3, 4, 2, 5)
notice: 3 + 4 - 2 == 5

[3]
0s
"""
# modify this cell

def inclusion_exclusion(A, B):

    # Converter para conjuntos para operações eficientes
    set_a = set(A)
    set_b = set(B)

    # Comprimentos de A e B
    length_a = len(A)
    length_b = len(B)

   
    # União: combina elementos únicos de ambos
    union_set = set_a | set_b
    length_union = len(union_set)

    # Interseção: elementos presentes em ambos
    intersection_set = set_a & set_b
    length_intersection = len(intersection_set)

    return length_a, length_b, length_intersection, length_union



# Check Function

A = {1, 2, 3, 4, 5}
B = {0, 2, -6, 5, 8, 9}
assert inclusion_exclusion(A, B) == (5, 6, 2, 9)

#
# AUTOGRADER TEST - DO NOT REMOVE
#

"""
Problem 2
The inclusion-exclusion principle says that for three sets A, B and C,

|A∪B∪C|=|A|+|B|+|C|−|A∩B|−|B∩C|−|C∩A|+|A∩B∩C|

We will write the following functions to determine |A∪B∪C| in two different ways.

Problem 2.1
Write function union3 that first determines A∪B∪C and then evaluates the size of this union. Output the tuple (A∪B∪C,|A∪B∪C|).

* Sample run: *

A = {1, 2, 3, 4, 5}
B = {0, 2, -6, 5, 8, 9}
C = {2, 10}
union3(A, B, C)
* Expected Output: *

({-6, 0, 1, 2, 3, 4, 5, 8, 9, 10}, 10)

[31]
0s
"""

# modify this cell

def union3(A, B, C):

  union_list = []

       # Adiciona todos os elementos de A
  for item_a in A:
        # Verifica se já não está na união
        encontrou = False
        for item_u in union_list:
            if item_a == item_u:  # Comparação fundamental
                encontrou = True
                break
        if not encontrou:
            union_list.append(item_a)
    
    # Adiciona elementos de B que não estão na união
  for item_b in B:
        encontrou = False
        for item_u in union_list:
            if item_b == item_u:  # Outra comparação
                encontrou = True
                break
        if not encontrou:
            union_list.append(item_b)

             # Adiciona elementos de C que não estão na união
  for item_c in C:
        encontrou = False
        for item_u in union_list:
            if item_c == item_u:  # Outra comparação
                encontrou = True
                break
        if not encontrou:
            union_list.append(item_c)
        
  union_list = set(union_list)
  

  return union_list, len(union_list)

# check Function
A = {1, 2, 4, 5, 10}
B = {5, 2, -6, 5, 8, 9}
C = {2, 10, 13}
assert union3(A,B,C) == ({-6, 1, 2, 4, 5, 8, 9, 10, 13}, 9)

#
# AUTOGRADER TEST - DO NOT REMOVE
#
"""
Problem 2.2
A function inclusion_exclusion3 that first deterimines the sizes of A, B, C and their mutual intersections, and then uses the inclusion-exclusion principle to determine the size of the union. Output the tuple (|A∩B∩C|,|A∪B∪C|). Note that for brevity we are asking you to output the intermediate answer just for A∩B∩C, but you need to calculate all.

* Sample run: *

A = {1, 2, 3, 4, 5}
B = {0, 2, -6, 5, 8, 9}
C = {2, 10}
print inclusion_exclusion3(A, B, C)
* Expected Output: *

(1, 10)

[33]
0s
"""

# modify this cell

def inclusion_exclusion3(A, B, C):

     # Comprimentos de A, B e C
    length_a = len(A)
    length_b = len(B)
    length_c = len(C)

    # Converter para conjuntos para operações eficientes

# Check Function

A = {1, 2, 4, 5, 10}
B = {5, 2, -6, 5, 8, 9, 10}
C = {2, 10, 13}
assert inclusion_exclusion3(A,B,C) == (2, 9)

#
# AUTOGRADER TEST - DO NOT REMOVE
#

Produtos pagos do Colab - Cancelar contratos
