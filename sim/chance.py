from . import obj


def one():
    return tuple([obj.Organism('Dove', 100, 100)])


def two():
    return tuple([obj.Organism('Dove', 100, 0), obj.Organism('Dove', 100, 0)])


def three():
    return tuple([obj.Organism('Hawk', 100, 100)])


def four():
    return tuple([obj.Organism('Hawk', 100, 50), obj.Organism('Dove', 50, 0)])


def six():
    return tuple([obj.Organism('Hawk', 0, 0), obj.Organism('Hawk', 0, 0)])


def switch(i):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        6: six
    }

    func = switcher.get(i)
    return func()


def main():
    organisms = [switch(1), switch(1)]
    print(organisms)


if __name__ == '__main__':
    main()