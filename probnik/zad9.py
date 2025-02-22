f = open('9_1.txt')
p = 0
for n in f:
    c=[int(x) for x in n.split()]
    if len(set(c))==5:
        pov = [x for x in c if c.count(x)==2]
        nepov=[x for x in c if c.count(x)==1]
        if (sum(pov)/2) < (sum(nepov)/4):
            p+=1
print(p)