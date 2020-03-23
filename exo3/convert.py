import os
from datetime import datetime

a = '203'
print("type a", type(a))
b = 7
print("type b", type(b))
a = int(a)
print("type a", type(a))
c = a / b
print("type c", type(c))

myTuple = ('un','deux', 3,)
print(type(myTuple))
divMyTuple = myTuple[2] / 4
print(divMyTuple)

date = datetime.now()
print(date)
os.system("pause")