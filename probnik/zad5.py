p = []
for n in range(19, 1000):
    b=bin(n)[2:]

    b = b + b[1] + b[0]
    r=int(b,2)
    if r > 74:
        p.append(n)
print(min(p))
