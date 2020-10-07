## Software Setup for CS4DS

 - Unix bash
 - Python 3+
 - pip
 - Jupyter Lab
 - Python IDE, e.g. PyCharm

&nbsp;
#### Set up Unix-bash (Windows only)

 - A terminal window is needed to enter commands using a Unix shell such as bash (see [introduction](https://cs.lmu.edu/~ray/notes/bash), [tutorial](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)).
 - While on Linux and Mac laptops, a shell is preinstalled, Windows requires additional setup:
    - Alt-1: using https://www.cygwin.com (works for all versions of Windows)
    - Alt-2: Windows Subsystem for Linux (WSL, for Win10)
    - Alt-3: https://cmder.net

Test, open terminal window and type shell commands:

    > ls -la
    > pwd
    > whoami
    > cat ~/.bashrc
    > echo $PATH

&nbsp;
#### Install Python 3+

 - install from https://www.python.org/downloads
 - difference between python 2 and 3, https://www.guru99.com/python-2-vs-python-3.html

Test, open terminal window and type:

    > python --version
    > Python 3.8.5

    > python
    Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win3
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
#### Install pip

 - [`pip`](https://pip.pypa.io) is Python's package manager needed to install new python packages.
 - follow [instructions](https://pip.pypa.io/en/stable/installing) for installation:
    - [download](https://bootstrap.pypa.io/get-pip.py) the `get-pip.py` file.
    - run `python get-pip.py`
    - or update pip to latest version: `python -m pip install --upgrade pip`

Test:

    > pip --version
    > pip 20.2.3 from c:\opt\python38\lib\site-packages\pip (python 3.8)

&nbsp;
#### Install Jupyter Lab

 - [Jupyter](https://jupyter.org) is an interactive python environment that has become popular among data scientists for developing and sharing their projects.
 - Jupyter Lab is a newer version of Jupyter Notebook, learn about the [differences](https://stackoverflow.com/questions/50982686/what-is-the-difference-between-jupyter-notebook-and-jupyterlab).
 - Follow [installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) instructions: `pip install jupyterlab`

Test, start Jupyter server, opens browser:

    > jupyter lab

&nbsp;
#### Install a Python IDE

 - An Integrated Development Environment (IDE) is useful for more serious program development. IDE support additional functionality such as debugging, code management, code quality control, test and test coverage, etc.
 - **PyCharm** is a fully-featured IDE for Python, [download](https://www.jetbrains.com/pycharm/download) and follow instructions.

