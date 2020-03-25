import logging
class Vehicule():

    __roues = 4

    @property
    def nbRoues(self):
        logging.warning('attentio')
        return self.__roues

    @nbRoues.setter
    def nbRoues(self, nbRoue):
        self.__roues = nbRoue
        logging.critical('critique')

