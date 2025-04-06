from itertools import product
a=product('0123456789ab',repeat=6)
c=0
for i in a:
    num=''.join(i)
    if num[0] != '0':
        if num.count('b')==1:
            num=num.replace('1', '*')
            num = num.replace('3', '*')
            num = num.replace('5', '*')
            num = num.replace('7', '*')
            num = num.replace('9', '*')
            num = num.replace('b', '*')
            if num.count('*')==3:
                c+=1
print(c)