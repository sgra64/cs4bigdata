## Assignment A: Software Setup for CS4BigData Class
This class will use the following software:
 - Python 3
 - git
 - Docker
 - IDE for development, e.g. VSCode (with extensions for Python, Docker, remote development)
 
 Difference between Python 2 and 3: https://www.guru99.com/python-2-vs-python-3.html

### Setup recommendations for Windows
 - Terminal software is needed to enter Unix shell (bash) commands (see [introduction](https://cs.lmu.edu/~ray/notes/bash), [tutorial](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)).
    - Alt-1: using https://www.cygwin.com (works for all versions of Windows)
    - Alt-2: Windows Subsystem for Linux (WSL, for Win10)

### Challenges
1. [Challenge 1](#1-challenge-1)
2. [Challenge 2](#2-challenge-2)
3. [Challenge 3](#3-challenge-3)
4. [Challenge 4](#4-challenge-4)
5. [Challenge 5](#5-challenge-5)

&nbsp;
### 1.) Challenge 1
Open a terminal window and type commands:

    > ls -la
    > pwd
    > whoami
    > cat ~/.bashrc
    > echo $PATH

### 2.) Challenge 2
Check python on your system (version 3+ is required, exact versions may vary). Open a terminal window and run commands:

    > python --version
    > Python 3.9.0

Check [`pip`](https://pip.pypa.io) (Python's package manager to install python libraries).
 - follow [instructions](https://pip.pypa.io/en/stable/installing) for installation:
    - [download](https://bootstrap.pypa.io/get-pip.py) the `get-pip.py` file.
    - run `python get-pip.py`
    - or update pip to latest version: `python -m pip install --upgrade pip`

Run commands in terminal:

    > pip --version
    > pip 20.2.3 from c:\opt\python38\lib\site-packages\pip (python 3.8)

Test Python:

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

Python built-in functions, https://docs.python.org/3/library/functions.html#globals

    >>> globals()
    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_
    importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module
    'builtins' (built-in)>, 'fruits': ['apple', 'pear', 'orange', 'banana']}

    >>> s = input('--> ')
    --> Monty Python's Flying Circus
    >>> s
    "Monty Python's Flying Circus"

    exit()

&nbsp;
### 3.) Challenge 3
Set up Docker.


&nbsp;
### 4.) Challenge 4
Set up Docker.


&nbsp;
### 5.) Challenge 5
Set up Docker.