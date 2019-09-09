from terminal_ascii import welcome_message


class UserInput:

    def yesno_question(self):
        self.response = input('Please enter Yes or No here: ')
        if self.response == 'Yes':
            print('Hurray')
        else:
            print('That is not an accetable response, please try again')
            self.yesno_question()


class InfOutput:

    def animal_info(self, animal_stats: list):
        for stats in animal_stats:
            print('''Name: {name} \nHealth: {health}%\nType: {animal_type}
            '''.format(name=stats['name'], health=stats['health'], animal_type=stats['type']))
