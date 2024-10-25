'''
<경로 압축 기법 소스코드>

# 입력


# 출력


'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


'''
# 생각


'''