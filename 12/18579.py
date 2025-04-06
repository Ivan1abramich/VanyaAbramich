def f(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s







a='>' +'3' * 10 + '5' * 10 + '7' * 10
while '>3' in a or '>5' in a or '>7' in a:
    if '>3' in a:
        a= a.replace('>3','55>',1)
    if '>5' in a:
        a= a.replace('>5','5>3',1)
    if '>7' in a:
        a= a.replace('>7','3>5',1)
b=int(a[:-1])
print(f(b))
