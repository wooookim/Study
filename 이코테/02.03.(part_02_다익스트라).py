"""
최단 거리 알고리즘
1. 다익스트라 최단 경로 알고리즘
2. 플로이드 워셜
3. 벨만 포드 알고리즘

- 그리디 알고리즘 및 다이나믹 프로그래밍 알고리즘의 한 유형
"""


"""
다익스트라 최단 경로 알고리즘
- 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
- '음의 간선'이 없을 경우 정상 작동
* 음의 간선 : 0보다 작은 값을 가지는 간선

알고리즘 원리
1. 출발노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산해 최단 거리 테이블 갱신
5. 3, 4번 과정 반복
"""
# # 간단한 다익스트라 알고리즘 소스코드
# import sys

# input = sys.stdin.readline
# INF = int(1e9)  # 무한 / 10억

# # 노드, 간선 개수 입력
# n, m = map(int, input().split())
# # 시작 노드 번호 입력 받기
# start = int(input())
# # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
# graph = [[] for i in range(n + 1)]
# # 방문한 적이 있는지 체크하는 목적의 리스트 만들기
# visited = [False] * (n + 1)
# # 최단 거리 테이블을 모두 무한으로 초기화
# distance = [INF] * (n + 1)

# # 모든 간선 정보 입력받기
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     # a번 노드에서 b번 노드로 가능 비용이 c라는 의미
#     graph[a].append((b, c))


# # 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호를 반환
# def get_smallest_node():
#     min_value = INF
#     index = 0  # 가장 최단 거리가 짧은 노드
#     for i in range(1, n + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     # 시작 노드에 대해 초기화
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
#     for i in range(n - 1):
#         # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
#         now = get_smallest_node()
#         visited[now] = True
#         # 현재 노드와 연결된 다른 노드를 확안
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost

# # 다익스트라 알고리즘 수행
# dijkstra(start)

# # 모든 노드로 가기 위한 최단 거리를 출력
# for i in range(1, n + 1):
#     # 도달할 수 없는 경우, 무한이라고 출력
#     if distance[i] == INF:
#         print("INF")
#     # 도달할 수 있는 경우 거리를 출력
#     else:
#         print(distance[i])
"""
[입/출력]
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3 
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
0
2
3
1
2
4
"""


"""
개선된 다익스트라 알고리즘
- O(ElogV)  (E : 간선 개수 / V : 노드 개수)
- Heap 자료구조 사용

Heap
- 우선순위 큐를 구현하귀 위해 사용하는 자료구조
- 우선순위 큐 : 우선순위가 가장 높은 데이터를 가장 먼제 삭제
"""
# 개선된 다익스트라 알고리즘
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INF")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
