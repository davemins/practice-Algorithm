'''
<선택 정렬>

# 입력
없음

# 출력
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)

'''
# 생각
구현은 간단하다.
반복해서 비교하여 가장 작은 것으로 최신화하고, 마지막에 스와프한다.

시간복잡도가 O(n^2)이기 때문에 n이 3000 이하일 때 사용할 수 있을 것 같다.
'''