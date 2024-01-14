import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from check import check

cases = [
    ([{'a': 1, 'b': 'two', 'c': 3, 'd': 4}, 'a', 'd'], {'b': 'two', 'c': 3}),
    ([{'a': 1, 'b': 'two', 'c': 3, 'd': 4}, 'a'], {'b': 'two', 'c': 3, 'd': 4}),
    ([{'a': 1, 'b': 'two', 'c': 3, 'd': 4}], {'a': 1, 'b': 'two', 'c': 3, 'd': 4}),
    ([{'a': 1, 'b': 'two'}, 'c', 'd', 'e'], {'a': 1, 'b': 'two'}),
    ([{}, 'a'], {}),
]

check(cases)('except')
