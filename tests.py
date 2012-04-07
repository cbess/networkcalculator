# ref: http://www.numion.com/calculators/
import unittest
import calc
from pdb import set_trace

def run_all(test_case):
    """Runs all the tests for the specified test case
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    pass


class TestCalc(unittest.TestCase):
    def test_bandwidth_formula_fail(self):
        formula = calc.BandwidthFormulaItem()
        formula.users_per_day = 7
        success, message = formula.validate()
        self.assertFalse(success, 'should fail valid')
        pass


if __name__ == "__main__":
    run_all(TestCalc)