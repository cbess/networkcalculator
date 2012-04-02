# ref: http://www.numion.com/calculators/
import unittest

def run_all(test_case):
    """Runs all the tests for the specified test case
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    pass


class TestObject(unittest.TestCase):
    pass


if __name__ == "__main__":
    run_all(TestObject)