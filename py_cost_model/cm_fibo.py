import timeit
import py_cost_model.cm_kernel as pcm

counter = 0         # global counter for function executions
fib_result = 0      # global var for passing function result back from timeit execution


# Fibonacci numbers are defined (starting with n=0):
# n:       0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11,  12,    20,      30,          40, ...
# fib(n):  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 6.765, 832.040, 102.334.155, ...
#
def fib_1(_n: int) -> int:
    global fib_result, counter
    fib_result = 0 if _n <= 0 else 1

    if _n > 2:
        fib_result = fib_1(_n - 2) + fib_1(_n - 1)

    counter = counter + 1
    return fib_result


def print_fib(_func, _numbers: []):
    global _fib_func, counter
    _fib_func = _func   # global to pass via timeit statement
    for _n in _numbers:

        _elapsed_time = timeit.timeit(  # in ms
            #setup='from __main__ import f123',
            stmt='_fib_func(' + str(_n) + ')',
            number=1,
            globals=globals(),
        )

        out = ''
        out += str('fib(' + str(_n) + ') -> ' + str(fib_result)).ljust(24)
        out += 'counter: ' + str(counter).rjust(8)
        out = out.ljust(48) + 'time: ' + str(pcm.fmt_time(_elapsed_time)).rjust(8)
        # out += str(_n) + '\t' + str(counter)
        print(out)
        counter = 0


print_fib(fib_1, range(21))
#print_fib(fib_1, [40])
print()


def fib_meomized(_n: int, _memory=[]) -> int:
    global fib_result, counter
    _memory = _memory if len(_memory) > 0 else [0] * _n
    fib_result = 0 if _n <= 0 else 1

    if _n > 2:
        if _memory[_n - 1] <= 0:
            _memory[_n - 1] = fib_meomized( _n - 1, _memory )

        if _memory[_n - 2] <= 0:
            _memory[_n - 2] = fib_meomized( _n - 2, _memory )

        fib_result = _memory[_n - 2] + _memory[_n - 1]

    counter = counter + 1
    return fib_result


#print_fib(fib_meomized, range(21))
#print_fib(fib_meomized, [100])
