import random
from replit import clear
from art import logo

def difficulty():
	attempts = 0 
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard:' ")
	if difficulty == "easy":
		attempts = 10
		return attempts
	elif difficulty == "hard":
		attempts = 5
		return attempts


def game():
	print(logo)
	print("Welcome to the Number Guessing Game!\nI'm thinking 🤔 of a number between 1 and 100.")
	number = random.randint(1, 100)
	attempts = difficulty()
	while attempts > 0:
		print(f"You have {attempts}, attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		if guess == number:
			print(f"You win the corect number was 🤗{number}")
			break
		elif guess > number:
			print("Too high.\nGuess Again.😲")
			attempts -= 1
		elif guess < number:
			print("Too low.\nGuess again.😲")
			attempts -= 1
	if attempts == 0:
		print(f"You are out of attempts the correct answer was {number} 🙃")
	go_again = input("Do you want to play again? y / n : ")
	if go_again == "y":
		clear()
		game()

game()


		