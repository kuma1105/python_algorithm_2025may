# 첫 번째 구멍을 만나면 테이프를 붙이고
# 오른쪽으로 3칸 이동해서 구멍이 있으면 테이프를 붙이고
# 없으면 구멍을 만날 때까지 한 칸씩 이동한다.

N, L = map(int, input().split()) # 물 세는 구멍 개수, 테이프 길이
coordinates = [False] * 1001
for i in map(int, input().split()):
    coordinates[i] = True

x = 0 #현재 구멍 여부를 확인하는 좌표
ans = 0 # 테이프 사용 횟수
while x < 1001:
    if (coordinates[x]):
        ans += 1
        x += L
    else:
        x += 1

print(ans)