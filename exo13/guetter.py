class Vehicule():

    Roues = 4

    @property
    def nbRoues(self):
        return self.Roues

    @nbRoues.setter
    def nbRoues(self, nbRoues):
        self.nbRoues = nbRoues