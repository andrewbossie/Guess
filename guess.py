#Author: Andrew Bossie

playerName = str(input(("Hello! What is your name?"))
print = ("Well", playerName, "I'm thinking of a number between 1 and 20. You have three chances to figure it out.")

n = int(10)
guess = int(input("Guess a number"))
numAttempts = int(0)
playerAttempts = numAttempts + 1 in range (0,4)

while playerAttempts < 3:
	if guess==n:
		print("WOW", playerName, "you guess corectly on your first attempt!")
		playerAttempts = numAttempts + 1
		done = true

	elif guess<n:
		print(playerName, "your number is too low.")	
		guess = int(input("Guess again!"))
		playerAttempts = numAttempts + 1
		done = false

	efif guess>n:
		print(playerName, "your number is too high.")
		guess = int(input("Guess again!"))
		playerAttempts = numattempts + 1
		done = false

if playerAttempts>3:
	print("Sorry your three guesses are over. The number I was thinking of was", n, ".")		