'''
# 문제 이해
좌우의 자릿수가 같으면 LUCKY, 다르면 READY를 출력한다.

# 발상
완전 탐색 : 모든 경우의 수를 빠짐없이 계산하면 될 것 같다.

# 복잡도
정수의 길이가 n일 떄 O(n)의 시간복잡도를 가진다.

'''
data = input()
n = len(data)

left, right = 0, 0

for i in range(n // 2):
    left += int(data[i])

for j in range(n // 2, n):
    right += int(data[j])

if left == right:
    print("LUCKY")
else:
    print("READY")
'''
# 푼 시간
7분

# 채점
정답

# 느낀 점
이정도는 풀 수 있다는 생각이 든다.
'''