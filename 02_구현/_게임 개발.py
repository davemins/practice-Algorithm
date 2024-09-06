'''
# 문제 이해
시물레이션 문제다.

# 발상


# 복잡도


'''
n, m = map(int, input().split())
x, y, present_dir = map(int, input().split())

map_list = [[] * n for _ in range(n)]

for i in range(n):
    map_list[i] = list(map(int, input().split()))
    print(map_list)

nx, xy = x - 1, y - 1
dir_move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dir_move_x = [0, 1, 0, -1]
dir_move_y = [1, 0, -1, 0]


'''
# 푼 시간
30분

# 채점
오답

# 느낀 점
구현 능력이 떨어진다.
파싱하는 것까지만 했다.
'''