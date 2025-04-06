f = open('17550.txt')
k=0
for i in f:
    a=[int(x) for x in i.split()]
    pov= [x for x in a if a.count(x)==3]
    nepov = [x for x in a if a.count(x) == 1]
    if len(pov)== 3 and len(nepov)==3:
        if sum(pov)**2 > sum(nepov)**2:
            k+=1
print(k)
