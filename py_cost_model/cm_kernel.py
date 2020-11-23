#
# Source:
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/python-cost-model
#
# Converted from python 2 to python 3 with:
# https://www.pythonconverter.com
# further changes labelled with: @orig svgr

# based on timing.py
# Author: Ronald L. Rivest
# Date last modified: March 6, 2007

import math
import sys
import scipy.optimize


# Parameter generation routines

def lg(x):
    return math.log(x ) /math.log(2.0)

def sqrt(x):
    return math.sqrt(x)

def make_param_list(spec_string ,growth_factor):
    """
    Generate a list of dictionaries
    given maximum and minimum values for each range.
    Each min and max value is a *string* that can be evaluted;
    each string may depend on earlier variable values
    Values increment by factor of growth_factor from min to max
    Example:
       make_param_list("1<=n<=1000")
       make_param_list("1<=n<=1000;1<=m<=1000;min(n,m)<=k<=max(n,m)")
    """
    var_list = []
    spec_list = spec_string.split(";")
    D = {}
    D['lg' ] = lg
    D['sqrt'] = sqrt
    D_list = [D]
    for spec in spec_list:
        spec_parts = spec.split("<=")
        assert len(spec_parts ) == 3
        lower_spec = spec_parts[0]
        var_name = spec_parts[1]
        assert len(var_name ) == 1
        var_list.append(var_name)
        upper_spec = spec_parts[2]
        new_D_list = []
        for D in D_list:
            new_D = D.copy()
            val = eval(lower_spec ,D)
            while val <= eval(upper_spec ,D):
                new_D[var_name] = val
                new_D_list.append(new_D.copy())
                val *= growth_factor
        D_list = new_D_list
    # for D in D_list: print D
    return (var_list ,D_list)


def fit(var_list, param_list, run_times, f_list):
    """
    Return matrix A needed for least-squares fit.
    Given:
        list of variable names
        list of sample dicts for various parameter sets
        list of corresponding run times
        list of functions to be considered for fit
            these are *strings*, e.g. "n","n**2","min(n,m)",etc.
    prints:
        coefficients for each function in f_list
    """
    print("var_list" ,var_list)
    print("Function list:" ,f_list)
    print("run times:", end=' ')
    for i in range(len(param_list)):
        print()
        for v in var_list:
            print(v ,"= %6s " %param_list[i][v], end=' ')
        print(": %8f " %run_times[i] ,"microseconds", end=' ')
        # print "  n = %(n)6s"%param_list[i],run_times[i],"microseconds"
    print()
    rows = len(run_times)
    cols = len(f_list)
    A = [ [0 for j in range(cols)] for i in range(rows) ]
    for i in range(rows):
        D = param_list[i]
        for j in range(cols):
            A[i][j] = float(eval(f_list[j] ,D))
    b = run_times
    # print "A:"
    # print A
    # print "b:"
    # print b

    # (x,resids,rank,s) = scipy.linalg.lstsq(A,b)
    (x ,resids ,rank ,s) = fit2(A ,b)

    print("Coefficients as interpolated from data:")
    for j in range(cols):
        sign = ''
        if x[j ] >0 and j> 0:
            sign = "+"
        elif x[j] > 0:
            sign = " "
        print("%s%g*%s" % (sign, x[j], f_list[j]))

    print("(measuring time in microseconds)")
    print("Sum of squares of residuals:", resids)
    print("RMS error = %0.2g percent" % (math.sqrt(resids / len(A)) * 100.0))
    # print "Rank:",rank
    # print "SVD:",s
    sys.stdout.flush()


def fit2(A, b):
    """ Relative error minimizer """

    def f(x):
        assert len(x) == len(A[0])
        resids = []
        for i in range(len(A)):
            sum = 0.0
            for j in range(len(A[0])):
                sum += A[i][j] * x[j]
            relative_error = (sum - b[i]) / b[i]
            resids.append(relative_error)
        return resids

    ans = scipy.optimize.leastsq(f, [0.0] * len(A[0]))
    # print "ans:",ans
    if len(A[0]) == 1:
        x = [ans[0]]
    else:
        x = ans[0]
    resids = sum([r * r for r in f(x)])
    return (x, resids, 0, 0)


def fmt_time(_time: float, _unit=-1, _label='') -> str:
    _units = ['s', 'ms', '\u00B5s', 'ps']   # units: s, ms, µs
    _unit_factor = [1.0, 1000.0, 1000000.0, 1000.0 * 1000000.0]   # factor for unit adjustments
    _rounded_digits = [2, 2, 0, 0]          # rounded digits
    _i = _unit
    if _i < 0 or _i >= len(_units):
        _i = 0 if _time >= 1.0 else (1 if _time >= 0.001 else 2)

    _t = _time * _unit_factor[_i]
    _rdg = _rounded_digits[_i] if _t >= 1.0 else 3 if _t >= 0.01 else 5
    _t = round(_t, _rdg)
    _fmt = _label + '{:.' + str(_rdg) + 'f}' + _units[_i]   # "{:.3f}"
    return _fmt.format(_t) #.rjust(20, '-')
