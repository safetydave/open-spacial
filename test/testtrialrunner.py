import os
import sys
import unittest

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../src'))
from src.trialrunner import TrialRunner


class TestTrialRunner(unittest.TestCase):

    def test_run(self):
        tr = TrialRunner(10, [1.0])
        tr.run()
        self.assertEqual("Number of samples for each p: 10\n1.0 0.000\n", tr.summary())
