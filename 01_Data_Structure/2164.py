from collections import deque
q = deque()
for n in range(int(input())):
    q.append(n+1)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
    
print(q.pop())