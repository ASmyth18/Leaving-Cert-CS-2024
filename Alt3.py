"""
Alt 3 asks the student to create a programme that solves a problem that is traditionally considered difficult to solve analytically.
They provide an example here:
https://www.curriculumonline.ie/senior-cycle/senior-cycle-subjects/computer-science/support-material-for-teaching-and-learning/2-alt-resources/alt3-support/
However, the Python example they provide seems to miss the point of the prompt and thus, I decided to branch down a different route:
The monty hall problem is a probability puzzle that is difficult to solve analytically but can be easily understood through simulation.
As such, it is a far better example of a programme that satisfies the prompt.
"""

import random

def monty_hall_simulation(num_simulations):
    wins_with_switch = 0
    wins_without_switch = 0

    for _ in range(num_simulations):
        # Create doors: one with a car (1) and two with goats (0)
        doors = [0, 0, 1]
        random.shuffle(doors)

        # Contestant randomly chooses a door
        chosen_door = random.randint(0, 2)

        # Host opens a door with a goat (not the chosen door)
        host_door = next(i for i in range(3) if i != chosen_door and doors[i] == 0)

        # Contestant decides to switch or not
        if doors[chosen_door] == 1:
            wins_without_switch += 1
        else:
            wins_with_switch += 1

    print(f"Simulations: {num_simulations}")
    print(f"Wins with switching: {wins_with_switch}")
    print(f"Wins without switching: {wins_without_switch}")
    print(f"Probability of winning with switching: {wins_with_switch / num_simulations:.2f}")
    print(f"Probability of winning without switching: {wins_without_switch / num_simulations:.2f}")

num_simulations = 10000
monty_hall_simulation(num_simulations)
