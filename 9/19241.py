f = open('19241.txt')
for i in f:
    print(i.split())
    a=[int(x) for x in i.split()]
    pov = [x for x in c if c.count(x)==3]
    pov2 = [x for x in c if c.count(x) == 3]
    nepov = [x for x in c if c.count(x) == 1]