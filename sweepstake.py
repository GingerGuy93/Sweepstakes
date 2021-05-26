from user_interface import UserInterface
import random


class Sweepstake:
    def __init__(self, name):
        self.contest_name = name
        self.contestants = {}
        self.user_interface = UserInterface()

    def register_contestant(self, contestant):
        self.contestants.update({f'{contestant.registration_num}': contestant})

    def pick_winner(self, contestant):
        selected_winner = random.choice(list(contestant.registration_num))
        return selected_winner

    def print_contestant_info(self, contestant):
        pass


