"""
정렬
- 데이터를 특정한 기준에 따라서 순서대로 나열
- 이진탐색의 전처리 과정

선택정렬
- 데이터가 무작위로 여러개 있을 때
  이중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 것
- O(N^2)
"""
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     min_index = i  # 가장 작은 원소의 인덱스
#     for j in range(i + 1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]  # 스와프

# print(array)


"""
삽입정렬
- 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입
- 데이터가 대부분 정렬된 상태에서 효율적
- 정렬이 진행되는 동안 계속 오름차순을 유지함
- 정렬된 데이터의 좌/우 중 어디에 삽입될지 결정 후 다음 데이터의 좌/우 중 삽입 위치를 반복해서 결정
- O(N^2) / 일부 정렬된 상태에서는 단축됨
"""
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(1, len(array)):
#     for j in range(i, 0, -1):  # 인덱스 i부터 1까지 감소하며 반복하는 문법
#         if array[j] < array[j - 1]:  # 한 칸씩 왼쪽으로 이동
#             array[j], array[j - 1] = array[j - 1], array[j]
#         else:
#             break

# print(array)


"""
퀵 정렬
- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
- 기준을 설정 후 큰 수와 작은 수를 교환 하고 리스트를 반으로 나누는 방식으로 동작
- 피벗 : 기준
- O(N log N)
"""
# 방법 1)
# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quik_sort(array, start, end):
#     if start >= end:  # 원소가 1개인 경우 종료
#         return
#     pivot = start  # 피벗은 첫 번쨰 원소
#     left = start + 1
#     right = end
#     while left <= right:
#         # 피벗보다 큰 데이터를 찾을 때까지 반복
#         while left <= end and array[left] <= array[pivot]:
#             left += 1
#         # 피벗보다 작은 데이터를 찾을 때까지 반복
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:  # 엇갈렸을 때 작은 데이터와 피벗을 교체
#             array[right], array[pivot] = array[pivot], array[right]
#         else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
#             array[right], array[left] = array[left], array[right]
#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
#     quik_sort(array, start, right - 1)
#     quik_sort(array, right + 1, end)

# quik_sort(array, 0, len(array) - 1)
# print(array)


# 방법 2)
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행 후 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))
