p = []
for N in range(3,1000):
    b=bin(N)[2:]
    if N % 2 == 0:
        b =b + b[:3]
    else:
        b = '1' + b + '01'
    r=int(b,2)
    if r > 600:
        p.append(r)
print(min(p))
