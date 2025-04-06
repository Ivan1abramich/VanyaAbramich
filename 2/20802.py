print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f=(w<=(not(z<=x))) or y
                if f==0:
                    print(w,x,y,z)