p=[]
for n in range(3,1000):
    a='7' +'6' * n
    while '766' in a or '667' in a:
        if '766' in a:
            a= a.replace('766','67',1)
        if '667' in a:
            a= a.replace('667','7',1)


    p.append(a)
print(p)
