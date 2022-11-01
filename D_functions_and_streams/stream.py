import random
from functools import cmp_to_key


class Stream:
    """
    Class of a data stream comprised of a sequence of stream operations:
     - slice(i1, i2, i3)    # slice stream in analogy to python slicing
     - filter(filter_func)  # pass only elements for which filter_func yields True
     - map(map_func)        # pass stream where each element is mapped by map_func
     - sort(comperator_func) # pass stream sorted by comperator_func
     - cond(cond, cond_func) # pass stream or apply conditional function
     - print()              # pass unchanged stream and print as side effect

    and with terminal functions:
     - reduce(reduce_func, start)   # compound stream to single value with reduce_func
     - count()              # return number of elements in terminal stream
     - get()                # return final stream data
    """

    class __Stream_op:
        """
        Inner class of one stream operation with chainable functions.
        Instances comprise the stream pipeline.
        """
        
        def slice(self, i1, i2=None, i3=1):
            # function that returns new __Stream_op instance that slices stream
            if i2 == None:
                # flip i1, i2 for single arg, e.g. slice(0, 8), slice(8)
                i2, i1 = i1, 0
            #
            # return new __Stream_op instance with sliced __data
            return self.__new(self.__data[i1:i2:i3])


        def filter(self, filter_func=lambda d : True):
            # return new __Stream_op instance that passes only elements for
            # which filter_func yields True
            #
            return self.__new([d for d in self.__data if filter_func(d)])


        def map(self, map_func=lambda d : d):
            # return new __Stream_op instance that passes elements resulting
            # from map_func of corresponding elements in the inbound stream
            #
            # input data is list of current instance: self.__data
            # mapping means a new list needs to be created with same number of
            # elements, each obtained by applying map_func

            # create new data for next __Stream_op instance from current instance
            # data: self.__data
            new_data = self.__data      # <-- compute new data here

            # create new __Stream_op instance with new stream data
            new_stream_op_instance = self.__new(new_data)
            return new_stream_op_instance


        def reduce(self, reduce_func=lambda compound, d : compound + d, start=0) -> any:
            # terminal function that returns single value compounded by reduce_func
            #
            compound = 0                # <-- compute compound result here

            return compound


        def sort(self, comperator_func=lambda n1, n2 : -1 if n1 < n2 else 1):
            # return new __Stream_op instance that passes stream sorted by
            # comperator_func
            #
            # create new data for next __Stream_op instance from current instance
            # data: self.__data
            new_data = self.__data      # <-- compute new data here

            # create new __Stream_op instance with new stream data
            new_stream_op_instance = self.__new(new_data)
            return new_stream_op_instance


        def cond(self, cond: bool, conditional):
            # return same __Stream_op instance or apply conditional function
            # on __Stream_op instance if condition yields True
            #
            return conditional(self) if cond else self


        def print(self, prefix=''):
            # return same, unchanged __Stream_op instance and print as side effect
            #
            print(f'{prefix}{self.__data}')
            return self


        def count(self) -> int:
            # terminal function that returns number of elements in terminal stream
            #
            return len(self.__data)


        def get(self) -> any:
            # terminal function that returns final stream __data
            #
            return self.__data


        def __init__(self, _new_op_func, _data):
            self.__data = _data
            self.__new = _new_op_func    # __new_op() function injected from outer context


    def source(self):
        # return first __Stream_op instance of stream as source
        #
        return self.__streamSource


    def __new_op(self, *argv):
        # private method to create new __Stream_op instance
        return Stream.__Stream_op(self.__new_op, *argv)


    def __init__(self, _data=[]):
        # constructor to initialize instance member variables
        #
        self.__streamSource = self.__new_op(_data)


names = ['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez',
    'Howe', 'Ray', 'Navarro', 'Talley', 'Bernard', 'Gomez', 'Hamilton',
    'Case', 'Petty', 'Lott', 'Casey', 'Hall', 'Pena', 'Witt', 'Joyner',
    'Raymond', 'Crane', 'Hendricks', 'Vance', 'Cleveland', 'Duncan', 'Soto',
    'Brock', 'Graham', 'Nielsen', 'Rutledge', 'Strong', 'Cox']


try:
    # overload main class with solution class from (package, path), if exists
    ovl = ('stream_sol', 'Stream')
    Stream = getattr(__import__(ovl[0], fromlist=[ovl[1]]), ovl[1])
except ImportError:
    pass


if __name__ == '__main__':

    # Challenge 1, Data streams in Python, run the first example
    result = Stream(names).source() \
        .filter(lambda n : len(n) == 4) \
        .print() \
        .count()
    #
    print(f'found {result} names with 4 letters.')

    # Challenge 2, complete map() function
    # to map names to name lengths for the first 8 names
    Stream(names).source() \
        .slice(8) \
        .print() \
        .map(lambda n : len(n)) \
        .print()


    # Challenge 3, complete reduce() function

    # Challenge 3.1, example RAYCOX, compound single string of all n-letter names

    # Challenge 4, complete sort() function

    # Challenge 4.1, len-alpha comperator

    # Challenge 4.2, tuple output: ('Cox', 'Xoc', 3)

    # Challenge 5, Pipeline for product codes

    # Challenge 5.1, even digit codes
