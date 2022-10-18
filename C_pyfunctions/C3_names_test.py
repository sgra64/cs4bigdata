"""
Python unit tests for example C3_names.py (unit-under-test)

https://docs.python.org/3/library/unittest.html#module-unittest
"""
import unittest
from C3_names import C3_names


class C3_names_test(unittest.TestCase):
    """
    Test class.
    """

    # "Objects under test":
    nam_1 = C3_names(['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller',
        'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris',
        'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis',
        'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez',
        'Hill', 'Scott', 'Green', 'Adams', 'Cox', 'Gomez', 'Murray', 'Freeman', 'Wells',
        'Webb', 'Simpson', 'Stevens', 'Tucker', 'Porter', 'Hunter', 'Hicks', 'Crawford',
        'Henry', 'Boyd', 'Mason', 'Morales', 'Kennedy', 'Warren', 'Dixon', 'Ramos', 'Reyes',
        'Burns', 'Gordon', 'Shaw', 'Holmes', 'Rice', 'Robertson', 'Henderson', 'Patterson',
        'Red', 'Willoughby', 'Fitzgerald'
    ])
    nam_2 = C3_names(['Hans', 'Gretchen', 'Lotte', 'Gudrun', 'Ingrid'])
    nam_3 = C3_names(['Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill',
        'Scott', 'Green', 'Adams', 'Cox', 'Gomez', 'Murray', 'Freeman', 'Wells', 'Webb', 'Simpson',
        'Stevens', 'Tucker', 'Porter', 'Hunter', 'Hicks'])
    nam_4 = C3_names(['A'])
    nam_5 = C3_names([''])
    nam_6 = C3_names([])


    # tests a): lengths of names list
    def test_a_name_lengths_nam_1(self):
        self.assertEqual(self.nam_1.name_lengths, [5, 7, 8, 5, 5, 5, 6, 6, 5, 6, 8, 6, 7, 5, \
            6, 6, 8, 6, 8, 8, 5, 9, 5, 3, 6, 4, 5, 5, 9, 4, 6, 5, 4, 5, 5, 5, 3, 5, 6, 7, 5, 4, \
            7, 7, 6, 6, 6, 5, 8, 5, 4, 5, 7, 7, 6, 5, 5, 5, 5, 6, 4, 6, 4, 9, 9, 9, 3, 10, 10])

    def test_a_name_lengths_nam_2(self):
        self.assertEqual(self.nam_2.name_lengths, [4, 8, 5, 6, 6])

    def test_a_name_lengths_nam_3(self):
        self.assertEqual(self.nam_3.name_lengths, [4, 5, 5, 9, 4, 6, 5, 4, 5, 5, 5, 3, 5, 6, 7, 5, 4, 7, 7, 6, 6, 6, 5])

    def test_a_name_lengths_nam_4(self):
        self.assertEqual(self.nam_4.name_lengths, [1])

    def test_a_name_lengths_nam_5(self):
        self.assertEqual(self.nam_5.name_lengths, [0])

    def test_a_name_lengths_nam_6(self):
        self.assertEqual(self.nam_6.name_lengths, [])


    # tests b): most and least frequent names, nam_1
    def test_b_most_frequent_names_nam_1(self):
        self.assertEqual(len(self.nam_1.freq['most_freq']), 3)  # 3 tuples
        self.assertEqual(self.nam_1.freq['most_freq'][0], (23, 5, ['Smith', 'Jones', 'Brown', 'Davis', \
            'Moore', 'White', 'Clark', 'Lewis', 'Allen', 'Young', 'Lopez', 'Scott', 'Green', 'Adams', \
            'Gomez', 'Wells', 'Hicks', 'Henry', 'Mason', 'Dixon', 'Ramos', 'Reyes', 'Burns'
        ]))
        self.assertEqual(self.nam_1.freq['most_freq'][1], (16, 6, ['Miller', 'Wilson', 'Taylor', \
            'Thomas', 'Harris', 'Martin', 'Garcia', 'Walker', 'Wright', 'Murray', 'Tucker', 'Porter', \
            'Hunter', 'Warren', 'Gordon', 'Holmes'
        ]))
        self.assertEqual(self.nam_1.freq['most_freq'][2], (7, 7, [
            'Johnson', 'Jackson', 'Freeman', 'Simpson', 'Stevens', 'Morales', 'Kennedy'
        ]))

    def test_b_least_frequent_names_nam_1(self):
        self.assertEqual(len(self.nam_1.freq['least_freq']), 3)  # 3 tuples
        self.assertEqual(self.nam_1.freq['least_freq'][0], (2, 10, ['Willoughby', 'Fitzgerald']))
        self.assertEqual(self.nam_1.freq['least_freq'][1], (3, 3, ['Lee', 'Cox', 'Red']))
        self.assertEqual(self.nam_1.freq['least_freq'][2], (5, 9, ['Rodriguez', 'Hernandez', 'Robertson', 'Henderson', 'Patterson']))


    # tests c): most and least frequent names, nam_2
    def test_c_most_frequent_names_nam_2(self):
        self.assertEqual(len(self.nam_2.freq['most_freq']), 3)  # 3 tuples
        self.assertEqual(self.nam_2.freq['most_freq'][0], (2, 6, ['Gudrun', 'Ingrid']))
        self.assertEqual(self.nam_2.freq['most_freq'][1], (1, 8, ['Gretchen']))
        self.assertEqual(self.nam_2.freq['most_freq'][2], (1, 5, ['Lotte']))

    def test_c_least_frequent_names_nam_2(self):
        self.assertEqual(len(self.nam_2.freq['least_freq']), 3)  # 3 tuples
        self.assertEqual(self.nam_2.freq['least_freq'][0], (1, 4, ['Hans']))
        self.assertEqual(self.nam_2.freq['least_freq'][1], (1, 5, ['Lotte']))
        self.assertEqual(self.nam_2.freq['least_freq'][2], (1, 8, ['Gretchen']))


    # tests d): most and least frequent names, nam_3
    def test_d_most_frequent_names_nam_3(self):
        self.assertEqual(len(self.nam_3.freq['most_freq']), 3)  # 3 tuples
        self.assertEqual(self.nam_3.freq['most_freq'][0], (9, 5, [
            'Allen', 'Young', 'Lopez', 'Scott', 'Green', 'Adams', 'Gomez', 'Wells', 'Hicks'
        ]))
        self.assertEqual(self.nam_3.freq['most_freq'][1], (5, 6, [
            'Wright', 'Murray', 'Tucker', 'Porter', 'Hunter'
        ]))
        self.assertEqual(self.nam_3.freq['most_freq'][2], (4, 4, ['Hall', 'King', 'Hill', 'Webb']))

    def test_d_least_frequent_names_nam_3(self):
        self.assertEqual(len(self.nam_3.freq['least_freq']), 3)  # 3 tuples
        self.assertEqual(self.nam_3.freq['least_freq'][0], (1, 3, ['Cox']))
        self.assertEqual(self.nam_3.freq['least_freq'][1], (1, 9, ['Hernandez']))
        self.assertEqual(self.nam_3.freq['least_freq'][2], (3, 7, ['Freeman', 'Simpson', 'Stevens']))


    # tests e): most and least frequent names, nam_4
    def test_e_most_frequent_names_nam_4(self):
        self.assertEqual(len(self.nam_4.freq['most_freq']), 1)  # 1 tuple
        self.assertEqual(self.nam_4.freq['most_freq'][0], (1, 1, ['A']))

    def test_e_least_frequent_names_nam_4(self):
        self.assertEqual(len(self.nam_4.freq['least_freq']), 1)  # 1 tuple
        self.assertEqual(self.nam_4.freq['least_freq'][0], (1, 1, ['A']))


    # tests f): most and least frequent names, nam_5
    def test_f_most_frequent_names_nam_5(self):
        self.assertEqual(len(self.nam_5.freq['most_freq']), 1)  # 1 tuple
        self.assertEqual(self.nam_5.freq['most_freq'][0], (1, 0, ['']))

    def test_f_least_frequent_names_nam_5(self):
        self.assertEqual(len(self.nam_5.freq['least_freq']), 1)  # 1 tuple
        self.assertEqual(self.nam_5.freq['least_freq'][0], (1, 0, ['']))


    # tests g): most and least frequent names, nam_6
    def test_g_most_frequent_names_nam_6(self):
        self.assertEqual(self.nam_6.freq['most_freq'], [])  # empty list

    def test_g_least_frequent_names_nam_6(self):
        self.assertEqual(self.nam_6.freq['least_freq'], [])  # empty list


    # # https://stackoverflow.com/questions/35229770/python-unit-test-testcase-class-with-own-constructor-fails-in-standard-library
    # def __init__(self, *args, **kwargs):
    #     super(C3_names_test, self).__init__(*args, **kwargs)


def run_tests(test_class):
    print('Unit testing using test objects:')
    #
    _suite = unittest.makeSuite(test_class, "test")
    _runner = unittest.TextTestRunner(verbosity=0)  # stream=sys.stdout
    _result = _runner.run(_suite)   # run test suite
    _n = _result.testsRun
    _succ = [m for m in dir(test_class) if m.startswith('test_')]
    _failed = [(str(_test).split()[0], _trace.split(',')[1]) for _test, _trace in _result.failures]
    for _f in _failed:
        _succ.remove(_f[0])
    #
    for t in _succ:
        # if t not in _failed:
        print(f' - {t}()')
    #
    print(f'---> {_n - len(_failed)}/{_n} TESTS SUCCEEDED')
    #
    if len(_failed) > 0:
        print(f'\n---> {len(_failed)}/{_n} TESTS FAILED {"*" * 20}')
        for _f in _failed:  # _f[0]: _meth, _f[1]: _line
            print(f' - FAILED: {_f[0]}(), {_f[1]}')


if __name__ == '__main__':
    run_tests(C3_names_test)
