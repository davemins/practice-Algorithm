'''
# 문제 이해
룰을 지키며 카드를 뽑아야 한다.
행을 선택하여 그 행에서 가장 작은 값을 뽑을 수 있다.

# 발상
for문을 돌리며 행의 가장 작은 값을 찾고 그 다음 행과 비교해 큰 것을 저장한다

# 복잡도
행이 n이라고 할 때 시간복잡도는 O(n)

'''

n, m = map(int, input().split())

number_list = [[] * n for _ in range(n)]

for i in range(n):
    number_list[i] = list((map(int, input().split())))

final_number = 0

for i in range(n):
    if min(number_list[i]) > final_number:
        final_number = min(number_list[i])

print(final_number)

'''
# 푼 시간
25분

# 채점
맞음

# 느낀 점
이거 리스트 입력 받는데 시간을 많이 썼다.
구현에 아직 약하다 생각이 든다.
그리고 for 문이 많아서 만약 많은 행을 처리하는 문제였으면 시간복잡도에서 걸렸을 수도 있다.

해설을 확인하니 더 간단하게 설계할 수 있는 방법이 있다.
조금 더 효율적으로 설계하기 위한 고민을 더 해보자.
'''