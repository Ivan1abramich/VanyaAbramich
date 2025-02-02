for x in '0123456789abcdefghijklmnop':
    num1 = int('123' +x + '24' ,27)
    num2 = int('135' +x + '78',27)
    summ= num1 + num2
    if summ % 26 ==0:
        print(summ//26)