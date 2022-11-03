"""
Simple time formatter for us, ms, sec
"""
def fmt_time(t):
    return f'{round(t*1e6, 1)} us' if t < 1e-3 else \
        f'{round(t*1e3, 1)} ms' if t < 1.0 else \
        f'{round(t, 1)} sec'
