from itertools import permutations
v = [0,1,2,3]

for i in permutations(v, 4): # 배열, 뽑을 개수
    print(i)

print()

for i in permutations(v, 3): # 배열, 뽑을 개수
    print(type(i), i)