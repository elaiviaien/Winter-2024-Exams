import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from check import check

cases = [
    [[{'a': 'uno', 'b': 'due', 'c': 'tre'}, 'b', 'f'], {'a': 'uno', 'c': 'tre'}],
    [[{'a': 'uno', 'b': 'due', 'c': 'tre'}], {'a': 'uno', 'b': 'due', 'c': 'tre'}],
    [[{'a': 'uno', 'b': 'due'}, 'x', 'y'], {'a': 'uno', 'b': 'due'}],
    [[{'a': 'uno', 'b': 'due'}, 'b', 'a'], {}],
]

check(cases)('drop')
