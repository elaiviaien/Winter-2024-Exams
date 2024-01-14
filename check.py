import json
import sys

COLOR_ERROR = '\x1b[0;31m'
COLOR_INFO = '\x1b[1;37m'
COLOR_NORM = '\x1b[0m'


def logger(color):
    def log(s):
        print(color + s + COLOR_NORM)

    return log


logger_error = logger(COLOR_ERROR)
logger_info = logger(COLOR_INFO)


def serialize(args):
    return ', '.join(map(lambda x:
                         json.dumps(x) if type(x) == dict
                         else
                         f"'{x}'" if type(x) == str
                         else str(x), args))


def check(cases):
    def test_function(name):
        module = __import__('Tasks.' + name)
        fn = getattr(module, name, None).run
        passed = 0
        for args, expected in cases:
            msg = f"Case: {fn.__name__}({serialize(args)}) ->"
            result = None
            try:
                res = fn(*args)
                result = json.dumps(res)
            except Exception as err:
                logger_error(f"{msg} {result}, exception: {err}")
                continue

            if callable(expected):
                if not expected(res):
                    logger_error(f"{msg} {result}")
                passed += 1
                continue

            try:
                assert res == expected
                passed += 1
            except:
                ex = json.dumps(expected)
                logger_error(f"{msg} {result}, expected: {ex}")

        logger_info(f"Test {name}.py: Passed: {passed} of {len(cases)}")
        if passed != len(cases):
            sys.exit(1)

    return test_function
