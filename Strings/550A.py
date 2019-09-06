import re

a = input()

x = [m.start() for m in re.finditer('AB', a)]
y = [m.start() for m in re.finditer('BA', a)]

res = 0
i = 0
j = len(y) - 1
k = len(x) - 1
l = 0
while i < len(x) and j > -1 and k > -1 and l < len(y):
	if abs(x[i] - y[j]) > 1 or abs(x[k] - y[l]) > 1:
		res = 1
	i += 1
	j -= 1
	k -= 1
	l += 1

if res:
	print('YES')
else:
	print('NO')