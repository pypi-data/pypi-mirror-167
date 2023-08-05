import builtins


class Error(Exception):
    def explain(self):
        return self.args[0]


def check(b, msg):
    if not b:
        raise Error(msg)


def _check_type(type):
    def func(value) -> type:
        if isinstance(value, type):
            return value
        else:
            raise Error(f"Type error, expected: {type.__name__}")

    return func


int = _check_type(int)
float = _check_type(float)
str = _check_type(str)


def dict(value, keys=None) -> list:
    check(isinstance(value, builtins.dict), "Type error, expected a dictionary")
    if keys is not None:
        check(set(value.keys()) == set(keys), "Wrong keys for dictionary")
        return [value[key] for key in keys]
    else:
        return value
