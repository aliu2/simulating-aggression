import random
import organisms


def simulate_round(organisms):
    pass


def find_food(organisms):
    # list of tuples
    fed_organisms = []

    # while there are still some organisms to find food
    while len(organisms) > 0:
        prob = 1/(len(organisms)**2)
        rand = random.uniform(0,1)
        if rand <= prob and len(organisms) > 1:
            nem_index = random.randint(1, len(organisms)-1)
            food = (organisms.pop(0), organisms.pop(nem_index-1))
        else:
            food = (organisms.pop(0))
        fed_organisms.append(food)

    return fed_organisms


def evaluate_chances(organisms):
    pass


def evolutionize(organisms):
    pass


def main():
    org = organisms.Organism(0.5, 0.5)
    print(org)


if __name__ == '__main__':
    main()
