import logging
import sys


class Vehicule():
    
    __roues = 4
    __log = logging.getLogger("Vehicule")

    def __init__(self):
        logging.basicConfig()
        self.__log.setLevel(logging.CRITICAL)

    @property
    def nbRoues(self):
        self.__log.warning('attention')
        return self.__roues

    @nbRoues.setter
    def nbRoues(self, nbRoue):
        self.__roues = nbRoue
        self.__log.critical('critique')


    
