'''
# 문제 이해
숫자로만 이루어진 문자열이 주어졌을 때 x 또는 + 연산자를 넣어 만들 수 있는 가장 큰 수를 구한다.

# 발상
문자열 data를 입력받는다.

문자열 data의 길이의 범위까지 반복문을 돌며 각 자리의 숫자를 정수로 파싱한다.
result에 0 또는 1일 경우 더하고, 그 이상이면 곱한다.

# 복잡도
문자열의 길이가 n이라고 할 때 O(n)의 시간복잡도를 가진다.
'''
data = input()

result = int(data[0])

for i in range(1, len(data)):
    if int(data[i]) <= 1 or result == 0:
        result += int(data[i])
    else:
        result *= int(data[i])

print(result)

'''
# 푼 시간
11분

# 채점
정답인 것 같지만 아니다
(그리고 or result <= 1이어야 한다.)

# 느낀 점
풀기 시작하는 시간이 늦어지더라도 생각을 먼저 많이 하자.
10분 남았을 때 풀기 시작해도 괜찮다.
'''