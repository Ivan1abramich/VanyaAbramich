def lol(n):
    if n%2==0:
        n/=2
    else:
        n -=3
    return (n)


def f(x,y):
    if x ==y:
        return 1
    if x <y or x==18:
        return 0
    if x>y:
        return f(x-2,y) + f(lol(x),y)
print(f(55,3))