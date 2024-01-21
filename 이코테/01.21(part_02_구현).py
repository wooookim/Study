"""
피지컬로 승부보기...

완전탐색
- 모든 경우의 수를 주저 없이 다 계산하는 해결 방법

시뮬레이션
- 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행


* 파이썬 int 자료형 데이터 개수에 따른 메모리 사용량
1. 1,000개 - 약 4kb
2. 1,000,000개 - 약 4mb
3. 1,000,000,000개 - 약 40mb
"""

"""
상하좌우
- 여행가 a는 N * N 크기의 정사각형 공간 위에 있다.
- 이 공간은 1 * 1 크기의 정사각형으로 나누어져 있다.
- 가장 왼쪽/위 좌표는 (1, 1), 가장 오른쪽/아래 좌표는 (N, N)에 해당
- 여행가는 상/하/좌/우 방향으로 이동 가능
- 시작 좌표는 (1, 1)
- 상하좌우는 각각 U, D, L, R 로 입력
- 지도 외 입력은 무시됨

입력이 있을 때 최종 도착 좌표는?
"""
# n = int(input())
# x, y = 1, 1
# plans = input().split()  # 리스트 형태

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ["L", "R", "U", "D"]

# # 이동 계획을 하나씩 확인
# for plan in plans:
#     # 이동 후 좌표 구하기
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
# print(x, y)
"""
입력
5
R R R U D D
"""

"""
pass = 실행할 코드가 없는 것으로 다음 행동을 계속해서 진행
continue = 바로 다음 순번의 loop 수행
break = 반복문 중단 후 loop 밖으로
"""

"""
시각
- 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초 까지의 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램
"""
# h = int(input())

# count = 0
# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 3이 포함되어 있다면 카운트 증가
#             if "3" in str(i) + str(j) + str(k):
#                 count += 1
# print(count)


"""
왕실 나이트
"""
# # 현재 나이트 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord("a")) + 1

# # 나이트가 이동할 수 있는 8가지 방향(L자형)
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -2), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_column <= 8 and next_column >= 1 and next_row <= 8:
#         result += 1
# print(result)


"""
게임 개발
"""
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x, y 좌표 방향을 입력 받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 사방위 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
print(count)
"""
입력
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
