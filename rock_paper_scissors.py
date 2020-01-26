from random import randint

options = ['rock', 'paper', 'scissors']

comp_choice = options[randint(0, 2)]

player_choice = False

while player_choice == False:

    player_choice = input('Rock, Paper, Scissors? ')
    if player_choice == comp_choice:
        print('Tie', comp_choice, '=', player_choice)
    elif player_choice == 'rock':
        if comp_choice == 'paper':
            print('You lose',  comp_choice,  'covers', player_choice)
        else:
            print('You Win', player_choice, 'smashes', comp_choice)
    elif player_choice == 'paper':
        if comp_choice == 'scissors':
            print('You lose', comp_choice, 'cuts', player_choice)
        else:
            print('You win', player_choice, 'covers', comp_choice)
    elif player_choice == 'scissors':
        if comp_choice == 'rock':
            print('You lose', comp_choice, 'smashes', player_choice)
        else:
            print('You win', player_choice, 'cuts', comp_choice)
    else:
        print("That's not a valid choice.")

    player_choice = False
    comp_choice = options[randint(0, 2)]