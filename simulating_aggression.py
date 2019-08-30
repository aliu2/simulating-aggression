from sim import organisms as org, utils

def main():
    # num_of_organisms = input("Number of organisms: ")
    num_of_organisms = 10
    # num_of_doves = input("Number of Doves: ")
    num_of_doves = 5
    # num_of_hawks = input("Number of Hawks: ")
    num_of_hawks = 5
    assert num_of_doves + num_of_hawks == num_of_organisms, "Check the number of organisms!"

    organisms = [org.Dove()] * num_of_doves + [org.Hawk()] * num_of_hawks

    print(len(organisms))
    # print(type(organisms[0]) == org.Dove)

if __name__ == '__main__':
    main()
