import random

def guess_game(x):
    rndm = random.randint(1,x)
    guess = 0
    while guess != rndm:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < rndm:
            print('Sorry! too low.')
        elif guess > rndm:
            print('Sorry! too high')
        else:
            print(f'Yay! you guess the number {rndm} correctly!')
guess_game(10)

# def guess_game(x):
#     rndm = random.randint(1,x)
#     guess = 0
#     while 1 != 0:
#         guess = int(input(f'Guess a number between 1 and {x}: '))
#         if guess < rndm:
#             print('Sorry! too low.')
#         elif guess > rndm:
#             print('Sorry! too high')
#         else:
#             print(f'Yay! you guess the number {rndm} correctly!')
# guess_game(10)