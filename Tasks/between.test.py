import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
from check import check
cases = [
    (['Hello <username> and bye!', '<', '>'], 'username'),
    (['<username>', '<', '>'], 'username'),
    (['Hello username and bye!', '<', '>'], ''),
]

check(cases)('between')
