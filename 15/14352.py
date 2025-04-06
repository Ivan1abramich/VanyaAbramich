def DEL(n,m):
    if n % m ==0:
        return True
    else:
        return False

for a in range(1,1000):
    flag = True
    for x in range(1,1000):
        f = DEL(x, a) or ((x >= 120 and x <= 180) <= ((not DEL(x, 16)) or (x + a <= 204)))
        if f == 0:
            flag = False
            break
    if flag == True:
        print(a)
