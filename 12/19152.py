p=[]
for n in range(2,10000):
    a='59' +'8' * n
    while '68' in a or '988' in a or '888' in a:
        if '68' in a:
            a= a.replace('68','8',1)
        if '988' in a:
            a= a.replace('988','86',1)
        if '888' in a:
            a= a.replace('888','9',1)
    c=sum(map(int, list(a)))
    if int(c ** (1/3))== c**(1/3) :
        p.append(n)
print(min(p))