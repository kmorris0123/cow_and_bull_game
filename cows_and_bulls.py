import random
import os


def user_guess():

	#this function asks the user for their guess

	print("Guess a 4 digit number:")
	usr_in = input("--> ")
	seperate = []
	for digit in str(usr_in):
		seperate.append(int(digit))
	return seperate


def random_num():

	#this function generates the random ints

	rand_list = []
	for i in range(1,5):
		digit = random.randint(0,9)
		rand_list.append(digit)
	
	return rand_list

def check(digits,rand_nums):

	#this function checks the digits and will print the number of cows and bulls in their guess
	
	cow_bull = []
	cow = 0
	bull = 0

	#this compares the digits

	if digits[0] == rand_nums[0]:
		cow += 1

	else: 
		bull += 1

	if digits[1] == rand_nums[1]:
		cow += 1

	else: 
		bull += 1

	if digits[2] == rand_nums[2]:
		cow += 1

	else: 
		bull += 1

	if digits[3] == rand_nums[3]:
		cow += 1

	else: 
		bull += 1

	#this prints the count of the bulls and cows
	
	if cow == 1 and bull == 1:
		print(str(cow)+" cow, "+str(bull)+" bull")

	elif cow == 1 and bull != 1:
		print(str(cow)+" cow, "+str(bull)+" bulls")

	elif cow != 1 and bull == 1:
		print(str(cow)+" cows, "+str(bull)+" bull")

	else:

		print(str(cow)+" cows, "+str(bull)+" bulls")
	return cow

def main():
	amout_played = 0
	play = True
	print("This will print all of the story headings from a section of the New York Times website.")
	random = random_num()
	while play == True:
		print("")
		amout_played += 1
		guess = user_guess()
		checker = check(guess,random)
		if checker == 4:
			print("You have won!")
			print(amout_played)

			play = False

if __name__ == '__main__':
	main()