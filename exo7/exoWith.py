import os
from random import randrange

nbAleatoire = randrange(50)
print(nbAleatoire)

with open("file.txt", "w") as file:
    file.write(str(nbAleatoire))

os.system("pause")
