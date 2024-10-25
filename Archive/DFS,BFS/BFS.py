"""
<미로 탈출>

# 입력
첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어집니다.
다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
각각의 수들은 공백 없이 붙어서 입력으로 제시된다.
또한 시작 칸과 마지막 칸은 항상 1이다.
5 6
101010
111111
000001
111111
111111

# 출력
첫째 줄에 최소 이동 칸의 개수를 출력한다.
10

"""
from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(int, input()))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            # (핵심 발상이다. 최단 거리 기록 조건..)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))




'''
# 생각
일단 queue를 사용하기 위해 라이브러리를 불러와야 한다.
그 다음에 이동할 방향을 dx, dy로 표현한 것도 알아야 한다.

무시하는 경우를 조건문으로 무시한다.
그리고 최다 거리 기록 조건이 맞으면 queue에 넣는다.
좌표랑 좌표의 값이랑 잘 구분해서 논리적으로 풀어야 할 것 같다.

BFS는 큐에 순서대로 넣는다.
그리고 큐에서 하나씩 꺼내면서 인접 노드를 삽입하고 방문 처리한다.

그래서 왔다갔다 하는 모습인 것 같다.
방문하지 않은 인접 노드가 없으면 무시한다.
'''