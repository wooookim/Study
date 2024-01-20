"""
그리디
- 현재 상황에서 지금 당장 좋은 것만 고르는 방법
"""

"""
거스름 돈
-> 가지고 있는 동전 중 큰 단위가 항상 작은 단위의 배수
    
[예제]
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
손님에게 서슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
"""
# n = 1260
# count = 0

# coin_types = [500, 100, 50, 10]

# for coin in coin_types:
#     count += n // coin
#     n %= coin

# print(count)


"""
큰 수의 법칙
- 반복되는 수열에 대해서 파악


[예제]
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
단, 배열의 특정 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.

예를 들어,
순서대로 2, 4, 5, 4, 6 으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하면,
이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로
6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 = 46이 된다

서로 다른 인덱스이면 같은 수여도 다른 것으로 간주 
"""
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()

# first = data[-1]
# second = data[-2]

# result = 0

"""
방법 1)

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
        
    # k + 1 로 나누어 떨어지지 않으면 아래 코드
    if m == 0:
        break
    result += second
    m -= 1
"""
"""
방법 2)

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second
"""
# print(result)


"""
숫자 카드 게임
- 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
- 숫자가 쓰인 카드들이 N * M 형태로 놓여 있다. 이때 N은 행의 개수, M은 열의 개수
1. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택
2. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다

- 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수
"""
# N, M = map(int, input().split())

# result = 0

"""
방법 1)
for i in range(N):
    data = list(int(input().split()))
    # 현재 줄에서 가장 작은 수
    min_value = min(data)
    # 가장 작은 수 들 중에서 가장 큰 수
    result = max(result, min_value)
"""

"""
for i in range(N):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은수
    min_value = 10001  # 문제 조건
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
"""

"""
입력 예)
2 4
7 3 1 8
3 3 3 4
"""
# print(result)


"""
1이 될 때까지
- 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
- 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있따
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

- 최대한 많이 나누기
"""
N, K = map(int, input().split())
result = 0

"""
방법 1)
# N이 K 이상이라면 K로 계속 나누기
while N >= K:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1 빼기
    while N % K != 0:
        N -= 1
        result += 1

    # K로 나누기
    N //= K
    result += 1

# 마지막으로 남은 수에 대해 1씩 빼기
while N > 1:
    N -= 1
    result += 1
"""

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (N // K) * K
    result += N - target
    N = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break
    # K로 나누기
    result += 1
    N //= K

# 마지막으로 남은 수에 대하여 1씩 빼기
result += N - 1

print(result)
