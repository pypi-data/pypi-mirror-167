<p align="center">
    <a href="https://github.com/kolitiri/validargs/actions/workflows/test.yml" target="_blank">
        <img src="https://github.com/kolitiri/validargs/actions/workflows/test.yml/badge.svg" alt="Test">
    </a>
    <a href="https://pypi.org/project/validargs" target="_blank">
        <img src="https://img.shields.io/pypi/v/validargs?color=%2334D058&label=pypi" alt="Package version">
    </a>
    <a href="https://pypi.org/project/validargs" target="_blank">
        <img src="https://img.shields.io/pypi/pyversions/validargs.svg?color=%2334D058" alt="Supported Python versions">
    </a>
</p>

# Validargs

1. [Description](#description)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributions](#contributions)


# Description <a name="description"></a>

A function decorator that is using the [inspect](https://docs.python.org/3/library/inspect.html) library to validate arguments passed in the decorated function.

It allows writing complex and re-usable argument validation rules injected directly in the function signature.

The validation is not based on type annotations, which allows to go beyond the basic type validations.

NOTE: [pydantic](https://pydantic-docs.helpmanual.io/) is a far more advanced and very well supported library, but requires to model your arguments. If you haven't already, make sure you check it out.

**Source Code**: https://github.com/kolitiri/validargs

# Requirements <a name="requirements"></a>
Python 3.8+

# Installation <a name="installation"></a>
```python
pip install validargs
```

# Usage <a name="usage"></a>
For best results, use the argument definitions syntax as of python v3.8.

Use "/" and "*" to distinguish between "positional only", "positional or keyword" and "keyword only" arguments.

Define custom validation rules using the `Validator` class.

```python
""" my_app.py """
from typing import Any

from validargs import validated, Validator


def positive_number(argument: int) -> None:
    if argument is None:
        return None
    if type(argument) is not int:
        raise TypeError("Number must be an integer")
    if argument <= 0:
        raise Exception("Number must be a positive integer")


def short_str(argument: str) -> None:
    if argument is None:
        return None
    if len(argument) > 20:
        raise Exception("String too long")
```

Use the `validated` decorator to decorate the functions that you want validated.

```python
@validated
def my_function(
    positive_number: int = Validator(positive_number),
    /,
    short_string: str = Validator(short_str),
    *,
    another_short_string: str = Validator(short_str),
):
    pass
```

You can mix and match arguments with and without validators and also assign default values.

```python
@validated
def my_function(
    positive_number: int = Validator(positive_number, default_value=10), # Validator with default value
    non_validated_arg: int = 0, # Regular argument with default value
    /,
    short_string: str = Validator(short_str), # Validator without default value
    *,
    another_validated_argument: str, # Regular argument without default value
):
    pass
```

# Contributions  <a name="contributions"></a>
If you want to contribute to the package, please have a look at the CONTRIBUTING.md file for some basic instructions.
Feel free to reach me in my email or my twitter account, which you can find in my github profile!

# License
This project is licensed under the terms of the MIT license.

# Authors
Christos Liontos