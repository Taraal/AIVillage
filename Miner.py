import Villager


class Miner(Villager.Villager):
    """
    Miner class derived from Villager.
    Currently useless class.
    Miners will gather stone, which will be used to create buildings.
    """
    counter = 0

    def __init__(self, name):
        Villager.Villager.__init__(self, name)
        self.id = Miner.counter
        Miner.counter += 1