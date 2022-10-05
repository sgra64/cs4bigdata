# Assignment A: Setup Python &nbsp; (<span style="color:red">10 Pts</span>)

This assignment will setup your base Python enviroment. If you already have it, simply run challenges and answer questions (if any). If you cannot run challenges, set up the needed software.

### Challenges
1. [Challenge 1:](#1-challenge-1) Terminal
2. [Challenge 2:](#2-challenge-2) Python3
3. [Challenge 3:](#3-challenge-3) pip
4. [Challenge 4:](#4-challenge-4) Test Python
5. [Challenge 5:](#5-challenge-5) Python built-in functions

&nbsp;
### 1.) Challenge 1
Open a terminal and type commands:
```sh
> ls -la
> pwd
> whoami
> cat ~/.profile
> cat ~/.bashrc
> echo $PATH
```
 Explain commands. If you are not familiar, find out about these basic Unix shell (bash, zsh, ...) commands (e.g. from [introduction](https://cs.lmu.edu/~ray/notes/bash) or [tutorial](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)).
 
 On *Mac*, refer to .zshrc instead of .bashrc.
 
 On *Windows*, consider using a Unix emulator such as [cygwin](https://www.cygwin.com), the built-in Windows Subsystem for Linux [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) or a [Linux VM](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox).
 *CMD.EXE* is no option, *Powershell* is not incompatible to Unix standards.

(2 Pts)

&nbsp;
### 2.) Challenge 2
Check if you have Python 3 installed on your system. Name three differences between [Python 2 and 3](https://www.guru99.com/python-2-vs-python-3.html#7). 

Run commands in terminal (exact version 3.x.x may vary):
```sh
> python --version
Python 3.9.0
```
(2 Pts)

&nbsp;
### 3.) Challenge 3
Check if you have a Python package manager installed (pip, conda, ... ). [`pip`](https://pip.pypa.io) is Python's default package manager needed to install additional python packages and libraries.

Follow [instructions](https://pip.pypa.io/en/stable/installing) for installation:
- [download](https://bootstrap.pypa.io/get-pip.py) the `get-pip.py` file.
- run `python get-pip.py`
- or update pip to latest version: `python -m pip install --upgrade pip`

Run commands in terminal:
```sh
> pip --version
pip 22.2.2 from c:\opt\python38\lib\site-packages\pip (python 3.9)
```
(2 Pts)

&nbsp;
### 4.) Challenge 4
Test Python:
```py
> python
Python 3.9.0 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win3
Type "help", "copyright", "credits" or "license" for more information.

>>> print('Hello World')
Hello World

>>> help('modules')
...lists installed python packages

>>> 2+3*4
14

>>> x = 2+3*4
>>> x
14

>>> fruits = ['apple', 'pear', 'orange', 'banana']
>>> print(fruits)
>>> fruits
['apple', 'pear', 'orange', 'banana']

>>> print(fruits[2])
orange
```

Create a file *print_sys.py* with following content.
```py
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
```

Run the file. Output varies depending on your system.
```
> python print_sys.py
Python impl:    CPython
Python version: 10.0.19041
Python machine: AMD64     
Python system:  Windows   
Python version: 3.9.0     
```
(2 Pts)

&nbsp;
### 5.) Challenge 5
Learn about Python's [built-in functions](https://docs.python.org/3/library/functions.html). Test the [*globals()*](https://docs.python.org/3/library/functions.html#globals) function.
```py
  >>> globals()
  {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_
  importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module
  'builtins' (built-in)>, 'fruits': ['apple', 'pear', 'orange', 'banana']}
```
Test the [*input()*](https://docs.python.org/3/library/functions.html#input) function.
```py
  >>> s = input('--> ')
  --> Monty Python's Flying Circus
  >>> s
  "Monty Python's Flying Circus"
  exit()
```
(2 Pts)
