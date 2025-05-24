import heapq as hq
import sys

input = sys.stdin.readline
pq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(pq, (abs(x), x))
        # 절댓값이 작은 순서로 먼저 나오고,
        # 절댓값이 같으면 원래 값이 작은 순서로 나옵니다
        # (음수가 양수보다 우선).
    else :
        # 튜플의 오른쪽 값을 출력 또는 0을 출력한다.
        print(hq.heappop(pq)[1] if pq else 0)
