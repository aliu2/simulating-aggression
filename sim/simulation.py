import random
import obj
import chance


def simulate_round(num_of_doves, num_of_hawks):
    doves = [obj.Organism("Dove") for i in range(num_of_doves)]
    hawks = [obj.Organism("Hawk") for i in range(num_of_hawks)]
    organisms = doves + hawks
    food = [obj.Food() for i in range(3)]
    fed_organisms = find_food(organisms, food)


def find_food(organisms, untaken_food):
    taken_food = []

    while len(organisms) > 0:
        chosen_food = random.randint(0, len(untaken_food)-1)
        curr_organism = organisms.pop(0)
        untaken_food[chosen_food].add_consumer(curr_organism)
        if untaken_food[chosen_food].num_consumers() == 2:
            taken_food.append(untaken_food.pop(chosen_food))

    return taken_food + untaken_food


def filter_food(list_of_food):
    taken_food = []
    for food in list_of_food:
        if food.num_consumers() > 0:
            taken_food.append(food)

    return taken_food


def calc_strategy_scores(taken_food):
    strategy_scores = {
        "Dove": 1,
        "Hawk": 3
    }

    organism_scores = []
    for food in taken_food:
        score = 0
        for organism in food.get_consumers():
            score += strategy_scores[organism.get_strategy()]
        organism_scores.append(score)

    return organism_scores


def evaluate_chances(list_of_chances):
    result = []

    for i in list_of_chances:
        result.append(chance.switch(i))

    return result


def evolutionize(organisms):
    pass


def main():
    # num_of_doves = 3
    # num_of_hawks = 3
    # doves = [obj.Organism("Dove") for i in range(num_of_doves)]
    # hawks = [obj.Organism("Hawk") for i in range(num_of_hawks)]
    # organisms = doves + hawks
    # food = [obj.Food() for i in range(10)]
    # food = find_food(organisms, food)
    # food = filter_food(food)
    # strategy_scores = calc_strategy_scores(food)
    print(evaluate_chances([1, 1, 3, 4]))
    pass


if __name__ == '__main__':
    main()
