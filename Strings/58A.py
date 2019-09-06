a = input()

arr = list('hello')

for i in a:
	if len(arr) and i == arr[0]:
		t = arr.pop(0)

if len(arr):
	print('NO')
else:
	print('YES')