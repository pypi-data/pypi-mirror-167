# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['smplstack']
setup_kwargs = {
    'name': 'smplstack',
    'version': '0.1.0',
    'description': 'Simple stack implementation',
    'long_description': 'Simple stack implementation.\n\nUse:\n .push method to add a new element into stack\n .pop to delete and return last element from stack\n .peek to return a last element from stack\n .delete to delete a last element from stack\n .show to print elements from stack \n .clear to clear a stack\n .pop_all to delete and return all elements from stack\n .peek_all to return all elements from stack\nAlso, this stack is iterable. The iteration starts from the last element of the stack.',
    'author': 'exerussus',
    'author_email': 'solovyov.production@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
