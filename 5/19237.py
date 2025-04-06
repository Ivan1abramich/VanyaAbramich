def f(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s



p=[]
for N in range(10,1000):
    b = f(N)
    if N % 3 == 0:
        b = b  + b[-2:]
    else:
        b = b + f(b.count('1')+b.count('2')*2)
    r = int(b,3)
    if r >220 and r%2==0:
        p.append(r)
print(min(p))