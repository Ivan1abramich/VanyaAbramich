s=[]
for n in range(1,1000):
    b=bin(n)[2:]
    if n%2==0:
        b= b+ '100'
    else:
        b=b + '011'
    r=int(b,2)
    if r>300:
        s.append(n)
print(min(s))
