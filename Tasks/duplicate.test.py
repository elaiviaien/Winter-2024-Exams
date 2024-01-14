import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from check import check

cases = [
  [['abc', 5], ['abc', 'abc', 'abc', 'abc', 'abc']],
  [['abc', 1], ['abc']],
  [['abc', -1], []],
  [['abc', 0], []],
  [['', 0], []],
]

check(cases)('duplicate')
