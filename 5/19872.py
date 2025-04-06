def f(n):
    s = ''
    while n != 0:
        s = str(n % 7) + s
        n //= 7
    return s
p=[]
for N in range(1,1000):
    c=f(N)
    if N % 2 == 0 :
        c = '52' + c + '1'
    else:
        c = c[-1] + c[1:-1] + c[0] + '15'
    r=str(int(c))
    if N<1000 and len(r)==4:
        p.append(N)
print(max(p))
