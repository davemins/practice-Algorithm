not_sel_num = []
def d(n):
	# 입력된 번호를 string 리스트로 만든다 -> 각 자리수를 더하기 위함.
	num_list = list(str(n))
	answer = 0

	# 각 자리수를 더함
	for num in num_list:
		answer += int(num)
	answer += n
	return answer

for i in range(1, 10001):
    dn = d(i)
    if dn not in not_sel_num:
        not_sel_num.append(dn)

for j in range(1, 10001):
    if j not in not_sel_num:
        print(j)