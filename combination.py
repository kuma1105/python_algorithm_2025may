from itertools import combinations

v = [0,1,2,3]

for i in combinations(v, 2):
    print(i)

print()

for i in combinations(v, 3):
    print(i)
    
print()

for i in combinations(v, 4):
    print(i)
