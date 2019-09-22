from sim import obj, simulation

def main():
    # num_of_organisms = input("Number of organisms: ")
    num_of_organisms = 10
    # num_of_doves = input("Number of Doves: ")
    num_of_doves = 5
    # num_of_hawks = input("Number of Hawks: ")
    num_of_hawks = 5
    # num_of_hawks = input("Number of Hawks: ")
    num_of_rounds = 5
    assert num_of_doves + num_of_hawks == num_of_organisms, "Check the number of organisms!"

    # print(type(organisms[0]) == obj.Dove)
    for i in range(num_of_rounds):
        # returns results of simulated round
        # (num_of_doves, num_of_hawks)
        results = simulation.simulate_round(num_of_doves, num_of_hawks)

if __name__ == '__main__':
    main()

# TODO: 1. Function to assign pairs
#       2. Dictionary that holds values of strategies
#       3. Function to evaluates values of strategies
#       4. Dictionary that holds tuple values
