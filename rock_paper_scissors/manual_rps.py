import random
from camera_rps import rock_paper_scissors_model

class Hangman:
    def __init__(self) -> None:
        self.computer_wins = 0
        self.user_wins = 0
        self.model = rock_paper_scissors_model()

    def get_computer_choice(self)->str:
        return random.choice(['rock','paper','scissors'])

    '''
    Gets user's choice by taking the output of the model which has the largest probability
    '''

    def get_usr_choice(self)-> str:
        prediction = self.model.get_user_prediction()
        return self.model.get_prediction(prediction)
    
    '''
    Gets the winner by following the usual definitions of the game 
    '''
    def get_winner(self,computer_choice:str,user_choice:str)->str:
        winner_dict = {'rock':'paper','scissors':'rock','paper':'scissors','None':'None'}
    
        victor_vs_computer = winner_dict[computer_choice]
        victor_vs_user = winner_dict[user_choice]
        if victor_vs_computer == user_choice:
            print('User wins')
            return 1,0
    
        elif victor_vs_user == computer_choice:
            print('Computer wins')
            return 0,1

        else:
            print(f'Nobody won, user chose {user_choice} and computer chose {computer_choice}')
            return 0,0

    '''
    Plays the game between the user and the computer
    '''
    def play(self)->None:
        keep_going = True
        while(keep_going):
            computer_choice = self.get_computer_choice()
            print('Hold your move to the camera')
            user_choice = self.get_usr_choice()
            user_won,computer_won = self.get_winner(computer_choice=computer_choice,user_choice=user_choice)
            self.user_wins += user_won
            self.computer_wins += computer_won
            if (self.computer_wins == 3) or (self.user_wins == 3):
                keep_going = False
