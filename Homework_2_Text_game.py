# flying the planet
flying = ["Fly", "fly"]

# planets_func
def Geonosis():
	global count
	print("The planet has always been a droid factory. From here you can fly in 3 systems: Felucia, Kamino or Utapau. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 1 # Geonosis
	elif ch1 == "Felucia":
		print ("You fly to Felucia and spend 1 day.")
		count += 1
		return 2 # Felucia()
	elif ch1 == "Kamino":
		print ("You fly to Kamino and spend 1 day.")
		count += 1
		return 7 # Kamino()
	elif ch1 == "Utapau":
		print ("You fly to Utapau and spend 1 day.")
		count += 1
		return 8 # Utapau()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 1 # Geonosis()

def Felucia():
	global count
	print("The planet has jungle.\
		From here you can fly in 3 systems: Geonosis, Mustafor or Tatooine. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 2 # Felucia()
	elif ch1 == "Geonosis":
		print ("You fly to Geonosis and spend 1 day.")
		count += 1
		return 1 # Geonosis()
	elif ch1 == "Mustafor":
		print ("You fly to Mustafor and spend 1 day.")
		count += 1
		return 3 # Mustafor()
	elif ch1 == "Tatooine":
		print ("You fly to Tatooine and spend 1 day.")
		count += 1
		return 6 # Tatooine()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 2 # Felucia()

def Mustafor():
	global count
	print("From here you can fly in 2 systems: Felucia, Polis_Massa. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 3 # Mustafor()
	elif ch1 == "Felucia":
		print ("You fly to Felucia and spend 1 day.")
		count += 1
		return 2 # Felucia()
	elif ch1 == "Polis_Massa":
		print ("You fly to Polis_Massa and spend 1 day.")
		count += 1
		return 4 # Polis_Massa()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 3 # Mustafor()

def Polis_Massa():
	global count
	print("From here you can fly in 4 systems: Yavin, Mustafor, Tatooine, Alderaan. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 4 # Polis_Massa()
	elif ch1 == "Yavin":
		print ("You fly to Yavin and spend 1 day.")
		count += 1
		return 14 # Yavin()
	elif ch1 == "Mustafor":
		print ("You fly to Mustafor and spend 1 day.")
		count += 1
		return 3 # Mustafor()
	elif ch1 == "Tatooine":
		print ("You fly to Tatooine and spend 1 day.")
		count += 1
		return 6 # Tatooine()
	elif ch1 == "Alderaan":
		print ("You fly to Alderaan and spend 1 day.")
		count += 1
		return 5 # Alderaan()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 4 # Polis_Massa()

def Alderaan():
	global count
	print("From here you can fly in 3 systems: Polis_Massa, Nabu, Chot. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 5 # Alderaan()
	elif ch1 == "Polis_Massa":
		print ("You fly to Polis_Massa and spend 1 day.")
		count += 1
		return 4 # Polis_Massa()
	elif ch1 == "Nabu":
		print ("You fly to Nabu and spend 1 day.")
		count += 1
		return 11 # Nabu()
	elif ch1 == "Chot":
		print ("You fly to Chot and spend 1 day.")
		count += 1
		return 12 # Chot()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 5 # Alderaan()

def Tatooine():
	global count
	print("From here you can fly in 4 systems: Felucia, Polis_Massa, Nabu, Kamino. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 6 # Tatooine()
	elif ch1 == "Felucia":
		print ("You fly to Felucia and spend 1 day.")
		count += 1
		return 2 # Felucia()
	elif ch1 == "Polis_Massa":
		print ("You fly to Polis_Massa and spend 1 day.")
		count += 1
		return 4 # Polis_Massa()
	elif ch1 == "Nabu":
		print ("You fly to Nabu and spend 1 day.")
		count += 1
		return 11 # Nabu()
	elif ch1 == "Kamino":
		print ("You fly to Kamino and spend 1 day.")
		count += 1
		return 7 # Kamino()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 6 # Tatooine()

def Kamino():
	global count
	print("From here you can fly in 5 systems: Geonosis, Tatooine, Utapau, Nabu, Corasant. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 7 # Kamino()
	elif ch1 == "Geonosis":
		print ("You fly to Geonosis and spend 1 day.")
		count += 1
		return 1 # Geonosis()
	elif ch1 == "Utapau":
		print ("You fly to Utapau and spend 1 day.")
		count += 1
		return 8 # Utapau()
	elif ch1 == "Tatooine":
		print ("You fly to Tatooine and spend 1 day.")
		count += 1
		return 6 # Tatooine()
	elif ch1 == "Nabu":
		print ("You fly to Nabu and spend 1 day.")
		count += 1
		return 11 # Nabu()
	elif ch1 == "Corasant":
		print ("You fly to Corasant and spend 1 day.")
		count += 1
		return 10 # Corasant()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 7 # Kamino()

def Utapau():
	global count
	print("From here you can fly in 3 systems: Geonosis, Kamino, Keshyyk. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 8 # Utapau()
	elif ch1 == "Geonosis":
		print ("You fly to Geonosis and spend 1 day.")
		count += 1
		return 1 # Geonosis()
	elif ch1 == "Kamino":
		print ("You fly to Kamino and spend 1 day.")
		count += 1
		return 7 # Kamino()
	elif ch1 == "Keshyyk":
		print ("You fly to Keshyyk and spend 1 day.")
		count += 1
		return 9 # Keshyyk()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 8 # Utapau()

def Keshyyk():
	global count
	print("From here you can fly in 2 systems: Utapau, Corasant. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 9 # Keshyyk()
	elif ch1 == "Utapau":
		print ("You fly to Utapau and spend 1 day.")
		count += 1
		return 8 # Utapau()
	elif ch1 == "Corasant":
		print ("You fly to Corasant and spend 1 day.")
		count += 1
		return 10 # Corasant()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 9 # Keshyyk()

def Corasant():
	global count
	print("From here you can fly in 3 systems: Kamino, Keshyyk, Dagoba. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 10 # Corasant()
	elif ch1 == "Kamino":
		print ("You fly to Kamino and spend 1 day.")
		count += 1
		return 7 # Kamino()
	elif ch1 == "Keshyyk":
		print ("You fly to Keshyyk and spend 1 day.")
		count += 1
		return 9 # Keshyyk()
	elif ch1 == "Dagoba":
		print ("You fly to Dagoba and spend 1 day.")
		count += 1
		return 13 # Dagoba()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 10 # Corasant()

def Nabu():
	global count
	print("From here you can fly in 5 systems: Chot, Dagoba, Kamino, Tatooine, Alderaan. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 11 # Nabu()
	elif ch1 == "Chot":
		print ("You fly to Chot and spend 1 day.")
		count += 1
		return 12 # Chot()
	elif ch1 == "Dagoba":
		print ("You fly to Dagoba and spend 1 day.")
		count += 1
		return 13 # Dagoba()
	elif ch1 == "Tatooine":
		print ("You fly to Tatooine and spend 1 day.")
		count += 1
		return 6 # Tatooine()
	elif ch1 == "Kamino":
		print ("You fly to Kamino and spend 1 day.")
		count += 1
		return 7 # Kamino()
	elif ch1 == "Alderaan":
		print ("You fly to Alderaan and spend 1 day.")
		count += 1
		return 5 # Alderaan()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 11 # Nabu()

def Chot():
	global count
	print("From here you can fly in 2 systems: Nabu, Alderaan. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 12 # Chot()
	elif ch1 == "Alderaan":
		print ("You fly to Alderaan and spend 1 day.")
		count += 1
		return 5 # Alderaan()
	elif ch1 == "Nabu":
		print ("You fly to Nabu and spend 1 day.")
		count += 1
		return 11 # Nabu()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 12 # Chot()

def Dagoba():
	global count
	print("From here you can fly in 2 systems: Nabu, Corasant. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		print("You've flown around the planet. Unfortunately, there is almost no life, except for local primitive animals. You spent 1 day. Look further.")
		count += 1
		return 13 # Dagoba()
	elif ch1 == "Nabu":
		print ("You fly to Nabu and spend 1 day.")
		count += 1
		return 11 # Nabu()
	elif ch1 == "Corasant":
		print ("You fly to Corasant and spend 1 day.")
		count += 1
		return 10 # Corasant()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		return 13 #Dagoba()

def Yavin():
	global count
	print("From here you can fly in 1 systems: Polis_Massa. Or you can fly the planet itself and look here.")
	ch1 = str(input("What do you choose? > "))
	if ch1 in flying:
		winn()
		return -1 # winn()
	elif ch1 == "Polis_Massa":
		print ("You fly to Polis_Massa and spend 1 day.")
		count += 1
		return 4 # Polis_Massa()
	else:
		print("Hey, Young padavan, do not waste your time! Do something.")
		Yavin()

# winn_func
def winn():
	print("You've flown around the planet. Finally you found some movement.") 
	print("Deep in the jungle the scanner noticed the force.")
	print("Yes, yes, this is a Great Master Yoda.")
	print("You are the winner. Congratulations!")

#introduction
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~Welcome to the world of Star Wars~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print ("~~~~~~~~~~~~~~~~~~~~Luke Skywalker has returned to his home planet of Tatooine~~~~~~~~~~~~~~~~~~~~")
print ("in an attempt to rescue his friend Han Solo from the clutches of the vile gangster Jabba the Hutt.")
print ("~~~~~~~~~~Little does Luke know that the GALACTIC EMPIRE has secretly begun construction~~~~~~~~~~")
print ("~~~~~~~on a new armored space station even more powerful than the first dreaded Death Star.~~~~~~~")
print ("~~~~~When completed, this ultimate weapon will spell certain doom for the small band of rebels~~~~") 
print ("~~~~~~~~~~~~~~~~~~~~~~~~struggling to restore freedom to the galaxy...~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print ("You are on the planet Geonosis. In order to save the galaxy, you need to find the master of Yoda.")
print ("But nobody knows where he is. So you will have to fly all the systems and ask everyone who can know where the great master is.")
print ("And do not hesitate. There is very little time. You need to make it to May 4th. So, you have 20 days.")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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

# game
count = 0
go_to = 1
while True:
	if go_to == -1:
		break
	if count == 20:
		print("You lose. The empire struck back!")
		break
	elif go_to == 1:
		go_to = Geonosis()
		print ("Today is ", count, "day of your trip")
	elif go_to == 2:
		go_to = Felucia()
		print ("Today is ", count, "day of your trip")
	elif go_to == 3:
		go_to = Mustafor()
		print ("Today is ", count, "day of your trip")
	elif go_to == 4:
		go_to = Polis_Massa()
		print ("Today is ", count, "day of your trip")
	elif go_to == 5:
		go_to = Alderaan()
		print ("Today is ", count, "day of your trip")
	elif go_to == 6:
		go_to = Tatooine()
		print ("Today is ", count, "day of your trip")
	elif go_to == 7:
		go_to = Kamino()
		print ("Today is ", count, "day of your trip")
	elif go_to == 8:
		go_to = Utapau()
		print ("Today is ", count, "day of your trip")
	elif go_to == 9:
		go_to = Keshyyk()
		print ("Today is ", count, "day of your trip")
	elif go_to == 10:
		go_to = Corasant()
		print ("Today is ", count, "day of your trip")
	elif go_to == 11:
		go_to = Nabu()
		print ("Today is ", count, "day of your trip")
	elif go_to == 12:
		go_to = Chot()
		print ("Today is ", count, "day of your trip")
	elif go_to == 13:
		go_to = Dagoba()
		print ("Today is ", count, "day of your trip")
	elif go_to == 14:
		go_to = Yavin()
		print ("Today is ", count, "day of your trip")

#finish
print("May the force be with you.")