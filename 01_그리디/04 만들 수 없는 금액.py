'''
# 문제 이해
주어진 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값 구하기

# 발상
모두 더한 것보다 1 큰 정수 max가 일단 당연히 만들 수 없는 정수일 것이다.

1부터 max 전까지 가능한지 확인하면 될 것 같다.
근데 어떻게 확인하지?

# 복잡도
모두 더한 값을 n이라고 할 때 O(n)의 시간복잡도를 가진다.
개수의 최대 * 단위의 최대 = 10억 이므로 O(n)이면 아슬아슬하게 가능할 것 같다.
'''



n = int(input())

data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

"""
result = sum(data) + 1
combination = []

for i in range(len(data)):
    combination.append(data[i])
    for j in range(len(data)):
        if i != j and data[i] + data[j] not in combination:
            combination.append(data[i] + data[j])
print(combination)

for i in range(1, sum(data)):
    if i in combination:
        continue
    else:
        if i <= result:
            result = i
            break
        continue

print(result)"""




'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
도저히 발상이 떠오르지 않는다.
조합의 경우의 수를 전부 만들어야 하는 것일까?

어떻게 비교하는 것이 옳을까?

답지를 본 후 든 생각은 어떻게 이걸 떠올릴 수 있지? 라는 생각이다.
많은 경험과 훈련이 필요할 것 같다.
많이 틀리기 시작하니까 서럽다..
근데 실력이 안되니 어쩔 수 없다.

그리디 알고리즘은 '현재 상태에서 가장 좋아보이는 것만을 선택하는 알고리즘'이다.
다음에 한번 더 보자.
'''
