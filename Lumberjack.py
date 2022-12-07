from itertools import count
import Villager


class Lumberjack(Villager.Villager):
    counter = 0

    def __init__(self, name):
        Villager.Villager.__init__(self, name)
        self.id = Lumberjack.counter
        Lumberjack.counter += 1