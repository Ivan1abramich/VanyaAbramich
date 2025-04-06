s = open('9156.txt')
c = 0


for i in s:
    a = [int(x) for x in i.split()]
    if (max(a) + min(a)) % 3 == 0:
        if (a[0] - a[1]) == (a[2] - a[3]) or (a[1] - a[0]) == (a[2] - a[3]) or (a[0] - a[1]) == (a[3] - a[2]) or (a[1] - a[0]) == (a[3] - a[2]) or (a[0] - a[2]) == (a[1] - a[3]) or (a[2] - a[0]) == (a[1] - a[3]) or (a[0] - a[2]) == (a[3] - a[1]) or (a[2] - a[0]) == (a[3] - a[1]) or (a[0] - a[1]) == (a[2] - a[3]) or (a[1] - a[0]) == (a[2] - a[3]) or (a[0] - a[1]) == (a[3] - a[2]) or (a[1] - a[0]) == (a[3] - a[2]):
            c += 1
print(c)