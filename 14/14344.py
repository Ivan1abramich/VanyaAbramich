for p in range(16,37):
    s=int('17496',p) + int('91f83',p) + int('d9543',p)
    if s % 12 == 0:
        print(s//12)