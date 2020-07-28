'''
Monty Hall Simulation in Python
as in: https://en.wikipedia.org/wiki/Monty_Hall_problem.

Particular implementation by Joel Stremmel
and licensed under the MIT license on July 28th, 2020.
'''

import random 
import numpy as np

def simulate(switch, n_doors):

	# create doors numbered 1 to the number of doors
	doors = list(range(1, n_doors + 1))

	# randomly select the door that has the car, the players door, and the door revealed by Monty
	# note that Monty only reveals a door which is known to not contain the car
	door_with_car = random.choice(doors)
	door_selected_by_player = random.choice(doors)
	door_opened_by_monty = random.choice([door for door in doors if door not in [door_with_car, door_selected_by_player]])

	# apply switching strategy
	if switch:
		new_door_selected_by_player = random.choice([door for door in doors if door not in [door_selected_by_player, door_opened_by_monty]])

	# apply keeping strategy
	else:
		new_door_selected_by_player = door_selected_by_player

	# return a win as 1 and loss as 0
	return int(new_door_selected_by_player == door_with_car)

if __name__ == '__main__':

	SWITCH = True
	N_DOORS = 3
	N_SIMULATIONS = 10000

	results = [simulate(SWITCH, N_DOORS) for _ in range(N_SIMULATIONS)]
	win_pct = round(np.mean(results), 5) * 100.0

	print(f'Win percentage with {N_DOORS} doors, {N_SIMULATIONS} simulations, and SWITCH={SWITCH}: {win_pct}%.')

