'''
# 문제 이해
배열이 주어진다
배열의 크기 n이 주어진다
더할 횟수 m이 주어진다
연속 최대 횟수 제한 k가 주어진다
-> 조건에 맞는 더해진 값을 구하면 된다

# 발상
최대 숫자를 구한다
다음 숫자를 구한다 -> 리스트에서 최대 숫자를 뺀 후
s "최대 숫자 * k + 다음 숫자"를 구한다
v : m / (k+1) 하고 r : m % (k+1)을 구한다

v * s + 최대 숫자 * r을 출력한다

# 복잡도
O(1)이다.
'''

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

maximum_num = max(data)
data.remove(maximum_num)
next_num = max(data)

s = maximum_num * k + next_num

v = m / (k + 1)
r = m % (k + 1)

print(v * s + maximum_num * r)

'''
# 푼 시간
18분

# 채점
정답(그러나 숫자 타입이 다르다)

# 느낀 점
map(int, input().split()) 이 부분은 해설을 보고 왔다.
파이썬을 사용한 지 오래되어 기억이 가물가물하다.
익숙해지자.

가장 큰 수와 그다음 수를 구하는 과정은 max로 찾을 수 있지만 인덱스로 찾는 것도 깔끔할 것 같다.
그리고 int랑 float 이것도 신경 써야 할 것 같다.
변수 이름도 신경 서야 할 것 같다.
'''