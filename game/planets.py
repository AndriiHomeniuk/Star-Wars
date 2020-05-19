import re

FLY_COMMAND = ('Fly', 'fly')
CHOICE_MSG = 'What do you choose? "Fly" or some planet? > '
DELIMITER = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
FLY_AROUND_PLANET_MSG = 'You\'ve flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further!'
WASTING_MSG = 'Hey, Young padavan, do not waste your time! Do something.'
PLANET_DICT = {
	"Geonosis": 1,
	"Felucia": 2,
	"Mustafor": 3,
	"Polis_Massa": 4,
	"Alderaan": 5,
	"Tatooine": 6,
	"Kamino": 7,
	"Utapau": 8,
	"Keshyyk": 9,
	"Corasant": 10,
	"Nabu": 11,
	"Chot": 12,
	"Dagoba": 13,
	"Yavin": 14,
}


def parse_system(message):
	raw_data = re.search(r'systems: (?P<planets>.+). Or', message).group('planets')
	planets = re.sub('or', ',', raw_data).split(',')
	return [planet.strip() for planet in planets]


def wasting_flying():
	print(DELIMITER)
	print(WASTING_MSG)


def flying_around_planet():
	print(DELIMITER)
	print(FLY_AROUND_PLANET_MSG)


def fly_to_planet(planet):
	print(DELIMITER)
	print(f"You fly to {planet} and spend 1 day.")
	return PLANET_DICT[planet]


def planet_template(planet_msg, planet_index, day_counter):
	print(DELIMITER)
	print(planet_msg)
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	if result_of_choice in FLY_COMMAND:
		flying_around_planet()
	elif result_of_choice in parse_system(planet_msg):
		planet_index = fly_to_planet(result_of_choice)
	else:
		wasting_flying()
	return planet_index, day_counter


def geonosis(day_counter):
	planet_msg = "The planet has always been a droid factory. From here you can fly in 3 systems: Felucia, Kamino or Utapau. Or you can fly the planet itself and look here."
	planet_index = 1
	return planet_template(planet_msg, planet_index, day_counter)


def felucia(day_counter):
	planet_msg = "The planet has jungle. From here you can fly in 3 systems: Geonosis, Mustafor or Tatooine. Or you can fly the planet itself and look here."
	planet_index = 2
	return planet_template(planet_msg, planet_index, day_counter)


def mustafor(day_counter):
	planet_msg = "From here you can fly in 2 systems: Felucia, Polis-Massa. Or you can fly the planet itself and look here."
	planet_index = 3
	return planet_template(planet_msg, planet_index, day_counter)


def polis_massa(day_counter):
	planet_msg = "From here you can fly in 4 systems: Yavin, Mustafor, Tatooine, Alderaan. Or you can fly the planet itself and look here."
	planet_index = 4
	return planet_template(planet_msg, planet_index, day_counter)


def alderaan(day_counter):
	planet_msg = "Alderaan has the capital - Aldera. There you can find something interesting. From here you can fly in 3 systems: Polis-Massa, Nabu, Chot. Or you can fly the planet itself and look here."
	planet_index = 5
	return planet_template(planet_msg, planet_index, day_counter)


def tatooine(day_counter):
	planet_msg = "The planet has only desert and nothing else. From here you can fly in 4 systems: Felucia, Polis-Massa, Nabu, Kamino. Or you can fly the planet itself and look here."
	planet_index = 6
	return planet_template(planet_msg, planet_index, day_counter)


def kamino(day_counter):
	planet_msg = "From here you can fly in 5 systems: Geonosis, Tatooine, Utapau, Nabu, Corasant. Or you can fly the planet itself and look here."
	planet_index = 7
	return planet_template(planet_msg, planet_index, day_counter)


def utapau(day_counter):
	planet_msg = "From here you can fly in 3 systems: Geonosis, Kamino, Keshyyk. Or you can fly the planet itself and look here."
	planet_index = 8
	return planet_template(planet_msg, planet_index, day_counter)


def keshyyk(day_counter):
	planet_msg = "The planet has a jungle, where the wookiees live. The capital of planet is Rwookrrorro. From here you can fly in 2 systems: Utapau, Corasant. Or you can fly the planet itself and look here."
	planet_index = 9
	return planet_template(planet_msg, planet_index, day_counter)


def corasant(day_counter):
	planet_msg = "This giant planet-city has a 10 billion people. Here we can see Senat and Temple of the Jedi. From here you can fly in 3 systems: Kamino, Keshyyk, Dagoba. Or you can fly the planet itself and look here."
	planet_index = 10
	return planet_template(planet_msg, planet_index, day_counter)


def nabu(day_counter):
	planet_msg = ("More than 85 percentages of the surface of the planet is covered with waterFrom here you can fly in 5 systems: Chot, Dagoba, Kamino, Tatooine, Alderaan. Or you can fly the planet itself and look here.")
	planet_index = 11
	return planet_template(planet_msg, planet_index, day_counter)


def chot(day_counter):
	planet_msg = "From here you can fly in 2 systems: Nabu, Alderaan. Or you can fly the planet itself and look here."
	planet_index = 12
	return planet_template(planet_msg, planet_index, day_counter)


def dagoba(day_counter):
	planet_msg = "From here you can fly in 2 systems: Nabu, Corasant. Or you can fly the planet itself and look here."
	planet_index = 13
	return planet_template(planet_msg, planet_index, day_counter)


def yavin(day_counter):
	planet_msg = "The planet has a lot of deciduous forests. From here you can fly in 1 systems: Polis-Massa. Or you can fly the planet itself and look here."
	day_counter += 1
	result_of_choice = str(input(CHOICE_MSG))
	planet_index = 14
	print(DELIMITER)
	print(planet_msg)
	if result_of_choice in FLY_COMMAND:
		print(DELIMITER)
		winn()
		planet_index = -1
	elif result_of_choice in parse_system(planet_msg):
		planet_index = fly_to_planet(result_of_choice)
	else:
		wasting_flying()
	return planet_index, day_counter


def winn():
	print('You\'ve flown around the planet. Finally you found some movement.')
	print('Deep in the jungle the scanner noticed the force.')
	print('Yes, yes, this is a Great Master Yoda.')
	print('You are the winner. Congratulations!')
