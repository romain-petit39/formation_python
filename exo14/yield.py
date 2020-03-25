import math
import os

def createGenerator():
    myList = range(10)
    for i in myList:
        yield math.sqrt(i)

generator = createGenerator()
print(generator)

for i in generator:
    print(i)

os.system("pause")