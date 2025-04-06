f = open('999.txt')
c = 0
for i in f:
    a=[int(x) for x in i.split()]
    a_pov=[x for x in a if a.count(x)==2]
    a_nepov=[x for x in a if a.count(x)==1]
    if len(a_nepov)==5:
        if sum(a_pov) //2 < sum(a_nepov) // 5:
            c+=1
print(c)