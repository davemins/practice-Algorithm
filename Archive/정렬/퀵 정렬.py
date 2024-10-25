'''
<퀵 정렬>

# 입력
없음

# 출력
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
'''
# 생각
위는 파이썬의 장점을 살린 퀵 정렬 구현이다.
전통 퀵 정렬의 분할 방식보다 훨씬 간단하다.
재귀가 여기서도 이용된다.

사실 전통 퀵 정렬은 pivot, left, right를 좀 더 잘 구분할 줄 알아야 한다.
그리고 매개변수로 array뿐 아니라 start, end도 필요하다.

시간복잡도가 O(nlogn)이기 때문에 n이 10만 이하일 때 사용할 수 있을 것 같다.
근데 이게 사람마다 수행시간 예측이 달라서 조금 부정확하다.
'''