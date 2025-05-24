# print("Hello!")
# 
# n = input() #한 줄을 통째로 입력받는다.
# print(n)
# 
# intN = int(input())
# print(intN)
# 
# a, b = map(int, input().split())
# print(a + 100)
# print(b)
# -----------------------------------
# import sys
# for _ in range(10):
#     n = int(sys.stdin.readline()) # input()보다 빠르게 입력받는다.
#     print(n)
# 백준 15552. 빠른A+B문제를 확인해보자.
# -----------------------------------
# 주석 Alt + 3
# 주석 해제 Alt + 4
# -----------------------------------
# 배열 Array
# v = []
# v.append((123, 456))
# v.append((789, 789))
# print("size: ", len(v)) # 2
# for p in v:
#     print(p)
# -----------------------------------
# 스택 Stack
# s = []
# s.append(123)
# s.append(456)
# s.append(789)
# print("size: ", len(s))
# while len(s) > 0:
#     print(s[-1])
#     s.pop(-1)
# -----------------------------------
# 큐 Queue
# from collections import deque
# q = deque()
# q.append(12)
# q.append(34)
# q.append(56)
# q.append(78)
# q.append(910)
# print("size: ", len(q)) # 5
# print(q.pop()) # 910
# print(q.popleft()) # 12
# while len(q) > 0:
#     print(q.popleft())
# -----------------------------------
# 우선순위 큐 Priority Queue (Heap)
# import heapq
# # import heapq as hp #heapq 단어가 길다면 hp로 줄여서 사용하자
# pq = []
# heapq.heappush(pq, 456)
# heapq.heappush(pq, 123)
# heapq.heappush(pq, 789)
# print("size: ", len(pq))
# print(pq)
# while len(pq) > 0:
#     print(heapq.heappop(pq))
# -----------------------------------
# 맵 Map (Dictionary)
# m = {}
# m["A"] = 40
# m["B"] = 100
# m["J"] = 50
# print("size: ", len(m))
# for k in m:
#     print(k, m[k])
# -----------------------------------
# 집합 Set
# s = set()
# s.add(10)
# s.add(10)
# s.add(50)
# s.add(70)
# print(s)
# s.remove(50) # 지정한 요소를 제거한다.
# print(s)
# s.pop() # 임의의 요소가 제거된다.
# print(s)
# s.clear()
# print(s)
