import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from check import check

cases = [
  [[[1, 2, 'three', 4, 5, 'six'], 'int'], [1, 2, 4, 5]],
  [[[-1, 0, 1, 2], 'int'], [-1, 0, 1, 2]],
  [[[-1, 0, 1, 2], 'string'], []],
  [[[True, True, False, 1, 'six'], 'bool'], [True, True, False]],
  [[[], 'string'], []],
]

check(cases)('filter')
