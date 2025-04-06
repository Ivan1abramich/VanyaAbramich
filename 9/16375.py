s = open('16375.txt')
c = 0

for i in s:
    a = [int(x) for x in i.split()]
    a_2 = [x for x in a if a.count(x) == 2]
    a_bez = sorted([x for x in a if a.count(x) == 1])

    if len(a_2) == 2 and len(a_bez)==5:
        if a_bez[0] * a_bez[1] * a_bez[2] > a_2[0] ** 2:
            c += 1
print(c)
