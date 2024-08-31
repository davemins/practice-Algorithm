number = input()
number_list = []

sum1 = 0
sum2 = 0

for i in number:
    number_list.append(int(i))

for j in range(len(number_list) // 2):
    sum1 += number_list[j]

for k in range(len(number_list) // 2, len(number_list)):
    sum2 += number_list[k]

if sum1 == sum2:
    print('LUCKY')
else:
    print('READY')
