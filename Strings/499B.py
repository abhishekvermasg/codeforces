r = [int(i) for i in input().split(' ')]
n, m = r[0], r[1]

d = {}

for i in range(m):
	t = input().split(' ')
	d[t[0]] = t[1]

k = input().split(' ')
for i in range(len(k) - 1):
	if len(k[i]) <= len(d[k[i]]):
		print(k[i], end=' ')
	else:
		print(d[k[i]], end=' ')
if len(k[-1]) <= len(d[k[-1]]):
	print(k[-1])
else:
	print(d[k[-1]])		