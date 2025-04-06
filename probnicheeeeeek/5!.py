p = []
for N in range(0,1000):
    b = bin(N)[2:]
    c=N%3
    if N % 3==0:
        b= b + b[-3:]
    else:
        c = (N % 3)*3
        a = bin(c)[2:]

        b= b + a
    R = int(b,2)
    if R < 76:
        p.append(N)
print(max(p))

