'''
<>

# 입력


# 출력


'''
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end= ' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
'''
# 생각
구현은 매우 간단하다.
최댓값만큼의 인덱스를 가진 별도의 리스트를 만들고,
데이터를 확인하면서 각 데이터에 해당하는 인덱스의 값을 증가시키면 된다.

데이터의 개수가 n, 데이터 중 최댓값이 k일 때, 계수 정렬은 최악의 경우에도 수행시간 O(n + k)를 보장한다.
일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용할 수 있다.
'''