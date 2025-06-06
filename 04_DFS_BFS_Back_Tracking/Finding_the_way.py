dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
chk = [[False] * 100 for _ in range(100)]
N = int(input())

# 유효한 칸인지 확인하기
def is_valid_cord(y, x):
    return 0 <= y < N and 0 <= x < N

def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x))
    while len(q) > 0:
        y, x = q.popleft()
        chk[y][x] = True # 방문했음을 체크함
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_cord(ny, nx) and not chk[ny][nx]:
                a.append((ny, nx))
