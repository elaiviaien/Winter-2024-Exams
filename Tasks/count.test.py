import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from check import check

cases = [
    [[{"a": 1, "b": "two", "c": 3, "d": 4}], 8],
    [[{"a": 1, "b": "two", "c": -3, "d": 4}], 2],
    [[{"a": 0, "b": "two", "c": 0, "d": -1}], -1],
    [[{"a": -1, "b": "two", "c": -3, "d": -4}], -8],
    [[{"a": 1, "b": "two", "c": -1, "d": 0}], 0],
    [[{"a": '1', "b": "two", "c": 3, "d": 4}], 7],
]

check(cases)('count')
