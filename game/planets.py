FLY_COMMAND = ('Fly', 'fly')
CHOICE_MSG = 'What do you choose? "Fly" or some planet? > '
DELIMITER = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
FLY_AROUND_PLANET_MSG = 'You\'ve flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further!'
WASTING_MSG = 'Hey, Young padavan, do not waste your time! Do something.'


def wasting_flying():
	print(DELIMITER)
	print(WASTING_MSG)


def flying_around_planet():
	print(DELIMITER)
	print(FLY_AROUND_PLANET_MSG)


def geonosis(day_counter):
	print(DELIMITER)
	print("The planet has always been a droid factory. From here you can fly in 3 systems: Felucia, Kamino or Utapau. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 1
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Felucia":
		print(DELIMITER)
		print("You fly to Felucia and spend 1 day.")
		planet_index = 2
	elif result_of_choice == "Kamino":
		print(DELIMITER)
		print("You fly to Kamino and spend 1 day.")
		planet_index = 7
	elif result_of_choice == "Utapau":
		print(DELIMITER)
		print("You fly to Utapau and spend 1 day.")
		planet_index = 8
	else:
		wasting_flying()
	return planet_index, day_counter


def felucia(day_counter):
	print(DELIMITER)
	print("The planet has jungle. From here you can fly in 3 systems: Geonosis, Mustafor or Tatooine. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 2
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Geonosis":
		print(DELIMITER)
		print("You fly to Geonosis and spend 1 day.")
		planet_index = 1 
	elif result_of_choice == "Mustafor":
		print(DELIMITER)
		print("You fly to Mustafor and spend 1 day.")
		planet_index = 3
	elif result_of_choice == "Tatooine":
		print(DELIMITER)
		print("You fly to Tatooine and spend 1 day.")
		planet_index = 6
	else:
		wasting_flying()
	return planet_index, day_counter


def mustafor(day_counter):
	print(DELIMITER)
	print("From here you can fly in 2 systems: Felucia, Polis-Massa. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 3
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Felucia":
		print(DELIMITER)
		print("You fly to Felucia and spend 1 day.")
		planet_index = 2
	elif result_of_choice == "Polis-Massa":
		print(DELIMITER)
		print("You fly to Polis-Massa and spend 1 day.")
		planet_index = 4
	else:
		wasting_flying()
	return planet_index, day_counter


def polis_massa(day_counter):
	print(DELIMITER)
	print("From here you can fly in 4 systems: Yavin, Mustafor, Tatooine, Alderaan. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 4
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Yavin":
		print(DELIMITER)
		print("You fly to Yavin and spend 1 day.")
		planet_index = 14 
	elif result_of_choice == "Mustafor":
		print(DELIMITER)
		print("You fly to Mustafor and spend 1 day.")
		planet_index = 3
	elif result_of_choice == "Tatooine":
		print(DELIMITER)
		print("You fly to Tatooine and spend 1 day.")
		planet_index = 6
	elif result_of_choice == "Alderaan":
		print(DELIMITER)
		print("You fly to Alderaan and spend 1 day.")
		planet_index = 5
	else:
		wasting_flying()
	return planet_index, day_counter


def alderaan(day_counter):
	print(DELIMITER)
	print("Alderaan has the capital - Aldera. There you can find something interesting. From here you can fly in 3 systems: Polis-Massa, Nabu, Chot. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 5
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Polis-Massa":
		print(DELIMITER)
		print("You fly to Polis-Massa and spend 1 day.")
		planet_index = 4
	elif result_of_choice == "Nabu":
		print(DELIMITER)
		print("You fly to Nabu and spend 1 day.")
		planet_index = 11
	elif result_of_choice == "Chot":
		print(DELIMITER)
		print("You fly to Chot and spend 1 day.")
		planet_index = 12
	else:
		wasting_flying()
	return planet_index, day_counter


def tatooine(day_counter):
	print(DELIMITER)
	print("The planet has only desert and nothing else. From here you can fly in 4 systems: Felucia, Polis-Massa, Nabu, Kamino. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 6
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Felucia":
		print(DELIMITER)
		print("You fly to Felucia and spend 1 day.")
		planet_index = 2
	elif result_of_choice == "Polis-Massa":
		print(DELIMITER)
		print("You fly to Polis-Massa and spend 1 day.")
		planet_index = 4
	elif result_of_choice == "Nabu":
		print(DELIMITER)
		print("You fly to Nabu and spend 1 day.")
		planet_index = 11
	elif result_of_choice == "Kamino":
		print(DELIMITER)
		print("You fly to Kamino and spend 1 day.")
		planet_index = 7
	else:
		wasting_flying()
	return planet_index, day_counter


def kamino(day_counter):
	print(DELIMITER)
	print("From here you can fly in 5 systems: Geonosis, Tatooine, Utapau, Nabu, Corasant. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 7
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Geonosis":
		print(DELIMITER)
		print("You fly to Geonosis and spend 1 day.")
		planet_index = 1 
	elif result_of_choice == "Utapau":
		print(DELIMITER)
		print("You fly to Utapau and spend 1 day.")
		planet_index = 8
	elif result_of_choice == "Tatooine":
		print(DELIMITER)
		print("You fly to Tatooine and spend 1 day.")
		planet_index = 6
	elif result_of_choice == "Nabu":
		print(DELIMITER)
		print("You fly to Nabu and spend 1 day.")
		planet_index = 11
	elif result_of_choice == "Corasant":
		print(DELIMITER)
		print("You fly to Corasant and spend 1 day.")
		planet_index = 10
	else:
		wasting_flying()
	return planet_index, day_counter


def utapau(day_counter):
	print(DELIMITER)
	print("From here you can fly in 3 systems: Geonosis, Kamino, Keshyyk. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 8
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Geonosis":
		print(DELIMITER)
		print("You fly to Geonosis and spend 1 day.")
		planet_index = 1 
	elif result_of_choice == "Kamino":
		print(DELIMITER)
		print("You fly to Kamino and spend 1 day.")
		planet_index = 7
	elif result_of_choice == "Keshyyk":
		print(DELIMITER)
		print("You fly to Keshyyk and spend 1 day.")
		planet_index = 9
	else:
		wasting_flying()
	return planet_index, day_counter


def keshyyk(day_counter):
	print(DELIMITER)
	print("The planet has a jungle, where the wookiees live. The capital of planet is Rwookrrorro. From here you can fly in 2 systems: Utapau, Corasant. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 9
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Utapau":
		print(DELIMITER)
		print("You fly to Utapau and spend 1 day.")
		planet_index = 8
	elif result_of_choice == "Corasant":
		print(DELIMITER)
		print("You fly to Corasant and spend 1 day.")
		planet_index = 10
	else:
		wasting_flying()
	return planet_index, day_counter


def corasant(day_counter):
	print(DELIMITER)
	print("This giant planet-city has a 10 billion people. Here we can see Senat and Temple of the Jedi. From here you can fly in 3 systems: Kamino, Keshyyk, Dagoba. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 10
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Kamino":
		print(DELIMITER)
		print("You fly to Kamino and spend 1 day.")
		planet_index = 7
	elif result_of_choice == "Keshyyk":
		print(DELIMITER)
		print("You fly to Keshyyk and spend 1 day.")
		planet_index = 9
	elif result_of_choice == "Dagoba":
		print(DELIMITER)
		print("You fly to Dagoba and spend 1 day.")
		planet_index = 13
	else:
		wasting_flying()
	return planet_index, day_counter


def nabu(day_counter):
	print(DELIMITER)
	print("More than 85 percentages of the surface of the planet is covered with waterFrom here you can fly in 5 systems: Chot, Dagoba, Kamino, Tatooine, Alderaan. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 11
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Chot":
		print(DELIMITER)
		print("You fly to Chot and spend 1 day.")
		planet_index = 12
	elif result_of_choice == "Dagoba":
		print(DELIMITER)
		print("You fly to Dagoba and spend 1 day.")
		planet_index = 13
	elif result_of_choice == "Tatooine":
		print(DELIMITER)
		print("You fly to Tatooine and spend 1 day.")
		planet_index = 6
	elif result_of_choice == "Kamino":
		print(DELIMITER)
		print("You fly to Kamino and spend 1 day.")
		planet_index = 7
	elif result_of_choice == "Alderaan":
		print(DELIMITER)
		print("You fly to Alderaan and spend 1 day.")
		planet_index = 5
	else:
		wasting_flying()
	return planet_index, day_counter


def chot(day_counter):
	print(DELIMITER)
	print("From here you can fly in 2 systems: Nabu, Alderaan. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 12
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Alderaan":
		print(DELIMITER)
		print("You fly to Alderaan and spend 1 day.")
		planet_index = 5
	elif result_of_choice == "Nabu":
		print(DELIMITER)
		print("You fly to Nabu and spend 1 day.")
		planet_index = 11
	else:
		wasting_flying()
	return planet_index, day_counter


def dagoba(day_counter):
	print(DELIMITER)
	print("From here you can fly in 2 systems: Nabu, Corasant. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 13
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice == "Nabu":
		print(DELIMITER)
		print("You fly to Nabu and spend 1 day.")
		planet_index = 11
	elif result_of_choice == "Corasant":
		print(DELIMITER)
		print("You fly to Corasant and spend 1 day.")
		planet_index = 10
	else:
		wasting_flying()
	return planet_index, day_counter


def yavin(day_counter):
	print(DELIMITER)
	print("The planet has a lot of deciduous forests. From here you can fly in 1 systems: Polis-Massa. Or you can fly the planet itself and look here.")
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 14
	if result_of_choice in FLY_COMMAND:
		print(DELIMITER)
		winn()
		planet_index = -1  # winn()
	elif result_of_choice == "Polis-Massa":
		print(DELIMITER)
		print("You fly to Polis-Massa and spend 1 day.")
		planet_index = 4
	else:
		wasting_flying()
	return planet_index, day_counter


def winn():
	print('You\'ve flown around the planet. Finally you found some movement.')
	print('Deep in the jungle the scanner noticed the force.')
	print('Yes, yes, this is a Great Master Yoda.')
	print('You are the winner. Congratulations!')
