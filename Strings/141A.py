a, b, c = input(), input(), input()

from collections import Counter

if Counter(a + b) == Counter(c):
	print('YES')
else:
	print('NO')