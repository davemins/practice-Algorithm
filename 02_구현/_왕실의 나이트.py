'''
# 문제 이해
8가지 방향에 대하여 현재 위치 기준에서 이동이 가능한 경우의 수를 구하자.

# 발상
먼저 파싱한 후에 가능한 이동 경로를 대입하여 이동한 후, 범위에 벗어나지 않았으면 카운트한다.

# 복잡도
O(1)의 시간복잡도를 가진다.

'''
location = input()

x = location[0]
y = int(location[1])

location_dir = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
x_location = location_dir[x]

x_move = [1, 2, 2, 1, -1, -2, -2, -1]
y_move = [2, 1, -1, -2, -2, -1, 1, 2]

result = 0

for i in range(8):
    mx = x_location + x_move[i]
    my = y + y_move[i]

    if mx < 1 or mx > 8 or my < 1 or my > 8:
        continue
    result += 1

print(result)
'''
# 푼 시간
18분

# 채점
정답

# 느낀 점
범위를 나가는 값의 경우를 정확하게 확인하는 것이 좋다.
'''