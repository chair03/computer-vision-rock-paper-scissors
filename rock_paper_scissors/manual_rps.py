import imp


import random

def get_computer_choice()->str:
    return random.choice(['rock','paper','scissors'])

def get_usr_choice()-> str:
    return input('Enter your choice: ')

def get_winner(computer_choice:str,user_choice:str)->str:
    winner_dict = {'rock':'paper','scissors':'rock','paper':'scissors'}
    
    victor_vs_computer = winner_dict[computer_choice]
    victor_vs_user = winner_dict[user_choice]

    if victor_vs_computer == user_choice:
        print('User wins')
    
    elif victor_vs_user == computer_choice:
        print('Computer wins')

    else:
        print(f'Nobody won, user chose {user_choice} and computer chose {computer_choice}')

def play():

    computer_choice = get_computer_choice()
    user_choice = get_usr_choice()
    get_winner(computer_choice=computer_choice,user_choice=user_choice)
