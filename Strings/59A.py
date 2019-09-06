a = input()

l = sum([int(i.islower()) for i in a])
u = sum([int(i.isupper()) for i in a])

if l >= u:
	print(a.lower())
else:
	print(a.upper())