
def f(x,y,z):
    if x >y + 4:
        return  0
    if x == y:
        return 1

    if x<= y+3:
        if z.count('A')==2:
            return f(x * 2, y, z + 'B') + f(x * 3, y, z + 'C')
        else:
            return f(x - 2, y, z + 'A') + f(x * 2, y, z + 'B') + f(x * 3, y, z + 'C')
print(f(6,48,''))