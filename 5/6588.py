s=[]
for n in range(4,1000):
    b=bin(n)[2:]
    b=b.replace('1','*')
    b = b.replace('0', '1')
    b = b.replace('*', '0')
    b= '1' + b
    if b.count('0')%2!=0:
        b= b +'1'
    else:
        b = b + '0'
    r=int(b,2)
    if r >180:
        s.append(n)
print(min(s))