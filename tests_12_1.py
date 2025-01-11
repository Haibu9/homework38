import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        sportsman = Runner("Ben")
        for _ in range(10):
            sportsman.walk()
        self.assertEqual(sportsman.distance, 50)

    def test_run(self):
        sportsman = Runner("Ben")
        for _ in range(10):
            sportsman.run()
        self.assertEqual(sportsman.distance, 100)

    def test_challenge(self):
        sportsman_1 = Runner("Ben")
        sportsman_2 = Runner("Dave")
        for _ in range(10):
            sportsman_1.run()
            sportsman_2.walk()
        self.assertNotEqual(sportsman_1.distance, sportsman_2.distance)

if __name__ == '__main__':
    unittest.main()