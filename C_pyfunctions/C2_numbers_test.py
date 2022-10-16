"""
Python unit tests for example C2_numbers.py (unit-under-test)

https://docs.python.org/3/library/unittest.html#module-unittest
"""
import unittest
from C2_numbers import C2_numbers


# lists for creating test objects
list_1 = [4, 12, 3, 8, 17, 12, 1, 8, 7]
list_2 = [1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8]
list_3 = [1, 2, 3, 4, 5, 6]
list_4 = [6, 2, 1, 5]
list_5 = [100]
list_6 = []

test_lists = {
    'list_1': C2_numbers(list_1),
    'list_2': C2_numbers(list_2),
    'list_3': C2_numbers(list_3),
    'list_4': C2_numbers(list_4),
    'list_5': C2_numbers(list_5),
    'list_6': C2_numbers(list_6),
}


"""
Test class.
"""
class C2_numbers_test(unittest.TestCase):

    """
    References to "objects under test" created from lists:
    """
    numb_1 = test_lists['list_1']
    numb_2 = test_lists['list_2']
    numb_3 = test_lists['list_3']
    numb_4 = test_lists['list_4']
    numb_5 = test_lists['list_5']
    numb_6 = test_lists['list_6']


    # tests for a): number of numbers
    def test_a_number_of_numbers_numb_1(self):
        self.assertEqual(self.numb_1.a, 9)

    def test_a_number_of_numbers_numb_2(self):
        self.assertEqual(self.numb_2.a, 22)

    def test_a_number_of_numbers_numb_3(self):
        self.assertEqual(self.numb_3.a, 6)

    def test_a_number_of_numbers_numb_4(self):
        self.assertEqual(self.numb_4.a, 4)

    def test_a_number_of_numbers_numb_5(self):
        self.assertEqual(self.numb_5.a, 1)

    def test_a_number_of_numbers_numb_6(self):
        self.assertEqual(self.numb_6.a, 0)


    # tests for b): first three numbers
    def test_b_first_three_numbers_numb_1(self):
        self.assertEqual(self.numb_1.b, [4, 12, 3])

    def test_b_first_three_numbers_numb_2(self):
        self.assertEqual(self.numb_2.b, [1, 4, 6])

    def test_b_first_three_numbers_numb_3(self):
        self.assertEqual(self.numb_3.b, [1, 2, 3])

    def test_b_first_three_numbers_numb_4(self):
        self.assertEqual(self.numb_4.b, [6, 2, 1])

    def test_b_first_three_numbers_numb_5(self):
        self.assertEqual(self.numb_5.b, [100])

    def test_b_first_three_numbers_numb_6(self):
        self.assertEqual(self.numb_6.b, [])


    # tests for c): last three numbers
    def test_c_last_three_numbers_numb_1(self):
        self.assertEqual(self.numb_1.c, [1, 8, 7])

    def test_c_last_three_numbers_numb_2(self):
        self.assertEqual(self.numb_2.c, [67, 6, 8])

    def test_c_last_three_numbers_numb_3(self):
        self.assertEqual(self.numb_3.c, [4, 5, 6])

    def test_c_last_three_numbers_numb_4(self):
        self.assertEqual(self.numb_4.c, [2, 1, 5])

    def test_c_last_three_numbers_numb_5(self):
        self.assertEqual(self.numb_5.c, [100])

    def test_c_last_three_numbers_numb_6(self):
        self.assertEqual(self.numb_6.c, [])


    # tests for d): last three numbers reverse
    def test_d_last_three_numbers_reverse_numb_1(self):
        self.assertEqual(self.numb_1.d, [7, 8, 1])

    def test_d_last_three_numbers_reverse_numb_2(self):
        self.assertEqual(self.numb_2.d, [8, 6, 67])

    def test_d_last_three_numbers_reverse_numb_3(self):
        self.assertEqual(self.numb_3.d, [6, 5, 4])

    def test_d_last_three_numbers_reverse_numb_4(self):
        self.assertEqual(self.numb_4.d, [5, 1, 2])

    def test_d_last_three_numbers_reverse_numb_5(self):
        self.assertEqual(self.numb_5.d, [100])

    def test_d_last_three_numbers_reverse_numb_5(self):
        self.assertEqual(self.numb_6.d, [])


    # tests for e): odd numbers
    def test_e_odd_numbers_numb_1(self):
        self.assertEqual(self.numb_1.e, [3, 17, 1, 7])

    def test_e_odd_numbers_numb_2(self):
        self.assertEqual(self.numb_2.e, [1, 67, 23, 49, 67, 23, 37, 67, 19, 67])

    def test_e_odd_numbers_numb_3(self):
        self.assertEqual(self.numb_3.e, [1, 3, 5])

    def test_e_odd_numbers_numb_4(self):
        self.assertEqual(self.numb_4.e, [1, 5])

    def test_e_odd_numbers_numb_5(self):
        self.assertEqual(self.numb_5.e, [])

    def test_e_odd_numbers_numb_6(self):
        self.assertEqual(self.numb_6.e, [])


    # tests for f): number of odd numbers
    def test_f_number_of_odd_numbers_numb_1234(self):
        self.assertEqual(self.numb_1.f, 4)
        self.assertEqual(self.numb_2.f, 10)
        self.assertEqual(self.numb_3.f, 3)
        self.assertEqual(self.numb_4.f, 2)
        self.assertEqual(self.numb_5.f, 0)
        self.assertEqual(self.numb_6.f, 0)


    # tests for g): sum of odd numbers
    def test_g_sum_of_odd_numbers_numb_1234(self):
        self.assertEqual(self.numb_1.g, 28)
        self.assertEqual(self.numb_2.g, 420)
        self.assertEqual(self.numb_3.g, 9)
        self.assertEqual(self.numb_4.g, 6)
        self.assertEqual(self.numb_5.g, 0)
        self.assertEqual(self.numb_6.g, 0)


    # tests for h): duplicate numbers removed
    def test_h_duplicate_numbers_removed_numb_1(self):
        self.assertEqual(self.numb_1.h, [4, 12, 3, 8, 17, 1, 7])

    def test_h_duplicate_numbers_removed_numb_2(self):
        self.assertEqual(self.numb_2.h, [1, 4, 6, 67, 8, 23, 34, 49, 37, 19])

    def test_h_duplicate_numbers_removed_numb_3(self):
        self.assertEqual(self.numb_3.h, [1, 2, 3, 4, 5, 6])

    def test_h_duplicate_numbers_removed_numb_4(self):
        self.assertEqual(self.numb_4.h, [6, 2, 1, 5])

    def test_h_duplicate_numbers_removed_numb_5(self):
        self.assertEqual(self.numb_5.h, [100])

    def test_h_duplicate_numbers_removed_numb_6n(self):
        self.assertEqual(self.numb_6.h, [])


    # tests for i): number of duplicate numbers
    def test_i_number_of_duplicate_numbers_numb_1234(self):
        self.assertEqual(self.numb_1.i, 2)
        self.assertEqual(self.numb_2.i, 12)
        self.assertEqual(self.numb_3.i, 0)
        self.assertEqual(self.numb_4.i, 0)
        self.assertEqual(self.numb_5.i, 0)
        self.assertEqual(self.numb_6.i, 0)


def run_tests(test_class):
    print('Unit testing using lists:')
    for key, value in test_lists.items():
        print(f'{key}: {value.numbers}')
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
    run_tests(C2_numbers_test)
