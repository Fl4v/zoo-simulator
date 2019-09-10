from terminal_ascii import welcome_message
from health_modifier import HealthLifeCycle


class InfOutput:

    def animal_info(self, animal_stats: list):
        for stats in animal_stats:
            print('''Name: {name}\nHealth: {health}%\nType: {animal_type}\nCan Walk: {can_walk}\nAlive: {is_alive}
            '''.format(name=stats['name'], health=stats['health'], animal_type=stats['type'], can_walk=stats['can_walk'], is_alive=stats['alive']))

    def yesno_question(self, elephants_stats: list, monkeys_stats: list, giraffes_stats: list):
        self.response = input("Woud you like to feed the animals? (if you choose 'No', the animals life is going to deteriorate!)\nPlease type Yes or No here: ")

        if self.response == 'Yes':
            HealthLifeCycle().feed_animal(elephants_stats)
            HealthLifeCycle().feed_animal(monkeys_stats)
            HealthLifeCycle().feed_animal(giraffes_stats)
            self.animal_info(elephants_stats)
            self.animal_info(monkeys_stats)
            self.animal_info(giraffes_stats)

        elif self.response == 'No':
            HealthLifeCycle().remove_health(elephants_stats)
            HealthLifeCycle().remove_health(monkeys_stats)
            HealthLifeCycle().remove_health(giraffes_stats)
            self.animal_info(elephants_stats)
            self.animal_info(monkeys_stats)
            self.animal_info(giraffes_stats)

        else:
            print('Response not recognised, please try again')
