from parent1 import Parent1
from parent2 import Parent2


class Enfant(Parent1, Parent2):
    def __init__(self):
        super().__init__()

    def appel(self):
        self.test()

