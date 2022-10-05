import platform

impl = platform.python_implementation()
ver = platform.version()
mach = platform.machine()
sys = platform.system()

print('Python impl:    ' + impl)
print('Python version: ' + ver)
print('Python machine: ' + mach)
print('Python system:  ' + sys)
print('Python version: ' + platform.python_version())
