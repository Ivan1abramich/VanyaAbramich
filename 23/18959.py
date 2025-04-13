def f(x,y):
    if x ==y:
        return 1
    if x <y or x==40:
        return 0
    if x>y:
        return f(x-3,y) + f(x//2,y) + f(x//5,y)
print(f(120,49)*f(49,6))