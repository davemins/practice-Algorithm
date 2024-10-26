'''
<크루스칼 알고리즘>

# 입력


# 출력


'''
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


'''
# 생각
신장 트리라는 것이 있다.
하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프이다.
근데 크루스칼 알고리즘은 신장 트리 중에서 최소 비용을 만들 수 있는 신장 트리를 찾는 알고리즘이다.

비용이 작은 간선부터 하나씩 확인하면서 사이클을 발생시키지 않으면 최소 신장 트리에 포함시킨다.
항상 최종 간선의 개수는 '노드의 개수 - 1'이 된다.

서로소 집합 알고리즘이 활용되는 것을 알 수 있다.
그거 말고는 조건문 하나 빼고 다를 게 없다.
여기서 활용하기 위해 앞에서 서로소 집합 알고리즘을 설명해준 것 같다.
'''