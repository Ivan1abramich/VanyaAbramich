p=[]

a=81*'1'
while '111' in a or '88888' in a :
    if '111' in a:
        a= a.replace('111','88',1)
    if '88888' in a:
        a= a.replace('88888','8',1)

print(a)
