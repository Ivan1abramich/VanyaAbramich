p = []
for n in range(4,1000):
    a ='3' + '5' * n
    while '25' in a or '355' in a or '555' in a:
        if '25' in a:
            a=a.replace('25','3',1)
        if '355' in a:
            a=a.replace('355','52',1)
        if '555' in a:
            a=a.replace('555','23',1)
    summa=sum(map(int,list(a)))
    if summa==27:
        p.append(n)
print(min(p))