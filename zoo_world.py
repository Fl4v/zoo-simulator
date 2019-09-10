from zoo_animals import Elephant, Monkey, Giraffe
from terminal_ascii import welcome_sign, welcome_message
from animals_stats import AnimalInfoArray
from terminal_output import InfOutput


class World:

    total_animals = 5

    elephant = Elephant()
    monkey = Monkey()
    giraffe = Giraffe()

    animal_info_array = AnimalInfoArray()

    output = InfOutput()

    elephants_stats = []
    monkeys_stats = []
    giraffes_stats = []

    def __init__(self):

        # Create animals arrays to store animals information

        self.animal_info_array.create_array(self.total_animals, self.elephants_stats, self.elephant)
        self.animal_info_array.create_array(self.total_animals, self.monkeys_stats, self.monkey)
        self.animal_info_array.create_array(self.total_animals, self.giraffes_stats, self.giraffe)

        # Presenting stats to the user for first iteration

        self.output.animal_info(self.elephants_stats)
        self.output.animal_info(self.monkeys_stats)
        self.output.animal_info(self.giraffes_stats)

        # Starting infite loop

        while True:
            self.output.yesno_question(self.elephants_stats, self.monkeys_stats, self.giraffes_stats)

if __name__ == "__main__":
    print(welcome_sign)
    print(welcome_message)
    World()
