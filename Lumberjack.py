import Villager


class Lumberjack(Villager.Villager):
    """
    Lumberjack class derived from Villager.
    Lumberjacks should gather wood when supplies are low and temperatures are dropping.
    """
    counter = 0

    def __init__(self, name):
        Villager.Villager.__init__(self, name)
        self.id = Lumberjack.counter
        Lumberjack.counter += 1