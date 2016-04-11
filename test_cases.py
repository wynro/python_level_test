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

    def test_exercise_4(self):
        # I don't know how to check a function output
        c = py_ex.Cancion(["linea0", "linea1", "linea2", "linea3", "linea4", "linea5", "linea6", "linea7", "linea8", "linea9", "linea10"])
        c.play()

    def test_exercise_5(self):
        """
        Test corresponding with the fifth exercise
        """

        tests = [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 4),
            (10, 274),
            (100, 180396380815100901214157639)
        ]

        for test in tests:
            self.assertEquals(py_ex.staircase_count_v2(test[0]), test[1])

        # Speed test
        tests = [
            (2500, 25995141303821807172626236125906607615866791331561915620894574816921166800783923163332957535456271118463859873532852472723081575732040959420569217974251649035410975341213005762974633863697137749526890977505439660087436608713532914323869402616134445658944972896728120963411762122409556001067164509550348737157978465715896564604789452958067810550967263935696654067812304084042952611890333378496696245046542645295156787769713726767193263664300047841280740907689056815793889572131230684861580654047165401179620363687057859687709472816310747945105347461038894919004972392012629651907230981574199275727359628753065632760532058527830684202805216236662454100846575950215)
        ]

        before = datetime.datetime.now()
        for test in tests:
            self.assertEquals(py_ex.staircase_count_v2(test[0]), test[1])
        after = datetime.datetime.now()
        self.assertTrue((before-after).microseconds < 1000000)

if __name__ == '__main__':
    unittest.main()
