from itertools import permutations 


n = 10

perm = permutations(list(range(n)), n//2)

for index in perm:
    print(index)