def f(n):
    s=[]
    while n > 0:
        s.append(n%25)
        n//=25
    return s[::-1]

a=15625**16 - 3125**3 * 25 ** 19 + 625**4 - 2005
c=(f(a))
print(c.count(0))