def f(a,n):
    a=a[::-1]
    return sum(a[i]*n**i for i in range(len(a)))

for x in range(39):
    for y in range(39):
        a=f([5, 8, x, 7, 2, 3, y, 4, 9],39)
        if a % 38 == 0:
            b = y * 39 + x
            if int(b**0.5)**2 == b:
                print(b)
