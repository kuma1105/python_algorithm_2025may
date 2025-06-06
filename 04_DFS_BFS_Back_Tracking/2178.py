from collections import deque

import sys
input = sys.stdin.readline # 빠른 입력 함수

N, M = map(int, input().split())

board = [input() for _ in range(N)] # 값이 문자열로 저장된다.

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_cord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    chk = [[False]*M for _ in range(N)]
    chk[0][0] = True
    dq = deque()
    dq.append((0,0,1)) # (y좌표, x좌표, 지나온 칸 수)
    while dq:
        y, x, d = dq.popleft()
        
        if y == N-1 and x == M-1:
            return d
        
        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_cord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, nd))
    return -1 # 만약 문제에서 도착 위치로 도착할 수 없는 경우가 있다면 -1을 출력한다.
    
print(bfs())