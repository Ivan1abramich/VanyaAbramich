def lol(n):
    if n%2==0:
        n/=2
    else:
        n-=7


def f(x,y,z):
    if (x <y) or (('AAA' in z) or ('BBB' in z)):
        return  0
    if x == y:
        return 1

    if x>y:
        if x%2==0:
            return f(x-2,y,z+'A') + f(x/2,y,z+'B')
        else:
            return f(x - 2, y, z + 'A') + f(x - 7, y, z + 'B')

print(f(40,1,''))