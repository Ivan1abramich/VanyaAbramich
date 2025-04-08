from math import prod
p=[]
for n in range(3,10000):
    a='2' +'7' * n
    while '27' in a or '777' in a or '377' in a:
        if '27' in a:
            a= a.replace('27','7',1)
        if '777' in a:
            a= a.replace('777','3',1)
        if '377' in a:
            a= a.replace('377','72',1)
    c=prod(map(int, str(a)))
    if c%3==0 and c%10==1:
        p.append(n)
print(max(p))