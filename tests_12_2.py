import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers


class all_results:
    def __init__(self):
        self.results = []

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.res = all_results()

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.res.results:
            print(i)

    def test_Tournament1(self):
        race = Tournament(90, self.runner_1, self.runner_3)
        self.res.results.append(race.start())
        self.assertTrue(self.res.results[-1][max(self.res.results[-1])] == 'Ник')

    def test_Tournament2(self):
        race = Tournament(90, self.runner_2, self.runner_3)
        self.res.results.append(race.start())
        self.assertTrue(self.res.results[-1][max(self.res.results[-1])] == 'Ник')

    def test_Tournament3(self):
        race = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.res.results.append(race.start())
        self.assertTrue(self.res.results[-1][max(self.res.results[-1])] == 'Ник')


if __name__ == '__main__':
    unittest.main()