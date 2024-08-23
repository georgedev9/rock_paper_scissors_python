import os.path
from random import choice

move_list = ['rock', 'paper', 'scissors']
DRAW = 50
WIN = 100


def startGame(user_option, user_rating):

    winning_cases = {
        'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
        'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
        'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
        'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
        'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'lizard', 'spock'],
        'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
        'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
        'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
        'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
        'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
        'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
        'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
        'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'spock'],
        'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
        'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
        "spock": ['lizard', 'scissors'],
        "lizard": ['paper', 'scissors'],
    }

    cp_option = choice(move_list)

    game_state = f'Sorry, but the computer chose {cp_option}'

    if user_option == cp_option:
        game_state = f'There is a draw ({cp_option})'
        user_rating += DRAW

    elif cp_option in winning_cases[user_option]:
        game_state = f'Well done. The computer chose {cp_option} and failed'
        user_rating += WIN

    print(game_state)

    return user_rating


def readRating(user_name):

    user_score = 0

    if os.path.exists('rating.txt'):
        with open('rating.txt', 'r') as text_file:
            for line in text_file:
                if user_name in line:
                    user_score = int(line.split()[1])

    return user_score


def saveRating(user_name, user_rating):

    with open('rating.txt', 'a+') as text_file:
        print(f"{user_name} {user_rating}", file=text_file)


def main():

    user_name = input('Enter your name: ')
    print(f"Hello, {user_name}")

    user_options = input().split(',')
    print("Okay, let's start")

    global move_list
    if len(user_options) > 1:
        move_list = user_options

    user_rating = readRating(user_name)

    while True:

        player_move = input()

        if player_move == '!exit':
            saveRating(user_name, user_rating)
            print('Bye!')
            break
        elif player_move in move_list:
            user_rating = startGame(player_move, user_rating)
        elif player_move == '!rating':
            print(f'Your rating: {user_rating}')
        else:
            print("Invalid input")


if __name__ == '__main__':
    main()