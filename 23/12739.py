
def f(x,y):
    if x ==y:
        return 1
    if x <y or x==36 or x==100:
        return 0
    if x>y:
        return f(x//2,y) + f(x//3,y) + f(x-3,y)
print(f(163,45)*f(45,3))