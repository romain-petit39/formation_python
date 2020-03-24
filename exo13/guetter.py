class Vehicule():

    __roues = 4

    @property
    def nbRoues(self):
        return self.__roues

    @nbRoues.setter
    def nbRoues(self, nbRoue):
        self.__roues = nbRoue