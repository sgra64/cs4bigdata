# Assignment D: Data Streams &nbsp; (<span style="color:red">12 Pts</span>)

This assignment demonstrates classes and functions.

### Challenges
1. [Challenge 1:](#1-challenge-1) Data streams in Python
2. [Challenge 2:](#2-challenge-2) complete *map()* function
3. [Challenge 3:](#3-challenge-3) complete *reduce()* function
4. [Challenge 4:](#4-challenge-4) complete *sort()* function
5. [Challenge 5:](#5-challenge-5) Pipeline for product codes
6. [Challenge 6:](#6-challenge-6) run unit tests


&nbsp;
### 1.) Challenge 1
Data streams are powerful abstractions for data-driven applications that also work in distributed environments. Big Data platforms often build on streams such as
[Spark Streams](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
or
[Kafka](https://kafka.apache.org/documentation/streams).

A data stream starts with a *source* (here just a list of names) followed by a pipeline of *chainable operations* performed on each data element passing through the stream. Results can be collected at the *terminus* of the stream.

Pull [stream.py](https://github.com/sgra64/cs4bigdata/blob/main/D_functions_and_streams/stream.py).

```py
class Stream:
    """
    Class of a data stream comprised of a sequence of stream operations:
    """

    class __Stream_op:
        """
        Inner class of one stream operation with chainable functions.
        Instances comprise the stream pipeline.
        """

        def slice(self, i1, i2=None, i3=1):
            # function that returns new stream operation instance that slices stream
            if i2 == None:
                i2, i1 = i1, 0
            #
            return self.__new(self.__data[i1:i2:i3])

        def filter(self, filter_func=lambda d : True) ...
            # return new stream operation instance that passes only elements for
            # which filter_func yields True

        def map(self, map_func=lambda d : d) ...
            # return new stream operation instance that passes elements resulting
            # from map_func of corresponding elements in the inbound stream

        def reduce(self, reduce_func, start=0) -> any: ... 
            # terminal function that returns single value compounded by reduce_func

        def sort(self, comperator_func=lambda d1, d2 : True) ...
            # return new stream operation instance that passes stream sorted by
            # comperator_func

        def cond(self, cond: bool, conditional):
            # return same stream operation instance or apply conditional function
            # on stream operation instance if condition yields True

        def print(self) ...
            # return unchanged (same) stream operation instance and print as side effect

        def count(self) -> int: ...
            # terminal function that returns number of elements in terminal stream

        def get(self) -> any: ...
            # terminal function that returns final stream data
```

Application of the stream can demonstrated by the example of a stream of names. The stream is instantiated from the `names` list. The `source()` - method returns the first `__Stream_op` - instance onto which chainable stream methods can be attached.

The stream in the example filters names of lenght = 4, prints those names and counts their number. The *lambda*-expression controls the filter process. Only names of length 4 pass to subsequent pipeline operations.

```py
names = ['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez',
    'Howe', 'Ray', 'Navarro', 'Talley', 'Bernard', 'Gomez', 'Hamilton',
    'Case', 'Petty', 'Lott', 'Casey', 'Hall', 'Pena', 'Witt', 'Joyner',
    'Raymond', 'Crane', 'Hendricks', 'Vance', 'Cleveland', 'Duncan', 'Soto',
    'Brock', 'Graham', 'Nielsen', 'Rutledge', 'Strong', 'Cox']

result = Stream(names).source() \
    .filter(lambda n : len(n) == 4) \
    .print() \
    .count()

print(f'found {result} names with 4 letters.')
```

Output:
```c++
['Gill', 'Howe', 'Case', 'Lott', 'Hall', 'Pena', 'Witt', 'Soto']
found 8 names with 4 letters.
```
(1 Pts)


&nbsp;

### 2.) Challenge 2
Complete the `map()` function in
[stream.py](https://github.com/sgra64/cs4bigdata/blob/main/D_functions_and_streams/stream.py) so that the example produces the desired result: Names are mapped to name lengths for the first 8 names. Name lengths are then compounded to a single result.

```py
result = Stream(names).source() \
    .slice(8) \
    .print() \
    .map(lambda n : len(n)) \
    .print()
```

Output:
```c++
['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez', 'Howe', 'Ray']
[8, 4, 6, 10, 7, 7, 4, 3]
```
(2 Pts)


&nbsp;

### 3.) Challenge 3
Complete the `reduce()` function in
[stream.py](https://github.com/sgra64/cs4bigdata/blob/main/D_functions_and_streams/stream.py) so that name lengths are compounded (added one after another) to a single result.

```py
result = Stream(names).source() \
    .slice(8) \
    .print() \
    .map(lambda n : len(n)) \
    .print() \
    .reduce(lambda x, y : x + y)
#
print(f'compound number of letters in names is: {result}.')
```

Output:
```c++
['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez', 'Howe', 'Ray']
[8, 4, 6, 10, 7, 7, 4, 3]
compound number of letters in names is: 49.
```
(2 Pts)


3.1) Test your implementation to also work for the next example that produces
a single string of all n-letter names:

```py
n = 5
result = Stream(names).source() \
    .filter(lambda name : len(name) == n) \
    .print() \
    .map(lambda n : n.upper()) \
    .reduce(lambda x, y : str(x) + str(y), '')
#
print(f'compounded {n}-letter names: {result}.')
```

Output for n=3 and n=5:
```c++
['Ray', 'Cox']
compounded 3-letter names: RAYCOX.

['Gomez', 'Petty', 'Casey', 'Crane', 'Vance', 'Brock']
compounded 5-letter names: GOMEZPETTYCASEYCRANEVANCEBROCK.
```
(1 Pts)


&nbsp;

### 4.) Challenge 4
Complete the `sort()` function in
[stream.py](https://github.com/sgra64/cs4bigdata/blob/main/D_functions_and_streams/stream.py)
so that the example produces the desired result (use Python's built-in `sort()` or `sorted()` functions).

```py
Stream(names).source() \
    .slice(8) \
    .print('unsorted: ') \
    .sort() \
    .print('  sorted: ')
```

Output:
```c++
unsorted: ['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez', 'Howe', 'Ray']
  sorted: ['Buckner', 'Gill', 'Gonzalez', 'Hardin', 'Howe', 'Marquez', 'Ray', 'Richardson']
```
(1 Pts)

4.1) Understand the sorted sequence below and define a `comperator` (expression that compares two elements (n1, n2) and yields `-1` if n1 should come before n2, `+1` if n1 must be after n2 or `0` if n1 is equal to n2):

```py
len_alpha_comperator = lambda ...

Stream(names).source() \
    .sort(len_alpha_comperator) \
    .print('sorted: ')
```

Output:
```c++
sorted: ['Cox', 'Ray', 'Case', 'Gill', 'Hall', 'Howe', 'Lott', 'Pena', 'Soto', 'Witt', 'Brock', 'Casey', 'Crane', 'Gomez', 'Petty', 'Vance', 'Duncan', 'Graham', 'Hardin', 'Joyner', 'Strong', 'Talley', 'Bernard', 'Buckner', 'Marquez', 'Navarro', 'Nielsen', 'Raymond', 'Gonzalez', 'Hamilton', 'Rutledge', 'Cleveland', 'Hendricks', 'Richardson']
```
(1 Pts)

4.2) Extend the pipeline so that it produces the following output:
```c++
sorted: [('Cox', 'Xoc', 3), ('Ray', 'Yar', 3), ('Brock', 'Kcorb', 5), ('Casey', 'Yesac', 5), ('Crane', 'Enarc', 5), ('Gomez', 'Zemog', 5), ('Petty', 'Yttep', 5), ('Vance', 'Ecnav', 5), ('Bernard', 'Dranreb', 7), ('Buckner', 'Renkcub', 7), ('Marquez', 'Zeuqram', 7), ('Navarro', 'Orravan', 7), ('Nielsen', 'Neslein', 7), ('Raymond', 'Dnomyar', 7), ('Cleveland', 'Dnalevelc', 9), ('Hendricks', 'Skcirdneh', 9)]
\\
16 odd-length names found.
```
(1 Pts)


&nbsp;

### 5.) Challenge 5
Build a pipeline that produces batches of five 6-digit numbers with prefix 'X'.
Numbers are in ascending order within each batch and end with a 1-digit checksum
after a dash. The checksum is the sum of all six digits of the random number modulo 10.

```py
for i in range(1, 5):
    # Stream of 5 random numbers from integer range, feel free to change
    codes = Stream([random.randint(100000,999999) for j in range(5)]).source() \
        ... \
        .get()
    #
    print(f'batch {i}: {codes}')
```

Output:
```c++
batch 1: ['X102042-9', 'X102180-2', 'X103228-6', 'X104680-9', 'X106782-4']
batch 2: ['X200064-2', 'X200732-4', 'X202090-3', 'X209056-2', 'X211464-8']
batch 3: ['X300186-8', 'X301416-5', 'X305962-5', 'X307938-0', 'X312524-7']
batch 4: ['X400216-3', 'X401436-8', 'X401682-1', 'X405256-2', 'X406376-6']
```
(1 Pts)

5.1) Alter the pipeline such that it produces only even digit codes:
```c++
batch 1: ['X226840-2', 'X284240-0', 'X448288-4', 'X804080-0', 'X888620-2']
batch 2: ['X220640-4', 'X248066-6', 'X648466-4', 'X680404-2', 'X882868-0']
batch 3: ['X262626-4', 'X608662-8', 'X626404-2', 'X662424-4', 'X846228-0']
batch 4: ['X224200-0', 'X282204-8', 'X448426-8', 'X600282-8', 'X802882-8']
```
(1 Pts)


&nbsp;

### 6.) Challenge 6
Pull file [stream_test.py](https://github.com/sgra64/cs4bigdata/blob/main/D_functions_and_streams/stream_test.py) into same directory. Run unit tests to confirm the 
correctness of your solution.
```sh
test_url=https://raw.githubusercontent.com/sgra64/cs4bigdata/main/D_functions_and_streams/stream_test.py
curl -O $(echo $test_url)           # download stream_test.py from URL
python stream_test.py               # run tests from test file

curl $(echo $test_url) | python     # run tests from URL (use to demonstrate)
```
Output:
```sh
Ran 12 tests in 0.001s

OK
Unit testing using test objects:
 - test_filter_1()
 - test_filter_11()
 - test_filter_12()
 - test_filter_13()
 - test_map_2()
 - test_map_21()
 - test_reduce_3()
 - test_reduce_31()
 - test_sort_4()
 - test_sort_41()
 - test_sort_42()
 - test_stream_generation()
---> 12/12 TESTS SUCCEEDED
```
(1 Pts)
