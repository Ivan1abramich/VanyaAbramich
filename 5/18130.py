p=[]
for n in range(1,1000):
    b=bin(n)[2:]
    if n%3==0:
        b='1'+ b[:-2] + '11'
    else:
        b='10' + b + '0'
    r=int(b,2)
    if r > 1000 and n%2==0:
        p.append(r)
print(min(p))