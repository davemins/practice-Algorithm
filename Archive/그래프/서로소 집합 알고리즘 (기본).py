'''
<서로소 집합 알고리즘 (기본)>

# 입력


# 출력


'''
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

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

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
'''
# 생각
서로소 집합 알고리즘은 union 연산과 find 연산으로 조작한다.
union 연산은 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산이다.
find 연산은 특정한 원소가 속한 집합이 어떤 집합인지 알려준다.

이를 바탕으로 위 알고리즘은 각 원소가 속한 집합을 출력하고, 부모 테이블 내용을 출력한다.
굉장히 간단하다.
두 원소의 루트 노드를 찾을 때까지 재귀적으로 호출하여 더 작은 원소로 집합을 지정한다.
그리고 속한 집합과 부모 테이블을 출력하면 된다.

노드의 개수가 V개이고 find 혹은 union 연산의 개수가 M개일 때, 시간복잡도는 O(VM)이다.
'''