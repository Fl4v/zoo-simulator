from terminal_ascii import welcome_message


class UserInput:

    def ask_question(self):
        print(welcome_message)
        self.response = input('Please enter Yes or No here: ')
        if self.response == 'Yes':
            print('Hurray')
