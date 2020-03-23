import os
from datetime import datetime

date1 = datetime.now()
date2 = datetime(2019,5,10,00,37,59)

tempsRestant = date1 - date2

print(type(tempsRestant))

os.system("pause")