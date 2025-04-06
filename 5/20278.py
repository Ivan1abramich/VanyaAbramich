s = []
for N in range(1,1000):
    b=bin(N)[2:]
    if int(b) % 2 == 0:
        b = b + '01'
        b='101' + b[3:]
    else:
        b = b + '10'
        b = '111' + b[3:]
    r=int(b,2)
    if r < 385:
        s.append(N)
print(max(s))
