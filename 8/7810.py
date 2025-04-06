k=0
from itertools import *
for i in product('МАСЛО', repeat = 6):
    i=''.join(i)
    if i.count('A')+ i.count('О') == 1:
        k += 1
print(k)