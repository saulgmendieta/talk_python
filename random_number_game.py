import random

print('------------------------------------------')
print('             GUESS THE PROGRAM')
print('------------------------------------------')

random_number = random.randint(0, 100)
guess_number = -1

while guess_number != random_number:
    guess_number = int(input('Guess a number between 0 and 100: '))
    if guess_number > random_number:
        print('Wrong!! its LOWER than {0}'.format(guess_number))
    elif guess_number < random_number:
        print('Wrong!! its HIGHER than {0}'.format(guess_number))
    else:
        print('You got it, the number is ', random_number)
