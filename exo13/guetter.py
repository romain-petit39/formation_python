class Vehicule():

    @property
    def nbRoues(self):
        return 4

    @nbRoues.setter
    def nbRoues(self, nbRoues):
        self.nbRoues = nbRoues