p = []
for N in range(3,1000):
    b=bin(N)[2:]
    if N % 5 == 0:
        b =b[:3] + b
    else:
        b= b + bin((N%5)*5)[2:]
    r=int(b,2)
    if r < 313 and N%2 != 0:
        p.append(N)
print(max(p))