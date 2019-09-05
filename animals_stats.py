

class AnimalInfoArray:

    def create_array(self, no_of_animals: int, array: list, animal_class: object):
        counter = 0
        for animal in range(no_of_animals):
            counter += 1
            array.append(
                {
                    'name': animal_class.name + str(counter),
                    'health': animal_class.health,
                    'can_walk': animal_class.can_walk,
                    'alive': animal_class.alive
                }
            )
