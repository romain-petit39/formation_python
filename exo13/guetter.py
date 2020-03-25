import logging
import sys


class Vehicule():
    logging.basicConfig()
    log = logging.getLogger("Vehicule")
    log.setLevel(logging.CRITICAL)
    __roues = 4

    @property
    def nbRoues(self):
        log.warning('attention')
        return self.__roues

    @nbRoues.setter
    def nbRoues(self, nbRoue):
        self.__roues = nbRoue
        log.critical('critique')


    
