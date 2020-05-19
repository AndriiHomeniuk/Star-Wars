from game.planets import *
from game.messages import *


def print_today_counter(day):
	print(f'Today is {day} day of your trip')


def main_logic():
	day_counter = 0
	planet_index = 1

	while True:
		if planet_index == -1:
			break

		if day_counter == 20:
			print('You lose. The empire struck back!')
			break

		elif planet_index == 1:
			result = geonosis(day_counter)
		elif planet_index == 2:
			result = felucia(day_counter)
		elif planet_index == 3:
			result = mustafor(day_counter)
		elif planet_index == 4:
			result = polis_massa(day_counter)
		elif planet_index == 5:
			result = alderaan(day_counter)
		elif planet_index == 6:
			result = tatooine(day_counter)
		elif planet_index == 7:
			result = kamino(day_counter)
		elif planet_index == 8:
			result = utapau(day_counter)
		elif planet_index == 9:
			result = keshyyk(day_counter)
		elif planet_index == 10:
			result = corasant(day_counter)
		elif planet_index == 11:
			result = nabu(day_counter)
		elif planet_index == 12:
			result = chot(day_counter)
		elif planet_index == 13:
			result = dagoba(day_counter)
		elif planet_index == 14:
			result = yavin(day_counter)
		planet_index, day_counter = result
		print_today_counter(day_counter)


# winn = -1

# Planets:
# Geonosis = 1
# Felucia = 2
# Mustafor = 3
# Polis_Massa = 4
# Alderaan = 5
# Tatooine = 6
# Kamino = 7
# Utapau = 8
# Keshyyk = 9
# Corasant = 10
# Nabu = 11
# Chot = 12
# Dagoba = 13
# Yavin = 14

if __name__ == '__main__':
	introduction()
	main_logic()
	final_msg()
