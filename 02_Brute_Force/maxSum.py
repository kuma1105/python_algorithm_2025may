# N개의 수를 입력 받아서 두 수를 뽑아 합이 가장 클 때는?
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
print(arr[n-1] + arr[n-2])
