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

    def test_exercise_2(self):
        """
        Test corresponding with the second exercise
        """
        tests = [
            ({'a':5, 'b':3, 'c':2, 'd':3}, {2: ['c'], 3: ['b', 'd'], 5: ['a']}),
            ({'a':5, 'b':3, 'c':[2], 'd':3}, {3: ['b', 'd'], 5: ['a']})
        ]
        for test in tests:
            self.assertEqual(py_ex.invertir(test[0]), test[1])

    def test_exercise_3(self):
        """
        Test corresponding with the third exercise
        """
        tests = [
            ([1, 3, 2, 2, 5, 3, 4, 1], [2, 3, 1]),
            ([1, 3, 2, 2, 5, 2, 4, 1], [2, 1]),
            ([1, 3, 1], [1])
        ]
        for test in tests:
            self.assertEquals(list(py_ex.no_unico(test[0])), test[1])

if __name__ == '__main__':
    unittest.main()
