class Organism:

    def __init__(self, chance_of_survival=0, chance_of_reproduction=0):
        # float 0-1
        self.chance_of_survival = chance_of_survival
        # float 0-1
        self.chance_of_reproduction = chance_of_reproduction

    def set_chance_of_survival(self, chance):
        self.chance_of_survival = chance

    def get_chance_of_survival(self):
        return self.chance_of_survival

    def set_chance_of_reproduction(self, chance):
        self.chance_of_reproduction = chance

    def get_chance_of_reproduction(self):
        return self.chance_of_reproduction


class Dove(Organism):
    pass

class Hawk(Organism):
    pass
