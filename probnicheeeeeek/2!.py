print('w x y z')
for w in range (2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = ((w <= y) <= x) or not z
                if F == 0:
                    print(w, x, y, z)