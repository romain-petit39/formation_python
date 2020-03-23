import os
import datetime

now = datetime.datetime.now()


def calculDatePlus1(date):
    def functionImbrique(p):
        return p + datetime.timedelta(2)
    return str(functionImbrique(date))

result = calculDatePlus1(now)
print(type(result))
print(result)
os.system("pause")
