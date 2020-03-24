from parent1 import Parent1
from parent2 import Parent2


class Enfant(Parent1, Parent2):
    """Classe enfant extend de parent1 et parent2
    
    Arguments:
        Parent1 {class} -- class parent1
        Parent2 {class} -- class parent2
    """
    def __init__(self):
        super().__init__()

    def appel(self):
        """appel test de parent
        """
        self.test()

