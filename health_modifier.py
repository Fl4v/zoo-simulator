from random import uniform


class HealthLifeCycle:

    def __subtract(self):
        return round(uniform(0, 20), 2)

    def __add(self):
        return round(uniform(10, 25), 2)

    def remove_health(self, animal_stats: list):
        # first loop to amend the animal's health
        for each_dict in animal_stats:
            updated_health = float(each_dict['health']) - self.__subtract()
            each_dict['health'] = format(updated_health, '.2f')
        # second loop to check animal's health
        for each_dict in animal_stats:
            if each_dict['type'] == 'Elephant' and float(each_dict['health']) < 70:
                each_dict['can_walk'] = False
            if each_dict['type'] == 'Monkey' and float(each_dict['health']) < 30:
                each_dict['alive'] = False
            if each_dict['type'] == 'Giraffe' and float(each_dict['health']) < 50:
                each_dict['alive'] = False
        # third loop to check if animal is alive
        for each_dict in animal_stats:
            if not each_dict['alive']:
                each_dict['can_walk'] = False

    def feed_animal(self, animal_stats: list):
        for each_dict in animal_stats:
            updated_health = float(each_dict['health']) + self.__add()
            if each_dict['alive'] and updated_health > 100:
                updated_health = 100
                each_dict['health'] = format(updated_health, '.2f')
            elif each_dict['alive']:
                each_dict['health'] = format(updated_health, '.2f')
