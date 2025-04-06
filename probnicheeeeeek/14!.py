def f(n):
    s=[]
    while n !=0:
        s.append(n%16)
        n//=16
    return s[::-1]
for x in range (400,10000):
    a = 16 **560 + 16 ** 120 - x
    c= f(a)
    if c.count(0) == 442:
        print(x)