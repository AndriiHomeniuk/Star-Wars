from game.planets import *


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
	# introduction
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome to the world of Star Wars~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~Luke Skywalker has returned to his home planet of Tatooine~~~~~~~~~~~~~~~~~~~~')
	print('in an attempt to rescue his friend Han Solo from the clutches of the vile gangster Jabba the Hutt.')
	print('~~~~~~~~~~Little does Luke know that the GALACTIC EMPIRE has secretly begun construction~~~~~~~~~~')
	print('~~~~~~~on a new armored space station even more powerful than the first dreaded Death Star.~~~~~~~')
	print('~~~~~When completed, this ultimate weapon will spell certain doom for the small band of rebels~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~struggling to restore freedom to the galaxy...~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~You are on the planet Geonosis.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~~~~~~~~~~~~~~~In order to save the galaxy, you need to find the master of Yoda.~~~~~~~~~~~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~But nobody knows where he is.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~So you will have to fly all the systems and ask everyone who can know where the great master is.~')
	print('~~~~~~~~~~And do not hesitate. There is very little time. You need to make it to May 4th.~~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~So, you have 20 days.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

	main_logic()
	
	# finish
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~May the force be with you.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
