"""그룹 단어 체커"""
# https://www.acmicpc.net/problem/1316

test_case = int(input())
# 전체 단어의 개수 저장
count = test_case

for _ in range(test_case):
    word = input()
    word_box = [word[0]]
    for i in range(1, len(word)):
        if (word[i - 1] != word[i]) and (word[i] in word_box):
            # 그룹 단어가 아닌 경우가 발생할 시 전체 단어의 개수에서 1을 뺀 후 다음 반복문으로 넘어감
            count -= 1
            break
        # 각 문자가 떨어져 나타나는 경우를 검사하기 위해 word_box에 문자 저장
        word_box.append(word[i])

print(count)