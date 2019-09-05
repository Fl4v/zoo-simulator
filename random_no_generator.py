from random import uniform


def hunger():
    return round(uniform(0, 20), 2)


def feeding():
    return round(uniform(10, 25), 2)
