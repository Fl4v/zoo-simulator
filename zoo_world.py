from zoo_animals import Elephant, Monkey, Giraffe
from random_no_generator import hunger, feeding
from terminal_ascii import welcome_sign, welcome_message
from animals_stats import AnimalInfoArray
from terminal_input import UserInput


class World:

    total_animals = 5

    elephant = Elephant()
    monkey = Monkey()
    giraffe = Giraffe()

    animal_info_array = AnimalInfoArray()
    user_input = UserInput()

    elephants_stats = []
    monkeys_stats = []
    giraffes_stats = []

    def __init__(self):
        '''for elephant in range(self.total_animals):
            print(self.elephant.health - hunger())'''

        # Create animals arrays to store animals information

        self.animal_info_array.create_array(self.total_animals, self.elephants_stats, self.elephant)
        self.animal_info_array.create_array(self.total_animals, self.monkeys_stats, self.monkey)
        self.animal_info_array.create_array(self.total_animals, self.giraffes_stats, self.giraffe)

        self.user_input.ask_question()


if __name__ == "__main__":
    print(welcome_sign)
    World()
