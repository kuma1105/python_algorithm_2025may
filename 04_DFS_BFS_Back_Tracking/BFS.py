from collections import deque

# 인접행렬
adj = [[0] * 13 for _ in range(13)]

# 간선
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1

# for row in adj:
#     print(row)
    
# 재귀로 구현한 DFS
def bfs():
    dq = deque()
    dq.append(0)
    while dq:
        now = dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)

bfs()

