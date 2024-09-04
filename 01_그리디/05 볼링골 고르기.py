'''
# 문제 이해
주어진 공 중에 서로 무게가 다른 볼링공을 고르는 경우의 수를 모두 구하기

# 발상
모두 비교하여 같으면 경우의 수에 1을 더하고 아니면 넘어가는 로직을 짜면 될 것 같다.

# 복잡도
볼링공의 개수가 n일 때 O(n!)의 시간 복잡도를 가진다.
그러나 볼링공의 개수는 1000보다 작다는 조건이 있으므로 괜찮을 것 같다.
'''

n, m = map(int, input().split())

balls = list(map(int, input().split()))

result = 0

for a in range(len(balls)):
    for b in range(a + 1, len((balls))):
        if balls[a] != balls[b]:
            result += 1

print(result)
'''
# 푼 시간
8분

# 채점
정답

# 느낀 점
많이 쉬웠다.
좋아 보이는 것만 골랐다.
'''