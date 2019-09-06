a = input()

j = 0
k = 0

i = 0
while i < len(a) - 1:
	if a[i] == 'A' and a[i + 1] == 'B':
		j = 1
		i += 1
	if a[i] == 'B' and a[i + 1] == 'B':
		k = 1
		i += 1
	i += 1

if j * k:
	print('YES')
else:
	print('NO')