s=[]
for n in range(1,1000):
    b=bin(n)[2:]
    if len(b)%2==0:
        b= '10' + b[2:] + '0'
    else:
        b = '11' + b[2:] + '1'
    r=int(b,2)
    if r > 171:
        s.append(n)
print(min(s))