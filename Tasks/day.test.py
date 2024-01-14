import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from check import check

cases = [
    [['friday'], 6],
    [['Friday'], -1],
    [['Fri'], -1],
    [['monday'], 2],
    [['abc'], -1],
]

check(cases)('day')