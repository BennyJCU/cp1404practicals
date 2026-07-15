import datetime


class Guitar:
    def __init__(self, name="", year=0, cost=0.0,):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        return datetime.datetime.now().year - self.year

    def is_vintage(self):
        return self.get_age() > 50


def run_tests():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2017, 12030.50)

    # print(gibson)
    print(f"{gibson.name} get_age() - expected {datetime.datetime.now().year - gibson.year}. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - expected {datetime.datetime.now().year - another_guitar.year}. Got "
          f"{another_guitar.get_age()}")

    print(f"{gibson.name} is_vintage() - expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - expected False. Got "
          f"{another_guitar.is_vintage()}")


# run_tests()
