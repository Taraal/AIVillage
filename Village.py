from time import sleep
import Farmer
import Lumberjack
import Miner
import Villager


#####
# WIP 
TEMPERATURE = 20
DAY = 1
SEASONS = ("spring", "summer", "fall", "winter")
#####

class Village():

    def __init__(self) -> None:
        self.villagers = []
        self.population = 0
        self.food = 100
        self.wood = 100
        
        self.new_villager(Farmer.Farmer, "1")

        
    def food_consumption(self):
        self.food = round(self.food + (1.7 * int(Farmer.Farmer.counter) - self.population))
        print(self.food)

    def new_villager(self, Job, name):
        new_entity = Job(name)
        self.villagers.append(new_entity)
        self.population += 1

    def day(self):
        self.food_consumption()
        sleep(0.5)