"""
Write single-line expressions to initialize member variables `a) - k)`
such that they yield the results shown in comments.

Only use [built-in functions](https://docs.python.org/3/library/functions.html)
or Python's powerful expressions
[ternary operators](https://book.pythontips.com/en/latest/ternary_operators.html)
or
[list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)

Don't write own functions.
"""

class C2_numbers:

    numbers=[4, 12, 3, 8, 17, 12, 1, 8, 7]

    def __init__(self, _numbers=numbers):
        """
        Constructor to initialize member variables.
        """
        # initialize numbers list
        self.numbers = _numbers

        # a) initialize with number of numbers: 9
        self.a = len(self.numbers)    # <-- expression for a)

        # b) initialize with first three numbers: [4, 12, 3]
        self.b = []      # <-- write expression here

        # c) initialize with last three numbers: [1, 8, 7]
        self.c = []

        # d) initialize with last three numbers reverse: [7, 8, 1]
        self.d = []

        # e) initialize with odd numbers: [3, 17, 1, 7]
        self.e = []

        # f) initialize with number of odd numbers: 4
        self.f = 0

        # g) initialize with sum_ of odd numbers: 28
        self.g = 0

        # h) duplicate numbers removed: [4, 12, 3, 8, 17, 1, 7]
        self.h = []

        # i) number of duplicate numbers: 2
        self.i = 0

        # j) ascending list of squared numbers with no duplicates: [1, 9, 16, 49, 64, 144, 289]
        self.j = []

        # k) initialize with "ODD_LIST", "EVEN_LIST" or "EMPTY_LIST" depending on numbers length
        self.k = "NEITHER"


        # Ignore this code that loads solution from file, if exists.
        # The solution is not distributed.
        try:
            _from, _import = 'C2_numbers_sol', 'solution'
            solution = getattr(__import__(_from, fromlist=[_import]), _import)
            solution(self)
        #
        except ImportError:
            pass


    def print_results(self):
        print(f'numbers: {self.numbers}\n#')
        fmt = {
            # key: (value, output string)
            'a': (self.a, 'number of numbers'),
            'b': (self.b, 'first three numbers'),
            'c': (self.c, 'last three numbers'),
            'd': (self.d, 'last three numbers reverse'),
            'e': (self.e, 'odd numbers'),
            'f': (self.f, 'number of odd numbers'),
            'g': (self.g, 'sum of odd numbers'),
            'h': (self.h, 'duplicate numbers removed'),
            'i': (self.i, 'number of duplicate numbers'),
            'j': (self.j, 'ascending, de-dup (n^2) numbers'),
            'k': (self.k, 'length'),
        }
        # format output, e.g.: "b) first three numbers: [1, 4, 6]"
        for k in sorted(fmt.keys()):
            print(f'{k}) {fmt[k][1]}: {fmt[k][0]}')


if __name__ == '__main__':
    """
    Main driver that runs when this file is executed by Python interpreter.
    """
    #
    n1 = C2_numbers()   # use default list in C2_numbers
    #
    n2 = C2_numbers([1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67,
        6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8])
    #
    n1.print_results()
    # n2.print_results()     # try also other list
