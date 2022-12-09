import Villager

class Mayor(Villager.Villager):
    """
    Mayor can buff specialized villagers and keep moral high
    There can be only one mayor.    
    """
    elected = 1
    
    def __init__(self, name):
        Villager.Villager.__init__(self, name)        
        self.id = Mayor.elected        