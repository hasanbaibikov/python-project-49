## ***Brain_games***

### Hexlet tests and linter status:
[![Actions Status](https://github.com/hasanbaibikov/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/hasanbaibikov/python-project-49/actions).
[![Maintainability](https://api.codeclimate.com/v1/badges/5c48c65296eb2dc70c17/maintainability)](https://codeclimate.com/github/hasanbaibikov/python-project-49/maintainability)
_____

## ***Discription***

***Brain_games*** - this package includes five elementary games. The complexity of which ranges from less complex, such as determining the parity of numbers and determining the result of performing elementary arithmetic calculations, to working with finding the greatest common divisor and working with an arithmetic progression.

_______


### ***Requirements***
* [Python](https://www.python.org) - ^3.10

* [Poetry](https://python-poetry.org) - ^1.3.1

_______


### ***Installation***
______

### 1. ***For developers:***

* Install [Poetry](https://python-poetry.org) (if it is not already installed):

```python
pip install poetry
```

* Clone the repository with the project from [GitHub](https://github.com/hasanbaibikov/python-project-49):
```python
git clone git@github.com:hasanbaibikov/python-project-49.git
```

* Change to the project directory:
```python
cd python-project-49
```

* Install dependencies from [pyproject.toml](https://github.com/hasanbaibikov/python-project-49/blob/main/pyproject.toml):
```python
poetry install --dev
```

* Assemble the package:
```python
make build
```
* Install the package:
```python
make package-install
```
____

### ***Running the linter***
* To run the linter, you need to run the command:
```python
make lint
```

______

### 2. ***For users:***
* Install the package from the repository:
```python3
python3 -m pip install --user git+https://github.com/hasanbaibikov/python-project-49
```
_____
## ***Games:***

### 1. ***Brain_even***
A game in which you need to answer the question, is a number even? If your answer does not turn out to be true, then the game will end and offer you to play again, and if you answered correctly three times in a row, then congratulations, you won!
```python
brain-even
```
[![asciicast](https://asciinema.org/a/sX9Re3DU1lbBWrnxSY5VFyn6f.svg)](https://asciinema.org/a/sX9Re3DU1lbBWrnxSY5VFyn6f)

______

### 2. ***Brain_calc***
A game in which you will need to think over the simplest arithmetic expressions consisting of addition, subtraction and multiplication. If your answer is not correct, don't be discouraged, try again. To win you need to answer three questions in a row.

```python
brain-calc
```

[![asciicast](https://asciinema.org/a/hyrPqrWXU9NPpyE7i4ME6BAf9.svg)](https://asciinema.org/a/hyrPqrWXU9NPpyE7i4ME6BAf9)

______

### 3. ***Brain_gcd***
A game that will require a lot of brain work, you will need to determine the greatest common divisor of two completely random numbers.
Also, to win, you must answer correctly three times in a row.

```python
brain-gcd
```

[![asciicast](https://asciinema.org/a/0Nxmq1DLqUifp9FVqFZxe8wgJ.svg)](https://asciinema.org/a/0Nxmq1DLqUifp9FVqFZxe8wgJ)

________

### 4. ***Brain_progression***
A game in which you need to apply your logical skills. You will need to determine which number is missing, in a specific arithmetic progression. The game still lasts up to three wins in a row.
```python
brain-progression
```

[![asciicast](https://asciinema.org/a/9ZZgGkNpCOK5t46yThz26cF6p.svg)](https://asciinema.org/a/9ZZgGkNpCOK5t46yThz26cF6p)

_______

### 5. ***Brain_prime***
A game that will require elementary arithmetic knowledge. You will need to determine whether a completely random number is prime. The game lasts up to three wins in a row, and if your answer does not match the true one, do not worry, try again!
```python
brain-prime
```

[![asciicast](https://asciinema.org/a/KYTzOdYczF1tLJfj1rERo0rVS.svg)](https://asciinema.org/a/KYTzOdYczF1tLJfj1rERo0rVS)
