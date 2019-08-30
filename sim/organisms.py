class Organism:

    def __init__(self):
        self.chance_of_survival = 0
        self.chance_of_reproduction = 0

    def get_chance_of_survival(self):
        return self.chance_of_survival

    def get_chance_of_reproduction(self):
        return self.chance_of_reproduction


class Dove(Organism):
    pass

class Hawk(Organism):
    pass
