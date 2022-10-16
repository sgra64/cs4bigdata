"""
Write expressions to initialize member variables a) - i) such that
they yield the results indicated in comments for the example list.

Only use [built-in functions](https://docs.python.org/3/library/functions.html).
Don't write own functions.
Use Python's powerful concepts for collections such as
[list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp).

Make sure your solution works for any list numbers[].
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


    def value(self, selector):
        return { 'a': self.a, 'b': self.b, 'c': self.c, 'd': self.d,
            'e': self.e, 'f': self.f, 'g': self.g, 'h': self.h, 'i': self.i
        }[selector]


    def fmt_value(self, selector):
        fmt = {
            'a': 'number of numbers',
            'b': 'first three numbers',
            'c': 'last three numbers',
            'd': 'last three numbers reverse',
            'e': 'odd numbers',
            'f': 'number of odd numbers',
            'g': 'sum of odd numbers',
            'h': 'duplicate numbers removed',
            'i': 'number of duplicate numbers'
        }[selector]
        return f'{selector}) {fmt}: {self.value(selector)}'


    def solution(self):
        pass    # you may place your solution here as well

    def __init__(self, numbers=None):
        if numbers != None and type(numbers==list):
            self.numbers = numbers
        self.solution()


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
    for _sel in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',]:
        print(f'{numb.fmt_value(_sel)}')
