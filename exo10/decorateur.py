import os


def decorateurTest(func):
    def custom():
        return print(func()[0:5])
    return custom


@decorateurTest
def carac():
    return "j'aime le python"


carac()

os.system("pause")
