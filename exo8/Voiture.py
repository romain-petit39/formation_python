from direction import Direction
class Voiture(Direction):


    NB_ROUE = 4
    __couleur = 'bleu'


    def __init__(self):
      super().__init__()


    def demarrer(self):
        print("vroum vroum")
