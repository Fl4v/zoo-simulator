from random import uniform


class HealthLifeCycle:

    def __subtract(self):
        return round(uniform(0, 20), 2)

    def __add(self):
        return round(uniform(10, 25), 2)

    def remove_health(self, animal_stats: list):
        for each_dict in animal_stats:
            updated_health = each_dict['health'] - self.__subtract()
            each_dict['health'] = format(updated_health, '.2f')

    def feed_animal(self, animal_stats: list):
        for each_dict in animal_stats:
            updated_health = each_dict['health'] + self.__add()
            if updated_health > 100:
                updated_health = 100
                each_dict['health'] = format(updated_health, '.2f')
            else:
                each_dict['health'] = format(updated_health, '.2f')
