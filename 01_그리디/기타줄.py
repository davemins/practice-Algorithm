n, m = map(int, input().split())

package_price = []
line_price = []

result = 0

for i in range(m):
    a, b = map(int, input().split())
    package_price.append(a)
    line_price.append(b)

package_price_min = min(package_price)
line_price_min = min(line_price)

package = n // 6
line = n % 6

'''
if (line_price_min * n) > (package_price_min * package + (line_price_min * line)):
    result = package_price_min * package + (line_price_min * line)
else:
    if (line_price_min * n) > package_price_min * (package + 1):
        result = package_price_min * (package + 1)
    else:
        result = line_price_min * n
'''

min(package_price_min * package + (line_price_min * line), package_price_min * (package + 1), line_price_min * n)

print(result)