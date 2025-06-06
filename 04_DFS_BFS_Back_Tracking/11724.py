import sys
sys.setrecursionlimit(10 ** 6) # 파이썬 재귀 깊이를 100에서 1000000으로 늘림
input = sys.stdin.readline # 빠른 입력 함수 
N, M = map(int, input().split())

adj = [[0]*N for _ in range(N)]

for _ in range(M):
    # 정점 번호가 0이 아닌 1부터 시작하므로 입력값에서 1씩 뺀다.
    a, b = map(lambda x: x-1, map(int, input().split()))
    adj[a][b] = adj[b][a] = 1 # 무방향 그래프이므로.

ans = 0 # 연결요소 개수
chk = [False] * N

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True # 방문 체크를 미리 하는 것이 효율적이다.
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans += 1
        chk[i] = True # 방문 체크를 미리 하는 것이 효율적이다.
        dfs(i)

print(ans)