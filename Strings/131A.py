a = input()

b = [int(i.isupper()) for i in a]

if (not b[0] and sum(b[1:]) == len(a) - 1):
	print(a.capitalize())
elif sum(b) == len(a):
	print(a.lower())
else:
	print(a)