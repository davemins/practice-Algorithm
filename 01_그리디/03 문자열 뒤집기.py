s = input()

result = 0

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        continue
    else:
        result += 1

result = (result + 1) // 2

print(result)