'''
# 문제 이해
대문자와 숫자를 분리한 후 대문자는 모두 오름차순 정렬하고, 숫자는 모두 더하여 둘을 이어 출력한다.

# 발상
이것도 완전탐색 문제이다.

# 복잡도
입력 문자열의 길이를 n이라고 할 때 O(n)의 시간복잡도를 가진다.

'''
data = input()

alphabets = []
alphabet = ''
numbers = []

number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(len(data)):
    if data[i] in number_list:
        numbers.append(data[i])
    else:
        alphabets.append(data[i])

alphabets.sort()

for a in range(len(alphabets)):
    alphabet += alphabets[a]

if len(numbers) != 0:
    result = 0
    for j in range(len(numbers)):
        result += int(numbers[j])
    print(alphabet + str(result))
else:
    print(alphabet)
'''
# 푼 시간
14분

# 채점
정답

# 느낀 점
확실히 구현의 난이도 낮은 문제는 빨리 풀 수 있다.
'''