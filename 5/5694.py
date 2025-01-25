s=[]
m=278
for n in range(120,1000):
    b=m | n
    b=bin(n)[2:]
    if b.count('1')==7:
        r=int(b,2)
        s.append(r)
print(min(s))