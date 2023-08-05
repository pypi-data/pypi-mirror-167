# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['validargs']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'validargs',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Validargs\n\n1. [Description](#description)\n2. [Requirements](#requirements)\n3. [Installation](#installation)\n4. [Usage](#usage)\n5. [Contributions](#contributions)\n\n\n# Description <a name="description"></a>\n\nA function decorator that is using the [inspect](https://docs.python.org/3/library/inspect.html) library to validate arguments passed in the decorated function.\n\nIt allows writing complex and re-usable argument validation rules injected directly in the function signature.\n\nThe validation is not based on type annotations, which allows to go beyond the basic type validations.\n\nNOTE: [pydantic](https://pydantic-docs.helpmanual.io/) is a far more advanced and very well supported library, but requires to model your arguments. If you haven\'t already, make sure you check it out.\n\n**Source Code**: https://github.com/kolitiri/validargs\n\n# Requirements <a name="requirements"></a>\nPython 3.8+\n\n# Installation <a name="installation"></a>\n```python\npip install validargs\n```\n\n# Usage <a name="usage"></a>\nFor best results, use the argument definitions syntax as of python v3.8.\n\nUse "/" and "*" to distinguish between "positional only", "positional or keyword" and "keyword only" arguments.\n\nDefine custom validation rules using the `Validator` class.\n\n```python\n""" my_app.py """\nfrom typing import Any\n\nfrom validargs import validated, Validator\n\n\ndef positive_number(argument: int) -> None:\n    if argument is None:\n        return None\n    if type(argument) is not int:\n        raise TypeError("Number must be an integer")\n    if argument <= 0:\n        raise Exception("Number must be a positive integer")\n\n\ndef short_str(argument: str) -> None:\n    if argument is None:\n        return None\n    if len(argument) > 20:\n        raise Exception("String too long")\n```\n\nUse the `validated` decorator to decorate the functions that you want validated.\n\n```python\n@validated\ndef my_function(\n    positive_number: int = Validator(positive_number),\n    /,\n    short_string: str = Validator(short_str),\n    *,\n    another_short_string: str = Validator(short_str),\n):\n    pass\n```\n\nYou can mix and match arguments with and without validators and also assign default values.\n\n```python\n@validated\ndef my_function(\n    positive_number: int = Validator(positive_number, default_value=10), # Validator with default value\n    non_validated_arg: int = 0, # Regular argument with default value\n    /,\n    short_string: str = Validator(short_str), # Validator without default value\n    *,\n    another_validated_argument: str, # Regular argument without default value\n):\n    pass\n```\n\n# Contributions  <a name="contributions"></a>\nIf you want to contribute to the package, please have a look at the CONTRIBUTING.md file for some basic instructions.\nFeel free to reach me in my email or my twitter account, which you can find in my github profile!\n\n# License\nThis project is licensed under the terms of the MIT license.\n\n# Authors\nChristos Liontos',
    'author': 'christos.liontos',
    'author_email': 'christos.liontos.pr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kolitiri/validargs',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
