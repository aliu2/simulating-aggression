import random
import obj


def simulate_round(num_of_doves, num_of_hawks):
    organisms = [obj.Organism("Dove")] * num_of_doves + [obj.Organism("Hawk")] * num_of_hawks
    food = [obj.Food()] * (num_of_doves + num_of_hawks)

    fed_organisms = find_food(organisms, food)

# TODO: 1. Probability of finding food is incorrect
def find_food(organisms, untaken_food):
    # list of tuples
    taken_food = []

    while len(organisms) > 0:
        chosen_food = random.randint(0, len(untaken_food)-1)
        untaken_food[chosen_food].add_consumer(organisms.pop(0))
        if untaken_food[chosen_food].num_consumers() == 2:
            taken_food.append(untaken_food.pop(chosen_food))
    print(untaken_food)
    for org in untaken_food:
        print(org)
    return taken_food


def evaluate_chances(organisms):
    pass


def evolutionize(organisms):
    pass


def main():
    num_of_doves = 3
    num_of_hawks = 3
    organisms = [obj.Organism("Dove")] * num_of_doves + [obj.Organism("Hawk")] * num_of_hawks
    food = [obj.Food()] * 3
    find_food(organisms, food)


if __name__ == '__main__':
    main()
