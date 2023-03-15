import random

def guess_number():
    number = random.randint(1, 100)
    print('I am thinking of a number between 1 and 100.')
    num_of_guesses = 0
    while True:
        guess = input('Guess the number: ')
        num_of_guesses += 1
        try:
            guess = int(guess)
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 100.')
            continue
        if guess < 1 or guess > 100:
            print('Number out of range. Please enter a number between 1 and 100.')
        elif guess < number:
            print('Too low. Guess again.')
        elif guess > number:
            print('Too high. Guess again.')
        else:
            print(f'Congratulations! You guessed the number in {num_of_guesses} guesses.')
            break

play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    guess_number()
    play_again = input('Do you want to play again? Enter Yes or No: ').lower()
