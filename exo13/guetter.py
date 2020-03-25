import logging
import sys


class Vehicule():

    __roues = 4

    @property
    def nbRoues(self):
        logging.warning('attention')
        return self.__roues

    @nbRoues.setter
    def nbRoues(self, nbRoue):
        self.__roues = nbRoue
        logging.critical('critique')


    logging.basicConfig()
    log = logging.getLogger("Vehicule")
    log.setLevel(logging.CRITICAL)
