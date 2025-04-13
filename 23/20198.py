def f(x,y,z):
    if x >y + 3 or "AAA" in z:
        return  0
    elif x == y and 'AAA' not in z:
        return 1

    else:
        return f(x-1,y,z +'A') + f(x+5,y,z +'B') + f(x*2,y,z +'C')
print(f(5,34,''))