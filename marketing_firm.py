from user_interface import UserInterface
from marketing_firm_creator import MarketingFirmCreator
from sweepstake import Sweepstake


class MarketingFirm:
    def __init__(self, manager):
        self.manager = manager
        self.user_interface = UserInterface()

    def create_sweepstakes(self):
        self.manager = MarketingFirmCreator()
        self.manager.insert(Sweepstake())
        # I used dependency here for after the user chooses their choice of stack or queue the sweepstake
        # function gets passed through that manager.



