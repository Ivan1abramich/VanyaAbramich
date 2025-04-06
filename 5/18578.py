def f(n):
    s = ''
    while n != 0:
        s = str(n % 4) + s
        n //= 4
    return s



p=[]
for N in range(10,1000):
    b = f(N)
    if N % 4 == 0:
        b = '2' + b  +'03'
    else:
        b = b + str(f((N%4)*5))
    r = int(b,4)
    if r < 567:
        p.append(N)
print(max(p))