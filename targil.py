import random
def get_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def get_user_guess(min_num, max_num):
    while True:
        user_guess = int(input('Guess a number between 1 and 100: '))
        if user_guess >= min_num or user_guess <= max_num:
            return user_guess
        print('number not in range')

def get_game_message(user_guess, random_number):
    if user_guess > random_number:
        return 'guesse lower'
    return 'guesse higher'