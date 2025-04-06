from string import ascii_uppercase
alph = '0123456789' + ascii_uppercase[:12]
for x in alph:
    summa= int('A23'+ x + 'AC0', 22) +int('GB'+ x + '21670', 22)
    if summa % 21==0:
        print(summa//22)