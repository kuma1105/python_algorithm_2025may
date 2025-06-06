# 인접행렬
adj = [[0] * 13 for _ in range(13)]

# 간선
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1

# for row in adj:
#     print(row)
    
# 재귀로 구현한 DFS
def dfs(now):
    for nxt in range(13):
        if adj[now][nxt]:
            dfs(nxt)
    
dfs(0)
