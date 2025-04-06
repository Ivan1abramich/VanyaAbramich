from itertools import product
a = product('012345', repeat = 6)
c = 0
for i in a:
    num=''.join(i)
    if num[0] != 0:
        if num.count('2') == 1:
            p = num.index('2')
            for b in '04':
                num=num.replace(b,'*')
            if p==0 and [p+1]=='*':
                c+=1
            if p==5 and [p-1]=='*':
                c+=1


print(c)


print(c)

