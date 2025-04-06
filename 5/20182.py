def f(n):
    s=[]
    while n !=0:
        s.append(n%3)
        n//=3
    return s[::-1]




for N in range(10,1000):
    b=f(N)
    c=''
    for n in b:
        c+=str(n)
    if sum(map(int,c))%2==0:
        c= '12' + c[2:]  +'0'
    else:
        c= '10' + c[2:] + '2'
    r=int(c,3)
    if r > 105:
        print(N)
        break

