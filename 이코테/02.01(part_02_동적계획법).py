"""
- 메모리를 약간 더 사용하면서 효율을 증대시킴
- 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결


- 피보나치 수열(이전 두 항의 합을 현재 항으로 설정)

- O(N)
"""
# 비효율적인 재귀함수
# def fibo(x):
#     if x == 1 or x == 2:
#         return 1
#     return fibo(x - 1) + fibo(x - 2)

# print(fibo(4))


"""
메모제이션 기법
- 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법
- (= 캐싱)
- 리스트에 저장해 둠
"""
# # 한 번 계산된 결과를 메모제이션하기 위한 리스트 초기화
# d = [0] * 100

# # 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹)
# def fibo(x):
#     # 종료 조건(1 혹은 2일 때 1일 반환)
#     if x == 1 or x == 2:
#         return 1
#     # 이미 계산한 적 있는 문제라면 그대로 반환
#     if d[x] != 0:
#         return d[x]
#     # 아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
#     d[x] = fibo(x - 1) + fibo(x - 2)
#     return d[x]

# print(fibo(99))

"""
"""

# d = [0] * 100

# def pibo(x):
#     print("f(" + str(x) + ")", end=" ")
#     if x == 1 or x == 2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = pibo(x - 1) + pibo(x - 2)
#     return d[x]

# pibo(6)

"""
탑다운 : 큰 문제를 해결하기 위해 작은 문제를 호출
<-> 바텀업
"""


"""
1로 만들기
- 정수 x가 주어졌을 때, 연산 4개를 적절히 사용해 1로 만들기
1. 5로 나누어 떨어지면 5로 나누기
2. 3으로 나누어 떨어지면 3으로 나누기
3. 2로 나누어 떨어지면 2로 나누기
4. 1 빼기
"""
# x = int(input())

# d = [0] * 30001

# for i in range(2, x + 1):
#     # 현재의 수에서 1을 빼는 경우
#     d[i] = d[i - 1] + 1
#     # 현재 수가 2로 나누어 떨어지는 경우
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i // 2] + 1)
#     # 현재 수가 3로 나누어 떨어지는 경우
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i // 3] + 1)
#     # 현재 수가 5로 나누어 떨어지는 경우
#     if i % 5 == 0:
#         d[i] = min(d[i], d[i // 5] + 1)

# print(d[x])


"""
개미 전사
"""
# n = int(input())
# array = list(map(int, input().split()))

# d = [0] * 100

# d[0] = array[0]
# d[1] = max(array[0], array[1])

# for i in range(2, n):
#     d[i] = max(d[i - 1], d[i - 2] + array[i])

# print(d[n - 1])


"""
바닥 공사
"""
# n = int(input())
# d = [0] * 1001

# d[1] = 1
# d[2] = 3
# for i in range(3, n + 1):
#     d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

# print(d[n])


"""
효율적 화폐 구성
"""
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
