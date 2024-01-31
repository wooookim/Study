"""
순차 탐색
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례로 확인하는 방법
- O(N)
"""
# def sequential_search(n, target, array):
#     # 원소를 하니씩 확인
#     for i in range(n):
#         # 현재의 원소가 찾고자 하는 원소와 동일한 경우
#         if array[i] == target:
#             return i + 1  # 현재의 위치 반환(인덱스기 때문에 +1)


# print("생성할 원소 개수를 입력 후 한 칸 띄고 찾을 문자열 입력")
# input_data = input().split()
# n = int(input_data[0])  # 원소의 개수
# target = input_data[1]  # 찾으려는 문자열

# print("앞서 적은 원소 개수만큼 문자열 입력, 구분은 띄어쓰기 한 칸")
# array = input().split()

# # 순차 탐색 수행 결과
# print(sequential_search(n, target, array))
"""
[입/출력]
5 kim
앞서 적은 원소 개수만큼 문자열 입력, 구분은 띄어쓰기 한 칸
lee park kim choi jeong
3
"""


"""
이진 탐색
- 내부 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
- 변수를 3개 사용(시작, 끝, 중간)
- 찾으려는 데이터와 중간(실수일 경우 소수점 버림 값) 위치에 있는 데이터를 반복적으로 비교
- O(logN)
"""
# # 이진 탐색 소스코드 구현(재귀)
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     # 찾은 경우 인덱스 반환
#     if array[mid] == target:
#         return mid
#     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
#     else:
#         return binary_search(array, target, mid + 1, end)

# # n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
# n, target = list(map(int, input().split()))
# # 전체 원소 입력받기
# array = list(map(int, input().split()))

# # 이진 탐색 수행 결과 출력
# result = binary_search(array, target, 0, n - 1)
# if result == None:
#     print("원소가 존재하지 않음")
# else:
#     print(result + 1)
"""
[입/출력]
10 7
1 3 5 7 9 11 13 15 17 19
4
"""
# # 반복문으로 구현
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid= (start + end) // 2
#         # 찾은 경우 중간점 인덱스 반환
#         if array[mid] == target:
#             return mid
#         # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
#         elif array[mid] > target:
#             end = mid - 1
#         # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
#         else:
#             start = mid + 1
#     return None

# # 이진 탐색 수행 결과 출력
# result = binary_search(array, target, 0, n - 1)
# if result == None:
#     print("원소가 존재하지 않음")
# else:
#     print(result + 1)
"""
[입/출력]
10 7
1 3 5 7 9 11 13 15 17 19
4
"""
"""
이진트리
- 부모노드가 왼쪽 자식보다 크고 오른쪽 자식보다 작다
- 특정 값을 찾을 때
1. 부모와 비교
2. 작으면 왼쪽, 크면 오른쪽 노드로 이동
3. 2를 반복해 타겟을 찾음
"""
"""
input보다 처리가 빠른 sys 라이브러리 활용
"""
# import sys
# input_data = sys.stdin.readline().rstrip()


"""
부품 찾기
"""
# # 이진 탐색
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         # 찾은 경우 중간점 인덱스 반환
#         if array[mid] == target:
#             return mid
#         # 중간점보다 타겟이 작은 경우
#         elif array[mid] > target:
#             end = mid - 1
#         # 중간점이 타겟보다 작은 경우
#         else:
#             start = mid + 1
#     return None

# n = int(input())  # 가게 부품 수
# array = list(map(int, input().split()))  # 가게 물품 리스트
# array.sort()  # 탐색 수행 전 정렬

# m = int(input())  # 손님 요청 부품
# x = list(map(int, input().split()))

# for i in x:
#     result = binary_search(array, i, 0, n - 1)
#     if result != None:
#         print("yes", end=" ")
#     else:
#         print("no", end=" ")
"""
[입/출력]
5
8 3 7 9 2
3
5 7 9
no yes yes
"""
# # 계수 정렬
# n = int(input())
# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] = 1

# m = int(input())
# x = list(map(int, input().split()))

# for i in x:
#     if array[i] == 1:
#         print("yes", end=" ")
#     else:
#         print("no", end=" ")
"""
[입/출력]
5
8 3 7 9 2
3
5 7 9
no yes yes
"""


"""
파라메트릭 서치
- 최적화를 동시에 진행
- 재귀보다 반복으로 구현하면 더 간결해짐
"""
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진탐색 수행
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
