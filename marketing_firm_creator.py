from sweepstakes_queue_manager import SweepstakesQueueManager
from sweepstakes_stack_manager import SweepstakesStackManager


class MarketingFirmCreator:
    def __init__(self):
        self.option = None
        self.choice = None

    def choose_manager(self):
        self.option = input("Please enter which type of manager you would like to use, enter 'stack' or 'queue': ")

        if self.option == 'stack':
            self.choice = SweepstakesStackManager()
        elif self.option == 'queue':
            self.choice = SweepstakesQueueManager()
