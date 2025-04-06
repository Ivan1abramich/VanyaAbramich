s = []
for N in range(9,1000):
    b=bin(N)[2:]
    if N % 3 == 0:
        b = b + b[-2:]
    else:
        b = '1'+ b + '1'

    r=int(b,2)
    if r > 700:
        s.append(r)
print(min(s))