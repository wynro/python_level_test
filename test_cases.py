import unittest
import python_exercises as py_ex
import datetime

class FullTest(unittest.TestCase):
    """
    Basic testing class
    """

    def test_exercise_1(self):
        """
        Test corresponding with the first exercise
        """
        tests = {
            '(1)': True,
            '(2)': False,
            '((2)((3)))': True,
            '((3)((2)))': False,
            '(((3)((4))(3))(2)((3)))': True
        }
        for test, result in tests.iteritems():
            self.assertEqual(py_ex.bien_formada(list(test)), result)


if __name__ == '__main__':
    unittest.main()
