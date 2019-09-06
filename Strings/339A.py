a = input()

a = [int(i) for i in a.split('+')]

a.sort()

t = [print(i, end='+') for i in a[:-1]]
print(a[-1])