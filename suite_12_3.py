import unittest, tests_12_3

tournamentST = unittest.TestSuite()

tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tournamentST)