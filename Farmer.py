
import Villager


class Farmer(Villager.Villager):
    counter = 0

    def __init__(self, name):
        Villager.Villager.__init__(self, name)
        self.id = Farmer.counter
        Farmer.counter += 1