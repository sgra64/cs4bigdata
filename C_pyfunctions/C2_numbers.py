"""
Write expressions to initialize member variables a) - i) such that
they yield the results shown in comments for the example list.

Use only [built-in functions](https://docs.python.org/3/library/functions.html),
no own functions. Use Python's powerful collections constructs such as
[list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp).

Make sure your solution works for any numbers[] list. Try numbers_2 in __main__.
"""
class C2_numbers:

    # default numbers (updated with constructor)
    numbers = [4, 12, 3, 8, 17, 12, 1, 8, 7]

    # a) initialize with number of numbers: 22
    a = len(numbers)    # initializes a with value 22

    # b) initialize with first three numbers: [1, 4, 6]
    b = []          # <-- write expression here

    # c) initialize with last three numbers: [67, 6, 8]
    c = []

    # d) initialize with last three numbers reverse: [8, 6, 67]
    d = []

    # e) initialize with odd numbers: [1, 67, 23, 49, 67, 23, 37, 67, 19, 67]
    e = []

    # f) initialize with number of odd numbers: 10
    f = 0

    # g) initialize with sum_ of odd numbers: 420
    g = 0

    # h) initialize with duplicate numbers removed: [1, 4, 6, 67, 8, 23, 34, 49, 37, 19]
    h = []

    # i) number of duplicate numbers: 12
    i = 0


    def __init__(self, numbers=None):
        """
        Constructor
        """
        if numbers != None and type(numbers==list):
            self.numbers = numbers
        solution(self)


def solution(_: C2_numbers):
    """
    Another way to include your solution for initializing member variables:
        _.a = len(_.numbers)
        _.b = []
        _.c = []
        _.d = []
        _.e = []
        _.f = 0
        _.g = 0
        _.h = []
        _.i = 0
    """
    pass    # you may place your solution here as well


if __name__ == '__main__':
    #
    numb = C2_numbers()     # use default list
    #
    numbers_2 = [1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67,
        6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8]
    #
    # remove comment to use another list:
    # numb = C2_numbers(numbers_2)
    #
    print(f'numbers: {numb.numbers}\n#')
    for _selector in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',]:
        fmt = {
            # selector, value, output string
            'a': (numb.a, 'number of numbers'),
            'b': (numb.b, 'first three numbers'),
            'c': (numb.c, 'last three numbers'),
            'd': (numb.d, 'last three numbers reverse'),
            'e': (numb.e, 'odd numbers'),
            'f': (numb.f, 'number of odd numbers'),
            'g': (numb.g, 'sum of odd numbers'),
            'h': (numb.h, 'duplicate numbers removed'),
            'i': (numb.i, 'number of duplicate numbers')
        }[_selector]
        # output for _selector 'b': "b) first three numbers: [1, 4, 6]"
        print(f'{_selector}) {fmt[1]}: {fmt[0]}')
