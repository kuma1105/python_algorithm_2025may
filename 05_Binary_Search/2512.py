from bisect import bisect_left, bisect_right

N = int(input())						# 지방의 수
req = list(map(int, input().split()))	# 지방의 예산요청
M = int(input())						# 총 예산

low = 0
high = max(req)
mid = (low + high) // 2 # 상한선
ans = 0

def is_possible(mid):
    total = 0
    for r in req:
        total += min(r, mid)
    return total <= M # mid로 설정한 상한선의 가능, 불가능 여부를 반환

# 언제나 low는 high보다 작고, 언젠가 값이 같아지면서 만나게 된다.
# low가 high보다 커지게 되는 경우는 더 이상 볼 필요가 없으므로 탈출한다.
while low <= high: 
#     print(f'low: {low}, mid: {mid}, high: {high}, ans: {ans}')
    if is_possible(mid):
        low = mid + 1
        ans = mid
    else:
        high = mid - 1
    
    mid = (low + high) // 2

print(ans)

# 상한선 찾는 문제다.
# 1~100,000 범위를 순차적으로 탐색하면 시간이 오래 걸리므로
# 이진 탐색을 사용한다.