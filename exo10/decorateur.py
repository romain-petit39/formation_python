import os


def decorateurTest(func):
    def custom():
        return func()[0:5]
    return custom


@decorateurTest
def carac():
    return "j'aime le python"


print(carac())

os.system("pause")
