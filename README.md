# Simulating Aggression
This program runs a simulation that demonstrates an interesting argument in the field of game theory. The argument is that there is no one ideal strategy when referring to the term "survival of the fittest", it's not always the most aggressive members of a given primitive population that survive. This simulation includes two strategies, the Dove strategy (passive) and the Hawk strategy (aggressive). The simulation runs through forty rounds and plots the number of Doves and Hawks for each round on the Y axis, and the rounds on the X axis. What you'll notice is that, even though Hawks tend to come out on top, the number of Doves is never too far behind!


## Rules
The rules for the simulation are as follows:
- Each member of the population has one of the two strategies, Dove or Hawk.
- Each organism has two main attributes, a chance for survival and a chance to reproduce.
- Each day, every organism goes out and finds a piece of food.
- Food comes in pairs.
- A whole piece of food (half of a pair) firstly adds to an organism's chance for survival and then adds to an organism's chance for reproducing.
- A maximum of two organisms can land at one pair of food and their chance of surviving and reproducing depends on the adopted strategy of both organisms.

Outcomes of landing on a pair of food are illustrated in the following tables (numbers represent percentages):

**Chance of survival**
|      | Dove | Hawk |  
| ---- | ---- | ---- |  
| Dove | 100 | 100  |  
| Hawk |  50 | 0 |
| (None) | 100 | 100 |

**Chance of reproducing**
|      | Dove | Hawk |  
| ---- | ---- | ---- |  
| Dove | 0 | 50  |  
| Hawk |  0 | 0 |
| (None) | 100 | 100 |


## Usage
Once you have cloned the repo, activate a pipenv shell environment (making sure simulating-aggression is your cwd):

`$ pipenv shell`

Then run the main program to start the simulation:

`$ python3 simulating-aggression.py`
