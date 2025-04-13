p = set()
def f(x,y):
    if y==7:
        p.add(x)
    else:
        f(x+7,y+1)
        f(x + 5,y+1)
        f(x-3,y+1)
f(5,0)
print(len(p))