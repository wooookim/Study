"""
탐색
- 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

자료구조
- 데이터를 표현하고 관리하고 처리하기 위한 구조
- push : 데이터 삽입
- pop : 데이터 삭제
- 오버플로 : 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행
- 언더플로 : 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행

스택
- 선입후출, 후입선출
"""
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# print(stack)
# print(stack[::-1])
# [5, 2, 3, 1]
# [1, 3, 2, 5]


"""
큐
- 대기줄
- 공정한 자료구조
- 선입선출
"""
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.popleft()

queue.append(1)
queue.append(4)

queue.popleft()

# print(queue)
# queue.reverse()
# print(queue)
# deque([3, 7, 1, 4])
# deque([4, 1, 7, 3])
# list(queue) 로 자료형 변환


"""
재귀함수
- 자기 자신을 다시 호출하는 함수
- 재귀함수는 Fractal 구조와 흡사하다
"""

# def recursive_function():
#     print("재귀함수 호출")
#     recursive_function()

# recursive_function()
"""
- 재귀함수는 종료 조건을 꼭 명시해서 무한히 호출되는 것을 방지
"""
# def recursive_function(i):
#     # 100번째 출력했을 때 종료 조건 명시
#     if i == 100:
#         return
#     print(i, "번째 재귀함수에서", i + 1, "번째 재귀함수를 호출")
#     recursive_function(i + 1)
#     print(i, "번째 재귀 함수를 종료")


# recursive_function(1)
"""
- 컴퓨터 내부에서 재귀함수 수행은 스택 자료구조를 이용
"""

"""
1) 반복으로 구현한 팩토리얼
"""


def factorial_iterative(n):
    result = 1
    # 1부터 n까지 수 차례로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result


"""
2) 재귀로 구현한 팩토리얼
"""


def factorial_recursive(n):
    # n이 1 이하인 경우 1을 반환, 함수 종료
    if n <= 1:
        return 1
    # n! = n * (n-1)을 그대로 코드로 작성
    return n * factorial_recursive(n - 1)


# print("반복 구현: ", factorial_iterative(5))
# print("재귀 구현: ", factorial_recursive(5))


"""
탐색 알고리즘

DFS(Depth-Fisrt Search)
- 깊이 우선 탐색
- 그래프의 깊은 부분을 우선 탐색
"""


"""
인접 행렬(Adjacency Matrix)
- 2차원 배열로 그래프의 연결 관계를 표현하는 방식
- 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
"""
# inf = 999999999  # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
# graph = [[0, 7, 5], [7, 0, inf], [5, inf, 0]]

# print(graph)
# [[0, 7, 5], [7, 0, 999999999], [5, 999999999, 0]]

"""
인접 리스트(Adjacency List)
- 리스트로 그래프의 연결 관계를 표현하는 방식
"""
# 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0이 연결된 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 정보 저장(노드, 거리)
graph[2].append((0, 5))

# print(graph)
# [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]

"""
메모리 측면 차이
- 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비됨
- 인접 리스트 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용

속도 측면
- 인접 행렬 > 인접 리스트
"""


"""
DFS 동작 과정
1. 탐색 노드를 스택에 삽입하고 방문 처리
2-1. 스택 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리
2-2. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복

* 깊이 들어가다 종점에 도달해 이전 노드로 돌아가면 방문(종점) 노드를 삭제(POP)

데이터 개수가 N인경우 O(N) 시간 소요
"""
# DFS 매서드 정의
# def dfs(graph, v, visited):
#     # 현재 노드 방문 처리
#     visited[v] = True
#     print(v, end=" ")
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)


# # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# graph = [[], [2, 3, 8], [1, 7], [1, 4, 7], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# visited = [False] * 9

# # 정의된 dfs 함수 호출
# dfs(graph, 1, visited)


"""
BFS(Breadth First Search)
- 너비 우선 탐색
- 가까운 노드부터 탐색

동작방식
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
3. 2번을 더 이상 수행할 수 없을 때까지 반복

- deque 라이브러리 활용
- O(N)
- 일반적인 경우 수행 시간이 DFS보다 좋은 편
"""
# from collections import deque


# # BFS 매서드 정의
# def bfs(graph, start, visited):
#     # 큐 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하나의 원소르 뽑아 출력
#         v = queue.popleft()
#         print(v, end=" ")
#         # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# # 각 노드가 연결된 정보를 리스트 자료형을 표현(2차원 리스트)
# graph = [[], [2, 3, 8], [1, 7], [1, 4, 7], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# visited = [False] * 9

# # 정의된 BFS 함수 호출
# bfs(graph, 1, visited)


"""
음료수 얼려 먹기

구현 방식
1. 특정한 지점의 주변 상하좌우를 확인 후 주변 지점 중 값이 0이면서 아직 방문하지 않은 지점이 존재하면 해당 지점 방문
2. 방문한 지점에서 다시 상하좌우를 확인하며 방문해 연결된 모든 지점 방문
3. 1, 2번 반복 후 방문하지 않은 지점 수 확인
"""
# n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))


# def dfs(x, y):
#     # 주어진 범위 이탈 시 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재 노드를 방문하지 않은 경우
#     if graph[x][y] == 0:
#         # 방문 처리
#         graph[x][y] = 1
#         # 상하좌우 위치 모두 재귀 호출
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False


# 모든 노드에 대해 음료 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 dfs 수행
#         if dfs(i, j) == True:
#             result += 1

# print(result)


"""
미로 탈출
"""
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간을 벗어날 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 변환
    return graph[n - 1][m - 1]


print(bfs(0, 0))
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# 10
