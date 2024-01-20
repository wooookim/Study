"""
시간 복잡도
"""
array = [3, 5, 1, 2, 4]  # N = 5
summary = 0

for x in array:
    summary += x  # 연산이 N번

# print(summary)
# -> O(N)

a, b = 5, 7
# print(a + b)  # 연산이 1번
# -> O(1)

"""
for i in array:
    for j in array:  # 이중 반복문
        temp = i * j  # O(N * N) = O(N^2)
        print(temp)
"""

# 시간, 메모리 측정
import time

start_time = time.time()  # 측정 시작
# 여기에 프로그램 소스코드
end_time = time.time()
# print('time: ', end_time - start_time)


# 선택정렬과 기본 정렬 라이브러리 수행 시간 비교
from random import randint
import time

# 배열에 10,000개 정수 삽입
array = []
for _ in range(10000):
    array.append(randint(1, 100))  # 1부터 100 사이 랜덤 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()
# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프
# 측정 종료
end_time = time.time()
print("선택 정렬 성능 측정: ", end_time - start_time)

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()
array.sort()
end_time = time.time()
print("기본 정렬 라이브러리 성능 측정", end_time - start_time)
