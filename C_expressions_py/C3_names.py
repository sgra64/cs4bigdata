"""
Write Python code that analyses names and creates a composite structure
`freq` in the `solutions()` method that holds the three most frequent
and the least frequent names.
"""

class C3_names:

    default_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller',
        'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White',
        'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark',
        'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez',
        'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Cox', 'Gomez',
        'Murray', 'Freeman', 'Wells', 'Webb', 'Simpson', 'Stevens', 'Tucker', 'Porter',
        'Hunter', 'Hicks', 'Crawford', 'Henry', 'Boyd', 'Mason', 'Morales', 'Kennedy',
        'Warren', 'Dixon', 'Ramos', 'Reyes', 'Burns', 'Gordon', 'Shaw', 'Holmes', 'Rice',
        'Robertson', 'Henderson', 'Patterson', 'Red', 'Willoughby', 'Fitzgerald']

    def __init__(self, names=default_names):
        """
        Constructor to initialize member variables.
        """
        self.names = names

        # list of corresponding name lengths
        # name_lengths = [5, 7, 8, 5, 5, 5, 6, 6, ... 6, 4, 9, 9, 9, 3, 10, 10]
        self.name_lengths = []

        # composite structure with the three most and the three least frequent
        # name lengths such as: 23x names of length 5, 16x names of length 6
        # and 7 names of length 7 as three most_frequent names.
        """
        freq = {
            "most_freq": [
                (23, 5, [names...]), (16, 6, [names...]), (7, 7, [names...])
            ]
            "least_freq": [
                (2, 10, [names...]), (3, 3, [names...]), (5, 9, [names...])
            ]
        }
        holding information for output:
        #
        The three most frequent name lenghts are:
        - 23 names of length 5: ['Smith', 'Jones', 'Brown', 'Davis', 'Moore', ... ]
        - 16 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas', 'Harris', ... ]
        -  7 names of length 7: ['Johnson', 'Jackson', 'Freeman', 'Simpson', 'Stevens', ... ]
        The three least frequent name lenghts are:
        -  2 names of length 10: ['Willoughby', 'Fitzgerald']
        -  3 names of length 3: ['Lee', 'Cox', 'Red']
        -  5 names of length 9: ['Rodriguez', 'Hernandez', 'Robertson', 'Henderson', 'Patterson']
        """
        self.freq = None

        # Ignore this code that loads solution from file, if exists.
        # The solution is not distributed.
        try:
            _from, _imp1, _imp2 = 'C3_names_sol', 'solution', 'avg_name_length'
            C3_names.solution = getattr(__import__(_from, fromlist=[_imp1]), _imp1)
            C3_names.avg_name_length = getattr(__import__(_from, fromlist=[_imp2]), _imp2)
        #
        except ImportError:
            pass

        self.solution()    # invoke solution method


    def solution(self): # -> Self: from Python 3.10
        """
        Method to create freq structure.
        """
        # Code:
        # self.name_lengths = ...
        # self.freq = ...
        #
        return self


    def avg_name_length(self) -> float:
        """
        Return average name length.
        """
        return 0.0


    def print_names_and_name_lengths(self, enabled=True): # -> Self: from Python 3.10
        """
        Print lists of names and name lengths.
        """
        if enabled:
            sep = '' if len(self.names) < 20 else '\n\\\\'
            print(f'Names: {self.names}{sep}')
            print(f'Name lengths: {self.name_lengths}{sep}')
        return self


    def print_freq(self, enabled=True): # -> Self: from Python 3.10
        """
        Pretty-print freq struct.
        """
        if enabled:
            def limit(l_, n_):
                return str(l_) if len(l_) <= n_ else str(l_[0:n_]) + " ..."

            if self.freq != None:
                print('The three most frequent name lenghts are:')
                for t in self.freq['most_freq']:
                    print(f' - {t[0]:2} names of length {t[1]}: {limit(t[2], 5)}')
                #
                print('The three least frequent name lenghts are:')
                for t in self.freq['least_freq']:
                    print(f' - {t[0]:2} names of length {t[1]}: {limit(t[2], 5)}')
                #
            else:
                print('self.freq: not implemented in solution() method')
        #
        return self


    def print_avg_name_length(self, enabled=True): # -> Self: from Python 3.10
        """
        Print average name length.
        """
        if enabled:
            print(f'The average name length: {self.avg_name_length():.2f}')
        return self


if __name__ == '__main__':
    """
    Main driver that runs when this file is executed by Python interpreter.
    """
    #
    n1 = C3_names()   # use default list in C2_numbers
    n1.print_names_and_name_lengths() \
        .print_freq() \
        .print_avg_name_length()     # method chaining
    #
    # n2 = C3_names(['Hans', 'Gretchen', 'Lotte', 'Gudrun', 'Ingrid'])   # use constructor list
    # n2.print_names_and_name_lengths() \
    #     .print_freq() \
    #     .print_avg_name_length()     # method chaining
