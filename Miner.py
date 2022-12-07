from itertools import count
import Villager


class Miner(Villager.Villager):
    counter = 0

    def __init__(self, name):
        Villager.Villager.__init__(self, name)
        self.id = Miner.counter
        Miner.counter += 1