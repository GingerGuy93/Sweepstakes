from contestant import Contestant


class UserInterface:
    def __init__(self):
        pass

    def new_contestant(self):
        registration_num = int(input("Please Enter a registration Number:"))
        first_name = input("Please enter your first name:")
        last_name = input("Please enter your last name:")
        email = input("Please enter your email address:")
        added_user = Contestant(registration_num, first_name, last_name, email)
        return added_user


