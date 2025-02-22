p=[]
for x in '0123456789abcdefghij':
    x1='98' + str(x) + '79641'
    x2='36' + str(x) + '14'
    x3='73' + str(x) + '4'
    r = int(x1,19) +int(x2,19) + int(x3,19)
    if r % 18 == 0:
        r = r //18
        p.append(r)
    print(max(p))

