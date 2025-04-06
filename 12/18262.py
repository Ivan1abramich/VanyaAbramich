def f(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


p=[]
for n in range(8,12):
    a = '>' + '0' * 17 + '3' * n + '2' * 17
    while '>3' in a or '>2' in a or '>0' in a:
        if '>3' in a:
            a = a.replace('>3', '22>', 1)
        if '>2' in a:
            a = a.replace('>2', '2>', 1)
        if '>0' in a:
            a = a.replace('>0', '3>', 1)

    b = f(int(a[:-1]))
    print(n,b)
