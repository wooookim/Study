"""
계수 정렬(Count Sort)
- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
- 데이터 수가 N, 데이터중 최댓값이 K일 때 -> O(N + K)
- 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용 가능
- 일반적으로 최솟값과 최댓값이 1,000,000을 넘지 않을 때 효과적 차이가 너무 클 경우 계수 정렬 사용 불가
"""
# # 모든 원소의 값이 0보다 크거나 같다고 가정
# array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#     count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

# for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
#     for j in range(count[i]):
#         print(i, end="")  # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
"""
비효율성을 고려해야 한다
-> 데이터가 0, 999999 만 존재하는 경우에도 0부터 100만까지 리스트를 생성해야하기 때문

특성을 파악하기 어려울 경우 퀵정렬을 사용하는게 유리하다
"""


"""
파이썬 라이브러리
- sorted()
- 퀵 정렬과 유사한 병합 정렬 기반으로 만들어짐
- O(NlogN)
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)

# print(result)
"""
변수 지정 없이 바로 지정
- .sort()
"""
array.sort()
# print(array)
"""
key 매개변수
- key 값으로 하나의 함수가 들어가야 함
"""
# array = [("바나나", 2), ("사과", 5), ("당근", 3)]

# def setting(data):
#     return data[1]  # 데이터의 두 번째 값을 기준으로 정렬

# result = sorted(array, key=setting)
# print(result)


"""
위에서 아래로
- 수열을 내림차순으로 정렬하는 프로그램
"""
# n = int(input())

# array = []
# for i in range(n):
#     array.append(int(input()))

# array = sorted(array, reverse=True)

# for i in array:
#     print(i, end=" ")
"""
3
15
27
12
27 15 12
"""


"""
성적이 낮은 순서로 학생 출력
"""
# n = int(input())

# # n명의 학생 정보를 입력받아 리스트에 저장
# array = []
# for i in range(n):
#     input_data = input().split()
#     # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
#     array.append((input_data[0], int(input_data[1])))

# # key를 이용, 점수를 기준으로 정렬
# array = sorted(array, key=lambda student: student[1])

# for student in array:
#     print(student[0], end=" ")
"""
2
홍길동 95
이순신 77
이순신 홍길동
"""


"""
두 배열의 원소 교체
- a, b배열 중 a 원소 합이 최대가 되도록 함
- n, k, a, b를 입력 받고 k번 서로 바꿀 수 있을 때 최댓값 출력
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:  # A의 원소가 B의 원소보다 크거나 같을 때 반복문 탈출
        break

print(sum(a))
