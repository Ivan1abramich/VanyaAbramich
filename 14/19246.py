for x in '0123456789abcdefghijklmn':
    num1 = int('11353' + x + '12',25)
    num2 = int('135' + x + '21',25)
    summ= num1 + num2
    if summ % 24 ==0:
        print(summ//24)
