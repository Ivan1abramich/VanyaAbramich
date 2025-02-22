from itertools import combinations
p=0
for p4 in range(6):
    for c in combinations([i for i  in range(6) if i!= p4],2):
        cnt4 = 1
        cnt0 = 4**2
        cnt3 = 4**3
        p+= cnt4 * cnt0 * cnt3
print(p)