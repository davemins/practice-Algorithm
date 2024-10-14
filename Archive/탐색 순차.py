'''
<순차 탐색>

# 입력


# 출력


'''
# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))

'''
# 생각
말 그대로 순차 탐색이다.
순차적으로 데이터를 방문하여 특정한 문자열과 같은지 검사하므로 구현도 간단하다.

'''