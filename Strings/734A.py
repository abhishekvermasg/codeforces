_, b = input(), input()

a = b.count('A')
d = b.count('D')

if a > d:
	print('Anton')
elif a < d:
	print('Danik')
else:
	print('Friendship')