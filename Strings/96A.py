a = input()

# z = a.count('0')
# o = a.count('1')

# if o < 7 and z < 7:
# 	print('NO')
# else:
# 	zs = [1 if len(i) > 6 else 0 for i in a.split('0')]
# 	os = [1 if len(i) > 6 else 0 for i in a.split('1')]
# 	if zs.count(1) or os.count(1):
# 		print('YES')
# 	else:
# 		print('NO')

cnt = 1
ans = 0
for i in range(len(a) - 1):
	if a[i] == a[i + 1]:
		cnt += 1
	else:
		cnt = 1
	if cnt > 6:
		ans = 1
		break

if ans:
	print('YES')
else:
	print('NO')