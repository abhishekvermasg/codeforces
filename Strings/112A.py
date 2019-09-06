a = input().lower()
b = input().lower()

# if a == b:
# 	print(0)
# elif a > b:
# 	print(1)
# else:
# 	print(-1)

ans = 0
for i in range(len(a)):
	if a[i] != b[i]:
		if ord(b[i]) - ord(a[i]) > 0:
			ans = -1
			break
		else:
			ans = 1
			break

print(ans)