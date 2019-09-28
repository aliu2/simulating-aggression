import random
import obj
import chance


def simulate_round(num_of_doves, num_of_hawks):
    doves = ['Dove'] * num_of_doves
    hawks = ['Hawk'] * num_of_hawks
    organisms = doves + hawks
    food = [obj.Food() for i in range(3)]
    fed_organisms = find_food(organisms, food)


def find_food(population, untaken_food):
    taken_food = []

    while len(population) > 0:
        chosen_food = random.randint(0, len(untaken_food)-1)
        curr_organism = population.pop(0)
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
        'Dove': 1,
        'Hawk': 3
    }

    organism_scores = []
    for food in taken_food:
        score = 0
        for member_of_pop in food.get_consumers():
            score += strategy_scores[member_of_pop]
        organism_scores.append(score)

    return organism_scores


def evaluate_chances(list_of_chances):
    result = []

    for i in list_of_chances:
        result.append(chance.switch(i))

    return result


def survives(organism):
    chance = random.randint(0, 100)
    if chance <= organism.get_chance_of_survival():
        return True
    else:
        return False


def reproduces(organism):
    chance = random.randint(0, 100)
    if chance <= organism.get_chance_of_reproduction():
        return True
    else:
        return False


def evolutionize(groupings):
    new_population = []

    for group in groupings:
        for organism in group:
            if survives(organism):
                if reproduces(organism):
                    new_population.append(organism.get_strategy())
                    new_population.append(organism.get_strategy())
                else:
                    new_population.append(organism.get_strategy())

    return new_population


def count_population(population):
    num_of_doves = population.count('Dove')
    num_of_hawks = population.count('Hawk')
    return tuple([num_of_doves, num_of_hawks])


def main():
    # num_of_doves = 3
    # num_of_hawks = 3
    # doves = ['Dove'] * num_of_doves
    # hawks = ['Hawk'] * num_of_hawks
    # organisms = doves + hawks
    # food = [obj.Food() for i in range(3)]
    # food = find_food(organisms, food)
    # food = filter_food(food)
    # strategy_scores = calc_strategy_scores(food)
    groupings = evaluate_chances([1, 1, 3, 4])
    new_population = evolutionize(groupings)
    num_of_organisms = count_population(new_population)
    pass


if __name__ == '__main__':
    main()
