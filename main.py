# This is guess the number game
from random import randint

# generate random number between 1 to 20
random_number = randint(1, 20)

print('Guess a number between 1 to 20.')
# Ask player to take guesses 6 times
for guess_number in range(1, 7):
    guess = int(input('Enter a guess: '))
    if guess > random_number:
        print('guess is too high.')
    elif guess < random_number:
        print('guess is too low.')
    else:
        # the mean the guess is correct
        break

if guess == random_number:
    print(f'Correct guess, you guessef the number in {guess_number} guesses')
else:
    print(f'Try again, the random number was {random_number}')