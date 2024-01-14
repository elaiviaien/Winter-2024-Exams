import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from check import check

cases = [
    [[{'a': 1, 'c': 'hello'}, {'a': 1, 'c': 'hello'}], True],
    [[{'a': 1, 'c': 'hello'}, {'a': 2, 'c': 'hello'}], False],
    [[{'a': 2, 'c': 'hello'}, {'a': 1, 'c': 'hello'}], False],
    [[{'a': 1, 'c': 'helo'}, {'a': 1, 'c': 'hello'}], False],
    [[{'a': 1, 'c': 'hello'}, {'a': 1, 'c': 'helo'}], False],
    [[{'c': 'hello', 'a': 1}, {'a': 1, 'c': 'hello'}], False],
    [[{'a': 1, 'c': 'hello'}, {'c': 'hello', 'a': 1}], False],
]

check(cases)('compare')