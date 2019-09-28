from sim import simulation
from matplotlib import pyplot as plt
from matplotlib import style


def main():
    # num_of_organisms = input("Number of organisms: ")
    num_of_organisms = 10
    # num_of_doves = input("Number of Doves: ")
    num_of_doves = 5
    # num_of_hawks = input("Number of Hawks: ")
    num_of_hawks = 5
    # num_of_hawks = input("Number of Hawks: ")
    num_of_rounds = list(range(1, 40))
    record_of_doves = []
    record_of_hawks = []
    assert num_of_doves + num_of_hawks == num_of_organisms, "Check the number of organisms!"

    # print(type(organisms[0]) == obj.Dove)
    for i in num_of_rounds:
        # returns results of simulated round
        # (num_of_doves, num_of_hawks)
        results = simulation.simulate_round(num_of_doves, num_of_hawks)
        record_of_doves.append(results[0])
        record_of_hawks.append(results[1])
        num_of_doves = results[0]
        num_of_hawks = results[1]

    style.use('ggplot')
    plt.plot(num_of_rounds, record_of_doves, 'g', label='Doves', linewidth=5)
    plt.plot(num_of_rounds, record_of_hawks, 'c', label='Hawks', linewidth=5)

    plt.title('Population Numbers')
    plt.ylabel('Number of Organisms')
    plt.xlabel('Rounds')

    plt.legend()

    plt.grid(True, color='k')

    plt.show()


if __name__ == '__main__':
    main()

# TODO: 1. Function to assign pairs
#       2. Dictionary that holds values of strategies
#       3. Function to evaluates values of strategies
#       4. Dictionary that holds tuple values
