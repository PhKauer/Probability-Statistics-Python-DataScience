import itertools
from itertools import product

'''
Problem 1
De Morgan's first law states the following for any two sets A and B
(A∪B)c=Ac∩Bc

In the following two exercises we calculate (A∪B)c in two different ways. Both functions must take A, B and the universal set U as their inputs.

Exercise 1.1
Write the function complement_of_union that first determines A∪B and then evaluates the complement of this set. Output the tuple: (A∪B,(A∪B)c).

Code

A = {1, 2, 3}
B = {3, -6, 2, 0}
U = {-10, -9, -8, -7, -6, 0, 1, 2, 3, 4}
complement_of_union(A, B, U)
Output

({-6, 0, 1, 2, 3}, {-10, -9, -8, -7, 4})
'''

# modify this cell

def complement_of_union(a, b, universe):
    # inputs: a, b and universe are of type 'set'
    # output: a tuple of the type (set, set)

    set_a = set(a)
    set_b = set(b)
    universal_set = set(universe)

    union_ab = set_a.union(set_b)
    complement = universal_set - union_ab

    return (union_ab, complement)


# Check Function

A = {1, 2, 3, 4, 5}
B = {0, 2, -6, 5, 8, 9}
U = A|B|{-3, 7, 10, -4}
assert( complement_of_union(A, B, U) == ({-6, 0, 1, 2, 3, 4, 5, 8, 9}, {-4, -3, 7, 10})  )

#
# AUTOGRADER TEST - DO NOT REMOVE
#


'''
Exercsise 1.2
Write the function intersection_of_complements that first determines  Ac  and  Bc  and then evaluates the intersection of their complements. Output the tuple:  (Ac,Ac∩Bc) 

Code

A = {1, 2, 3}
B = {3, -6, 2, 0}
U = {-10, -9, -8, -7, -6, 0, 1, 2, 3, 4}
intersection_of_complements(A, B, U)
Output

({-10, -9, -8, -7, -6, 0, 4}, {-10, -9, -8, -7, 4})
'''
# modify this cell

def intersection_of_complements(a, b, universe):
    # inputs: A, B and U are of type 'set'
    # output: a tuple of the form (set, set)

    complement_a = set(universe) - set(a)
    complement_b = set(universe) - set(b)

    intersection = complement_a.intersection(complement_b)

    return (complement_a, intersection)

# Check Function

A = {1, 2, 3, 4, 5}
B = {0, 2, -6, 5, 8, 9}
U = A|B|{-3, 7, 10, -4}
assert(  intersection_of_complements(A, B, U) == ({-6, -4, -3, 0, 7, 8, 9, 10}, {-4, -3, 7, 10})  )

#
# AUTOGRADER TEST - DO NOT REMOVE
#


'''
Problem 2
This problem illustrates a property of cartesian products of unions of two or more sets. For four sets A, B, S and T, the following holds:

(A∪B)×(S∪T)=(A×S)∪(A×T)∪(B×S)∪(B×T)

Write the following functions to determine (A∪B)×(S∪T) in two different ways.

Exercies 2.1
Write function product_of_unions that first determines (A∪B) and (S∪T) and then evaluates the cartesian products of these unions. Output the tuple ((A∪B),(A∪B)×(S∪T)).

Code

A = {1, 2}
B = {1, 3}
S = {-1, 0}
T = {0, 10}
product_of_unions(A, B, S, T)
Output

({1, 2, 3},
 {(1, -1),
  (1, 0),
  (1, 10),
  (2, -1),
  (2, 0),
  (2, 10),
  (3, -1),
  (3, 0),
  (3, 10)})
  '''
# modify this cell

def product_of_unions(A, B, S, T):
    # inputs: A, B, S and T are sets
    # output: a tuple of the type (set, set)

   uniao_ab = set(A).union(set(B))
   uniao_st = set(S).union(set(T))

   cartesian_product=set()
   for x in uniao_ab:
       for y in uniao_st:
           cartesian_product.add((x,y))


   return (uniao_ab, cartesian_product)

# Check Function

A = {5}
B = {5, 6}
S = {-1, 0, 1}
T = {1, 2}
assert( product_of_unions(A, B, S, T) == \
       ({5, 6}, {(5, -1), (5, 0), (5, 1), (5, 2), (6, -1), (6, 0), (6, 1), (6, 2)})   )

#
# AUTOGRADER TEST - DO NOT REMOVE
#
'''
Exercise 2.2
Write a function union_of_products that first determines  (A×S)  and the other three cartesian products that appear on the right hand side of the identity above, then evaluates the union of these cartesian products. Output the tuple  ((A×S),(A×S)∪(A×T)∪(B×S)∪(B×T)) .

Code

A = {1, 2}
B = {1, 3}
S = {-1, 0}
T = {0, 10}
union_of_products(A, B, S, T)
Output

({(1, -1), (1, 0), (2, -1), (2, 0)},
 {(1, -1),
  (1, 0),
  (1, 10),
  (2, -1),
  (2, 0),
  (2, 10),
  (3, -1),
  (3, 0),
  (3, 10)})
'''
# modify this cell

def union_of_products(A, B, S, T):
    # inputs: A, B, S and T are sets
    # output: a tuple of the type (set, set)

    set_a = set(A)
    set_b = set(B)
    set_s = set(S)
    set_t = set(T)

    lista_ab = [set_a, set_b]
    lista_st = [set_s, set_t]

    uniao_products = set()
    product_as = set()

    for set_1 in lista_ab:
      for x in set_1:
        for set_2 in lista_st:
          for y in set_2:
            uniao_products.add((x,y))
            if set_1 == set_a and set_2 == set_s:
              product_as.add((x,y))


    return(product_as, uniao_products)


# Check Function

A = {5}
B = {5, 6}
S = {-1, 0, 1}
T = {1, 2}
assert( union_of_products(A, B, S, T) == \
        ({(5, -1), (5, 0), (5, 1)}, \
         {(5, -1), (5, 0), (5, 1), (5, 2), (6, -1), (6, 0), (6, 1), (6, 2)})  \
      )

#
# AUTOGRADER TEST - DO NOT REMOVE
#
