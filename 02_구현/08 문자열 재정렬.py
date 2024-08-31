input_data = input()
output_data = ''

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', ' 8', '9']

input_str = []
sum = 0

for i in input_data:
    if i in num_list:
        sum += int(i)
    else:
        input_str.append(i)

input_str.sort()

for j in input_str:
    output_data += j

print(output_data + str(sum))
