for p in range(2,100):
    for x in range(p):
        for y in range(p):
            n1 = 7 * p ** 0 + 7 * p ** 1 + x * p ** 2 + 1 * p ** 3
            n2 = 7 * p ** 0 + 7 * p ** 1 + x * p ** 2 + x * p ** 3
            r = y * p ** 0 + y * p ** 1 + 0 + y * p ** 3
            if n1 + n2 == r:
                print(x * p ** 0 + y * p ** 1 + x * p ** 2 + y * p ** 3)