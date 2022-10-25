# Assignment C: Python Expressions &nbsp; (<span style="color:red">12 Pts</span>)

This assignment will demonstrate Python's built-in collection types.

### Challenges
1. [Challenge 1:](#1-challenge-1) List, Set, Tuple, Dictionary
2. [Challenge 2:](#2-challenge-2) Python expressions
3. [Challenge 3:](#3-challenge-3) Names example


&nbsp;
### 1.) Challenge 1
Python has four basic built-in collection types:
- **List []:** ordered, mutable, duplicates.
- **Set {}:** unordered, mutable, no duplicates.
- **Tuple ():** ordered, imutable (cannot add/remove elements), duplicates.
- **Dictonary[ key ]:** unordered, mutable, no duplicate keys.

Guess the output for the fruit collections.
```py
fruit_List = ['banana', 'apple', 'orange', 'banana', 'pineapple']
fruit_Set  = {'banana', 'apple', 'orange', 'banana', 'pineapple'}
fruit_Tuple= ('banana', 'apple', 'orange', 'banana', 'pineapple')
fruit_Dict = {10: 'banana', 20: 'apple', 30: 'orange', 40: 'banana', 20: 'pineapple'}
fruit_Dict2 = {'banana': 10, 'apple': 20, 'orange': 30, 'banana': 40, 'pineapple': 20}

print(f'fruit_List:  {fruit_List}')
print(f'fruit_Set:   {fruit_Set}')
print(f'fruit_Tuple: {fruit_Tuple}')
print(f'fruit_Dict:  {fruit_Dict}')
print(f'fruit_Dict2: {fruit_Dict2}')
```
<!--
Output:
fruit_List:  ['banana', 'apple', 'orange', 'banana', 'pineapple']
fruit_Set:   {'orange', 'apple', 'pineapple', 'banana'}
fruit_Tuple: ('banana', 'apple', 'orange', 'banana', 'pineapple')
fruit_Dict:  {1: 'banana', 2: 'pineapple', 3: 'orange', 4: 'banana'}
fruit_Dict2: {'banana': 4, 'apple': 2, 'orange': 3, 'pineapple': 2}
-->
Write down your expected output:
```py
(on paper)






```
Try out in Python and confirm your guesses.

Write Python code that counts the fruits in each bag.
```py
bag = fruit_List
print(f'bag of fruits of type_{type(bag)}')
...code
```
Output:
```py
bag of fruits of type_<class 'list'>
 - counted 2 x banana
 - counted 1 x apple
 - counted 1 x orange
 - counted 2 x banana
 - counted 1 x pineapple
```
(2 Pts)


&nbsp;
### 2.) Challenge 2
Pull file [C2_numbers.py](https://github.com/sgra64/cs4bigdata/blob/main/C_expressions_py/C2_numbers.py)
and write single-line expressions to initialize member variables `a) - k)`
such that they yield the results shown in comments for the example list.

Only use
[built-in functions](https://docs.python.org/3/library/functions.html) or Python's
powerful expressions
[ternary operators](https://book.pythontips.com/en/latest/ternary_operators.html) and
[list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)

Don't write own functions.

```py
numbers = [4, 12, 3, 8, 17, 12, 1, 8, 7]

# a) initialize with number of numbers[]: 9
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
```
Output:
```py
numbers: [4, 12, 3, 8, 17, 12, 1, 8, 7]
#
a) number of numbers: 9
b) first three numbers: [4, 12, 3]
c) last three numbers: [1, 8, 7]
d) last three numbers reverse: [7, 8, 1]
e) odd numbers: [3, 17, 1, 7]
f) number of odd numbers: 4
g) sum_ of odd numbers: 28
h) duplicate numbers removed: [4, 12, 3, 8, 17, 1, 7]
i) number of duplicate numbers: 2
j) ascending, de-duplicated (n^2) numbers: [1, 9, 16, 49, 64, 144, 289]
k) length: "ODD_LIST"
```
Try with second `C2_numbers()` object `n2` in [C2_numbers.py](https://github.com/sgra64/cs4bigdata/blob/main/C_expressions_py/C2_numbers.py):
```py
numbers: [1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8]
#
a) number of numbers: 22
b) first three numbers: [1, 4, 6]
c) last three numbers: [67, 6, 8]
d) last three numbers reverse: [8, 6, 67]
e) odd numbers: [1, 67, 23, 49, 67, 23, 37, 67, 19, 67]
f) number of odd numbers: 10
g) sum_ of odd numbers: 420
h) duplicate numbers removed: [1, 4, 6, 67, 8, 23, 34, 49, 37, 19]
i) number of duplicate numbers: 12
j) ascending, de-duplicated (n^2) numbers: [1, 16, 36, 64, 361, 529, 1156, 1369, 2401, 4489]
k) length: "EVEN_LIST"
```
Pull file [C2_numbers_test.py](https://github.com/sgra64/cs4bigdata/blob/main/C_expressions_py/C2_numbers_test.py) into same directory. Run unit tests to confirm the 
correctness of your solution.
```sh
test_url=https://raw.githubusercontent.com/sgra64/cs4bigdata/main/C_expressions_py/C2_numbers_test.py
curl -O $(echo $test_url)           # download C2_numbers_test.py from URL
python C2_numbers_test.py           # run tests from test file

curl $(echo $test_url) | python     # run tests from URL (use to demonstrate)
```
Output:
```
----------------------------------------------------------------------
Ran 40 tests in 0.001s

OK
Unit testing using test objects:
 - numb_1: [4, 12, 3, 8, 17, 12, 1, 8, 7]
 - numb_2: [1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8]
 - numb_3: [1, 2, 3, 4, 5, 6]
 - numb_4: [6, 2, 1, 5]
 - numb_5: [100]
 - numb_6: []
 - -----
 - test_a_number_of_numbers_numb_1()
 - test_a_number_of_numbers_numb_2()
 - test_a_number_of_numbers_numb_3()
 - test_a_number_of_numbers_numb_4()
 - test_a_number_of_numbers_numb_5()
 - test_a_number_of_numbers_numb_6()
 - test_b_first_three_numbers_numb_1()
 - test_b_first_three_numbers_numb_2()
 - test_b_first_three_numbers_numb_3()
 - test_b_first_three_numbers_numb_4()
 - test_b_first_three_numbers_numb_5()
 - test_b_first_three_numbers_numb_6()
 - test_c_last_three_numbers_numb_1()
 - test_c_last_three_numbers_numb_2()
 - test_c_last_three_numbers_numb_3()
 - test_c_last_three_numbers_numb_4()
 - test_c_last_three_numbers_numb_5()
 - test_c_last_three_numbers_numb_6()
 - test_d_last_three_numbers_reverse_numb_1()
 - test_d_last_three_numbers_reverse_numb_2()
 - test_d_last_three_numbers_reverse_numb_3()
 - test_d_last_three_numbers_reverse_numb_4()
 - test_d_last_three_numbers_reverse_numb_5()
 - test_e_odd_numbers_numb_1()
 - test_e_odd_numbers_numb_2()
 - test_e_odd_numbers_numb_3()
 - test_e_odd_numbers_numb_4()
 - test_e_odd_numbers_numb_5()
 - test_e_odd_numbers_numb_6()
 - test_f_number_of_odd_numbers_numb_1234()
 - test_g_sum_of_odd_numbers_numb_1234()
 - test_h_duplicate_numbers_removed_numb_1()
 - test_h_duplicate_numbers_removed_numb_2()
 - test_h_duplicate_numbers_removed_numb_3()
 - test_h_duplicate_numbers_removed_numb_4()
 - test_h_duplicate_numbers_removed_numb_5()
 - test_h_duplicate_numbers_removed_numb_6n()
 - test_i_number_of_duplicate_numbers_numb_1234()
 - test_j_ascending_list_of_squared_numbers_with_no_duplicates_numb_1234()
 - test_k_list_length_numb_1234()
---> 40/40 TESTS SUCCEEDED
```
(4 Pts)


&nbsp;
### 3.) Challenge 3
Write Python code that analyses names and creates a composite structure
`freq` in the `solutions()` method that holds the three most frequent
and the least frequent names.

Pull file [C3_names.py](https://github.com/sgra64/cs4bigdata/blob/main/C_expressions_py/C3_names.py)
```py
class C3_names:

    # list of names default initialization (updated by the constructor)
    names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Thompson', 'Garcia', 'Martinez', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Lee', 'Walker', 'Hall', 'Allen', 'Young', 'Hernandez', 'King', 'Wright', 'Lopez', 'Hill', 'Scott', 'Green', 'Adams', 'Cox', 'Gomez', 'Murray', 'Freeman', 'Wells', 'Webb', 'Simpson', 'Stevens', 'Tucker' 'Porter', 'Hunter', 'Hicks', 'Crawford', 'Henry', 'Boyd', 'Mason', 'Morales', 'Kennedy', 'Warren', 'Dixon', 'Ramos', 'Reyes', 'Burns', 'Gordon', 'Shaw', 'Holmes', 'Rice', 'Robertson', 'Henderson', 'Patterson', 'Red', 'Willoughby', 'Fitzgerald']

    # name_lengths: list of name lengths
    # [5, 7, 8, 5, 5, 5, 6, 6, ... 6, 4, 9, 9, 9, 3, 10, 10]
    name_lengths = []

    # freq: composite structure with the three most and the three least frequent
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
    #
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
    freq = None


    def solution(self): # -> Self: from Python 3.10
        """
        Method to create freq structure.
        """
        self.freq = ...
        return self


    def avg_length(self) -> float:
        """
        Return average name length.
        """
        return 0.0


    def print_name_lengths(self): # -> Self: from Python 3.10
        """
        Print list of name lengths.
        """
        print(f'Name lengths: {self.name_length}')
        return self


    def print_freq(self): # -> Self: from Python 3.10
        """
        Pretty-print freq struct.
        """
        ...
        return self


    def print_avg_length(self): # -> Self: from Python 3.10
        """
        Print average name length.
        """
        print(f'The average name length: {self.avg_length():.2f}')
        return self


    def __init__(self, names=None):
        """
        Constructor.
        """
        if names != None and type(names==list):
            self.names = names
        self.solution()


if __name__ == '__main__':
    """
    Main driver that starts program when called from command line.
    """
    #
    n1 = C3_names()   # use default list in C2_numbers
    n1.print_name_lengths() \
        .print_freq() \
        .print_avg_length()     # method chaining
    #
    # n2 = C3_names(['Hans', 'Gretchen', 'Lotte', 'Gudrun', 'Ingrid'])   # use constructor list
    # n2.print_freq() \
    #     .print_avg_length()
```
Output:
```py
name length: [5, 7, 8, 5, 5, 5, 6, 6, ... 6, 4, 9, 9, 9, 3, 10, 10]
```
Compute which name lengths are the three most and the three least frequent.

Output for `n1`:
```py
Names: ['Smith', 'Johnson', 'Williams', ... 'Red', 'Willoughby', 'Fitzgerald']
\\
Name lengths: [5, 7, 8, 5, 5, 5, 6, 6, ... 9, 9, 9, 3, 10, 10]
\\
The three most frequent name lenghts are:
 - 23 names of length 5: ['Smith', 'Jones', 'Brown', 'Davis', 'Moore'] ...
 - 16 names of length 6: ['Miller', 'Wilson', 'Taylor', 'Thomas', 'Harris'] ...
 -  7 names of length 7: ['Johnson', 'Jackson', 'Freeman', 'Simpson', 'Stevens'] ...
The three least frequent name lenghts are:
 -  2 names of length 10: ['Willoughby', 'Fitzgerald']
 -  3 names of length 3: ['Lee', 'Cox', 'Red']
 -  5 names of length 9: ['Rodriguez', 'Hernandez', 'Robertson', 'Henderson', 'Patterson']
The average name length: 5.94
```
Output for `n2`:
```py
Names: ['Hans', 'Gretchen', 'Lotte', 'Gudrun', 'Ingrid']
Name lengths: [4, 8, 5, 6, 6]
The three most frequent name lenghts are:
 -  2 names of length 6: ['Gudrun', 'Ingrid']
 -  1 names of length 8: ['Gretchen']
 -  1 names of length 5: ['Lotte']
The three least frequent name lenghts are:
 -  1 names of length 4: ['Hans']
 -  1 names of length 5: ['Lotte']
 -  1 names of length 8: ['Gretchen']
The average name length: 5.80
```
Pull file [C3_names_test.py](https://github.com/sgra64/cs4bigdata/blob/main/C_expressions_py/C3_names_test.py) into same directory. Run unit tests to confirm the 
correctness of your solution.
```sh
test_url=https://raw.githubusercontent.com/sgra64/cs4bigdata/main/C_expressions_py/C3_names_test.py
curl -O $(echo $test_url)           # download C2_numbers_test.py from URL
python C3_names_test.py             # run tests from test file

curl $(echo $test_url) | python     # run tests from URL (use to demonstrate)
```
Output:
```sh
Ran 18 tests in 0.001s

OK
Unit testing using test objects:
 - test_a_name_lengths_nam_1()
 - test_a_name_lengths_nam_2()
 - test_a_name_lengths_nam_3()
 - test_a_name_lengths_nam_4()
 - test_a_name_lengths_nam_5()
 - test_a_name_lengths_nam_6()
 - test_b_least_frequent_names_nam_1()
 - test_b_most_frequent_names_nam_1()
 - test_c_least_frequent_names_nam_2()
 - test_c_most_frequent_names_nam_2()
 - test_d_least_frequent_names_nam_3()
 - test_d_most_frequent_names_nam_3()
 - test_e_least_frequent_names_nam_4()
 - test_e_most_frequent_names_nam_4()
 - test_f_least_frequent_names_nam_5()
 - test_f_most_frequent_names_nam_5()
 - test_g_least_frequent_names_nam_6()
 - test_g_most_frequent_names_nam_6()
 - test_h_average_name_lengths()
---> 19/19 TESTS SUCCEEDED
```
(6 Pts)
