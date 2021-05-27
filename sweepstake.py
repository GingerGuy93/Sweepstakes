from user_interface import UserInterface
import random


class Sweepstake:
    def __init__(self):
        self.contest_name = None
        self.contestants = {}
        self.user_interface = UserInterface()

    def name_sweepstakes(self):
        self.contest_name = input('Please enter the name of your sweepstakes: ')

    def register_contestant(self, contestant):
        self.contestants.update({f'{contestant.registration_num}': contestant})

    def pick_winner(self, contestant):
        selected_winner = random.choice(list(contestant.registration_num.keys))
        return selected_winner

    def print_contestant_info(self, contestant, selected_winner):
        if contestant == selected_winner:
            print("Congrats You are the winner of the sweepstakes!")
        else:
            print(f"Lets give a big shoutout to {selected_winner} for winning this sweepstakes prize! Good luck next time!")


