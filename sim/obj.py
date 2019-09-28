class Food:

    def __init__(self):
        self.consumers = []

    def add_consumer(self, organism):
        self.consumers.append(organism)

    def get_consumers(self):
        return self.consumers

    def num_consumers(self):
        return len(self.consumers)

    def __str__(self):
        return f"{self.consumers}"


class Organism:

    def __init__(self, strategy, chance_of_survival=0, chance_of_reproduction=0):
        strategies = ["Dove", "Hawk"]

        assert strategy in strategies
        self.strategy = strategy
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

    def get_strategy(self):
        return self.strategy
