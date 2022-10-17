"""
Write single-line expressions to initialize member variables `a) - k)`
such that they yield the results shown in comments.

Only use [built-in functions](https://docs.python.org/3/library/functions.html)
or Python's powerful expressions
[ternary operators](https://book.pythontips.com/en/latest/ternary_operators.html),
[list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)

Don't write own functions.
"""
class C2_numbers:

    # default initialization (updated by the constructor)
    numbers = [4, 12, 3, 8, 17, 12, 1, 8, 7]

    # a) initialize with number of numbers: 9
    a = len(numbers)    # <-- expression for a)

    # b) initialize with first three numbers: [4, 12, 3]
    b = []      # <-- write expression here

    # c) initialize with last three numbers: [1, 8, 7]
    c = []

    # d) initialize with last three numbers reverse: [7, 8, 1]
    d = []

    # e) initialize with odd numbers: [3, 17, 1, 7]
    e = []

    # f) initialize with number of odd numbers: 4
    f = 0

    # g) initialize with sum_ of odd numbers: 28
    g = 0

    # h) duplicate numbers removed: [4, 12, 3, 8, 17, 1, 7]
    h = []

    # i) number of duplicate numbers: 2
    i = 0

    # j) ascending list of squared numbers with no duplicates: [1, 9, 16, 49, 64, 144, 289]
    j = []

    # k) initialize with "ODD_LIST", "EVEN_LIST" or "EMPTY_LIST" depending on numbers length
    k = "NEITHER"


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


    def __init__(self, numbers=None):
        """
        Constructor.
        """
        if numbers != None and type(numbers==list):
            self.numbers = numbers


if __name__ == '__main__':
    """
    main driver that starts program when called from command line
    """
    #
    n1 = C2_numbers()   # use default list in C2_numbers
    #
    n2 = C2_numbers([1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67,
        6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8])
    #
    n1.print_results()
    # n2.print_results()     # try also other list
