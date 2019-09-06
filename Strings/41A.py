a = input()
b = input()

if ''.join(list(reversed(a))) == b:
	print('YES')
else:
	print('NO')