res = 3 * 3125**9 + 2 * 625**8 - 4 * 625**7 + 3 * 125**6 - 2 * 25**5 - 2024
nulls = 0
while res != 0:
    b = res % 25
    if b == 0:
        nulls += 1
    res//=25
print(nulls)