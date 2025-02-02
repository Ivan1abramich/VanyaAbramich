res= 5 * 343**2031 + 4 * 49**2142 - 3 * 7**111 + 7**222
b=''
while res > 0:
    b+=str(res%7)
    res//=7
    b=b[::-1]
print(sum(map(int,list(b))))