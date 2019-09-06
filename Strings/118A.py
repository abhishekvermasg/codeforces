a = input()
for i in a:
	if i.lower() not in ['a', 'o', 'y', 'e', 'u', 'i']:
		print('.' + i.lower(), end='')
print()