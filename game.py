from Village import Village

DAY = 1



village = Village()
print(village.population)
while village.population > 0:
    village.day()