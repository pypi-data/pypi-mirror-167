# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iter_model']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'iter-model',
    'version': '1.2.1',
    'description': 'iter-model uses a method approach instead of individual functions to work with iterable objects.',
    'long_description': '<p align="center">\n    <a href="https://volodymyrbor.github.io/iter_model">\n        <img src="docs/img/iter_model-logos_transparent.png" alt="IterModel" width="300">\n    </a>\n</p>\n\n\n<a href="https://pypi.org/project/iter_model" target="_blank">\n    <img src="https://img.shields.io/pypi/pyversions/iter_model.svg?color=%2334D058" alt="Supported Python versions">\n</a>\n<a href="https://pypi.org/project/iter_model" target="_blank">\n    <img src="https://img.shields.io/pypi/v/iter_model?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n<a href="https://github.com/VolodymyrBor/iter_model/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">\n    <img src="https://github.com/VolodymyrBor/iter_model/workflows/Test/badge.svg?event=push&branch=master" alt="Test">\n</a>\n\n[![Supported Versions](https://img.shields.io/badge/coverage-100%25-green)](https://shields.io/)\n[![Supported Versions](https://img.shields.io/badge/poetry-✅-grey)](https://shields.io/)\n[![Supported Versions](https://img.shields.io/badge/async-✅-grey)](https://shields.io/)\n[![Supported Versions](https://img.shields.io/badge/mypy-✅-grey)](https://shields.io/)\n\n---\n\n**iter_model** - provides a convenient API for interacting with iterable objects ([Iterable]).\niter_model uses a methods approach instead of individual functions.\n\niter_model also provides **async** analog of all methods. \nThis is useful when interacting with asynchronous iterable objects ([AsyncIterable]), \nbecause python does not have ready functions for these cases.\n\nTherefore, **iter_model** provides **SyncIter** class for [Iterable],\nand **AsyncIter** for [AsyncIterable].\n\n---\n\n## Example\n\n```python\nfrom iter_model import SyncIter\n\nit = SyncIter(range(10))  # SyncIter for sync iterables\nresult = (\n    it.where(lambda x: x % 2 == 0)  # filter only odd values\n    .take(3)  # take first 3 value\n    .map(lambda x: x ** 2)  # square all values\n)\nprint(result.to_list())\n```\n\n## Links\n\n**Source code**: [github.com/VolodymyrBor/iter_model](https://github.com/VolodymyrBor/iter_model)\n\n**Documentation**: [iter_model](https://volodymyrbor.github.io/iter_model/)\n\n[Iterable]: https://docs.python.org/3/library/typing.html#typing.Iterable\n[AsyncIterable]: https://docs.python.org/3/library/typing.html#typing.AsyncIterable\n',
    'author': 'volodymyrb',
    'author_email': 'volodymyr.borysiuk0@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/VolodymyrBor/iter_model',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
